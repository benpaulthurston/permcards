import random
def blank(w, h):
    a = []
    for i in range(0, h):
        row = []
        for j in range(0, w):
            row.append(0)
        a.append(row)
    return a
def totuple(a):
    b = ()
    for i in range(0, len(a)):
        ta= tuple(a[i])
        b = b+(ta,)
    return b
    
def upbyrow(a):
    b = []
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            b.append(a[i][j])
    return b

def downbycol(b, w, h, d):
    a = blank(w,h)
    n = 0
    n+=d
    for j in range(0, w):
        for i in range(0, h):
            a[i][j] = b[n]
            n+=1
            n=n%(w*h)
    return a       
    
mats = set()
w = 2
h = 3
a = ((1,2),(3,4),(5,6))
mats.add(a)
iterates = 0
d = 0

while(len(mats)!=720):
    d = random.randint(0,1)
    b = upbyrow(a)
    c = downbycol(b, w, h, d)
    mats.add(totuple(c))
    a = c
    iterates +=1
print(iterates)

