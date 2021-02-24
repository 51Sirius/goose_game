import pygame as pg

first_color = (248, 243, 212)
second_color = (0, 184, 169)
third_color = (246, 65, 108)
four_color = (255, 222, 125)
display_size = (1000, 600)
display = pg.display.set_mode(display_size)
pg.init()
clock = pg.time.Clock()
pg.display.set_caption('Goose Game')


def move_goose(front, goose_surf, goose_rect, goose_pos):
    if front == 0:
        goose_surf = pg.image.load('goose/stop1.png')
        goose_rect = goose_surf.get_rect(center=tuple(goose_pos))
    elif front == 1:
        goose_surf = pg.image.load('goose/forward1.png')
        goose_pos[1] = goose_pos[1] - 2
        goose_rect = goose_surf.get_rect(center=tuple(goose_pos))
    elif front == 2:
        goose_surf = pg.image.load('goose/forward_down1.png')
        goose_pos[1] = goose_pos[1] + 2
        goose_rect = goose_surf.get_rect(center=tuple(goose_pos))
    elif front == 3:
        goose_surf = pg.image.load('goose/left1.png')
        goose_pos[0] = goose_pos[0] - 2
        goose_rect = goose_surf.get_rect(center=tuple(goose_pos))
    elif front == 4:
        goose_surf = pg.image.load('goose/right1.png')
        goose_pos[0] = goose_pos[0] + 2
        goose_rect = goose_surf.get_rect(center=tuple(goose_pos))
    return goose_surf, goose_rect, goose_pos


def move(event: pg.event.poll(), front_move, front):
    if event.type == pg.KEYDOWN:
        front_move = True
        if event.unicode == 'w' or event.unicode == 'W':
            front = 1
        elif event.unicode == 's' or event.unicode == 'S':
            front = 2
        elif event.unicode == 'a' or event.unicode == 'A':
            front = 3
        elif event.unicode == 'd' or event.unicode == 'D':
            front = 4
    if event.type == pg.KEYUP:
        front_move = False
        front = 0
    return front, front_move


def start_game():
    front_move = False
    front = 0
    goose_position = [15, 570]
    start_position = tuple(goose_position)
    goose_surf = pg.image.load('goose/forward1.png')
    goose_rect = goose_surf.get_rect(center=start_position)
    show_menu = True
    while show_menu:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            exit()
        display.fill(first_color)
        display.blit(goose_surf, goose_rect)
        front, front_move = move(event, front_move, front)
        goose_surf, goose_rect, goose_position = move_goose(front, goose_surf, goose_rect, goose_position)
        pg.display.update()
        clock.tick(60)


start_game()