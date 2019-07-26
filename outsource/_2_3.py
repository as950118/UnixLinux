'''
먼저 구성요소의 집합 이름(a~h)은 key라고 정의한다.
그리고 구성요소의 집합은(['a'], ['b','c']..)은 arr라고 정의한다.
구성요소(a / b,c / d,e,f)는 value 라고 정의한다.

예를들어, key가 'a'인 arr의 value는 'a'이다
(ex. arr['a'] = ['a'] )
예를들어, key가 'h'인 arr의 value는 'v','w','x','y','z'이다
(ex. arr['h'] = ['v','w','x','y','z'] )
'''
from collections import defaultdict
arr = defaultdict()
arr['a'] = ['a']
arr['b'] = ['b','c']
arr['c'] = ['d','e','f']
arr['d'] = ['g','h','i','j']
#arr['e'] = ['k','l','n','m','o']
#arr['f'] = ['p','q','r','s','t','u']
#arr['g'] = ['v','w','x','y','z']
'''
먼저 순열(permutation), 조합(combination)을 구분한다.
전자는 순서를 고려하고 후자는 순서를 고려하지않는다.
예를들면, arr['b']에서
전자는 b, c, bc, cb 가 가능하고
후자는 b, c, bc 만 가능하다.
왜냐하면 bc와 cb는 구성요소가 같기때문이다.
'''
'''
순열을 구하는 이유는 다음과 같다.
각각의 arr에서 2개 이상의 value를 꺼낼때 모든 순서를 고려하기 위해서이다.
예를들어, abc와 acb는 다르기 때문이다.
'''
'''
순열을 구하는 방법은 몇가지가 있는데, 재귀(recursion)를 이용하였다.
재귀란, 함수에서 자기자신 함수를 반복적으로 불러오는 형태를 의미한다.
함수에는 배열(arr), 순열의 크기(end), 현재 요소(cur), 남은 요소(remainder)를 입력받는다.
'''
import sys
sys.setrecursionlimit(10**9) #setrecursionlimit이란 재귀 가능횟수를 제한하는 것

def perm(arr, end, cur, remainder): #arr 찾을 배열, end 몇개를 찾을지, cur 현재 글자, remainder 조합 가능한 남은 글자
    ret = list()
    if end == len(cur): #현재 글자 크기가 end에 도달하면 종료
        if cur: #cur값이 공백이 아니라면
            ret.append(cur)
    else:
        for next_idx in range(len(remainder)):
            next_remainder = remainder[:] #다음 remainder
            next_val = next_remainder.pop(next_idx) #다음값에 해당하는 값을 제거하고 남은 리스트
            ret += perm(arr, end, cur+next_val, next_remainder)
    return ret
print("")
print("1. 순열")
print("B에서 2개를 선택하는 순열")
print(perm(arr['b'], 2, "", arr['c']))
'''
다음과 같이 좀 더 깔끔하게 작성이 가능하다
'''
def perm(arr, end): #arr는 찾을 배열, end는 몇개를 찾을지
    def func(cur, remainder):
        ret = list()
        if end == len(cur):#현재 글자 길이가 end에 도달하면 종료
            if cur: #cur값이 공백이 아니라면
                ret.append(cur)
        else:
            for next_idx in range(len(remainder)):
                next_remainder = remainder[:] #다음 remainder
                next_val = next_remainder.pop(next_idx) #next_idx에 위치하는 값을 제거하고 남은 리스트
                ret += func(cur + next_val, next_remainder)
        return ret
    return func("", arr)
print("")
print("2. 순열")
print("C에서 2개를 선택하는 순열")
print(perm(arr['c'], 2))
'''
사실 더 간단한 방법이있다.
구현해놓은 라이브러리를 사용하면 된다.
itetools에는 permutations라는 라이브러리가 있다.
참고로 조합도 combinations로 구현되어있다.
'''
from itertools import permutations, combinations
print("")
print("3. 순열")
print("이미 구현되어있는 라이브러리를 사용함")
print("D에서 2개를 선택하는 순열")
print(list(map(''.join, permutations(arr['d'], 2))))
#print(list(map(''.join, combinations(arr['e'],5))))

