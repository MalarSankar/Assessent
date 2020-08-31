list1=[1,7,-1,5,5]
sum=6
count=0

print("the pairs are")
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[i]+list1[j]==sum):
           count+=1
           print("(",list1[i],list1[j],")")

print("output",count)
