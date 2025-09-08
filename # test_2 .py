# 숫자 계산용 numPy 모듈 불러오기
import numpy as np
# 표로 된 데이터 다루는 pandas 모듈 불러오기
import pandas as pd
# 그래프 그리는 matplotlib 모듈 불러오기
import matplotlib.pyplot as plt
# 데이터베이스에 저장할 수 있게 하는 sqlite3 모듈 불러오기
import matplotlib
matplotlib.rc('font', family='Malgun Gothic')  
import sqlite3
# 웹사이트에서 자료를 가져올 수 있게 해주기
import requests
# 가져온 자료에서 원하는 부분을 뽑을 수 있게 해주기
from bs4 import BeautifulSoup
# 워드 클라우드를 만들어주는 모듈 불러오기 
from wordcloud import WordCloud
# 날짜와 시간 관련 기능 모듈 불러오기
from datetime import datetime, timedelta
# 윈도우용 한글 폰트 불러오기
import matplotlib
matplotlib.rc('font', family='Malgun Gothic') 

# 도시들 지정 및 30일 간의 날짜를 문자열로 바꿔주기
cities = ["Seoul", "Busan", "Incheon", "Daegu", "Gwangju"]
dates = [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(29, -1, -1)]

# 랜덤 숫자를 val로 만들고 날짜, 도시, 랜덤값을 리스트로 만드는데 랜덤값은 음수는 0으로 바꾸고 소수 둘째 자리까지 반올림해주기 
data = []
for city in cities:
    values = np.random.normal(25, 10, 30)
    for date, val in zip(dates, values):
        data.append([date, city, max(round(val, 2), 0)])

# 앞의 data 리스트를 표로 만들고 열 이름을 지정해주기  
df = pd.DataFrame(data, columns=["Date", "City", "PM25"])

# 만든 표를 그룹으로 나누고 도시별 PM25의 평균을 내고 avg_pm25에 저장하기
avg_pm25 = df.groupby("City")["PM25"].mean()

# 막대그래프 출력 및 이름붙이기와 그래프 이미지로 저장
avg_pm25.plot(kind="bar", title="도시별 평균 PM2.5")
plt.ylabel("PM2.5")
plt.tight_layout()
plt.savefig("avg_pm25_bar.png")
plt.close()

# 열에 해당도시의 데이터만 뽑게 해서 선그래프 만들고 이미지 파일로 저장
for city in cities:
    city_data = df[df["City"] == city]
    plt.plot(city_data["Date"], city_data["PM25"], label=city)
plt.xticks(rotation=45)
plt.title("도시별 PM2.5 변화 추이")
plt.xlabel("날짜")
plt.ylabel("PM2.5")
plt.legend()
plt.tight_layout()
plt.savefig("trend_pm25_line.png")
plt.close()

# sqlite3에 db로 저장하고 테이블 지정 해주기
conn = sqlite3.connect("pm25.db")
df.to_sql("AllCities", conn, if_exists="replace", index=False)

# 상위 3개 도시의 데이터만 뽑아 도시 이름으로 된 테이블에 저장해주기
top3 = avg_pm25.sort_values(ascending=False).head(3).index
for city in top3:
    df[df["City"] == city].to_sql(city, conn, if_exists="replace", index=False)

# 5. 웹 사이트에서 문자열만 꺼내와 분석가능 구조로 바꾸고 제목만 추출해서 이어붙이고 에러가 난다면 멈추지 않고 실패만 출력하기
try:
    url = "https://www.boannews.com/media/t_list.asp"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    titles = [t.text.strip() for t in soup.select(".news_list ul li .news_txt a strong")]
    text = " ".join(titles)
    wc = WordCloud(width=800, height=400, background_color="white",
                   font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf").generate(text)
    wc.to_file("news_wordcloud.png")
except:
    print("웹크롤링 실패")

# 데이터베이스 연결을 종료하기
conn.close()