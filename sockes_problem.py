string1=input("enter String")
count=0
for i in range(0,len(string1)):
   for j in range(i+1,len(string1)):
       if(string1[i]==string1[j]):
           count+=1
if(count%2==0):
    print("false")
else:
    print("true")