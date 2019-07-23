from collections import defaultdict
arr = defaultdict()
arr['a'] = ['ㄱ','ㄴ','ㄷ']
arr['b'] = ['ㅏ','ㅗ','ㅜ']
#arr['c'] = ['ㄹ','ㅁ','ㅂ','ㅅ']
#arr['d'] = ['ㅑ','ㅛ','ㅠ','ㅓ']
#arr['e'] = ['ㅇ','ㅈ','ㅊ','ㅋ']
#arr['f'] = ['ㅕ','ㅡ','ㅣ']
#arr['g'] = ['ㅌ','ㅍ','ㅎ']
'''
한글을 조합하는 것은 영어와는 다르다.
자음 모음, 초중성, 겹받침 등을 모두 고려해야하기 때문이다.
이것을 계산하는 방법은 있지만 사실 예외도 많고 복잡하다.

하지만 라이브러리가 구현되어있다.
그래서 해당 라이브러리를 이용하도록 한다.
https://github.com/bluedisk/hangul-toolkit
해당 라이브러리를 이용하면 영어처럼 사용이 가능하다
먼저 파이썬 환경에 해당 라이브러리를 추가해준다.
pip install hgtk

그 후 기본적인 사용법을 정리해보겠다.
'''
import hgtk
#글자를 조합
print(hgtk.letter.compose('ㅈ','ㅓ','ㅇ'))
#글자를 분해
print(hgtk.letter.decompose('정'))
#문장을 조합
print(hgtk.text.compose('ㅈㅓㅇㅎㅓㄴㅈㅣㄴㅇㅣㅂㄴㅣㄷㅏ'))
print(hgtk.text.compose('ㅈㅓㅇᴥㅎㅓㄴᴥㅈㅣㄴᴥㅇㅣㅂᴥㄴㅣᴥㄷㅏᴥ'))
#문장을 분해
print(hgtk.text.decompose('정헌진입니다'))
#한글인지 판단
print('한글',hgtk.checker.is_hangul('한글'))
print('latin',hgtk.checker.is_latin1('latin'))
print('韓字',hgtk.checker.is_hanja('韓字'))
#받침이 있는지 판단
print(hgtk.checker.has_batchim('정'))
print(hgtk.checker.has_batchim('저'))
#compose할때 불가능하면 (예를들어, ㅈ,ㅓ,ㅡ 같은 경우) 예외처리를해줌
try:
    print(hgtk.letter.compose('ㅈ','ㅓ','ㅇ'))
except "NotLetterException":
    print("글자가 성립하지 않음")

'''
기본적으로 이정도만 알면 어느정도 구현 할 수 있다.
먼저 모든 경우에 대해 순열을 구한다.
필요하다면 동시에 글자가 성립하는지 여부를 검사하여 가능한 경우만 반환한다.

하지만 요구사항에서는 글자가 안되는 경우도 포함하였으므로
hgtk.text.compose()를 사용하면 될것을 보인다.

코드는 다음과 같다.
'''
def trans_str(cur:str): #글자들의 배열을 한문장으로 만들어주는 함수
    ret = ""
    for elem in cur:
        ret+=elem
    return ret

def permAll_FromArrs_Hangul(arr): #arr는 찾을 배열, end는 몇개를 찾을지
    trans_arr = list()
    for key in arr:
        trans_arr += arr[key]
    def func(cur, remainder):
        ret = list()
        if not remainder:#남은게없다면 종료
            temp = trans_str(cur)
            temp = hgtk.text.compose(temp)
            ret.append(temp)
        else:
            temp = trans_str(cur)
            temp = hgtk.text.compose(temp)
            ret.append(temp)
            for next_idx in range(len(remainder)):
                next_remainder = remainder[:] #다음 remainder
                next_val = next_remainder.pop(next_idx) #next_idx에 위치하는 값을 제거하고 남은 리스트
                ret += func(cur + next_val, next_remainder)
        return ret
    return func("", trans_arr)
ret = permAll_FromArrs_Hangul(arr)
print(ret, len(ret))
'''
하지만 이렇게 할 경우에 문제가 나타난다.
중성 뒤에 나오는 모든 자음은 종성으로 처리되기된다.

예를 들어, 가나다 를 나타내기 위해 ㄱㅏㄴㅏㄷㅏ를 compse할 경우
간ㅏ다 처럼 나타난다.

그래서 모든 자음 앞에는 ᴥ를 두거나 안두는 경우를 모두 생각해야한다.

그렇게 작성한 코드는 다음과 같다.
'''
jaum = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
def permAll_FromArrs_Hangul_newline(arr): #arr는 찾을 배열, end는 몇개를 찾을지
    trans_arr = list()
    for key in arr:
        trans_arr += arr[key]
    def func(cur, remainder):
        ret = list()
        if not remainder:#남은게없다면 종료
            temp = trans_str(cur)
            temp = hgtk.text.compose(temp+'ᴥ') #마지막에 줄바꿈을 넣어준다
            ret.append(temp)
        else:
            temp = trans_str(cur)
            temp = hgtk.text.compose(temp+'ᴥ') #마지막에 줄바꿈을 넣어준다
            ret.append(temp)
            for next_idx in range(len(remainder)):
                next_remainder = remainder[:] #다음 remainder
                next_val = next_remainder.pop(next_idx) #next_idx에 위치하는 값을 제거하고 남은 리스트
                if next_val in jaum: #다음값이 자음이고
                    if cur in jaum: #현재값도 자음이라면
                        ret += func(cur + 'ᴥ' + next_val, next_remainder) #무조건 줄바꿈을 넣는다
                    else: #현재값이 모음이라면
                        ret += func(cur + 'ᴥ' + next_val, next_remainder) #두가지 경우 모두 생각해준다
                        ret += func(cur + next_val, next_remainder) #두가지 경우 모두 생각해준다
                else: #다음값이 모음이라면 딱히 줄바꿈을 넣지않는다
                    ret += func(cur + next_val, next_remainder)
        return ret
    return func("", trans_arr)
ret = permAll_FromArrs_Hangul_newline(arr)
print(ret, len(ret), ret.index('가노두'))

'''
이렇게 구한후 글자가 성립하는 것만 찾기 위해서는 결과 ret에 대해 한글자씩 decompse 가 가능한지 여부를 살펴보면 된다.
예를들자면
try:
    for elem in ret:
        hgtk.letter.decompse(elem)
except:
    print("성립하지 않는 글자가 있습니다.")

이런식으로 구현하면 된다
'''
