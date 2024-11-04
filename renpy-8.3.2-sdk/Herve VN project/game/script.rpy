# The script of the game goes in this file.

# The game starts here.

label start:
    play music driving
    show road1
    call car_bumps
    show road1 at tint18 with Dissolve(10)
    pause 5
    play sound phone_notification
    "*phone notification*"
    pause 2
    mci "Is that mom or Hervé ?"
    mco "*yawn* Geez it's long. Tired."
    mco "Those mountain roads are so sinuous now. Hopefully I'm nearly arrived."
    pause 1
    mco "Thinking about it, it's making me nervous."
    play sound clangclang
    "*cling clang badum*"
    mco "?! Oh shit."
    camera
    mco "Of course it's the snow chains."
    mci "I shouldn't have put them on, I made a mess. I hope they didn't scratch the car."
    pause 1
    mco "?!"
    "..."
    mco "I should call you by your nickname or real name ?"
    heo "Oh, Hervé. That will be more natural."
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
    if persistent.is_first_time:
        window hide
        centered "{cps=0}{color=#ffffff}- Notice -\n This game is a work of fiction.\n Any reference to real people, organizations or events has no connection with this game.\n
        In addition, this game is intended for an audience over 18, and may contain serious themes. By continuing, you accept these terms.\n\n
        {image=loading}
        {w=10}{nw}{/color}{/cps}"
        $ persistent.is_first_time = False  
    # $ renpy.music.play(, fadein=5.0, loop=True)