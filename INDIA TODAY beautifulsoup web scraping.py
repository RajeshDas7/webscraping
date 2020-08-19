from bs4 import BeautifulSoup
from urllib.request import urlopen
dict={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
import csv
sz=0
# https://www.ndtv.com/page/topic-load-more?+type=news&page=60&query=kolkata
assmebl=['delhi','chennai','indore']
so=0
with open('1_'+assmebl[so]+'.csv','a') as out:
    writer=csv.writer(out)
    writer.writerow(['story_url','heading','desc','published_date','auther','timestamp','img_link'])
    for ina in range(1,2):
        if ina==1:
            usl='https://www.indiatoday.in/topic/'+assmebl[so]
            print(usl)
        # else:
        #     usl='https://www.indiatoday.in/topic/'+assmebl[so]+'/'+str(ina)
        print(usl)
        html = urlopen(usl).read()
        bs = BeautifulSoup(html, 'html.parser')
        # print(bs)
        ul=bs.findAll('div',{'class':'view-content'})
        # print(ul)
        
        a=[]
        b=[]
        z=0

        for i in bs.findAll('li',{'class':'views-row-odd'}):
            w1=i.find('a')
            w2=w1['href']
            # print(w2)
            # print("^^^^^^^^^^^^^^^^^^^^^^^^^")
            html1 = urlopen(w2).read()
            bs1 = BeautifulSoup(html1, 'html.parser')
            ul1=bs1.findAll('div',{'class':'story-section'})
            for i1 in ul1:

                a.append(i1.findAll('h1',{'itemprop':'headline'}))
            #     print("@@@@@@@@@")
            # print(".................................................")
            

    
        for i in bs.findAll('li',{'class':'views-row-even'}):
            w1=i.find('a')
            w2=w1['href']
            # print(w2)
            # print("^^^^^^^^^^^^^^^^^^^^^^^^^")
            html1 = urlopen(w2).read()
            bs1 = BeautifulSoup(html1, 'html.parser')
            ul1=bs1.findAll('div',{'class':'story-section'})
            for i1 in ul1:

                b.append(i1.findAll('h1',{'itemprop':'headline'}))
            #     print("@@@@@@@@@")
            # print(".................................................")

        print("uuuuuuuuuuuuuuu")
        for i in range(0,len(b)):
            print(a[i])
            print(b[i])
        # for r in range(0,len(a)):
              
        
        # li=ul[0].findAll('span',{'class':'field-content'})
        # # for i in li:
        #     try:
        #         print(sz)
        #         sz+=1
        #         per='https://www.indiatoday.in/'+i.find('a')['href']
        #         html = urlopen(per).read()
        #         bs2 = BeautifulSoup(html, 'html.parser')
        #         h1=bs2.find("span" ,{"class":"title"})
        #         heading=h1.contents[0]
        #         print(h1.contents[0])
        #         print("-------------------------------------------------------------")
        #         story=bs2.find("div" ,{"class":"section1"})
        #         story1=story.find("div")
        #         s=''
        #         for sto in story1:
        #             if(str(sto)[0]!='<' and str(sto)[0]!=' ' and str(sto)[0]!='\n'):
        #                 s+=str(sto)
        #         print(s.strip())
        #         print("----------------------------------------------------------")
        #         time=bs2.find("span", {"class":"time_cptn"})
        #         time2=time.findAll("span")
        #         exact_time=''
        #         if(str(time2[2].contents[0])[0]=='U'):
                
        #             exact_time=(time2[2].contents[0][9:-4])
        #         else:    
        #             exact_time=(time2[2].contents[0][:-4])
        #         print(exact_time)    
        #         auther=time2[1].contents[0]
        #         print(time2[1].contents[0])
        #         sls=exact_time.split(",")
        #         sls1=sls[0].split(" ")
        #         sls1.append(sls[1])
        #         sls1.append(sls[2])
        #         sls1[0]=dict[sls1[0]]
        #         sls1[3]+=':00.0'
        #         string=sls1[1].strip()+'/'+sls1[0]+'/'+sls1[2].strip()+' '+sls1[3].strip()
        #         print(string)

        #         import time 
        #         import datetime 
        #         element = datetime.datetime.strptime(string,"%d/%m/%Y %H:%M:%S.%f") 
                
        #         tuple1 = element.timetuple() 
        #         timestamp = time.mktime(tuple1)*1000
        #         print(timestamp)
        #         print("----------------------------------------------------------")
        #         image=bs2.find("section", {"class":"highlight"} )
        #         img_link='https://www.indiatoday.in'+image.find("img")['src']
        #         print(img_link)
        #         print(usl)
        #         print("******************************"+assmebl[so]+str(sz)+"*****************************")
        #         output=[]
        #         output.append(per)
        #         output.append(heading)
        #         output.append(s.strip())
        #         output.append(exact_time)
        #         output.append(auther)
        #         output.append(timestamp)
        #         output.append(img_link)
        #         writer.writerow(output)
        #     except Exception as e:
        #         print(sz,"-",str(e))
        #         continue
so+=1
out.close()
