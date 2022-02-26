def main():
    p = [2]
    a=int(input("请输入上限："))
    sum=2
    for i in range(2, a+1):
        for temp in range(2, i):
            if i % temp == 0:
                break
            elif temp == i - 1:
                sum+=i
    print(sum)
if __name__=="__main__":
    main()