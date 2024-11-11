layeredimage mc:
    at sprite_highlight('mc')

    group base auto:
        attribute shirt default

    zoom 1.3
    xalign 0.5
    yalign -0.5

image side mcSide = LayeredImageProxy("mc", Transform(crop=(0, 0, 700, 510), zoom=0.75))
