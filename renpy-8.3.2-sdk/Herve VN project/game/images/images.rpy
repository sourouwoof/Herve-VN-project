define road1 = im.Scale("images/bgs/road1.jpg", 1920, 1080)

image placeholder:
    Text("{color=#ffffff}(Ceci est un placeholder pour un cg ou sprite à faire){/color}") 
    xalign 0.5 yalign 0.5

image main_menu_slideshow1:
    Solid("#000000")
    pause 10
    "tree13" with Dissolve(60)