while True:
    print("기능을 선택해주세요.")
    print("1. 메모작성 2. 메모읽기 3.종료하기")

    option = input()

    print(option)

    if option == '1':
        newmemo = input("메모를 입력해주세요 \n")
        print(newmemo)
        filename = 'memo.txt'
        f = open(filename, 'a')
        f.write(newmemo)
        f.close()
    elif option == '2':
        file_name = 'memo2.txt'
        f = open(file_name)
        memo = f.read()
        print(memo)
        f.close()
    elif option =='3':
        break
    else:
        print("잘못됨.")