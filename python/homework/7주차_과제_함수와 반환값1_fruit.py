#7주차 과제
'''
*과제 내용*
매개변수로 문자열을 받고,
해당 문자열이 red면 apple을,
yellow면 banana를, green이면 melon을,
어떤 경우도 아닐 경우 I don’t know를 리턴하는 함수를 정의하고,
사용하여 result변수에 결과를 할당하고 print해본다.
'''

def fruit(word):
    if word == 'red':
        result = 'apple'
    elif word == 'yellow':
        result = 'banana'
    elif word == 'green':
        result = 'melon'
    else:
        result = 'I don\'t know'
    return result

if __name__ == '__main__':
    word = input('과일의 색깔을 입력하세요 : ')

    result = fruit(word)

    import time
    if result == 'I don\'t know':
        for i in range(3):
            time.sleep(0.5)   #입력된 시간만큼 일시정지하는 sleep 함수입니다.
            print('.'*(i+1))
            i+=1
        time.sleep(0.5)
        print(result, 'that color. im sorry.')
    else:
        time.sleep(0.5)
        print('그 과일은', result, '입니다.')
