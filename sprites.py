import pygame
from settings import *
import math
import random


class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        # wyliczanie pozycji
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # przechowywanie zmian dotyczących ruchu gracza
        self.x_speed = 0
        self.y_speed = 0

        # ustawienie pozycji patrzenia gracza
        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_sprite.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()

        self.rect.x += self.x_speed
        self.collission('x')
        self.rect.y += self.y_speed
        self.collission('y')

        self.x_speed = 0
        self.y_speed = 0

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_speed -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_speed += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_speed -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_speed += PLAYER_SPEED
            self.facing = 'down'

    def collission(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_speed > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_speed < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED

        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_speed > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_speed < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED

    def animate(self):
        down_animations = [self.game.character_sprite.get_sprite(0, 0, self.width, self.height),
                           self.game.character_sprite.get_sprite(32, 0, self.width, self.height),
                           self.game.character_sprite.get_sprite(64, 0, self.width, self.height)]

        up_animations = [self.game.character_sprite.get_sprite(0, 32, self.width, self.height),
                         self.game.character_sprite.get_sprite(32, 32, self.width, self.height),
                         self.game.character_sprite.get_sprite(64, 32, self.width, self.height)]

        left_animations = [self.game.character_sprite.get_sprite(0, 96, self.width, self.height),
                           self.game.character_sprite.get_sprite(32, 96, self.width, self.height),
                           self.game.character_sprite.get_sprite(64, 96, self.width, self.height)]

        right_animations = [self.game.character_sprite.get_sprite(0, 64, self.width, self.height),
                            self.game.character_sprite.get_sprite(32, 64, self.width, self.height),
                            self.game.character_sprite.get_sprite(64, 64, self.width, self.height)]
        if self.facing == 'down':
            if self.y_speed == 0:
                self.image = self.game.character_sprite.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == 'up':
            if self.y_speed == 0:
                self.image = self.game.character_sprite.get_sprite(0, 32, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == 'right':
            if self.x_speed == 0:
                self.image = self.game.character_sprite.get_sprite(0, 64, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == 'left':
            if self.x_speed == 0:
                self.image = self.game.character_sprite.get_sprite(0, 96, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_speed = 0
        self.y_speed = 0

        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(20, 40)

        self.image = self.game.enemies_sprite.get_sprite(3, 2, self.width, self.height)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.aniamte()

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        self.x_speed = 0
        self.y_speed = 0

    def movement(self):
        if self.facing == 'left':
            self.x_speed -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'

        if self.facing == 'right':
            self.x_speed += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'

    def aniamte(self):
        left_animations = [self.game.enemies_sprite.get_sprite(0, 96, self.width, self.height),
                           self.game.enemies_sprite.get_sprite(32, 96, self.width, self.height),
                           self.game.enemies_sprite.get_sprite(64, 96, self.width, self.height)]

        right_animations = [self.game.enemies_sprite.get_sprite(0, 64, self.width, self.height),
                            self.game.enemies_sprite.get_sprite(32, 64, self.width, self.height),
                            self.game.enemies_sprite.get_sprite(64, 64, self.width, self.height)]
        if self.facing == 'right':
            if self.x_speed == 0:
                self.image = self.game.enemies_sprite.get_sprite(0, 64, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == 'left':
            if self.x_speed == 0:
                self.image = self.game.enemies_sprite.get_sprite(0, 96, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.block_sprite.get_sprite(960, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_sprite.get_sprite(64, 64, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_sprite.get_sprite(192, 128, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Button:
    def __init__(self, x, y, width, height, foreground, background, content, fontsize):
        self.font = pygame.font.Font('ArialTh.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = foreground
        self.bg = background

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE

        self.animation_loop = 0
        self.image = self.game.attack_sprite.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)

    def animate(self):
        direction = self.game.player.facing

        right_animations = [self.game.attack_sprite.get_sprite(0, 64, self.width, self.height),
                            self.game.attack_sprite.get_sprite(32, 64, self.width, self.height),
                            self.game.attack_sprite.get_sprite(64, 64, self.width, self.height),
                            self.game.attack_sprite.get_sprite(96, 64, self.width, self.height),
                            self.game.attack_sprite.get_sprite(128, 64, self.width, self.height)]

        down_animations = [self.game.attack_sprite.get_sprite(0, 32, self.width, self.height),
                           self.game.attack_sprite.get_sprite(32, 32, self.width, self.height),
                           self.game.attack_sprite.get_sprite(64, 32, self.width, self.height),
                           self.game.attack_sprite.get_sprite(96, 32, self.width, self.height),
                           self.game.attack_sprite.get_sprite(128, 32, self.width, self.height)]

        left_animations = [self.game.attack_sprite.get_sprite(0, 96, self.width, self.height),
                           self.game.attack_sprite.get_sprite(32, 96, self.width, self.height),
                           self.game.attack_sprite.get_sprite(64, 96, self.width, self.height),
                           self.game.attack_sprite.get_sprite(96, 96, self.width, self.height),
                           self.game.attack_sprite.get_sprite(128, 96, self.width, self.height)]

        up_animations = [self.game.attack_sprite.get_sprite(0, 0, self.width, self.height),
                         self.game.attack_sprite.get_sprite(32, 0, self.width, self.height),
                         self.game.attack_sprite.get_sprite(64, 0, self.width, self.height),
                         self.game.attack_sprite.get_sprite(96, 0, self.width, self.height),
                         self.game.attack_sprite.get_sprite(128, 0, self.width, self.height)]

        if direction == 'up':
            self.image = up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == 'down':
            self.image = down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == 'right':
            self.image = right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == 'left':
            self.image = left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

