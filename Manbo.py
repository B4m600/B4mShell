import os
import sys
import re
import requests
import json
from urllib.parse import unquote
from tqdm import tqdm

def clean_filename(text, max_length=100):
    """
    清理文本，使其适合作为文件名
    """
    # 移除Windows文件名中不允许的字符
    invalid_chars = r'[<>:"/\\|?*\x00-\x1f]'
    cleaned = re.sub(invalid_chars, '', text)
    
    # 限制文件名长度
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length]
    
    # 如果清理后为空，使用默认名称
    if not cleaned.strip():
        cleaned = "audio_file"
    
    return cleaned.strip()

def process_text_line(line):
    """
    处理单行文本，按优先级移除不需要的内容
    优先级: [] > () > #
    """
    # 第一步：移除方括号及其内容
    line = re.sub(r'\[.*?\]', '', line)
    
    # 第二步：移除圆括号及其内容
    line = re.sub(r'\(.*?\)', '', line)

    line = re.sub(r'\【.*?\】', '', line)

    line = re.sub(r'\.\.\.|🎦|⏹️|🔵', '', line)
    
    # 第三步：移除井号及之后的所有内容
    line = re.split(r'#', line)[0]
    
    return line.strip()

def read_and_process_file(file_path):
    """
    读取并处理文本文件
    """
    processed_lines = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                # 去除首尾空白字符
                original_line = line.strip()
                
                # 跳过空行
                if not original_line:
                    continue
                
                # 处理文本行
                processed_line = process_text_line(original_line)
                
                # 如果处理后的行不为空，则添加到列表
                if processed_line:
                    processed_lines.append({
                        'original': original_line,
                        'processed': processed_line,
                        'line_num': line_num
                    })
                    print(f"第{line_num}行: {processed_line}")
    
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 未找到")
        return None
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return None
    
    return processed_lines

