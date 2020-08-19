import requests
from bs4 import BeautifulSoup
def timesofindia():
    url = "https://www.indiatoday.in/topic/delhi"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    print(soup)
    # div=soup.find_all('div',{'class':'content'})
    # div=soup.find_all('div',{'id':'c_articlelist_stories_2'})
    # div1=soup.find_all('ul',{'class':'list5 clearfix'})
    # div2=soup.find_all('span',{'class':'w_tle'})
    # print(div2)
    # for i in range(0,len(div2)):

    #     print(div2[i])

    # div3=div2[3]
    # div4=div2.find("a")
    # print(len(div2))
    # for i in range(0,len(div2)):
    #     div3=div2[1]
    #     print(div3)
    #     print("========")

    # div=soup.find_all('ul',{'class':'list5 clearfix'})



    # try:
    #     for i in div:
    #         url1=i.find_all("span")
    #         url2=url1['href']
    #         url3="https://timesofindia.indiatimes.com"
    #         url4=url3+url2
    #         print(url4)
    #         # print(url1)


    #         # url1=i.find_all("li")
    #         # url2=url1.find("span")

    #         # print(url2)
            
    #         print("0--------------------------------------------------------------------------------")
    # except Exception as e:
    #     print(e)



    # counter = 0
    # for divtag in soup.find_all('div', {'class': 'content'}):
    #     for ultag in divtag.find_all('span', {'class': 'title'}):
    #         if (counter <= 10):
    #             for litag in ultag.find_all('li'):
    #                 counter = counter + 1
    #                 print(str(counter) + " - https://timesofindia.indiatimes.com" + litag.find('a')['href'])
    #                 print("0--------------------------------------------------------------------------------")
    #                 # print(str(counter) + "." + litag.text + " - https://timesofindia.indiatimes.com" + litag.find('a')['href'])

if __name__ == "__main__":
    timesofindia()






