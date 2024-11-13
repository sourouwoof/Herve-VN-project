# ===================================== init characters
"""
init python:
    config.tag_layer["he"] = 'char'
    config.tag_layer["mc"] = 'char'
"""
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
    what_color='#f3cf63',
    window_background=Image("gui/textbox.png", xalign=0.5, yalign=1.0, alpha=0.25),
    #window_style=dissolve,
    #what_style=dissolve
    )
    define inner = Character(None, who_suffix="  {image=emojis/thought-balloon.png}", what_prefix='(', what_suffix=')', who_italic=True, kind=base)
    define outter = Character(None, what_prefix='“', what_suffix='”', kind=base)
    define texting = Character(None, who_suffix="  {image=emojis/mobile-phone.png}{image=emojis/speech-balloon.png}", what_prefix='“', what_suffix='”', kind=base)
    define calling = Character(None, who_suffix="  {image=emojis/telephone-receiver.png}", what_prefix='“', what_suffix='”', kind=base)

    # main characters
    define player_name = "Me"
    define her = Character("Hervé", color="#80746e", image="he", kind=outter, callback = name_callback, cb_name = "he") # character
    define mco = Character("[player_name]", color="#97e99b", image="mcSide", kind=outter, callback = name_callback, cb_name = "mc")
    define mci = Character("[player_name]", color="#97e99b", kind=inner)
    define mct = Character("[player_name]", color="#97e99b", kind=texting)
    define hert = Character("Hervé", color="#80746e", kind=texting)
    define momt = Character("Mom", color="#cdb0f3", kind=texting)
    define womc = Character("Women voice", color="#fafafa", kind=texting)