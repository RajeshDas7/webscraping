import csv
import pageviewapi


with open('party_name.csv','r',encoding='utf-8') as inp, open('qwer.csv','w') as out:
    writer=csv.writer(out)
    s=0
    for row in csv.reader(inp):
        if row:
            try:
                s+=1v = pageviewapi.per_article('en.wikipedia', row[0], '20151106','20191120', access='all-access', agent='all-agents', granularity='daily')
                for i in v['items']:
                    
                    list1=[]
                    list1.append(row[0])
                    list1.append(i['timestamp'])
                    list1.append(i['views'])
                    
                    writer.writerow(list1)
                    print(list1)
            except Exception as e:
                print(e)
print("done")
                
    
