def find_factors(P):  
    # 用于存储结果  
    results = []

    # 递归函数来寻找因数  
    def backtrack(current_product, start, path):  
        if current_product == P:  
            results.append(path.copy())  
            return  
        if current_product > P:  
            return  
        
        for i in range(start, 10):  # 因数范围 2 到 9  
            if P % i == 0:  # 只有当 i 是 P 的因数时才能继续  
                path.append(i)  
                backtrack(current_product * i, i, path)  # 允许重复使用当前因数  
                path.pop()  # 回溯  

    backtrack(1, 2, [])  
    
    # 选择最短的解，若有多个，则选择字典序最小的  
    if not results:  
        return [-1]  
    
    results.sort(key=lambda x: (len(x), x))  # 按长度和字典序排序  
    return results[0]  

# 输入  
P = int(input().strip())  
result = find_factors(P)  

# 输出  
print(" ".join(map(str, result)),end="")
