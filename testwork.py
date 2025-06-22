num = int(input())
list = []
i = 9
while num != 1 and i > 1:
    if num % i == 0 and num / i > 0:
        list.append(i)
        num = num / i
    else:
        i = i-1
if i == 1:
    print("-1")
elif len(list) > 0:
    for j in range(len(list)):
        if j == len(list)-1:
            print(list[len(list)-1-j],end="")
        else:
            print(list[len(list)-1-j],end=" ")
else:
    print("-1")

