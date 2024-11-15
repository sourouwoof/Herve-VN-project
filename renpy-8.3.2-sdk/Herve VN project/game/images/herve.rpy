layeredimage he:
    at sprite_highlight('he')

    group base auto:
        attribute shirt default

    group eyebrows auto

    group eyes
    group glasses auto

    group mouth auto

    group blush auto

    group tongue auto

    zoom 1.3
    xalign 0.5
    yalign -0.5

image side heSide = LayeredImageProxy("he", Transform(crop=(0, 0, 700, 510), zoom=0.75))