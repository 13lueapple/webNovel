import requests, sys, os
from bs4 import BeautifulSoup


'''

각 회차 주소 모음 html 태그 : #content_wrap > div.toon_index > ul
#content_wrap > div.toon_index > ul > li

책 내용 태그 : #bo_v_con > div.bo_v_toon


sigil이라는 프로그램 형식에 맞춰 파일을 생성하기 때문에, sigil에서 바로 불러오기 한 후 책을 저장하면 됨.

'''
책목차주소 = "" #책 목차 주소를 집어넣기



itemHtml = requests.get(책목차주소).text
itemSoup = BeautifulSoup(itemHtml, "html.parser")
item = (itemSoup.select("#content_wrap > div.toon_index > ul > li > a"))

# print(item)
bookInfoList = []
for i, v in enumerate(item):
    # print(item[i].attrs['href'][-7:])
    # print(item[i].text[:-10])
    bookInfoList.append((v.attrs['href'][-7:], v.text[:-10]))

bookInfoList.reverse()
# print(bookInfoList)

baseUrl = 책목차주소
책이름 = "" # 책 이름 집어넣기
with open(os.path.join(__file__, f"../{책이름}.html"), "w", encoding="utf-8") as f:
    finalContent = ''
    for i, v in enumerate(bookInfoList):
        eachBookUrl = baseUrl +"/"+ v[0]
        eachBookHtml = requests.get(eachBookUrl).text
        eachBookSoup = BeautifulSoup(eachBookHtml, "html.parser")
        content = eachBookSoup.select_one("#bo_v_con > div.bo_v_toon")
        finalContent += '<hr class="sigil_split_marker" /><h1>'+v[1]+"</h1>"+ "\n" + str(content).replace('<div class="bo_v_toon">\n', '').replace('</div>', '') + "\n\n"
        print(f"\n\n\033[31m{i+1}번째 완료!!!!!\033[0m")
    f.write(finalContent)

