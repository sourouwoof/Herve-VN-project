# The script of the game goes in this file.

# The game starts here.

label start:

    pause 5

    "*bzzt*"

    pause 1

    "*bzzt*"

    "*bzzt*"

    pause 1

    "You have 21 notifications unread."

    mc "Geez, am I getting lost ?"

    call end

label end:
    system "To be continued...{w=2}{nw}"
    stop music
    stop sound
    scene black with Dissolve(1)
    pause 2
    $ MainMenu(confirm=False)
    return

# -------------------------------- before main menu
label before_main_menu:
    window hide
    # centered "{cps=0}{color=#ffffff}- Notice -\n This game is a work of fiction for the Novembear.\n\n
    # {image=loading}
    # {w=10}{nw}{/color}{/cps}"
    # $ renpy.music.play(, fadein=5.0, loop=True)
    call car_bumps