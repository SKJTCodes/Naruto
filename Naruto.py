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
        # self._user_input()

    # def _user_input(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_RIGHT]:
    #         self.direction_right = True
    #         self.rect.bottom = 915
    #         self._run()
    #     elif keys[pygame.K_LEFT]:
    #         self.direction_right = False
    #         self._run()
    #         self.rect.bottom = 915
    #     else:
    #         self.rect.bottom = 905

    def _get_frames(self, action, flip=True):
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

        # Get for other direction
        if flip:
            tmp_images = images.copy()
            for image in tmp_images:
                image = pygame.transform.flip(image, True, False).convert_alpha()
                image = pygame.transform.scale2x(image)
                image.set_colorkey(self.BG_COLOR)
                images.append(image)
        return images

    # def _run(self, speed=3):
    #     if self.direction_right:
    #         if self.rect.right > 1920:
    #             self.rect.right = 1920
    #         self._run_animation()
    #         self.rect.right += speed
    #     else:
    #         if self.rect.left <= 0:
    #             self.rect.left = 0
    #         self._run_animation()
    #         self.rect.left -= speed

    # def _run_animation(self, speed=0.1):
    #     self.frame_num += speed
    #     if self.frame_num >= len(self.frames['run']):
    #         self.frame_num = 0
    #
    #     if self.direction_right:
    #         self.image = self.frames['run'][int(self.frame_num)]
    #     else:
    #         self.image = pygame.transform.flip(self.frames['run'][int(self.frame_num)], True, False)
    #         self.image.set_colorkey(self.BG_COLOR)
    #
    def _idle_animation(self, speed=0.1):
        self.frame_num += speed

        # restart animation from frame 1 if reach end
        if self.frame_num >= len(self.frames) / 2:
            self.frame_num = 0 if self.direction_right else len(self.frames) / 2
        print(int(self.frame_num))
        self.image = self.frames[int(self.frame_num)]

    # def _get_image(self, img_path):
    #     img = pygame.image.load(img_path).convert_alpha()
    #     img.set_colorkey(self.BG_COLOR)
    #     return img

    # def _cut_frame(self, frame_num, point=(0, 1030), width=70, height=65):
    #     frame_surf = pygame.Surface((width, height)).convert_alpha()
    #     move_dist = frame_num * width
    #     point = (point[0] + move_dist, point[1])
    #     frame_surf.blit(self.sprite_sheet, (0, 0), (point[0], point[1], width, height))
    #     return frame_surf
