from utils import *
from ray import *
from cli import render
from PIL import Image

snowman_white = Material(vec([0.9, 0.9, 0.9]), k_s=0.2, p=90)
ground_white = Material(vec([0.85, 0.85, 0.85]), k_m=0.4)
cieling_gray = Material(vec([0.8, 0.8, 0.85]), k_s=0.3, p=90)
coal_black = Material(vec([0.05, 0.05, 0.05]), k_s=0.2, p=90)
rock_texture = np.array(Image.open("./textures/rock.jpg"))
rock_material = Material(vec([0.8, 0.8, 0.85]), k_s=0.3, p=90, texture=rock_texture)

scene = Scene([
    # snowman body
    Sphere(vec([0, 0, 0]), 1, snowman_white),
    Sphere(vec([0, 1.25, 0]), 0.75, snowman_white),
    Sphere(vec([0, 2.25, 0]), 0.5, snowman_white),

    # ground
    Sphere(vec([0, -40, 0]), 39.5, rock_material),

    # ceiling
    Sphere(vec([0, 5.9, 14]), 1, cieling_gray),

    # coals (eyes)
    Sphere(vec([0.1, 2.5, 0.4]), 0.05, coal_black),
    Sphere(vec([-0.1, 2.5, 0.4]), 0.05, coal_black),

    # coals (body)
    Sphere(vec([0, 1.75, 0.5]), 0.1, coal_black),
    Sphere(vec([0, 1.55, 0.6]), 0.1, coal_black),
    Sphere(vec([0, 1.35, 0.6]), 0.1, coal_black),

    # icicles
    #Cone(vec([2, 9, 0]), .1, 3, cieling_gray)
],
    bg_color=vec([0.155, 0.163, 0.21]))


lights = [
    PointLight(vec([10, 10, 16]), vec([250, 250, 250])),
    AmbientLight(0.1),
]

camera = Camera(vec([0, 5, 15]), target=vec(
    [0, 1.5, 0]), vfov=25, aspect=10/11)

render(camera, scene, lights)
