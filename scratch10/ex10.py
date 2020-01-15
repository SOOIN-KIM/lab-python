import requests
from bs4 import BeautifulSoup
import urllib

# 접속할 사이트(웹 서버) 주소
url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D'

# 사이트(웹 서버)로 요청(request)를 보냄
html = requests.get(url).text.strip() # 요청의 결과(응담,response- HTML을 저장)
print(html[0:100])

#BeautifulSoup 객체를 생성
soup = BeautifulSoup(html,'html5lib')

#HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
links = soup.find_all('a')
for link in links:
    print(link.get('href'))




# 관심 있는 링크(뉴스 들만 찾을 수 있는 방법을 고민)
div_coll_cont = soup.find_all(class_='coll_cont')
# soup.find_all(attrs={'class': 'call_cont'})
print(len(div_coll_cont)) # 같은 클래스 이름이 있는 모든 HTML 요소들을 찾음

print()
# HTML 하위 요소(sub/child element)를 찾는 방법:
# 1) parent_select > child_select (바로 아래쪽에 있는 element만 찾을수 있음)
#       div > ul > li
#       .call_cont > #clusterResultUL > .fst
# 2) ancestar_selector descendant_selector (아래 어디있는 element 모두 찾을 수있음)
#       div li
#       .coll_cont .fst(클래스 .call-cont 요소의 자손 요소들 중 클래스가.fst 인 요소)
# soup.select(css_selector): soup 객체에서 CSS 선택자료 요소들을 찾는 방법
news_link = soup.select('.coll_cont ul li a.f_link_b')
for link in news_link:
    print(link.get('href'))

