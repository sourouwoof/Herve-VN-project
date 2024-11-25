# ---------------------------------------------------------------- examples transforms
transform left_to_right:
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat

# https://lemmasoft.renai.us/forums/viewtopic.php?t=32626
transform text_fade_in:
    alpha 0.5
    linear 0.5 alpha 1

# ---------------------------------------------------------------- general transforms
transform bg_blur:
    linear 1 blur 5

transform bg_unblur:
    linear 0.5 blur 0

# A workaround to show an image while showing the text (preserving the image animation momentum)
transform dissolve_sequenced(when_time, duration=1):
    alpha 0
    pause(when_time) # when making a pause
    linear duration alpha 1 # and show the image after

transform bottom_appearing:
    xalign 0.5 yalign 2
    ease 0.5 yoffset 0.5
    # xalign 0.5 yalign 2
    # linear 1.2 xalign 0.5 yalign 0.50
    # linear 2.00 xalign 0.5 yalign 0.5

transform centered_image:
    zoom 0.7
    xalign 0.5 yalign 0.3

transform board_position:
    zoom .9
    xalign .5 yalign .35

transform blink_transition:
    "eye.png" 
    alpha 1.0
    .1
    alpha 0.0
    .2
    alpha 1.0
    .1
    alpha 0.0
    .7
    alpha 1.0
    .1
    alpha 0.0 

# https://lemmasoft.renai.us/forums/viewtopic.php?t=25749
init python:
    def eyewarp(x):
        return x**1.33
    open_eyes = ImageDissolve("./addons/eye.png", 1.5, ramplen=128, reverse=False, time_warp=eyewarp)
    close_eyes = ImageDissolve("./addons/eye.png", 1.5, ramplen=128, reverse=True, time_warp=eyewarp)
    # medium_transition = Fade(1, 0.75, 1)

# ---------------------------------------------------------------- screen bumps
# TODO https://www.youtube.com/watch?v=n7HzbZO-uIQ
transform x_shake(amt=5, repeats=None):
    xoffset 0
    linear .5 xoffset amt
    linear .75 xoffset -1 * amt
    linear .5 xoffset 0
    repeat repeats

transform y_shake(amt=5, repeats=None):
    yoffset 0
    linear .5 yoffset amt
    linear .75 yoffset -.25 * amt
    linear .5 yoffset 0
    repeat repeats

label car_bumps:
    camera:
        xalign 0.5 yalign 0.5
        ease 1.5 zoom 1.035
        choice:
            pause 0.5
        choice:
            y_shake(8, 2)
        repeat
    return

label train_bumps:
    camera:
        xalign 0.5 yalign 0.5
        ease 1.5 zoom 1.035
        choice:
            pause 0.5
        choice:
            x_shake(8, 2)
        repeat
    return
# camera # bumps end

# ---------------------------------------------------------------- character transforms
transform stand_up:
    linear 0.75 yalign -0.025
    linear 0.5 yalign 0.0

transform sit_down:
    linear 0.5 yalign -0.25
    linear 0.75 yalign -0.275

transform coming_close:
    ease 2.5 zoom 1.175

transform already_close:
    ease 0 zoom 1.175

transform already_far:
    ease 0 zoom 0.825
    yoffset 150

transform breath:
    linear 0.75 yalign -0.3
    linear 0.75 yalign -0.25
    repeat

transform happy_shake:
    ease 0.5 xoffset 30
    ease 0.5 xoffset -30

transform soft_shake:
    ease 0.5 xoffset 15
    ease 0.5 xoffset -15
    repeat

transform small_shake:
    linear 0.080 xoffset -3
    linear 0.080 xoffset +3
    linear 0.090 xoffset -2
    linear 0.090 xoffset +2
    pause 1.25
    linear 0.080 xoffset -3
    linear 0.080 xoffset +3
    linear 0.090 xoffset -2
    linear 0.090 xoffset +2
    pause 1.0
    repeat

transform cry_shake:
    linear 0.080 xoffset -3
    linear 0.080 xoffset +3
    linear 0.090 xoffset -2
    linear 0.090 xoffset +2
    pause 0.25
    linear 0.080 xoffset -3
    linear 0.080 xoffset +3
    linear 0.090 xoffset -2
    linear 0.090 xoffset +2
    pause 0.25
    repeat

transform shiver_shake:
    linear 0.070 xoffset -4
    linear 0.070 xoffset +4
    linear 0.070 xoffset -3
    linear 0.070 xoffset +3
    linear 0.090 xoffset -4
    linear 0.090 xoffset +4
    linear 0.090 xoffset -3
    linear 0.090 xoffset +3

# https://lemmasoft.renai.us/forums/viewtopic.php?t=26172
# https://www.renpy.org/doc/html/atl.html#transform-property-anchoraround
transform hops:
    align (0.46,0.20)
    alignaround (0.5,0.20)
    linear 0.875 angle 90.0 clockwise
    align (0.54,0.20)
    alignaround (0.5,0.20)
    linear 0.875 angle 270.0 counterclockwise
    repeat

