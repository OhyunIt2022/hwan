print("선택해")
print("1. 메모작성 2. 메모읽기")

option = input()

print(option)

if option == '1':
    print("아직 구현 안함")
elif option == '2':
    f = open('memo2.txt')
    memo = f.read()
    print(memo)
else:
    print("잘못됨.")