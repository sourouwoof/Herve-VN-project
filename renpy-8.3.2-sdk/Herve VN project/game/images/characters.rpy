# ===================================== init images

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

    zoom 0.55
    xalign 0.5
    yalign 0.30

image side heSide = LayeredImageProxy("he", Transform(crop=(250, 350, 700, 510), zoom=0.75))

layeredimage mc:
    at sprite_highlight('mc')

    group base auto:
        attribute shirt default

    group eyebrows auto

    group eyes
    group glasses auto

    group mouth auto

    group blush auto

    group tongue auto

    zoom 0.55
    xalign 0.5
    yalign 0.30

image side mcSide = LayeredImageProxy("mc", Transform(crop=(250, 350, 700, 510), zoom=0.75))

# ===================================== init characters

init python:
    config.tag_layer["he"] = 'char'
    config.tag_layer["mc"] = 'char'

transform ctc_transform:
        alpha 0
        pause 1
        block:
            linear 3 alpha 1
            linear 3 alpha 0
            repeat

label characters:
    define base = Character(
    None, 
    who_outlines=[(1, "#201515c2", 1, 1), (1, "#201515c2", 0, 0)], # who_outlines=[(1, "#00000045", 1, 1), (1, "#00000030", 0, 0)],
    what_outlines=[(1, "#201515f0", 1, 1), (1, "#201515f0", 0, 0)], # what_outlines=[(1, "#0000008b", 1, 1), (1, "#0000008b", 0, 0)],  
    #window_background="none_bg_slideshow", #"gui/textboxes/[textboxImage].png"
    ctc=At(Text(" >>", color="#f3cf63"), ctc_transform), ctc_pause=At(Text("", color="#f3cf63"), ctc_transform),
    what_color='#f3cf63' #fae8b0 #9dcfe9 #what_style
    )
    define inner = Character(None, what_prefix='(', what_suffix=')', who_italic=True, kind=base)
    define outter = Character(None, what_prefix='“', what_suffix='”', kind=base)
    define texting = Character(None, what_prefix='{image=emojis/speech-balloon.png} “', what_suffix='”', kind=base)
    define calling = Character(None, what_prefix='{image=emojis/telephone-receiver.png} “', what_suffix='”', kind=base)

    # main characters
    define he = Character("Hervé", color="#80746e", image="he", kind=outter, callback = name_callback, cb_name = "he") # character
    define mc = Character("MC", color="#97e99b", image="mc", kind=outter, callback = name_callback, cb_name = "mc")