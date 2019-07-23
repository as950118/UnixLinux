'''
추가 변경사항에 대한 설명
'''
from collections import defaultdict
arr = defaultdict()
arr['a'] = ['a']
arr['b'] = ['b','c']
arr['c'] = ['d','e','f']
#arr['d'] = ['g','h','i','j']
#arr['f'] = ['k','l','n','m','o']
#arr['g'] = ['p','q','r','s','t','u']
#arr['h'] = ['v','w','x','y','z']
'''
_3 에서 구한것은 각각의 arr가 순서를 지키고 있는 경우이다.
예를들자면 , abc, acb abd, acd는 가능하지만 adb는 불가능하다.
하지만 arr의 순서를 바꿔서도 가능하게 구현해보겠다

더 단순하다.
모든 arr를 합쳐서 순열을 구해주면 된다.

조합과 순열에 대한 설명은 _3 에서 했기에 생략한다
'''
def permAll_FromArrs(arr): #arr는 찾을 배열, end는 몇개를 찾을지
    trans_arr = list()
    for key in arr:
        trans_arr += arr[key]
    def func(cur, remainder):
        ret = list()
        if not remainder:#남은게없다면 종료
            ret.append(cur)
        else:
            ret.append(cur)
            for next_idx in range(len(remainder)):
                next_remainder = remainder[:] #다음 remainder
                next_val = next_remainder.pop(next_idx) #next_idx에 위치하는 값을 제거하고 남은 리스트
                ret += func(cur + next_val, next_remainder)
        return ret
    return func("", trans_arr)

temp = permAll_FromArrs(arr)
print(temp, len(temp))
