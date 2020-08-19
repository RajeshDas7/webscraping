# from bs4 import BeautifulSoup
# from urllib.request import urlopen
import csv
import time
from datetime import datetime

with open('ENTITIES_WIKI.csv', 'r',encoding='utf-8' ) as inp : #open('wiki_name_1.csv', 'w',encoding='utf-8') as out:
    list1=[]
    list2=[]
##    writer = csv.writer(out)
    for row in csv.reader(inp):
        print(row[1])
    #     a=row[0]
    #     b=a.split("/")
    #     list1.append(b[4])
    # for i in list1:
    #     list3=[]
    #     # print(type(i))
    #     x=str(i).replace("_"," ")
    #     list3.append(x)
    #     writer.writerow(list3)
    #     # print(list3)
    #     # list2.append(x)

    # # for i in list2:
    # #     writer.writerow(i)
