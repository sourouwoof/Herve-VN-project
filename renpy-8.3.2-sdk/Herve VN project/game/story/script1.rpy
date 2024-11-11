label story1:

    camera:
        #reset
        perspective True

    show road1
    call car_bumps
    show road1 at tint18 with Dissolve(10)
    play music music2
    play sfx1 driving
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
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
    mco "I admire him in some ways, he looks like doing what's he's passionate about while keeping a safe place in the Discord server."
    pause 1
    mco "*relieved sigh* It will be okay."
    pause 2
    $ renpy.music.set_volume(0.0, delay=0, channel='music')
    play sound clangclang
    "*cling clang badum*"
    mco "?! Not good not good. Talked too fast."
    camera
    play music driving
    play sound car_break
    show road2 at tint18 with dissolve
    pause 1
    camera: 
        xalign 0.5 yalign 0.5
        ease 2.0 zoom 1.25  
    "*car break squeak*"
    camera: 
        xalign 0.5 yalign 0.5
        ease 2.0 zoom 1.0  
    pause 1
    mco "Of course it's the snow chains."
    mci "I shouldn't have put them on, I really made a mess. I hope they didn't scratch the car."
    pause 2
    mco "It seems there are no problem, but I'm not too sure if I should continue driving..."
    pause 1
    mco "I forgot the messages."
    momt "Did you arrive at your friends house ?"
    $ renpy.music.set_volume(0.5, delay=5.0, channel='music')
    pause 1
    mct "Yes. Everything ok."
    pause 1
    mct "Gnight mom {image=emojis/polar-bear.png}"
    pause 1
    momt "{image=emojis/heart.png}"
    mci "And another message from Hervé."
    hert "You ok ? (don't respond while driving)"
    pause 1
    mct "I'm not too far but I have a problem with the snow chains."
    mci "He answers right away."
    hert "I'm coming where are you ?"
    pause 1
    mci "I share him my position."
    pause 1
    hert "{image=emojis/thumbs-up.png}"
    pause 2
    play sound car_door
    mci "Brrgh. It's so freezing, I'm going back to my car and crank up the heat."
    camera: 
        xalign 0.5 yalign 0.5
        ease 2.0 zoom 1.25  
    pause 2
    mci "I'm nervous with each car passing by."
    pause 1
    mci "... Maybe I can practice to introduce me to Hervé..."
    mco "Hello... Hervé, it's me,"
    $ mc_name = renpy.input("Your name is:", "Sébastien").strip() or "Sébastien"
    mco "You know... [mc_name]."
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
    scene black
    with close_eyes
    play sound car_arriving
    define heru = Character("???", color="#80746e", kind=outter) # character
    pause 5
    heru "{size=21}Hi ! Hello... ?{/size}"
    pause 1
    mci "I hear a familiar suave yet shy voice in the distance."
    mco "Zzz... {size=21}Hi...{/size}"
    play sound knockknock
    pause 1
    scene road2 at tint18 
    show he at middle
    with dissolve
    pause 1
    camera: 
        xalign 0.5 yalign 0.5
        zoom 1.25  
    with open_eyes
    mco "BWAAH !!"
    her "[mc_name] ! Woah, sorry I wasn't sure it was you."
    hide her with fade
    camera: 
        xalign 0.5 yalign 0.5
        ease 2.0 zoom 1.0
    show he with dissolve
    mco "Hello Hervé *yawn*. Urrgh my car did a \"clang clang\". So I stopped here."
    pause 1
    her "..."
    pause 1
    mci "He takes the time to look around my car,"
    pause 1
    her "Sorry I'm thinking."
    her "Your snow chains are too big, {size=21}it will take me some time to remove them and find other ones{/size}..."
    her "My home is not too far... {size=21}Maybe I can prepare the diner and take care of the car just after{/size}."
    mci "He speaks a little to himself in his beard, in a muffled voice. I'm not sure what he says, I'm quite sleepy, but I'm just glad to not be alone anymore."
    her "... {size=21}I hope I have everything in the garage. I think if we let the car here it wouldn't be a problem, there's not too many traffic now.{/size}..."
    mci "I feel some sense of safeness with him..."
    pause 1
    her "You okay if I drive you to my home ? I'll leave you at my place and take care of your car, we're 5 min from my house."
    pause 1
    mco "OK."
    pause 1
    scene black 
    hide he
    with close_eyes
    stop music
    stop sfx1
    pause 5
    mci "... I dreamt about driving with a big bear... And sleeping near a fireplace..."
    play sfx1 fireplace
    pause 5
    
    camera:
        #reset
        perspective True
        
    scene houseGuestHouse 
    show he:
        zpos -2000 xpos 200 ycenter 500
    with open_eyes
    pause 1
    mci "I awake slowly, watching around. I take off a small blanket, and try to remember how I arrived here."
    mci "A bear is reading in front of a fireplace."
    pause 1
    mco "Hi Hervé."
    her "Hello [mc_name] !"
    hide he
    show he at middle
    with dissolve
    pause 1
    mco "We're at your place ?"
    her "Yeah, you slept on this sofa, you slept on the spot."
    mci "I remember now."
    mco "It's cozy here, we're in your lounge ?"
    her "We're in the small lounge, it's an annex."
    mco "You have multiple lounges ?"
    her "Yeah... The house is quite big. I stayed here, I didn't want you to get lost."
    mci "I turn my head to the right and observe a big dark room. The house looks impressive."
    her "I renovated this annex to make a guest house for money, {size=21}but I've never been able to{/size}..."

    show screen timerFrame("continue1") # 10 seconds jump to label after: if fail
    menu:
        "Why ?":
            hide screen timerFrame
            $ affinity += 1
            $ renpy.notify(affinity)
            mco "Aww, why ?"
            her "Oh uhm."
            her "I found that a little complicated to set it up. Advertising isn't my strong point."
            her "It could help me for my retirement, and to keep the house up to date."
            mco "That sounds awesome, it would give you a chance to rest at home."
            her "I should, I should, {size=21}I quite like my own company too{/size}."
    label continue1:
        hide screen timerFrame

    her "*ahem* Other than that, have you had a good rest? "
    mci "I stretch myself a bit."
    mco "*yawn* I slept quite good."
    "*stomach growl"
    her "No worries, I have left overs if you want."
    mco "That would be great, thanks."
    show houseLounge at tint18 with dissolve
    mci "We traverse a large cluttered, dark room and we head to the kitchen."
    show houseKitchen 
    show he at middle
    with Fade(1,0,1)
    mco "Mmh~"
    mci "A gratin dauphinois, potatoes, cheese au gratin and ham. The potatoes are very creamy, which sweetens the whole dish."
    mco "That's real good, is that yours ?"
    her "Mhm, well I have my favourite dishes, and I'm good at making childhood dishes."
    mco "Uh, what time is it by the way ?"
    her "Around 2am."
    mco "Woah oh geez, I thought it was earlier than that."
    her "Sorry, You looked tired I didn't want to wake you up for my diner."
    mco "It's alright. What about you, not feeling tired ?"
    her "Oh no, I usually sleep quite late in the night. {size=21}I don't need it that much now, I'm not a youngster anymore{/size}..."
    mci "I remember he told me that quite a long time ago."
    pause 1
    her "Uhm, I have a day of work just for tomorrow... I've put in my leave for the rest of our vacations."
    her "Would you like to accompany me or stay here ?"
    mco "What will be the work ?"
    her "I'm going to mark out a few paths, clear them and then we'll head back."
    mco "Alright, I'm in. That would be fun to walk with you."
    her "Okay, super !"
    show houseBedroom with Fade(1,0,1)
    mci "After my diner I felt like to rest again. Hervé showed me this bedroom in front of the large lounge."
    mci "It's "
    mco "Really calm in here. A little colder than the guest room but alright."
    mco "*long sigh*"
    pause 1
    mco "What a day."
    pause 2
    mco "It was easier than I expected to talk to Hervé. He's a nice guy to be around."
    mco "A little quirky at times, but it's quite his charm. That's what I always found of him on Discord. A little old fashioned."
    play sound phone_call
    "*incoming phone call*"
    mco "Oh shit, in the middle of the night ?"
    mco "That got to be a scam--"
    womc "Hi mister [player_name] ?"
    mco "Hii ?"
    womc "Hello, I'm miss "
    