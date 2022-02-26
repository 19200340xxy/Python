import re

a = input("输入目标字符串：")
a = a.lower()
sign = 0  # 通过对sign是0还是1的赋值来判断正负号,0为正1为负

s1 = r"[a-f0-9]"
target = re.findall(s1, a)  # 正则表达式直接提取出需要的字符
tmp=[]
res=0

def exchange():
    global target,tmp,a,sign

    for i in target:
        if ord(i) > 58:
            i = ord(i) - 87
        i = int(i)
        tmp.append(i)

    for i in a:

        if (i == target[0]):
            break
        if i == "-":
            sign = 1
    target = tmp

def Count_res():
    global res,target
    length = len(target)
    squared = length - 1
    for i in range(0, length):
        res += target[i] * (16 ** squared)
        squared = squared - 1
    if (sign == 1):
        res=-res


def main():
    exchange()
    Count_res()
    print(res)
if __name__=="__main__":
    main()