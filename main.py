Web VPython 3.2
box(pos=vec(0, 0, 0), length=10, height=2, width=1, color=color.white)
box(pos=vec(0,-1,0), length=100, height=0.5, width=100, color=color.green)
cone(pos=vec(0, 1, 4), axis=vec(0, 2, 1), radius=1, color=color.red)
b = sphere(radius=3)
while True :
    rate(100)
    k=keysdown()
    if ' 'in k:
        b.pos=vec(0,0,0)
    if 'a'in k:
        b.pos.x = b.pos.x - 0.1
    if 'd'in k:
        b.pos.x = b.pos.x + 0.1
    if 'w'in k:
        b.pos.z = b.pos.z - 0.1
    if 's'in k:
        b.pos.z = b.pos.z + 0.1
  


