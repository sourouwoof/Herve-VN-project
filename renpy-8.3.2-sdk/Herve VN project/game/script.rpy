# The script of the game goes in this file.

# The game starts here.

label start:
    stop music fadeout 30.0
    show road1
    call car_bumps
    show road1 at tint18 with Dissolve(10)
    play music music2
    play sfx1 driving
    $ renpy.music.set_volume(0.10, delay=0, channel='music')
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    pause 5
    play sound phone_notification
    "*phone notification*"
    pause 2
    mci "Is that mom or Hervé ?"
    mco "*yawn* Geez this trip is getting long."
    mco "Those mountain roads are so sinuous. Hopefully I'm nearly arrived."
    mco "But it's not so bad, it's been a long time I've been in the Alps."
    pause 1
    mco "Ugh, it's making me a little nervous."
    mco "Not like I can go back now, I'm so far from home. So far from the city."
    pause 1
    mco "It's funny how I wanted to go back home at midway, I was so nervous... But I've also excitement again like when I planned the trip."
    mco "I wonder how's Hervé."
    pause 2
    mco "Maybe taller, or bigger than his photos ?"
    pause 1
    mco "*sigh* I don't know if he will remember the times I made him advances in Discord. That was cringe."
    mco "How should I be ?"
    pause 1
    mco "Mmh, maybe start slow, and for the rest... Yeah we'll see !"
    pause 2
    mco "He's my best friend, I don't wanna mess it up."
    mco "I don't know how many rants he read from me. But he was always there, and so chill. He helped me a lot going through college."
    pause 1
    mco "I admire him in some ways, he looks like doing what's he's passionate about while keeping a safe space in the Discord server."
    pause 1
    mco "*relieved sigh* It will be okay."
    $ renpy.music.set_volume(0.005, delay=0, channel='music')
    play sound clangclang
    "*cling clang badum*"
    mco "?! Oh shit. Talked too fast."
    camera
    play music driving
    play sound car_break
    show road2 at tint18 with dissolve
    "*car break squeak*"
    pause 1
    mco "Of course it's the snow chains."
    mci "I shouldn't have put them on, I really made a mess. I hope they didn't scratch the car."
    pause 2
    mco "It seems there are no problem, but I'm not too sure if I should continue driving..."
    pause 1
    mco "I forgot the messages."
    $ renpy.music.set_volume(0.5, delay=10, channel='music')
    momt "Did you arrive at your friends house ?"
    pause 1
    mct "Yes. Everything ok."
    pause 1
    mct "Gnight mom {image=emojis/polar-bear.png}"
    pause 1
    momt "{image=emojis/heart.png}"
    mci "And another message from Hervé."
    hert "You ok ?"
    pause 1
    mct "I'm not too far but I have a problem with the snow chains."
    mci "He answers right away,."
    hert "I'm coming where are you ?"
    pause 1
    mci "I share him my position."
    pause 1
    her "{image=emojis/thumbs-up.png}"
    pause 2
    play sound car_door
    mci "It's so freezing, I'm going back to my car and crank up the heat."
    pause 2
    mci "I'm nervous with each car passing by."
    pause 1
    mci "Maybe I can practice, yeah."
    mco "Hello... Hervé, it's me,"
    $ player_name = renpy.input("Your name is:", "Sébastien").strip() or "Sébastien"
    mco "You know... [player_name]."
    mci "Why do real names sound more cringe than online names ?"
    play sound phone_notification
    "*phone notification*"
    mco "New mails {i}\"{u}International corporate volunteering:{/u} Your job application for digital marketing in Seattle\"{/i}."
    mco "Oh shit !"
    pause 1
    mco "{i}... After our series of interviews, we preferred to put other, more adequatly experienced candidates forward for this position. But we hope to see you again very soon ! You can apply for other offers on our website...{/i}"
    mco "Haaan whyyy. My american accent was the best, I practiced so hard. I did like 3 interviews !"
    mco "Fuck them, \"{i}more experienced candidates{/i}\" no shit, it's supposed a program for fresh men ? How am I supposed to get experience for an entry job ?"
    mco "*long sigh* Aaah..."
    show black with close_eyes
    pause 2
    play sound car_arriving

    call end

label end:
    "To be continued...{w=2}{nw}"
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
        $ renpy.music.play(audio.driving, loop=True)
        centered "{cps=0}{color=#ffffff}- Notice -\n This game is a work of fiction.\n Any reference to real people, organizations or events has no connection with this game.\n
        In addition, this game is intended for an audience over 18, and may contain serious themes.\n\n
        Also the game has musics and sound effects, we recommend playing with headphones. Thank you !\n\n
        {image=loading}
        {w=20}{nw}{/color}{/cps}"
        $ persistent.is_first_time = False  
    
    $ renpy.music.play(audio.music1, loop=None)
    $ renpy.music.queue(audio.driving, fadein=5.0, loop=True)