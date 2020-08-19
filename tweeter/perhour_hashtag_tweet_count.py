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
                        
                        temp=q[0] 
                        j=0     
                    # print(q[0])
                    if q[0] == temp:
                        ww=q[1]
                        wq=ww.split(":")
                        if wq[0]!=temp1:
                            temp1=wq[0]
                            print(row[0], temp,temp1, j)
                            j =0



                        
                        
                        # qqq1=wqq.split(":")
                        # print(qqq1)
                        j+=1
                    
                    # if i == 5:
                    #     break
                except Exception as e:
                    print(e)
            
        # else:
        #     print("--")

# print(temp,j)