def download_mp3(url, file_path):
    """
    下载MP3文件到指定路径，带进度条显示
    """
    try:
        # 确保目标目录存在
        target_dir = os.path.dirname(file_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # 检查文件是否已存在
        if os.path.exists(file_path):
            return True, "文件已存在，跳过下载"
        
        # 下载文件，带进度条
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # 获取文件大小
        total_size = int(response.headers.get('content-length', 0))
        
        # 创建进度条
        filename = os.path.basename(file_path)
        progress_bar = tqdm(
            total=total_size, 
            unit='iB', 
            unit_scale=True,
            desc=f"下载 {filename[:30]}..."  # 限制进度条描述长度
        )
        
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                size = f.write(chunk)
                progress_bar.update(size)
        
        progress_bar.close()
        
        # 检查文件是否完整下载
        if total_size != 0 and progress_bar.n != total_size:
            return False, "下载不完整"
        
        return True, file_path
    
    except Exception as e:
        return False, str(e)

def call_api_and_download(text_data, is_file_mode=False, source_file_path=None):
    """
    调用API并下载MP3文件
    
    参数:
    - text_data: 文本数据列表
    - is_file_mode: 是否为文件模式
    - source_file_path: 源文件路径（仅在文件模式下使用）
    """
    base_url = "https://api.milorapart.top/apis/mbAIsc"
    
    # 创建目标目录
    if is_file_mode and source_file_path:
        # 文件模式：在target下创建以源文件名为名的子文件夹
        source_filename = os.path.splitext(os.path.basename(source_file_path))[0]
        target_dir = os.path.join("target", source_filename)
    else:
        # 直接文本模式：直接保存到target文件夹
        target_dir = "target"
    
    success_count = 0
    error_count = 0
    skip_count = 0
    error_messages = []
    
    print("\n开始调用API并下载MP3文件...")
    
    # 创建总体进度条
    overall_progress = tqdm(
        text_data, 
        desc="总体进度", 
        unit="文件",
        position=0
    )
    
    for item in overall_progress:
        text = item['processed']
        line_num = item['line_num']
        index = item['index']  # 在List中的序号
        
        # 更新进度条描述
        if is_file_mode:
            overall_progress.set_description(f"处理第{line_num}行")
        else:
            overall_progress.set_description(f"处理文本")
        
        try:
            # 准备请求参数
            params = {
                "text": text,
                "format": "mp3"
            }
            
            # 调用API
            response = requests.get(base_url, params=params, timeout=30)
            response.raise_for_status()
            
            # 解析响应
            result = response.json()
            
            # 检查返回码
            if result.get("code") == 200:
                mp3_url = result.get("url")
                if mp3_url:
                    # 生成文件名
                    safe_filename = clean_filename(text)
                    
                    if is_file_mode:
                        # 文件模式：使用序号前缀
                        filename = f"{index}：{safe_filename}.mp3"
                    else:
                        # 直接文本模式：不使用序号前缀
                        filename = f"{safe_filename}.mp3"
                    
                    # 完整的文件路径
                    file_path = os.path.join(target_dir, filename)
                    
                    # 检查文件是否已存在
                    if os.path.exists(file_path):
                        if is_file_mode:
                            tqdm.write(f"⚠ 第{line_num}行跳过: 文件已存在 - {filename}")
                        else:
                            tqdm.write(f"⚠ 跳过: 文件已存在 - {filename}")
                        skip_count += 1
                        continue
                    
                    # 下载MP3文件
                    success, result_info = download_mp3(mp3_url, file_path)
                    
                    if success:
                        if is_file_mode:
                            tqdm.write(f"✓ 第{line_num}行成功: {filename}")
                        else:
                            tqdm.write(f"✓ 成功: {filename}")
                        success_count += 1
                    else:
                        if is_file_mode:
                            tqdm.write(f"✗ 第{line_num}行下载失败: {result_info}")
                            error_messages.append(f"第{line_num}行下载失败: {result_info}")
                        else:
                            tqdm.write(f"✗ 下载失败: {result_info}")
                            error_messages.append(f"下载失败: {result_info}")
                        error_count += 1
                else:
                    if is_file_mode:
                        tqdm.write(f"✗ 第{line_num}行: 响应中未找到MP3 URL")
                        error_messages.append(f"第{line_num}行: 响应中未找到MP3 URL")
                    else:
                        tqdm.write(f"✗ 响应中未找到MP3 URL")
                        error_messages.append(f"响应中未找到MP3 URL")
                    error_count += 1
            else:
                error_msg = result.get('msg', '未知错误')
                if is_file_mode:
                    tqdm.write(f"✗ 第{line_num}行API调用失败: {error_msg}")
                    error_messages.append(f"第{line_num}行API调用失败: {error_msg}")
                else:
                    tqdm.write(f"✗ API调用失败: {error_msg}")
                    error_messages.append(f"API调用失败: {error_msg}")
                error_count += 1
                
        except requests.exceptions.Timeout:
            error_msg = "请求超时"
            if is_file_mode:
                tqdm.write(f"✗ 第{line_num}行: {error_msg}")
                error_messages.append(f"第{line_num}行: {error_msg}")
            else:
                tqdm.write(f"✗ {error_msg}")
                error_messages.append(f"{error_msg}")
            error_count += 1
        except requests.exceptions.RequestException as e:
            if is_file_mode:
                tqdm.write(f"✗ 第{line_num}行网络请求错误: {e}")
                error_messages.append(f"第{line_num}行网络请求错误: {e}")
            else:
                tqdm.write(f"✗ 网络请求错误: {e}")
                error_messages.append(f"网络请求错误: {e}")
            error_count += 1
        except json.JSONDecodeError as e:
            if is_file_mode:
                tqdm.write(f"✗ 第{line_num}行JSON解析错误: {e}")
                error_messages.append(f"第{line_num}行JSON解析错误: {e}")
            else:
                tqdm.write(f"✗ JSON解析错误: {e}")
                error_messages.append(f"JSON解析错误: {e}")
            error_count += 1
        except Exception as e:
            if is_file_mode:
                tqdm.write(f"✗ 第{line_num}行处理过程中出错: {e}")
                error_messages.append(f"第{line_num}行处理过程中出错: {e}")
            else:
                tqdm.write(f"✗ 处理过程中出错: {e}")
                error_messages.append(f"处理过程中出错: {e}")
            error_count += 1
    
    # 关闭进度条
    overall_progress.close()
    
    # 输出统计信息
    print(f"\n" + "="*50)
    print(f"处理完成!")
    print(f"成功: {success_count} 个文件")
    print(f"跳过: {skip_count} 个文件 (已存在)")
    print(f"失败: {error_count} 个文件")
    print(f"文件保存在: {os.path.abspath(target_dir)}")
    
    # 如果有错误，显示错误信息
    if error_messages:
        print(f"\n错误详情:")
        for msg in error_messages:
            print(f"  - {msg}")

def main():
    """
    主函数
    """
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("使用方法: python Manbo.py <文本文件路径或文本内容>")
        print("示例1 (文件模式): python Manbo.py \"C:\\Users\\LEGION\\Desktop\\测试文本.txt\"")
        print("示例2 (直接文本模式): python Manbo.py \"这是一段测试文本\"")
        sys.exit(1)
    
    arg = sys.argv[1]
    
    # 检查参数是否为空
    if not arg.strip():
        print("错误: 参数不能为空")
        sys.exit(1)
    
    # 判断是文件模式还是直接文本模式
    is_file_mode = False
    text_data = []
    
    # 检查参数是否是存在的TXT文件
    if arg.lower().endswith('.txt') and os.path.isfile(arg):
        is_file_mode = True
        print(f"文件模式: 正在读取文件 {arg}")
        print("-" * 50)
        
        # 读取并处理文件
        text_data = read_and_process_file(arg)
        
        if text_data is None:
            sys.exit(1)
        
        if not text_data:
            print("文件中没有找到有效文本行")
            sys.exit(1)
        
        # 为每个文本项添加在List中的序号
        for i, item in enumerate(text_data, 1):
            item['index'] = i
        
        print(f"\n共找到 {len(text_data)} 行有效文本")
    else:
        # 直接文本模式
        print(f"直接文本模式: 处理单条文本")
        print("-" * 50)
        
        # 处理文本
        processed_text = process_text_line(arg)
        
        if not processed_text:
            print("处理后的文本为空")
            sys.exit(1)
        
        print(f"文本内容: {processed_text}")
        
        # 创建文本数据
        text_data = [{
            'original': arg,
            'processed': processed_text,
            'line_num': 1,
            'index': 1
        }]
    
    print("-" * 50)
    
    # 用户确认
    while True:
        user_input = input("\n是否继续处理这些文本？(y/N): ").strip().lower()
        if user_input in ['y', 'yes']:
            break
        elif user_input in ['n', 'no', '']:
            print("程序已退出")
            sys.exit(0)
        else:
            print("请输入 y 或 n")
    
    # 调用API并下载文件
    if is_file_mode:
        call_api_and_download(text_data, is_file_mode=True, source_file_path=arg)
    else:
        call_api_and_download(text_data, is_file_mode=False)

if __name__ == "__main__":
    main()