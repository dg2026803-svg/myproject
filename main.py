Web VPython 3.2
box(pos=vec(40, 0, 40), length=8, height=2, width=10, color=color.white,opacity=0.5)
box(pos=vec(0,-1,0), length=100, height=0.5, width=100, color=color.green)
c = cone(pos=vec(2, 0, 0), axis=vec(0, 5, 0), radius=2, color=color.red)
b = sphere(radius=1.5, pos = vec(-5,0,0))
while True :
    rate(100)
    k=keysdown()
    if ' ' in k :
        b.pos=vec(0,0,0)
    if 'a'in k :
        b.pos.x = b.pos.x - 0.1
        if mag(c.pos - b.pos) < 4.5 : 
            b.color = color.red
            
    
    if 'd'in k and mag(c.pos - b.pos) > 3.5:
        b.pos.x = b.pos.x + 0.1
    if 'w'in k and mag(c.pos - b.pos) > 3.5:
        b.pos.z = b.pos.z - 0.1
    if 's'in k and mag(c.pos - b.pos) > 3.5:
        b.pos.z = b.pos.z + 0.1


