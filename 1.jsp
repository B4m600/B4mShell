
<!DOCTYPE HTML>
<html>
<head>
<title>登录页面</title>
<meta http-equiv=Content-Type content="text/html; charset=utf-8">

<link rel="stylesheet" type="text/css" href="/js/jquery-easyui-1.4.1/themes/default/easyui.css" />
<script type="text/javascript" src="/js/jquery-easyui-1.4.1/jquery.min.js"></script>
<script type="text/javascript" src="/js/jquery-easyui-1.4.1/jquery.easyui.min.js"></script>

<script type="text/javascript" src="/js/jquery-easyui-1.4.1/locale/easyui-lang-zh_CN.js"></script>
<script type="text/javascript" src="/js/json2.js"></script>
<script type="text/javascript" src="/js/jquery.form.js"></script>
</head>
<body leftMargin=0 topMargin=0 marginwidth="0" marginheight="0"	>
	<form method="post" id="form" action="/selectExam.action" >
		<div ALIGN="center">
			<table border="0" width="1000px" cellspacing="0" cellpadding="0"
				id="table1" style="margin: 0 auto;">
				<tr>
					<td style="text-align: center;"><img alt=""
						src="images/banner2.png" style="width: 1000px;height: 200px;">
					</td>
				</tr>

				<tr height="50px;">
					<td></td>
				</tr>
				<tr>
					<td class="login_msg" align="center">
						<!-- margin:0px auto; 控制当前标签居中 -->
						<fieldset style="width: auto; margin: 0px auto;">
                            <legend style="margin:0px auto;font-size:40px;color: red; font-weight: bolder; font-family: 隶书; text-align: center">
								考生须知							
							</legend>								
							<br>
							<div
								style="font-size:16px; line-height: 24px;padding-left: 150px; text-align: left;">								
								   1、请输入学号和姓名随机抽题;<br>
								   2、将抽到的试题中数据库语句在MYSQL执行创建满足题意要求的数据库;<br>
								   3、考试过程中注意保存操作，防止意外关机;<br>
								   4、考试后要求建立以学号姓名命名文件夹比如（16561140229张明明）， 将数据库也存放于该文件夹中<br>
								   5、考试完成先让教师检查后再提交<br>
								   6、提交后到教师机上查看是否正确提交<br>
								   7、考试过程中不允许来回走动，不允许交头接耳，有雷同卷者视同作弊							
							</div>
							<br>
						</fieldset>
					</td>
				</tr>
				<tr>
					<td height="30"></td>
				</tr>
				<tr>
					<td class="login_msg" align="center">
						<!-- margin:0px auto; 控制当前标签居中 -->
						<fieldset style="width: auto; margin: 0px auto;">
							           <legend style="margin:0px auto;font-size:40px;color: red; font-weight: bolder; font-family: 隶书; text-align: center">
								考生登录							
							</legend>							
							<div	style="font-size:30px; line-height: 30px;font-family: 隶书; margin-top: 20px;">


								学&nbsp;&nbsp;号：
								
								<input class="easyui-textbox" type="text" name="studentNo" id="no"
					 data-options="required:true"	style="width: 200px;height: 30px; "></input>
								
							
								<br>
								<br>
								姓&nbsp;&nbsp;号：
								
								<input class="easyui-textbox" type="text" name="studentName" id="name"
					 data-options="required:true"	style="width: 200px;height: 30px; "></input>
								
							
								<br>
								<br>
								
								<a href="javascript:void(0)" class="easyui-linkbutton"
			onclick="submitForm()"  style="width: 120px;height: 40px;font-size: 30px;">抽题</a>
								 <br> <br>

							</div>
						</fieldset>
					</td>
				</tr>
			</table>
		</div>
	</form>
</body>
</html>
<script  type="text/javascript">
	function submitForm() {		
		if (!$('#form').form('validate')) {
			$.messager.alert('提示', '学号或者姓名未填写!!');
			return;
		}
		if ($('#no').val().length!=11) {
			$.messager.alert('提示', '学号长度位数不够!!');
			return;
		}
		$("#form").submit();		
	}
</script>
