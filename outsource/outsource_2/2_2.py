'''
그러면 간단히 프로그램을 하나 짜보자.

먼저 문단을 입력받고
찾을 단어를 입력받는다.
그리고 해당 단어가 있는 문장을 출력한다.
'''
def program():
    paragraph = input("Input paragraph : ")
    word = input("Input word to search : ")
    sentences = list(map(str, paragraph.split(".")))
    #결과출력
    print("Results :", end=" ")
    for sentence in sentences:
        if word in sentence:
            print(sentence, end=" / ")
program()
