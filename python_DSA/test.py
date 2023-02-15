 # x = [1,2,3,4]

#
x = [1,2,3,4]
i = len(x)-1
w = x
while i >= 0:

    w += [x[i]]
    i -= 1


print(w)


a = ["hi","happy","new","year"]

dic = {}
for i in a:
    c =0
    d = ""
    for j in i:
        d += chr(ord(j)-28)
        c += 1


    dic[d] = c
print(dic)

print()



