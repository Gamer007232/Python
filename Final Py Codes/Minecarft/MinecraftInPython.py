from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController


boxes = []
for n in range(8):
    for k in range(8):
        box = Button(
            parent= scene,
            model= 'cube',
            origin_y= 8.5,
            texture= 'white_cube',
            color= color.orange,
            highlight_color= color.lime,
            position= (k,0,n)
        )
        boxes.append(box)

def input(key):
    for box in boxes:
        if box.hovered:
            if key== 'left mouse down':
                newBox = Button(
                    parent= scene,
                model= 'cube',
                origin_y= 8.5,
                texture= 'white_cube',
                color= color.orange,
                highlight_color= color.lime,
                position= box.position + mouse.normal

                )
                box.append(newBox)
            if key== 'right mouse down':
                boxes.remove(box)
                destroy(box)



app = Ursina()
Sky()
player = FirstPersonController()

app.run()