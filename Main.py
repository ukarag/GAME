#main game

import pygame as pg
import random
from Settings import *
from Sprites import *
from os import path
import sys
from os import path
from tilemap import *

class Game:
    def __init__(self):
        #initialize game
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.running = True

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, "map.txt"))

    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()

        self.walls = pg.sprite.Group()
        # enumerate gives row the index and tiles the value of the item
        # Y - Axis
        for row, tiles in enumerate(self.map.data):
            # X - Axis
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)
                if tile == "P":
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        #Update Game Loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def events(self):
        #game events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

            #if event.key == pg.K_UP or event.key == pg.K_w:
                #self.player.jump()
            #if event.key == pg.K_SPACE:
                #self.player.shoot()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, BLACK, (0, y), (WIDTH, y))

    def draw(self):
        #Draw/Render
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # flip display AFTER drawing everything
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_game_over_screen(self):
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_game_over_screen()
    pg.quit()
