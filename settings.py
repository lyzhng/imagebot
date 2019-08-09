import os

from check_ext import *


CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

IMG_DIR_PATH = os.path.join(CURRENT_DIR_PATH, 'img')

PHOTO_PATHS = {os.path.join(IMG_DIR_PATH, file) for file in os.listdir(IMG_DIR_PATH) if is_image(file)}

GIF_PATHS = {os.path.join(os.path.join(IMG_DIR_PATH, file)) for file in os.listdir(IMG_DIR_PATH) if is_gif(file)}

INTERVAL = 60 * 60 * 6 # 6 HOURS