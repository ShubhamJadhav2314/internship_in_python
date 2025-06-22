#task
marks=[]
n=int(input("how many subject  :"))

for i in range(n):
    mark=int(input(f"enter the sub mark {i+1}   :"))
    if mark < 0 or mark > 100:
        print("Invalid marks")
        exit()
    marks.append(mark)

fails=0
for m in marks:
    if  m<40:
        fails+=1  

if fails> 2:
    print("failed")      
elif fails > 0:
    print("atkt")  
else:
    sum=sum(marks)
    print("total :",sum)
    per=sum/n
    print(f"per : {per}%")
    if per >=75:
        print("grade : A")
    elif per >=60: 
        print("grade : b")
    else:
        print("grade : c")

            