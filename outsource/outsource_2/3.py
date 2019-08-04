'''
1-1, 1-2와 사실상 동일하다.

설명은 생략한다.
'''
from collections import defaultdict
dic = defaultdict()
dic['a'] = ['a','b','d']
dic['b'] = ['e','f']
dic['c'] = ['k','j']
dic['d'] = ['e','f','c','d','e']
dic['e'] = ['a','d','a']

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
