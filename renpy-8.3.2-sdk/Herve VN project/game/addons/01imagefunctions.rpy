# Mostly for char_blink, but also if anything misc comes along.
init python:
    # eye_open:   (String) Image displayable for eyes open
    # eye_closed: (String) Image displayable for eyes closed
    def char_blink(st, at, eye_closed, eye_open=None, name=None):
        global char_blink_amt, char_in_blink
        blink_image = renpy.displayable(eye_closed)
        open_image = Null()
        if eye_open != None:
            open_image =  renpy.displayable(eye_open)
        # Forced blink
        if name != None:
            if name not in char_blink_amt:
                char_blink_amt[name] = 0
                char_in_blink[name] = None

            if char_blink_amt[name] > 0:
                if char_in_blink[name] == None or char_in_blink[name] == True:
                    char_in_blink[name] = False
                    return (open_image, 0.1)
                else:
                    char_blink_amt[name] -= 1
                    char_in_blink[name] = True
                    return (blink_image, 0.1)
        rand_roll = renpy.random.random()
        if renpy.random.random() < 0.1:
            return (blink_image, rand_roll)
        return (open_image, rand_roll * 2)

    def setup_char_blink(name, blink_amt):
        global char_blink_amt, char_in_blink
        char_in_blink[name] = None
        char_blink_amt[name] = blink_amt + 4

default char_blink_amt = {}
default char_in_blink = {}