import pgzrun
import random

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ['bag','battery','bottle','chips']

game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global items,current_level,game_over,game_complete
    screen.clear()
    screen.blit('background', (0,0))

def update():
    pass


def get_option(extra_items):
    items_to_create = ["paper"]
    for i in range(extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option +'img')
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) +1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos = (index +1) *gap_size
        item.x = new_x_pos





        
                    































pgzrun.go()