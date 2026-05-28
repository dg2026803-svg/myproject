Web VPython 3.2
import random
box(pos=vec(1, 0, 40), length=60, height=2, width=10, color=color.white,opacity=0.5)
box(pos=vec(0,-1,0), length=100, height=0.5, width=100, color=color.green)

c = cone(pos=vec(4, 0, 7), axis=vec(0, 5, 0), radius=2, color=color.red)
c2 = cone(pos=vec(9, 0, 1), axis=vec(0, 5, 0), radius=2, color=color.red)
c3 = cone(pos=vec(2, 0, 29), axis=vec(0, 5, 0), radius=2, color=color.red)
c4 = cone(pos=vec(4, 0, 1), axis=vec(0, 5, 0), radius=2, color=color.red)
c5 = cone(pos=vec(7, 0, 20), axis=vec(0, 5, 0), radius=2, color=color.red)
c6 = cone(pos=vec(23, 0, 16), axis=vec(0, 5, 0), radius=2, color=color.red)
c7 = cone(pos=vec(29, 0, 2), axis=vec(0, 5, 0), radius=2, color=color.red)
c8 = cone(pos=vec(3, 0, 29), axis=vec(0, 5, 0), radius=2, color=color.red)
c9 = cone(pos=vec(15, 0, 1), axis=vec(0, 5, 0), radius=2, color=color.red)
c10 = cone(pos=vec(20, 0, 20), axis=vec(0, 5, 0), radius=2, color=color.red)
c11 = cone(pos=vec(4, 0, 32), axis=vec(0, 5, 0), radius=2, color=color.red)
c12 = cone(pos=vec(29, 0, 12), axis=vec(0, 5, 0), radius=2, color=color.red)
c13 = cone(pos=vec(2, 0, 29), axis=vec(0, 5, 0), radius=2, color=color.red)
c14 = cone(pos=vec(23, 0, 1), axis=vec(0, 5, 0), radius=2, color=color.red)
c15 = cone(pos=vec(11, 0, 20), axis=vec(0, 5, 0), radius=2, color=color.red)
cones = [c,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15]

b = sphere(radius=1.5, pos = vec(-45,0,-45))
while True :
    rate(100)
    k=keysdown()
       
    if ' ' in k :
        rate(5)
        b.pos=vec(-45,0,-45)
        for c in cones :
            c.pos.x = random.uniform(-45,45)
            c.pos.z = random.uniform(-45,30)
        
   
    if 'a' in k :
        b.pos.x = b.pos.x - 0.1
        for c in cones : 
            c.color = color.blue
    if 'd' in k:
        b.pos.x = b.pos.x + 0.1
        for c in cones : 
            c.color = color.red
    if 'w' in k:
        b.pos.z = b.pos.z - 0.1
        for c in cones : 
            c.color = color.green
    if 's' in k:
        b.pos.z = b.pos.z + 0.1
        for c in cones : 
            c.color = color.black
        for c in cones:
            if mag(c.pos-b.pos)<3.5:
               b.pos.x = random.uniform(-45,50)
               b.pos.z = random.uniform(-45,50)
        

