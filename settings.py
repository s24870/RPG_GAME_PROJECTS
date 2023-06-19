#Główne zmienne gry
WIDTH = 1280
HEIGHT = 704
FPS = 60
TILESIZE = 32

PLAYER_SPEED = 3
ENEMY_SPEED = 4

PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

BLACK = (0,0,0)
WHITE = (255,255,255)


tilemap = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOEOOOOOOOOOOOOOOOOOOOEOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOBBBOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOEOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOBBOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOBOOOOOOOOOOOOOOOOBOOOBOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOBOOOOOOOOOOOOOOOOBOOOBOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOBOOOOOOOOOOOOOOOOBBBBBOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOBBBBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOEOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOEOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOEOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',



]