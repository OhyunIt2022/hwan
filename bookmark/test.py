#사칙연산
a,b = input("숫자 두개를 띄어쓰기로 입력해주세요").split()
A = int(a)
B = int(b)
if (1<=a<=10000 & 1<=b<=10000):
    print(A+B)
    print(A-B)
    print(A*B)
    print(A/B)