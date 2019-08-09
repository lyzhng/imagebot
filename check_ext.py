def is_image(file):
    ext = ('.png', '.jpeg', '.jpg')
    return file.endswith(ext)

def is_gif(file):
    return file.endswith('.gif')