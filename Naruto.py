from pathlib import Path
import pygame
import json


class Naruto(pygame.sprite.Sprite):
    BG_COLOR = (0, 64, 128)
    PATH_BASE = "./{action}/{action}{frame}.png"
    with open('./pixel_coords.json') as f:
        COORDS = json.load(f)

    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load("Naruto.png")
        # frame vals
        self.frame_num = 0
        self.frames = self._get_frames('stance')
        self.image = self.frames[0]
        self.rect = self.image.get_rect(midbottom=(100, 905))
        self.direction_right = True

    def update(self):
        self._idle_animation()
        self._user_input()

    def _user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.bottom = 925
            self.direction_right = True
            self._run(speed=5)
        elif keys[pygame.K_LEFT]:
            self.rect.bottom = 925
            self.direction_right = False
            self._run(speed=5)
        else:
            self.rect.bottom = 905
            self._idle()

    def _get_frames(self, action):
        """
        all same width and height = (max_width, max_height)
        y = the lowest y
        x = need to adjust accordingly. sometimes need + 1 - 1 depending on width
        """
        images = []
        for coord in self.COORDS[action]:
            image = pygame.Surface((coord["w"], coord["h"])).convert_alpha()
            image.blit(self.sprite_sheet, (0, 0), (coord["x"], coord["y"], coord["w"], coord["h"]))
            image = pygame.transform.scale2x(image)
            image.set_colorkey(self.BG_COLOR)
            images.append(image)

        return images

    def _run(self, speed=3):
        if self.direction_right:
            self.rect.right += speed
        else:
            self.rect.left -= speed

        self.frames = self._get_frames('run')
        self._run_animation(speed=0.05)

    def _run_animation(self, speed=0.1):
        self.frame_num += speed

        if self.frame_num >= len(self.frames):
            self.frame_num = 0

        image = self.frames[int(self.frame_num)]
        if not self.direction_right:
            image = pygame.transform.flip(self.frames[int(self.frame_num)], True, False).convert_alpha()
            image.set_colorkey(self.BG_COLOR)

        self.image = image

    def _idle(self):
        self.frames = self._get_frames('stance')
        self._idle_animation(speed=0.05)

    def _idle_animation(self, speed=0.1):
        self.frame_num += speed

        # restart animation from frame 1 if reach end
        if self.frame_num >= len(self.frames):
            self.frame_num = 0

        image = self.frames[int(self.frame_num)]
        if not self.direction_right:
            image = pygame.transform.flip(self.frames[int(self.frame_num)], True, False).convert_alpha()
            image.set_colorkey(self.BG_COLOR)

        self.image = image