'''
모든 개수에 대해 순열을 구하려면 end에 1,2,3..을 대입하여 모두 구해도되지만
실행 시간을 아끼기 위해서는 다음의 함수를 사용해도된다.
기본적인 알고리즘은 비슷하다.
하지만 end를 따로 주지않고 remainder가 없을때 종료한다.
그리고 매번의 cur를 결과값(ret)에 저장해준다.
'''
def permAll(arr): #arr는 찾을 배열, end는 몇개를 찾을지
    def func(cur, remainder):
        ret = list()
        if not remainder:#남은게없다면 종료
            ret.append(cur)
        else:
            if cur: #cur값이 공백이 아니라면
                ret.append(cur)
            for next_idx in range(len(remainder)):
                next_remainder = remainder[:] #다음 remainder
                next_val = next_remainder.pop(next_idx) #next_idx에 위치하는 값을 제거하고 남은 리스트
                ret += func(cur + next_val, next_remainder)
        return ret
    return func("", arr)
print("")
print("4. 순열")
print("모든 경우에 관한 순열")
print("B에서 모든 경우의 순열")
print(permAll(arr['b']))
'''
그러면 이렇게 모든 arr에 대해 순열을 구하고
각각의 순열에서 하나씩을 꺼내어 합치기, 즉 조합을 구한다.
이미 순열로 모든 경우를 구했기때문에 중복되거나 손실되는 경우는 없다.
'''
def combiAll(arr): #조합 예시
    end = len(arr)
    def func(cur, idx):
        ret = list()
        if end == idx:
            ret.append(cur)
        else:
            if cur: #cur가 공백이 아니라면
                ret.append(cur)
            for next_idx, next_val in enumerate(arr[idx:]):
                ret += func(cur + next_val, idx+next_idx+1)
        return ret
    return func("", 0)

def combiAll_FromArrs_dictlist(arr): #dict(list()) 에서 조합 구하기
    end = len(arr)
    key_list = [k for k in arr] #dict와 list로 구현할 경우 이렇게 key를 따로 관리해줘야 한다. 때문에 개인적으로는 dict보다는 lsit(list()) 형태로 key와 value 모두 숫자로 처리하는 것이 더 편리하다. 관련 코드는 아래 참고
    print(key_list)
    def func(cur, idx):
        ret = list()
        if end == idx:
            ret.append(cur)
        else:
            if cur: #cur가 공백이 아니라면
                ret.append(cur)
            for next_val in arr[key_list[idx]]:
                ret += func(cur + next_val, idx+1)
        return ret
    return func("",0)

def combiAll_FromArrs_listlist(arrs): #list(list()) 에서 조합 구하기
    end = len(arrs)
    def func(cur, idx):
        ret = list()
        if end == idx:
            ret.append(cur)
        else:
            if cur: #cur가 공백이 아니라면
                ret.append(cur)
            for next_val in arrs[idx]:
                ret += func(cur + next_val, idx+1)
        return ret
    return func("", 0)

print("")
print("5. 조합")
print("C에서 모든 조합 구하기")
print(combiAll(arr['c']))
print("")
print("6. 조합")
print("arr 전체에서 모든 조합 구하기")
print(combiAll_FromArrs_dictlist(arr))
'''
결과적으로 다음과 같이 사용할 수 있다.
시간관계상 a~d만 돌려서 구해보겠다. (다하면 최소 몇십억개이기때문에..)
'''
temp = list()
temp.append(permAll(arr['a']))
print("")
print("7-1. A에 대한 순열")
print(temp)
temp.append(permAll(arr['b']))
print("")
print("7-2. A~B에 대한 순열")
print(temp)
temp.append(permAll(arr['c']))
print("")
print("7-3. A~C에 대한 순열")
print(temp)
temp.append(permAll(arr['d']))
print("")
print("7-4. A~D에 대한 순열")
print(temp)
temp = combiAll_FromArrs_listlist(temp)
print("")
print("8. A~D에 대한 순열에 대한 조합")
print(temp)
print("")
print("9. 특정 단어를 찾기")
def find(arr, string): #arr은 찾을 배열, string은 arr에서 찾을 문자
    try:
        return arr.index(string)
    except Excetion as e:
        return "key :", string, ", Error :" + e
print("key : acd", ", index :", find(temp, "acd"))
