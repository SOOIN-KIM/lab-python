from bs4 import BeautifulSoup

# 파일을 읽기 모드로 열기
with open(web01.thml, mode = 'r', encoding= 'UTF-8') as f:
    # HTML 문서와 HTML parser(분석기)를 파라미터에 전달해서,
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(f,'html5lib')
    # print(soup) # HTML의 내용

    # HTML 요소들 중에서 h1요소를 찾음
    h1 = soup.fine('h1') #find('태그이름')
    print(h1)
    print(h1.text) #h1 요소 안의 문자열

    h2 = soup.h2 #soup.태그이름 -soup.find('태그이름')와 동일
    print(h2)
    print(h2.text)

    # paragraph 요소 안의 문자열을 찾아서 출력
    # text 속성은 자식 요소(child element) 태그들을 제거하고, 텍스타만 찾아줌
    # print(soup.find('p').text)
    print(soup.p.text)

    # find는 HTML 문서를 처음부터 분석을 하다가 가장 처음에 만나는 요소를 리턴함
    # print(soup.find('a'))
    print(soup.a)

    # find_all은 HTML 문서 전체에서 찾은 모든 해당 요소들의 리스트를 리턴함.
    # print(soup.find_all('a'))

    # HTML 문서의 모든 링크에서 링크 주소(href)만 추출해서 출력
    for link in soup('a'):
        # HTML요소.get('attr이름') - attr의 값을 구함.
        print(link.get('href'))

    # HTML 문서안의 "class1" 클래스 속성을 갖는 모든 요소들을 찾음
    # soup(attrs={attr이름:attr값})
    # soup.find_all(attrs={attr이름 : attr값})

    for cls_1 in soup(attrs={"class" : "class1"}):
        print(cls_1)


    print(soup.find(attrs = {'id':'id1'}))
    print(soup.find(id='id1').text)
    print(soup(id='id1')[0].text)


    import requests
    from bs4 import BeautifulSoup
    import urllib

    url = 'https://book.naver.com/bookdb/book_detail.nhn?bid=15871940'

    # 사이트(웹 서버)로 요청(requests)를 보냄

    html = requests.get(url).text.strip() # 요청을보내고 그결과를 저장 html 변수에다가
    print(html[0:100])

    #Beautiful Soup 객체를 생성
    soup = BeautifulSoup(html,'html5lib')

    #HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
















