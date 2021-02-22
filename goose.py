import pygame as pg

first_color = (248, 243, 212)
second_color = (0, 184, 169)
third_color = (246, 65, 108)
four_color = (255, 222, 125)
display_size = (1000, 600)
goose_surf = pg.image.load('goose/forward1.png')
goose_rect = goose_surf.get_rect(center=(15, 570))
display = pg.display.set_mode(display_size)
pg.init()
clock = pg.time.Clock()
pg.display.set_caption('Goose Game')


def start_game():
    show_menu = True
    while show_menu:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            exit()
        display.fill(first_color)
        display.blit(goose_surf, goose_rect)
        pg.display.update()
        clock.tick(60)


start_game()