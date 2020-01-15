'''
1) csv 파일(stock_price.csv) write
6/20/2019,AAPL,90.91
6/20/2019,MSFT,41.68
6/21/2019,AAPL,90.86
6/21/2019,MSFT,41.51

2) csv 파일을 csv.reader를 사용해서 파일의 내용을 리스트로 변환
각 주식 종목의 주식 가격 평균을 계산해서 출력

3) csv파일을 csv.DictReader를 사용해서 파일의 내용을 리스트로 변환
각 주식 종목의 주식 가격 평균을 계산해서 출력


'''
import csv
import os

row1 = ['6/20/2019','AAPL',90.91]
row2 = ['6/20/2019','MSFT',41.68]
row3 = ['6/21/2019','AAPL',90.86]
row4 = ['6/21/2019','MSFT',41.51]
result=[row1,row2,row3,row4]

#1)
with open('stock_price.csv', mode='w', encoding ='UTF-8', newline='') as f:
    writer = csv.writer(f, delimiter = ',')
    for row in result:
        # writer 객체의 writterow() 메소드를 사용해서 한 줄씩 쓰기
        writer.writerow(row)

#2)
with open('stock_price.csv', mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    row = [row for row in reader]
print(row)

# 'AAPL' 종목의 주식 가격들의 리스트
aapl_prices = [float(item[2]) for item in row
               if item[1] == 'AAPL']
print(aapl_prices)
aapl_mean = sum(aapl_prices) / len(aapl_prices)
print('aapl_mean:', aapl_mean)

msft_prices = [float(item[2]) for item in row
        if item[1] == 'MSFT']
msft_mean = sum(msft_prices) / len(msft_prices)
print('msft_mean:', msft_mean)


#3)
file_path = os.path.join('', 'stock_price.csv')
with open(file_path, mode='r', encoding='UTF-8') as f:
    reader= csv.DictReader(f, fieldnames=('Date','Company','Price'))
    df = [row for row in reader]
print(df)
aapl_prices = [float(item['Price']) for item in df
                if item['Company'] == 'AAPL']
print(aapl_prices)
aapl_mean = sum(aapl_prices) / len(aapl_prices)
print(aapl_mean)
msft_prices = [float(item['Price']) for item in df
               if item['Company'] == 'MSFT']
print(msft_prices)
msft = sum(msft_prices) / len(msft_prices)
print(msft_mean)