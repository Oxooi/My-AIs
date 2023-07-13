import os
import pygame
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800

GEN = 0

textures_folders = ["minecraft"]

BIRD_IMGS = []

for folder in textures_folders:
    # Chemin du dossier
    folder_path = os.path.join("imgs", folder)
    
    # Chargement et mise à l'échelle des images de l'oiseau
    for i in range(1, 4):  # Les numéros des images vont de 1 à 3
        image_path = os.path.join(folder_path, f"bird{i}.png")
        bird_img = pygame.transform.scale2x(pygame.image.load(image_path))
        BIRD_IMGS.append(bird_img)

    # Chargement des autres images
    PIPE_IMG = pygame.transform.scale2x(
        pygame.image.load(os.path.join(folder_path, "pipe.png"))
    )
    BASE_IMG = pygame.transform.scale2x(
        pygame.image.load(os.path.join(folder_path, "base.png"))
    )
    BG_IMG = pygame.transform.scale2x(
        pygame.image.load(os.path.join(folder_path, "bg.png"))
    )

STAT_FONT = pygame.font.SysFont("impact", 40)