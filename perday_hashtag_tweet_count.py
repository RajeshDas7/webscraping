import csv
i=0
j=0
temp='xx'
temp1='xx'
with open('hashtagDATA.csv','r',encoding='utf-8') as inp:
    for row in csv.reader(inp):
        if row:

        
            if len(row[1])>0:
                i+=1
                # print(i,row[0])
                try:
                    q = row[1].split(' ')
                    if q[0] !=temp:
                        print(row[0],temp,j)
                        temp=q[0] 
                        j=0     
                    # print(q[0])
                    if q[0] == temp:
                        
                        j+=1
                    
                    # if i == 5:
                    #     break
                except Exception as e:
                    print(e)
            
        # else:
        #     print("--")

# print(temp,j)
