a=[[0, 0], [0, 2120], [1210, 0], [0, 800], [3100, 0], [0, 800], [1450, 0], [0, 2120], [440, 0]]
scalehalf=[]
scaleonenhalf=[]
for i in range(len(a)):
    c=[]
    d=[]
    for j in range(2):
        c.append(int(a[i][j]*1.5))
        d.append(int(a[i][j]*0.5))
    scaleonenhalf.append(c)
    scalehalf.append(d)
print(scalehalf,scaleonenhalf)