transform hops_slow:
    align (0.46,0.20)
    alignaround (0.5,0.20)
    linear 0.875 angle 90.0 clockwise
    pause 1
    align (0.54,0.20)
    alignaround (0.5,0.20)
    linear 0.875 angle 270.0 counterclockwise
    pause 1
    repeat

transform hops1:
    choice:
        pause 0.15
    choice:
        ease 0.35 yoffset -30
        ease 0.30 yoffset 0 xoffset -10
        ease 0.35 yoffset -30
        ease 0.30 yoffset 0 xoffset 10
    repeat

transform jolt:
    ease .1 yoffset 30
    ease .1 yoffset -30
    ease .1 yoffset 0

# ---------------------------------------------------------------- positionning characters on x-axis
# Divise the stage either as quarters, thirds or halves.
transform middle:
    zoom 1.0
    xalign 0.5

# -------------------------------- 3 characters
transform one_three:
    xalign -0.25

transform three_three:
    xalign 1.25

# -------------------------------- 2 characters
transform one_two_moving:
    linear 1.0 xalign 0.0

transform two_two_moving:
    linear 1.0 xalign 1.0

transform one_two:
    xalign 0.0

transform two_two:
    xalign 1.0

# ---------------------------------------------------------------- coloring and tints
# -------------------------------- tints per hour
transform tint6pink: # pink dawn
    matrixcolor TintMatrix("#c58aa3")*BrightnessMatrix(-0.30)

transform tint16: # soft blue
    matrixcolor TintMatrix("#617fbf")*BrightnessMatrix(-0.30)

transform tint16gray: # gray
    matrixcolor TintMatrix("#9b9a92")*BrightnessMatrix(-0.20) 

transform tint16dark: # dark gray
    matrixcolor TintMatrix("#4f4f4f")*BrightnessMatrix(-0.20) 

transform tint16orange: # orange dusk
    matrixcolor TintMatrix("#fdd9bc")*BrightnessMatrix(-0.40)

transform tint18: # blue
    matrixcolor TintMatrix("#2c497a")*BrightnessMatrix(-0.35)

transform tint20: # dark gray blue
    matrixcolor TintMatrix("#2a3d6a")*BrightnessMatrix(-0.55)

transform tint22: # dark dark blue
    matrixcolor TintMatrix("#4b72a5")*BrightnessMatrix(-0.70)

# -------------------------------- general tints
transform tintDarkNight: # darken night photos
    matrixcolor TintMatrix(Color(rgb=(0.575,0.565,0.575)))*BrightnessMatrix(-0.45)

transform tintDimRoom: # gray
    matrixcolor TintMatrix(Color(rgb=(0.575,0.565,0.575)))*BrightnessMatrix(-0.05) # matrixcolor TintMatrix("#4C4848")*BrightnessMatrix(0.05)

transform tintDimRoomPink:
    matrixcolor TintMatrix("#776363")*BrightnessMatrix(-0.05)

transform tintSmokyRoom:
    matrixcolor TintMatrix(Color(rgb=(0.255,0.23,0.23)))*BrightnessMatrix(0.55)

transform tintDarkRoom:
    matrixcolor TintMatrix("#4C4848")*BrightnessMatrix(-0.35)

label tintItem:
    show darker:
        alpha .8
    return

image tintPinkFog: # pink orange dawn
    Solid("#fcac9e")
    alpha .1

image tintOrangeFog: # orange dusk
    Solid("#f6c98d")
    alpha .1

# ---------------------------------------------------------------- shaders
# https://wattson.itch.io/kinetic-text-tags @inkacorn

# ---------------------------------------------------------------- TODO rewrite Fade transition
# https://github.com/renpy/renpy/blob/master/renpy/display/transition.py#L201

# -------------------------------- old tints
transform clean_tint:
    matrixcolor TintMatrix(Color(rgb=(0.3,0.3,0.3)))*BrightnessMatrix(0.10)

transform dim_tint:
    matrixcolor TintMatrix(Color(rgb=(0.575,0.565,0.575)))*BrightnessMatrix(-0.05)

transform dim_tint1:
    matrixcolor TintMatrix(Color(rgb=(0.175,0.15,0.15)))*BrightnessMatrix(0.15)

transform midnight_tint:
    matrixcolor TintMatrix(Color(rgb=(0.115,0.110,0.125)))*BrightnessMatrix(-0.15)

# -------------------------------- say window transform
# https://lemmasoft.renai.us/forums/viewtopic.php?t=41776
init python:
    def say_window_transform_function(trans, st, at):
        global say_window_show_transform

        if not "say_window_show_transform" in globals():
            say_window_show_transform = False

        if say_window_show_transform == False:
            st = 0.5
            trans.alpha = 1.0
            say_window_show_transform = True

        if say_window_show_transform == True:
            if st > 0.5:
                trans.alpha = 1
                return None
            else:
                trans.alpha += trans.alpha * st
                return 0
        else:
            return None

    def say_window_transform_reset(trans, st, at):
        global say_window_show_transform
        say_window_show_transform = False

transform text_fade_in_transform:
    alpha 0
    linear 0.5 alpha 1