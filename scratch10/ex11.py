'''
웹 주소(URI, URL)의 형식:
프로토콜://서버주소[:포트번호}/경로?쿼리스트링
http://www.naver.com
https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon
쿼리 스트링(query string): 클라이언트(브라우저)가 서버로 보내는 정보
    param이름=parm값

다음에서 '머신 러닝'으로 검색한 기사 100개의 url주소와 기사 제목을 출력
'''

import requests
from bs4 import BeautifulSoup
import urllib
#
# # 접속할 사이트(웹 서버) 주소
# url = 'https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&p=1'
#
# # 사이트(웹 서버)로 요청(request)를 보냄
# html = requests.get(url).text.strip() # 요청의 결과(응담,response- HTML을 저장)
# print(html[0:100])
#
# #BeautifulSoup 객체를 생성
# soup = BeautifulSoup(html,'html5lib')
#
# #HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))
#
#
#
#
# # 관심 있는 링크(뉴스 들만 찾을 수 있는 방법을 고민)
# div_coll_cont = soup.find_all(class_='coll_cont')
# # soup.find_all(attrs={'class': 'call_cont'})
# print(len(div_coll_cont)) # 같은 클래스 이름이 있는 모든 HTML 요소들을 찾음
#
# print()
# # HTML 하위 요소(sub/child element)를 찾는 방법:
# # 1) parent_select > child_select (바로 아래쪽에 있는 element만 찾을수 있음)
# #       div > ul > li
# #       .call_cont > #clusterResultUL > .fst
# # 2) ancestar_selector descendant_selector (아래 어디있는 element 모두 찾을 수있음)
# #       div li
# #       .coll_cont .fst(클래스 .call-cont 요소의 자손 요소들 중 클래스가.fst 인 요소)
# # soup.select(css_selector): soup 객체에서 CSS 선택자료 요소들을 찾는 방법
# news_link = soup.select('.coll_cont ul li a.f_link_b')
# for link in news_link:
#     print(link.get('href'))



# for page in range(10):
#     html = requests.get('https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&p=1'+str(page +1)).text.strip()
#     soup = BeautifulSoup(html, 'html5lib')
#     news_link = soup.select('.coll_cont ul li a.f_link_b')
#     for link in news_link:
#
#         print(link.get('href'))
#

def daum_search(keyword):
    url = 'https://search.daum.net/search?w=news&DA=PGD&spacing=0'
    # 검색결과는 1페이부터 10페이지 까지
    for page in range(1,11):
        print(f'=== Page {page} ===')
        req_params = {
            'q' : keyword, # 검색어(키워드)를 쿼리 스트링에 파라미터로 추가
            'p' : page # 검색 페이지 번호를 쿼리 스트링에 파라미터로 추가
        }
        response = requests.get(url,params = req_params)
        html = response.text.strip()

        soup = BeautifulSoup(html, 'html5lib')
        news_links = soup.select('.coll_cont ul li a.f_link_b')
        for link in news_links:
            news_url = link.get('href')
            news_title = link.text
            print(news_url, news_title)



if __name__ == '__main__':
    daum_search('시동')

if False:
    # url = 'https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&p='
    url = 'https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D'

    for page in range(1, 11):
        print(f'=== Page {page} ===')
        # page_url = url +str(page)

        # 해당 페이지 URL 주소로 GET 방식 요청(request)을 보내고,
        # 서버에서 보낸 응답(response)을 문자열로 처리
        # html = requests.get(page_url).text.strip()

        response = requests.get(url,params={'p' : page})
        # requests.get(url, parms={key: value})
        #   parms의 내용을 url의 query string의 파라미터를 추가해줌
        #   url?... &key=value
        html = response.text.strip()


        # Beautiful.Soup 객체 생성
        soup = BeautifulSoup(html, 'html5lib')
        news_links = soup.select('.coll_cont ul li a.f_link_b')
        for link in news_links:
            # HTML 요소(element)의 href 속성(attribute) 값을 읽음.
            news_url = link.get('href')
            # HTML 요소가 가지고 있는 컨텐트 문자열
            news_title = link.text
            print(news_url, news_title)



# 다음에서 ' 머신 러닝'으로 검색한 기사 1100개의 URL 주수와 기사 제목을 출력
