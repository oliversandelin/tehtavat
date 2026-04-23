import math

def create_point(x,y):
    return(x,y)

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
print("anna ensimmäinen pistee kordinaatti")
x1 =float(input("pistee kordinaatti: "))
y1 =float(input("pistee kordinaatti: "))
piste1 = create_point(x1,y1)

print("anna toisen pisteen kordinaatti")
x2 =float(input("pistee kordinaatti: "))
y2 =float(input("pistee kordinaatti: "))
piste2 = create_point(x2,y2)

etäisyys = distance(piste1,piste2)
print(etäisyys)