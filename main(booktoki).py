import requests, sys, os
from bs4 import BeautifulSoup

'''

각 회차 주소 모음 html 태그 : 
#content_wrap > div.toon_index > ul > li

책 내용 태그 : #bo_v_con > div.bo_v_toon


sigil이라는 프로그램 형식에 맞춰 파일을 생성하기 때문에, sigil에서 바로 불러오기 한 후 책을 저장하면 됨.

'''
책목차주소 = "" #원하는 소설의 목차 주소를 집어넣기



itemHtml = requests.get(책목차주소, headers={"User-agent":"Mozilla/5.0"}).text
itemSoup = BeautifulSoup(itemHtml, "html.parser")
item = itemSoup.select(".item-subject")

bookInfoList = []
for i, v in enumerate(item):
    # print(v.attrs['href'])
    temp = v.find_all("span")
    try:
        for t in temp:
            t.decompose()
    except:
        pass
    bookInfoList.append((v.attrs['href'], v.text.strip()))
bookInfoList.reverse()

책이름 = "" #책 이름 넣기
finalContent = ''
count = 1
for i, v in enumerate(bookInfoList):
    bookHtml = requests.get(v[0], headers={"User-agent":"Mozilla/5.0"}).text
    bookSoup = BeautifulSoup(bookHtml, "html.parser")
    content = bookSoup.select_one("#novel_content > div:nth-child(2)")
    finalContent += '<hr class="sigil_split_marker" /><h1>' + v[1] + "</h1>" + str(content)[25:-7] + "\n\n"
    print(f"\n\n\033[31m{count}번째 완료!!!!!\033[0m")
    count += 1
with open(os.path.join(__file__, f"../{책이름}.html"), "w", encoding="utf-8") as f:
    f.write(finalContent)




