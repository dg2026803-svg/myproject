Web VPython 3.2
box(pos=vec(1, 0, 40), length=60, height=2, width=10, color=color.white,opacity=0.5)
box(pos=vec(0,-1,0), length=100, height=0.5, width=100, color=color.green)
c = cone(pos=vec(2, 0, 0), axis=vec(0, 5, 0), radius=2, color=color.red)
c2 = cone(pos=vec(4, 0, 9), axis=vec(0, 5, 0), radius=2, color=color.red)
c3 = cone(pos=vec(4, 0, 15), axis=vec(0, 5, 0), radius=2, color=color.red)
c4 = cone(pos=vec(4, 0,24), axis=vec(0, 5, 0), radius=2, color=color.red)
c5 = cone(pos=vec(14, 0, 9), axis=vec(0, 5, 0), radius=2, color=color.red)
cones = [c,c2,c3,c4,c5]
b = sphere(radius=1.5, pos = vec(-5,0,0))
while True :
    rate(100)
    k=keysdown()
        
    if ' ' in k :
        b.pos=vec(35,0,0)
    if 'a'in k and mag(c.pos - b.pos) > 3.5  :
        b.pos.x = b.pos.x - 0.1
        for c in cones : 
            c.color = color.blue
        if mag(c.pos - b.pos) < 4.5 : 
            b.color = color.white
    
    if 'd'in k and mag(c.pos - b.pos) > 3.5:
        b.pos.x = b.pos.x + 0.1
        for c in cones : 
            c.color = color.red
        if mag(c.pos - b.pos) < 4.5 : 
            b.color = color.white
    if 'w'in k and mag(c.pos - b.pos) > 3.5:
        b.pos.z = b.pos.z - 0.1
        for c in cones : 
            c.color = color.green
        if mag(c.pos - b.pos) < 4.5 : 
            b.color = color.white
    if 's'in k and mag(c.pos - b.pos) > 3.5:
        b.pos.z = b.pos.z + 0.1
        for c in cones : 
            c.color = color.black
        if mag(c.pos - b.pos) < 4.5 : 
            b.color = color.white

