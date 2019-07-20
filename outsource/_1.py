#먼저 구성요소들을 만들어보자.
#1. list로 선언
#직관적이지만 유연하게 사용하기는 힘들다.
arr_a = ['a']
arr_b = ['b','c']
arr_c = ['d','e','f']
arr_d = ['g','h','i','j']
arr_f = ['k','l','n','m','o']
arr_g = ['p','q','r','s','t','u']
arr_h = ['v','w','x','y','z']
#2. dict와 list를 섞어서 선언
#구성요소들의 집합 이름은 dict로, 구성요소들은 list로 선언한다.
#직관적이고 비교적 유연하게 사용할 수 있다.
#dict에 관한 설명 https://wikidocs.net/16
arr = dict('a':['a'],
           'b':['b','c'],
           'c':['d','e','f'],
           'd':['g','h','i','j'],
           'f':['k','l','n','m','o'],
           'g':['p','q','r','s','t','u'],
           'h':['v','w','x','y','z']
          )
#3. defaultdict와 list를 섞어서 선언
#구성요소들의 집합 이름은 defaultidct로, 구성요소들은 list로 선언한다.
#defaultdict는 이름을 먼저 정의해줄 필요가없어 좀 더 유연하게 사용할 수 있다.
#default에 관한 설명 https://gomguard.tistory.com/126
from collections import defaultdict
arr = defaultdict()
arr['a'] = ['a']
arr['b'] = ['b','c']
arr['c'] = ['d','e','f']
arr['d'] = ['g','h','i','j']
arr['f'] = ['k','l','n','m','o']
arr['g'] = ['p','q','r','s','t','u']
arr['h'] = ['v','w','x','y','z']
