layeredimage he:
    at sprite_highlight('he')

    group base auto:
        attribute shirt default

    group eyebrows auto:
        attribute ebnormal default

    group eyes auto:
        attribute eynormal default DynamicDisplayable(char_blink, "he_eyes_eyclosed", "he_eyes_eyopen", name='he')
    
    group mouth auto:
        attribute mnormal default

    group blush auto

    group hat auto

    zoom 1.0
    xalign 0.5
    yalign -0.5

image side heSide = LayeredImageProxy("he", Transform(crop=(0, 0, 700, 510), zoom=0.75))