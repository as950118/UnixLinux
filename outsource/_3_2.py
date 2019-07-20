'''
추가 변경사항에 대한 설명
'''
from collections import defaultdict
arr = defaultdict()
arr['a'] = ['a']
arr['b'] = ['b','c']
arr['c'] = ['d','e','f']
arr['d'] = ['g','h','i','j']
arr['f'] = ['k','l','n','m','o']
arr['g'] = ['p','q','r','s','t','u']
arr['h'] = ['v','w','x','y','z']
'''
_3 에서 구한것은 각각의 arr가 순서를 지키고 있는 경우이다.
하지만 arr의 순서를 바꿔서도 가능하게 구현해보겠다

먼저 이 경우에는 조합을 이용해야한다.
각각의 arr에 대해 조합을 구하고
그 결과로 나온값들에 대해 각각 순열을 구해준다.
그러면 중복되거나 손실되지않게 모든 경우를 구할 수 있다.

조합과 순열에 대한 설명은 _3 에서 했기에 생략한다
'''
def combiAll(arr):
    def func(end, cur, remainder):
        ret = list()
        if not remainder:
            ret.append(cur)
        else:
            for next in remainder:
                ret += func(end, cur+next, idx+1)
        return ret
    return func(len(arr),"",0)
def permAll(arr): #arr는 찾을 배열, end는 몇개를 찾을지
    def func(cur, remainder):
        ret = list()
        if not remainder:#남은게없다면 종료
            ret.append(cur)
        else:
            ret.append(cur)
            for next in remainder:
                ret += func(cur+next, remainder - set(next))
        return ret
    return func("", set(arr))
temp = list()
temp.append(combiAll(arr['a']))
print(temp)
temp.append(combiAll(arr['b']))
temp.append(combiAll(arr['c']))
print(permAll(temp))
