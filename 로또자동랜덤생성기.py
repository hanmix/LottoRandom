import random
cn = 'y'
print ('★☆★☆★☆ 로또번호 자동생성기 ★☆★☆★☆')
print('----------------------------------------------')
print('게임 수를 입력하세요(숫자만 입력).')
while(cn == 'y' or cn == 'Y'):
    num = input('게임 수: ')
    if(num.isdigit() == True):
        print('----------------------------------------------')
        for i in range(0, int(num)):
            lotto = random.sample(range(1, 46), 6)
            lotto.sort()
            print(lotto)
    else:
        print('숫자를 입력하세요.')
        continue
    print('----------------------------------------------')
    print('★☆★☆★ 로또번호 자동 생성 완료 ★☆★☆★')
    print('----------------------------------------------')
    cn = input('다시 하시겠습니까? (Y/N) : ')
    while(cn != 'y' and cn != 'n' and cn != 'Y' and cn != 'N'):
        print('Y나 N만 입력하세요.')
        print('----------------------------------------------')
        cn = input('다시 하시겠습니까? (Y/N) : ')
print('----------------------------------------------')
print('★☆★☆★ 로또번호 자동 생성 종료 ★☆★☆★')