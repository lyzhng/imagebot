import random

from settings import IMG_DIR_PATH, PHOTO_PATHS, GIF_PATHS


def random_image():
    if not PHOTO_PATHS:
        return None
    choice = random.sample(PHOTO_PATHS, 1).pop()
    PHOTO_PATHS.remove(choice)
    return choice


def random_gif():
    if not GIF_PATHS:
        return None
    choice = random.sample(GIF_PATHS, 1).pop()
    GIF_PATHS.remove(choice)
    return choice


def random_function():
    return random.choice([random_image, random_gif])