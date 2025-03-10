from utils import *
from ray import *
from cli import render
from PIL import Image

snowman_white = Material(vec([0.9, 0.9, 0.9]), k_s=0.2, p=90)
ground_white = Material(vec([0.85, 0.85, 0.85]), k_m=0.4)
cieling_gray = Material(vec([0.8, 0.8, 0.85]), k_s=0.3, p=90)
coal_black = Material(vec([0.05, 0.05, 0.05]), k_s=0.2, p=90)
branch_brown = Material(vec([0.169, 0.094, 0]))

rock_texture = np.array(Image.open("./textures/rock.jpg"))
rock_material = Material(vec([0.8, 0.8, 0.85]), k_s=0.3, k_a = .2, p=90, texture=rock_texture)

snow_texture = np.array(Image.open("./textures/snow.jpg"))
snow_material = Material(vec([0, 0, 0]), k_s = .3, k_a = .2, p=90, texture=snow_texture)

ice_texture = np.array(Image.open("./textures/ice1.png"))
ice_material = Material(vec([0, 0, 0]), k_s = .3, k_a = .2, p=90, texture=ice_texture)

scene = Scene([
    # snowman body
    Sphere(vec([0, 0, 0]), 1, snow_material),
    Sphere(vec([0, 1.25, 0]), .75, snow_material),
    Sphere(vec([0, 2.25, 0]), 0.5, snow_material),

    # ground
    Sphere(vec([0, -40, 0]), 39.5, rock_material),

    # ceiling
    # Sphere(vec([0, 5.9, 14]), 1, cieling_gray),

    # coals (eyes)
    Sphere(vec([0.1, 2.4, 0.5]), 0.05, coal_black),
    Sphere(vec([-0.1, 2.4, 0.5]), 0.05, coal_black),

    # coals (body)
    Sphere(vec([0, 1.75, 0.5]), 0.1, coal_black),
    Sphere(vec([0, 1.5, 0.65]), 0.1, coal_black),
    Sphere(vec([0, 1.2, 0.7]), 0.1, coal_black),

    # icicles
    #Cone(vec([2, 0, 0]), .1, 3, cieling_gray),

    # hat
    Cylinder(vec([0,2.6,0]), 0.6, 0.1, 0, coal_black),
    Cylinder(vec([0,2.7,0]), 0.4, 0.3, 0, coal_black),

    # arms
    Cylinder(vec([0.6, 1.6, 0.3]), 0.1, 1.5, -60, branch_brown),
    Cylinder(vec([-0.6, 1.6, 0.3]), 0.1, 1.5, 60, branch_brown),

    # snowflakes
    Sphere(vec([-2.5, 3.75, 0.7]), 0.1, snowman_white),
    Sphere(vec([-2.4, 2, 0]), 0.1, snowman_white),
    Sphere(vec([-2.25, 1.4, 2]), 0.15, snowman_white),
    Sphere(vec([-1.75, 0.75, 1]), 0.15, snowman_white),
    Sphere(vec([-1.75, 4.2, 1]), 0.15, snowman_white),
    Sphere(vec([-1.5, 2.75, -1]), 0.1, snowman_white),
    Sphere(vec([-0.35, 3.85, 2]), 0.15, snowman_white),
    Sphere(vec([0.5, 4, 0.7]), 0.1, snowman_white),
    Sphere(vec([0.9, 2.4, 0]), 0.1, snowman_white),
    Sphere(vec([1.2, 4.55, 0]), 0.15, snowman_white),
    Sphere(vec([1.5, 1.25, 0]), 0.1, snowman_white),
    Sphere(vec([2, 3.6, 0]), 0.15, snowman_white),
    Sphere(vec([2.25, 0, 0]), 0.1, snowman_white),
    Sphere(vec([2.55, 2, -1]), 0.15, snowman_white),
    Sphere(vec([2.9, 3, -1]), 0.1, snowman_white),
],
    bg_color=vec([0.155, 0.163, 0.21]))


lights = [
    PointLight(vec([10, 10, 16]), vec([250, 250, 250])),
    AmbientLight(0.1),
]

camera = Camera(vec([0, 5, 15]), target=vec(
    [0, 1.5, 0]), vfov=25, aspect=10/11)

render(camera, scene, lights)
