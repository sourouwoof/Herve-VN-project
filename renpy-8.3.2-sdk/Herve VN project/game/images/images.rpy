define gui.main_menu_background = im.Scale("images/bgs/road1.jpg", 1920, 1080) # "gui/main_menu.png"
image road1 = im.Scale("images/bgs/road1.jpg", 1920, 1080)

image placeholder:
    Text("{color=#ffffff}(Ceci est un placeholder pour un cg ou sprite à faire){/color}") 
    xalign 0.5 yalign 0.5

image loading:
    alpha 0
    block:
        Text("{color=#ffffff}{font=fonts/NotoEmoji-Regular.ttf}🍂{/font}{/color}") 
        linear 1 alpha 1
        pause .25
        linear .5 alpha 0
        Text("{color=#ffffff}{font=fonts/NotoEmoji-Regular.ttf}🌲{/font}{/color}") 
        linear 1 alpha 1
        pause .25
        linear .5 alpha 0
        repeat
