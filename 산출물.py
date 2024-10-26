from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Player(FirstPersonController):
    def __init__(slef):
        super().__init__(
            speed = 10,
            model = 'cube',
            collider = 'box',
            scale =1
        )

player = FirstPersonController()


#땅
ground1 = Entity(
    model = 'plane',
    color = color.gray,
    position = (0,0,0),
    scale = (200,1,200),
    collider = 'mesh'
)

def update():
    if player.intersects(ground1).hit:
        player.position = (0, 0, 0)
#다시 돌아가는 땅
ground2 = Entity(
    model = 'plane',
    color = color.gray,
    position = (0,0,0),
    scale = (3,1,3),
    collider = 'mesh'
)





#땅-1층 계단

i=0
for i in range(4):
    ground = Entity(
        model = 'cube',
        color = color.green,
        position = (2+(i*5),1+i,0),
        scale = (3,1,3),
        collider = 'box'
    )

for i in range(2):
    ground = Entity(
        model = 'cube',
        color = color.green,
        position = (17,5+i,5+i*5),
        scale = (3,1,3),
        collider = 'box'
    )
for i in range(0,4):
    ground = Entity(
        model = 'cube',
        color = color.green,
        position = (17+(i*5),7+(i*0.5),13),
        scale = (3,0.1,3),
        collider = 'box'
    )

ground = Entity(
        model='cube',
        color=color.blue,
        position=(10, 1, 0),  # 원하는 위치
        scale=(1, 2, 1),
        collider='box',
        is_trigger=True
)
ground = Entity(
    model = 'cube',
    color = color.green,
    position = (37,9,13),
    scale = (3,0.1,9),
    collider = 'box'
)

ground = Entity(
    model = 'cube',
    color = color.red,
    position = (43,9,13),
    scale = (6,0.1,3),
    collider = 'box'
)

ground = Entity(
    model = 'cube',
    color = color.yellow,
    position = (43,9,16),
    scale = (6,0.1,3),
    collider = 'box'
)

ground = Entity(
    model = 'cube',
    color = color.blue,
    position = (43,9,10),
    scale = (6,0.1,3),
    collider = 'box'
)

ground = Entity(
    model = 'cube',
    color = color.green,
    position = (49,9,16),
    scale = (3,0.1,3)
)

ground = Entity(
    model = 'sphere',
    color = color.yellow,
    position = (49,9,20),
    scale = (2,2,2)
)


app.run()