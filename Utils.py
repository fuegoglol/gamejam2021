import pygame
import math

class Utils:

    GRAY = (89, 89, 89)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (115, 182, 254)
    RED = (255, 0, 0)
    GREEN = (50, 255, 0)

    TOWERS = {
        'apple': {
            'path': 'assets/fruits-veggies/apple_red.png',
            'name': 'Apple',
            'price': 5,
            'description': 'blablabla',
            'fire_rate': 2,
            'damage': 1,
            'range': 85,
            'max_attack': 1,
            'energy_consumption': 10,
            'sleeping_time': 2,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },
        'potato': {
            'path': 'assets/fruits-veggies/potato.png',
            'name': 'Potato',
            'price': 10,
            'description': 'blablabla',
            'fire_rate': 10,
            'damage': 15,
            'range': 16,
            'max_attack': 1,
            'energy_consumption': 100,
            'sleeping_time': 8,
            'ricochet': False,
            'path_border': False,
            'path_mine': True,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },

        'pear': {
            'path': 'assets/fruits-veggies/pear.png',
            'name': 'Pear',
            'price': 20,
            'description': 'blablabla',
            'fire_rate': 3,
            'damage': 2,
            'range': 90,
            'max_attack': 1,
            'energy_consumption': 9,
            'sleeping_time': 2,
            'ricochet': True,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },
        'pepper': {
            'path': 'assets/fruits-veggies/pepper_green.png',
            'name': 'Pepper',
            'price': 50,
            'description': 'blablabla',
            'fire_rate': 0.5,
            'damage': 50,
            'range': 100,
            'max_attack': 1,
            'energy_consumption': 50,
            'sleeping_time': 5,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },

        'banana': {
            'path': 'assets/fruits-veggies/banana.png',
            'name': 'Banana',
            'price': 100,
            'description': 'blablabla',
            'fire_rate': 6,
            'damage': 3,
            'range': 85,
            'max_attack': 3,
            'energy_consumption': 8,
            'sleeping_time': 3,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },
        'lettuce': {
            'path': 'assets/fruits-veggies/lettuce.png',
            'name': 'Lettuce',
            'price': 200,
            'description': 'blablabla',
            'fire_rate': 30,
            'damage': 0.5,
            'range': 50,
            'max_attack': 10,
            'energy_consumption': 0.5,
            'sleeping_time': 10,
            'ricochet': False,
            'path_border': True,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },

        'tomato': {
            'path': 'assets/fruits-veggies/tomato.png',
            'name': 'Tomato',
            'price': 250,
            'description': 'blablabla',
            'fire_rate': 1,
            'damage': 5,
            'range': 1,
            'max_attack': 1,
            'energy_consumption': 2,
            'sleeping_time': 1,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': True,
            'poison': 0,
            'confusing': 0
        },
        'carrot': {
            'path': 'assets/fruits-veggies/carrot.png',
            'name': 'Carrot',
            'price': 500,
            'description': 'blablabla',
            'fire_rate': 2.5,
            'damage': 50,
            'range': 300,
            'max_attack': 1,
            'energy_consumption': 25,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },

        'peach': {
            'path': 'assets/fruits-veggies/peach.png',
            'name': 'Peach',
            'price': 1000,
            'description': 'blablabla',
            'fire_rate': 5,
            'damage': 10,
            'range': 150,
            'max_attack': 1,
            'energy_consumption': 5,
            'sleeping_time': 5,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 300
        },
        'squash': {
            'path': 'assets/fruits-veggies/squash.png',
            'name': 'Squash',
            'price': 1500,
            'description': 'blablabla',
            'fire_rate': 1,
            'damage': 1,
            'range': 120,
            'max_attack': 1,
            'energy_consumption': 5,
            'sleeping_time': 5,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 600,
            'confusing': 0
        },

        'orange': {
            'path': 'assets/fruits-veggies/orange.png',
            'name': 'Orange',
            'price': 2000,
            'description': 'blablabla',
            'fire_rate': 30,
            'damage': 10,
            'range': 130,
            'max_attack': 1,
            'energy_consumption': 0.1,
            'sleeping_time': 3,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },
        'aubergine': {
            'path': 'assets/fruits-veggies/aubergine.png',
            'name': 'Aubergine',
            'price': 5000,
            'description': 'blablabla',
            'fire_rate': 0.25,
            'damage': 1000,
            'range': 500,
            'max_attack': 1000,
            'energy_consumption': 100,
            'sleeping_time': 8,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },

        'cherry': {
            'path': 'assets/fruits-veggies/cherry.png',
            'name': 'Cherry',
            'price': 10000,
            'description': 'blablabla',
            'fire_rate': 10,
            'damage': 10,
            'range': 200,
            'max_attack': 2,
            'energy_consumption': 1,
            'sleeping_time': 2,
            'ricochet': True,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 60,
            'confusing': 0
        },
        'broccoli': {
            'path': 'assets/fruits-veggies/broccoli.png',
            'name': 'Broccoli',
            'price': 99999,
            'description': 'blablabla',
            'fire_rate': 60,
            'damage': 100,
            'range': 1,
            'max_attack': 20,
            'energy_consumption': 1,
            'sleeping_time': 10,
            'ricochet': True,
            'path_border': False,
            'path_mine': True,
            'generator': False,
            'poison': 1,
            'confusing': 0
        }
    }

    ENEMIES = {
        'cow': {
            'path': 'assets/sprites/cow.png',
            'hp': 150,
            'speed': 0.5,
            'water': 20,
            'fly': False
        },
        'chicken': {
            'path': 'assets/sprites/chicken.png',
            'hp': 10,
            'speed': 1,
            'water': 3,
            'fly': False
        },
        'bat': {
            'path': 'assets/sprites/bat.png',
            'hp': 50,
            'speed': 1.5,
            'water': 25,
            'fly': True
        },
        'dog': {
            'path': 'assets/sprites/dog.png',
            'hp': 2000,
            'speed': 1.25,
            'water': 500,
            'fly': False
        },
        'fox': {
            'path': 'assets/sprites/fox.png',
            'hp': 500,
            'speed': 0.75,
            'water': 150,
            'fly': False
        },
        'frog': {
            'path': 'assets/sprites/frog.png',
            'hp': 2000,
            'speed': 0.25,
            'water': 200,
            'fly': False
        },
        'hyena': {
            'path': 'assets/sprites/hyena.png',
            'hp': 50000,
            'speed': 1.25,
            'water': 5000,
            'fly': False
        },
        'monkey': {
            'path': 'assets/sprites/monkey.png',
            'hp': 150,
            'speed': 1,
            'water': 50,
            'fly': False
        },
        'rabbit': {
            'path': 'assets/sprites/rabbit.png',
            'hp': 30,
            'speed': 2,
            'water': 10,
            'fly': False
        },
        'rat': {
            'path': 'assets/sprites/rat.png',
            'hp': 5,
            'speed': 0.5,
            'water': 1,
            'fly': False
        },
        'eagle': {
            'path': 'assets/sprites/eagle.png',
            'hp': 500,
            'speed': 1.5,
            'water': 2000,
            'fly': True
        },
    }

    WAVES = [
        (5 * ('rat', 80)),#1

        (7 * ('rat', 70)),#2

        (10 * ('rat', 60) +#3
         3 * ('chicken', 90)),

        (15 * ('rat', 50) +#4
         7 * ('chicken', 75)),

        (1 * ('rabbit', 120)),#5

        (30 * ('rat', 40) +#6
         1 * ('rabbit', 300)),

        (40 * ('rat', 40) +#7
         10 * ('chicken', 60) +
         1 * ('rabbit', 240)),
         
        (2 * ('cow', 600)),#8

        (3 * ('cow', 540) +#9
         10 * ('chicken', 120) +
         3 * ('rabbit', 240)),

        (10 * ('cow', 480)),#10

        (5 * ('bat', 600)),#11

        (10 * ('cow', 300) +#12
         20 * ('chicken', 30) +
         10 * ('bat', 120)),

        (5 * ('monkey', 60)),#13

        (1 * ('frog', 60)),#14

        (1 * ('frog', 600) +#15
         50 * ('rat', 10) +
         10 * ('cow', 60) +
         30 * ('chicken', 20) +
         15 * ('rabbit', 30) +
         10 * ('bat', 60) +
         10 * ('cow', 60)),

        (2 * ('frog', 300) +#16
         120 * ('rat', 5) +
         10 * ('monkey', 60)),

        (5 * ('monkey', 60)),#17

        (1 * ('fox', 60)),#18

        (3 * ('fox', 60) +#19
         120 * ('bat', 20) +
         10 * ('monkey', 60)),

        (1 * ('dog', 60) +#20
         600 * ('rat', 3) +
         30 * ('cow', 5) +
         45 * ('bat', 10)),

        (3 * ('dog', 60) +#21
         50 * ('rat', 3) +
         60 * ('bat', 10)),

        (2 * ('eagle', 600)),#22

        (100 * ('rat', 30) +#23
         90 * ('chicken', 30) +
         80 * ('rabbit', 30) +
         70 * ('cow', 30) +
         60 * ('bat', 30) +
         50 * ('monkey', 30) +
         20 * ('frog', 30) +
         10 * ('fox', 30) +
         5 * ('dog', 30) +
         5 * ('eagle', 240)),

         (200 * ('rat', 30) +#24
         150 * ('chicken', 30) +
         80 * ('rabbit', 30) +
         100 * ('cow', 30) +
         60 * ('bat', 30) +
         50 * ('monkey', 30) +
         20 * ('frog', 30) +
         11 * ('fox', 30) +
         6 * ('dog', 30) +
         8 * ('eagle', 240)),

         (300 * ('rat', 30) +#25
         200 * ('chicken', 30) +
         120 * ('rabbit', 30) +
         150 * ('cow', 30) +
         200 * ('bat', 30) +
         50 * ('monkey', 30) +
         20 * ('frog', 30) +
         11 * ('fox', 30) +
         6 * ('dog', 30) +
         8 * ('eagle', 240)),

         (600 * ('rat', 30) +#26
         250 * ('chicken', 30) +
         120 * ('rabbit', 30) +
         150 * ('cow', 30) +
         200 * ('bat', 30) +
         50 * ('monkey', 30) +
         20 * ('frog', 30) +
         20 * ('fox', 30) +
         15 * ('dog', 30) +
         20 * ('eagle', 240)),

         (600 * ('rat', 30) +#27
         400 * ('chicke100', 30) +
         250 * ('rabbit', 30) +
         300 * ('cow', 30) +
         200 * ('bat', 30) +
         100 * ('monkey', 30) +
         30 * ('frog', 30) +
         20 * ('fox', 30) +
         15 * ('dog', 30) +
         20 * ('eagle', 240)),

         800 * ('chicken', 30) +
         500 * ('rabbit', 30) +
         400 * ('cow', 30) +
         300 * ('bat', 30) +
         100 * ('monkey', 30) +
         40 * ('frog', 30) +
         20 * ('fox', 30) +
         15 * ('dog', 30) +
         20 * ('eagle', 240)),

         (1000 * ('rat', 30) +#29
         800 * ('chicken', 30) +
         500 * ('rabbit', 30) +
         400 * ('cow', 30) +
         300 * ('bat', 30) +
         100 * ('monkey', 30) +
         60 * ('frog', 30) +
         20 * ('fox', 30) +
         15 * ('dog', 30) +
         20 * ('eagle', 240)),

         (1000 * ('rat', 30) +#30
         1000 * ('chicken', 30) +
         800 * ('rabbit', 30) +
         600 * ('cow', 30) +
         500 * ('bat', 30) +
         150 * ('monkey', 30) +
         60 * ('frog', 30) +
         20 * ('fox', 30) +
         30 * ('dog', 30) +
         20 * ('eagle', 240)),

        (1000 * ('rat', 30) +#31
         1000 * ('chicken', 30) +
         1000 * ('rabbit', 30) +
         800 * ('cow', 30) +
         500 * ('bat', 30) +
         300 * ('monkey', 30) +
         100 * ('frog', 30) +
         20 * ('fox', 30) +
         30 * ('dog', 30) +
         20 * ('eagle', 240)),

        (1000 * ('rat', 30) +#32
         1000 * ('chicken', 30) +
         1000 * ('rabbit', 30) +
         800 * ('cow', 30) +
         500 * ('bat', 30) +
         300 * ('monkey', 30) +
         50 * ('frog', 30) +
         50 * ('fox', 30) +
         60 * ('dog', 30) +
         100 * ('eagle', 240)),

        (1 * ('rat', 300) +#33
         1 * ('chicken', 300) +
         1 * ('rabbit', 300) +
         1 * ('cow', 300) +
         1 * ('bat', 300) +
         1 * ('monkey', 300) +
         1 * ('frog', 300) +
         1 * ('fox', 300) +
         1 * ('dog', 300) +
         1 * ('eagle', 300) +
         1 * ('hyena', 300) +

         1 * ('rat', 240) +
         1 * ('chicken', 240) +
         1 * ('rabbit', 240) +
         1 * ('cow', 240) +
         1 * ('bat', 240) +
         1 * ('monkey', 240) +
         1 * ('frog', 240) +
         1 * ('fox', 240) +
         1 * ('dog', 240) +
         1 * ('eagle', 240) +
         1 * ('hyena', 240) +

         1 * ('rat', 180) +
         1 * ('chicken', 180) +
         1 * ('rabbit', 180) +
         1 * ('cow', 180) +
         1 * ('bat', 180) +
         1 * ('monkey', 180) +
         1 * ('frog', 180) +
         1 * ('fox', 180) +
         1 * ('dog', 180) +
         1 * ('eagle', 180) +
         1 * ('hyena', 180) +

         1 * ('rat', 120) +
         1 * ('chicken', 120) +
         1 * ('rabbit', 120) +
         1 * ('cow', 120) +
         1 * ('bat', 120) +
         1 * ('monkey', 120) +
         1 * ('frog', 120) +
         1 * ('fox', 120) +
         1 * ('dog', 120) +
         1 * ('eagle', 120) +
         1 * ('hyena', 120) +

         1 * ('rat', 60) +
         1 * ('chicken', 60) +
         1 * ('rabbit', 60) +
         1 * ('cow', 60) +
         1 * ('bat', 60) +
         1 * ('monkey', 60) +
         1 * ('frog', 60) +
         1 * ('fox', 60) +
         1 * ('dog', 60) +
         1 * ('eagle', 60) +
         1 * ('hyena', 60) +

         1 * ('rat', 30) +
         1 * ('chicken', 30) +
         1 * ('rabbit', 30) +
         1 * ('cow', 30) +
         1 * ('bat', 30) +
         1 * ('monkey', 30) +
         1 * ('frog', 30) +
         1 * ('fox', 30) +
         1 * ('dog', 30) +
         1 * ('eagle', 30) +
         1 * ('hyena', 30) +

         1 * ('rat', 10) +
         1 * ('chicken', 10) +
         1 * ('rabbit', 10) +
         1 * ('cow', 10) +
         1 * ('bat', 10) +
         1 * ('monkey', 10) +
         1 * ('frog', 10) +
         1 * ('fox', 10) +
         1 * ('dog', 10) +
         1 * ('eagle', 10) +
         1 * ('hyena', 10))
    ]

    MIN_SCORE = 99999999

    for tw in TOWERS.values():
        tw['sprite'] = pygame.image.load(tw['path'])

    for id, en in ENEMIES.items():
        en['score'] = en['hp'] * en['speed']
        if en['score'] < MIN_SCORE:
            MIN_SCORE = en['score']

        spritesheet = pygame.image.load(en['path'])
        sprite_list = []
        for direction in range(4):
            frames = []
            for frame in range(3):
                frames.append(spritesheet.subsurface(
                    ((32 * frame, 32 * direction), (32, 32))))
            sprite_list.append(frames)

        en['sprites'] = sprite_list
