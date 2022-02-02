
n=int(input("Enter the number: "))
m=(n*(n*n + 1))//2  # int object is not callable
print("sum of a row or column or diagonal: ",m)
matrix1=[ [0]*n for i in range(n) ]

p,q=(n//2),n-1
matrix1[p][q]=1
for i in range(2,n**2 +1):

    p,q=p-1,q+1

    if p==-1 and q==n:
        p,q=0,n-2
       
    if p==-1:
        p=n-1
       
    if q==n:
        q=0
           
    if matrix1[p][q]!=0:
        print(matrix1[p][q])
        p,q=p+1,q-2

    matrix1[p][q]=i
    print("( ",p,",",q," )",matrix1[p][q],"\n")
    print(matrix1)


for i in range(n):
    for j in range(n):
        print(matrix1[i][j],end=" ")
    print()
