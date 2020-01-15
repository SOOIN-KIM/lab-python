'''
' 빅데이터 분석' 단어가 포함된 회사 채용 리스트 100개 출력
'''
import requests
from bs4 import BeautifulSoup


def find_keyword(keyword):
    url = 'http://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=auto&recruitSort=relation&recruitPageCount=40&inner_com_type=&company_cd=0,1,2,3,4,5,6,7,9'
    for page in range(1,10):
        print(f'=== Page {page} ===')
        # 쿼리 스트링(query string)의 파라미터 설정
        req_params={
            'searchword' : keyword,
            'recruitPage' : page
        }
        response = requests.get(url,params=req_params)
        html = response.text.strip()

        soup = BeautifulSoup(html,'html5lib')
        results = soup.select('.section_search h2 a')
        for link in results:
            print(link.text)
        # for link in results:
        #     company_list = link.get('href')
        #     print(company_list)

if __name__ == '__main__':
    find_keyword('빅데이터')
