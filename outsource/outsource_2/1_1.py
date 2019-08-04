'''
0번에서 이야기했듯 자료는 다음과 같이 정의한다.
'''
from collections import defaultdict
dic = defaultdict()
dic['a'] = [1,3,4]
dic['b'] = [1,5]
dic['c'] = [2,3,7,4]
dic['d'] = [1]
dic['e'] = [8,10,2,7,5]

'''
가.
이 경우는 각각의 데이터에서 값을 하나씩 뽑아와
순서를 고려하지 않고 정렬하는 것을 의미한다.

이것은 수학에서 흔히 조합(combination)이라고 부르는 것이다.

함수는 다음과 같이 구현한다.
먼저 데이터들을 인자로 받는다.
데이터들은 2중 리스트로 구현되어있어야한다.
그래서 각각의 리스트 별로 하나씩 값을 꺼내어 조합한다.

예를들어 a,b를 조합하고 싶다면
[[1,3,4], [1,5]] 처럼 데이터가 들어오는 것이다.

이렇게 데이터를 구현하기 위해선
data = list()
data.append(dic['a'])
data.append(dic['b'])
처럼 리스트를 하나 만들고, 그안에 두개의 리스트를 담는다.
'''
def combiAll_dictarr(arrs): #dict(list()) 에서 조합 구하기
    end = len(arrs)
    key_list = [k for k in arr] #dict와 list로 구현할 경우 이렇게 key를 따로 관리해줘야 한다. 때문에 개인적으로는 dict보다는 lsit(list()) 형태로 key와 value 모두 숫자로 처리하는 것이 더 편리하다. 관련 코드는 아래 참고
    print(key_list)
    def func(cur, idx):
        ret = list()
        if end == idx:
            if cur: #cur가 공백이 아니라면
                ret.append(cur)
        else:
            if cur: #cur가 공백이 아니라면
                ret.append(cur)
            for next_val in arrs[key_list[idx]]:
                ret += func(str(cur) + str(next_val), idx+1)
        return ret
    return func("",0)

def combiAll_listlist(arrs): #list(list()) 에서 조합 구하기
    end = len(arrs)
    def func(cur, idx):
        ret = list()
        if end == idx:
            if cur: #cur가 공백이 아니라면
                ret.append(cur)
        else:
            if cur: #cur가 공백이 아니라면
                ret.append(cur)
            for next_val in arrs[idx]:
                ret += func(str(cur) + str(next_val), idx+1)
        return ret
    return func("", 0)

'''
그러면 프로그램을 하나 만들어보자.

먼저 dict와 list로 구성된 데이터(dictlist)의 key들을 출력해서
사용자에게 그중에서 원하는 key들을 선택하게 하자.
그리고 선택된 key를 이용해 data를 combiAll_dictarr의 인자(arr)에 넣도록 하자
'''
def program(dictlist):
    #key들을 출력하기
    keys = [key for key in dictlist]
    print("Select Keys From :", end=" ")
    for key in keys:
        print(key, end=" ")
    print("")

    #올바르게 입력되었는지 확인하는 함수
    def selected_keys_check(selected_keys):
        for selected_key in selected_keys:
            if not selected_key in keys:
                #선택한 key 중에서 keys에 속하는 key가 있다면 0을 반환
                return 0
        #무사히 통과한다면 1을 반환
        return 1

    #key를 입력받기
    #올바르게 입력받을때까지 반복
    while 1:
        selected_keys = list(map(str, input().split()))
        if selected_keys_check(selected_keys):
            #올바르게 입력받았다면 break를 통해 while 문을 탈출
            break
        #아니라면 다시 입력받기
        print('Try Again')

    #선택된 key들을 통해 데이터를 선택
    selected_data = list()
    for selected_key in selected_keys:
        data = dictlist[selected_key]
        selected_data.append(data)

    #선택된 data들을 이용해 combination 수행
    #함수는 위에 정의된 combiAll_listlist를 이용
    ret_datas = combiAll_listlist(selected_data)

    #깔끔하게 출력
    print("Selected Keys :", end=" ")
    for selected_key in selected_keys:
        print(selected_key, end=" ")
    print("")
    print("Result :", end=" ")
    for ret_data in ret_datas:
        print(ret_data, end=" ")

'''
결과
'''
program(dic)
