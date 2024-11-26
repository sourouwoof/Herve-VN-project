label story1:

    # ================================== day 1
    show road1
    call car_bumps
    show road1 at tint18 with Dissolve(10)
    show screen snow_screen2 with dissolve
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
    mco "Not like I can go back now, I'm so far from home and the city."
    pause 1
    mco "It's funny but, I wanted to go back home at midway, I was so nervous... But then I've also again excitement like when I planned the trip."
    pause 1
    mco "... I wonder how's Hervé."
    pause 2
    mco "Maybe taller, or bigger than his photos ?"
    pause 1
    mco "*sigh* Oh geez, I don't know if he will remember that one time I made him advances in Discord. That was cringe."
    mco "How should I be ?"
    pause 1
    mco "Mmh, maybe start slow, and for the rest... Yeah we'll see !"
    pause 2
    mco "He's my best friend, I don't wanna mess it up. It's been now, a good couple of years we know each other online."
    mco "I don't know how many rants he read from me. But he was always there, and so chill. He helped me a lot going through college."
    pause 1
    mco "I admire him in some ways, he looks like doing what's he's passionate about while keeping a safe place in our Discord server."
    pause 1
    mco "*relieved sigh* That will be okay."
    pause 2
    $ renpy.music.set_volume(0.0, delay=0, channel='music')
    play sound clangclang
    "*cling clang badum*"
    mco "?!"
    mco "Not good not good. Talked too fast."
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
    mci "I'm getting nervous with each car passing by."
    pause 1
    mci "... Maybe I can practice to introduce me to Hervé..."
    mco "Hello... Hervé, it's me,"
    $ player_name = renpy.input("Your name is:", "Sébastien").strip() or "Sébastien"
    mco "You know... [player_name]."
    mci "Why do real names sound more cringe than online names ?"
    pause 2
    play sound phone_notification
    "*phone notification*"
    mco "... ?"
    mco "New mails {i}\"{u}International corporate volunteering:{/u} Your job application for digital marketing in Vancouver\"{/i}."
    mco "Oh shit !"
    pause 1
    mco "{i}... After our series of interviews, we preferred to put other, more adequatly experienced candidates forward for this position. But we hope to see you again very soon ! You can apply for other offers on our website...{/i}"
    mco "Haaan whyyy. My american accent was the best, I practiced so hard. I did like 3 interviews with them !"
    mco "Fuck, \"{i}more experienced candidates{/i}\" no shit, it's supposed to be an entry job ? How am I supposed to get experience ?"
    mco "*long sigh* Aaah..."
    pause 1
    scene black
    hide screen snow_screen2
    with close_eyes
    play sound car_arriving
    define heru = Character("???", color="#80746e", kind=outter) # character
    pause 5
    heru "{color=#9e8b53}{size=27}Hi ! Hello... ?{/size}{/color}"
    pause 1
    mci "I hear a familiar suave yet shy voice in the distance."
    mco "Zzz... {color=#9e8b53}{size=27}Hi...{/size}{/color}"
    play sound knockknock
    pause 2
    scene road2 at tint22 
    show he hat at middle
    with dissolve
    pause 1
    camera: 
        xalign 0.5 yalign 0.5
        zoom 1.25  
    with open_eyes
    mco "BWAAH !!"
    her eyclosed "[player_name] ! Woah, sorry I wasn't sure it was you."
    hide her with fade
    camera: 
        xalign 0.5 yalign 0.5
        ease 2.0 zoom 1.0
    show he hat with dissolve
    mco "Hello Hervé *yawn*."
    mco "Urrgh I'm sorry we see each other like this... My car did a \"clang clang\". So I stopped here."
    pause 1
    her -eyclosed ebeto "..."
    pause 1
    mci "He takes the time to look around my car,"
    pause 1
    her "Sorry I'm thinking."
    her "Your snow chains are too big, {color=#9e8b53}{size=27}it will take me some time to remove them and find other ones...{/size}{/color}"
    her eblow "My home is not too far... {color=#9e8b53}{size=27}Maybe I can prepare the diner and take care of the car just after.{/size}{/color}"
    mci "He speaks a little to himself in his beard, in a muffled voice. I'm not sure what he says, I'm quite sleepy, but I'm just glad to not be alone anymore."
    her -eblow eyclosed msad "... {color=#9e8b53}{size=27}I hope I have everything in the garage. I think if we let the car here it wouldn't be a problem, there's not too many traffic now.{/size}{/color}"
    mci "I feel some sense of safeness with him... He's got the situation under control."
    pause 1
    her eblow -eyclosed -msad "Are you okay if I drive you back at my home ? I'll leave you at my place and take care of your car, we're 5 min away."
    pause 1
    mco "OK."
    pause 1
    scene black 
    hide he
    with close_eyes
    stop music
    stop sfx1
    pause 5
    mci "... I dreamt about driving with a big bear... And sleeping in a warm and comforting place, probably near a fireplace..."
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    play sfx1 fireplace
    pause 5
        
    scene houseGuestroom 
    show he:
        zoom 0.25
        xalign 0.3
        yalign 0.5
    with open_eyes
    pause 1
    mci "I awake slowly, watching around. I take off a small blanket, and try to remember how I arrived here."
    mci "A bear is reading in front of a heating stove."
    pause 1
    mco "Hi Hervé."
    her "Hello [player_name] !"
    hide he
    show he eyclosed at middle
    with Dissolve(1)
    pause 1
    mco "We're at your place ?"
    her -eyclosed "For sure ! You slept on this sofa, right on the spot."
    mci "I remember now."
    mco "It's cozy here, we're in your living room ?"
    her "We're in the small lounge, it's an annex."
    mco "You have multiple lounges ?"
    her eyclosed "Yeah... The house is quite big. I didn't want you to get lost, so I stayed here."
    mci "Behind Hervé I can watch a bigger room in the dark. Damn, this house looks impressive !"
    her eblow "I renovated this room to make a guest house for money, {color=#9e8b53}{size=27}but I've never been able to set that up...{/size}{/color}"

    show screen timerFrame("continue1") # 10 seconds jump to label after: if fail
    menu:
        "Why ?":
            hide screen timerFrame
            $ affinity += 1
            # $ renpy.notify(affinity)
            mco "Aww, why ?"
            her ebsad "Oh uhm."
            her -eyclosed "I found that a little complicated. Advertising isn't my strong point."
            her "Though, it could help me for my retirement, and to keep the house up to date, for sure."
            mco "That sounds awesome, it would give you a chance to rest at home."
            her eblow eyclosed "I should, I should, {color=#9e8b53}{size=27}I quite like my own company too.{/size}{/color}"
    label continue1:
        hide screen timerFrame

    her eblow eyclosed "*ahem* Other than that, are you fully rested ? "
    mci "I stretch myself a bit."
    mco "*yawn* yeah haha, oddly enough I slept quite good."
    pause 1
    play sound stomachgrowl
    "*stomach growl*"
    pause 1
    her -eyclosed -eblow "... And if you're hungry, I have some left overs."
    mco "... That would be great thanks."
    hide he at middle
    scene houseLounge at tint18 
    with dissolve
    stop sfx1 fadeout 25
    mci "We head forward to the dark room, and we traverse a large, quite cluttered place. I can't really see what's in there, except some decorations here and there. We continue forward, to a kitchen."
    show houseKitchen at tintDimRoom with Fade(1,0,1)
    show he at middle with dissolve
    pause 1
    mco "Mmh~ that's tasty."
    mci "A gratin dauphinois. Potatoes, grilled cheese and toasted ham. The potatoes are very creamy, which sweetens the whole dish."
    mco "That's real good, is that yours ?"
    her eyclosed eblow "Mhm. Well I have my favourite dishes, and I'm quite good at making my childhood dishes."
    pause 1
    mci "I watch the outside, it's really deep dark."
    pause 1
    mco "Uh, what time is it by the way ?"
    her -eyclosed -eblow "Around 2am."
    mco "Woah oh geez, I thought it was earlier than that."
    her eblow "Sorry, you looked so tired I didn't want to wake you up for the diner."
    mco "It's alright. But what about you, not feeling tired ?"
    her msad eyclosed "No, I usually sleep quite late in the night. {color=#9e8b53}{size=27}I don't need it that much sleep, I'm not a youngster anymore...{/size}{/color}"
    pause 1
    her -msad -eyclosed "Uhm [player_name], I wanted to tell you about tomorrow. I took the following days off for our vacations, expect, I couldn't for tomorrow, I will have to go to work."
    her -eblow "... Would you like to accompany me to work or stay at home ?"
    mco "What will be the work ?"
    her "I'm going to mark out a few paths, do some measurements of snow and then we'll head back. Not too much but I need to get that done."
    mco "Alright, I'm in. That would be fun to walk in the snow with you."
    her mhappy eyclosed eblow "Okay, superb !"
    scene houseBedroom at tint18 
    hide he
    with Fade(1,1,1)
    mci "After my diner I felt like to rest again. Hervé showed me this bedroom to settle in, this is front of the large lounge."
    mco "Really calm in here. A little colder than the guest room but it's alright."
    mco "*long sigh*"
    pause 1
    mco "What a long day."
    pause 1
    mco "It was easier than I expected to talk to Hervé. He's a nice guy to be around."
    mco "A little quirky at times, but it's quite his charm. That's what I always found of him on Discord. A little old fashioned."
    pause 2
    play sound phone_vibrating
    "*incoming phone call*"
    mco "Oh shit, in the middle of the night ?"
    mco "That got to be a scam--"
    womc "Hi mister [player_name] ?"
    mco "Hii ?"
    womc "Hello, I'm miss Deborah, from the McSimon company, about your resume for the digital marking job offer. Do you have a couple of minutes for a quick interview ?"
    mco "S-sure !"
    mci "Woah it's a job offer I sent just like that. It's from Seattle I think ?"
    scene houseBedroom at tint18 with Fade(1,1,1)
    womc "... And that's why in McSimon company, our top value is to make new innovations possible."
    pause 1
    womc "Alright, that will set it up. We'll give you an answer within a week."
    mco "O-okay thank you."
    pause 2
    mco "Woah it's been a long time I haven't had an interview..."
    pause 1
    mco "Seattle, it's so far... Though, it could be my only chance... Being independant and living far away..."

    # ================================== day 2
    scene black with Fade(1,0,1)
    pause 1
    scene houseBedroom with Fade(1,1,2)
    play music music1 fadein 15
    pause 1
    show houseLounge with Fade(1,0,1)
    pause 1
    show houseKitchen with Fade(1,0,1)
    pause .5
    
    show road2
    show screen snow_screen1
    show he hat at middle
    show he:
        ease 1.0 xpos 0.48
        pause 1
        ease 1.0 xpos 0.52
        pause 1
        repeat
    with Fade(1,0,1)
    $ renpy.music.set_volume(0.25, delay=0, channel='music')
    her eyclosed "Mmh mh mh~ 🎶 *whistling*"
    mco "*yaawn*"
    her -eyclosed "Woah there big guy, feeling tired again, today ?"
    her ebeto "Or is it not too boring to watch me work ?"
    mco "Oh no ! It's just..."
    pause 1
    her eyclosed eblow "... You must be a bit shifted with your sleep. Sorry, I won't hang around."
    mco "Mmh yeah."
    mci "The cold freezes me in place. And I can't get out of my mind the interview. But I don't really want to tell him about my job searches. It's probably not going to work anyway."
    pause 1
    mci "Hervé seems like to collect samples of snow and making measurments since a short time ago."
    mco "What are you doing, Hervé ?"
    her -eblow mhappy "Well, that's not for my personal collection, it's for scientists. I sometimes get contacted by some universities to take samples. And send remotely the measurements."
    her "{color=#9e8b53}{size=27}Rha ! Scholars are a lazier now with the internet. Hopefully they gave me their equipments and they showed me how to do the work.{/size}{/color}"
    mco "Woah that's more interesting than it looks, you should have explained me that first."
    her -eyclosed "Quite far from my job of forest ranger. That's a retraining I wasn't expecting at my age."
    mco "Hehe, poor old man..."
    pause 1
    show he hat at middle
    her msad eblow eyclosed "*sigh* I'm making the clown, but in reality it's more serious than it seems..."
    mco "It's for the environment ?"
    her -eblow "Indeed. It isn't going in the good direction..."
    mci "He seems careful to sample and measure the snow. He looks calmer now."
    pause 1
    mci "I think he cares deeply about his montains."
    pause 2
    her -eyclosed -msad "{color=#9e8b53}{size=27}That will be it.{/size}{/color} I'm good, we can head back home now."
    mci "Urh, he says that but he's still crouched, not ready to leave... I will give him a hand and help him finish."

    call car_bumps
    scene road1 
    hide he
    with Fade(1,0,1)
    play sfx1 driving
    mci "After the work, Hervé drives us back home."
    pause 2
    hero hat "H-hey soo... ? How was it to follow me to work ?"
    mci "... He breaks this long silence, I was paying attention to the wintry landskape."
    mco "Quite fun actually. I learnt a lot of things with you, for real. You're a real well of knowledge."
    mco "... {color=#9e8b53}{size=27}Like when you showed me how you tuck your pants in your shoes...{/size}{/color}"
    hero mhappy eyclosed eblow "Well, that's not very aesthetics, I admit that. But it's a constant challenge to keep out the cold."
    pause 1
    mci "It's crazy how we never stop joking about each other, it's like very natural. I don't know who started the first."
    pause 1
    mci "Though, I feel some hesitation in his voice sometimes, like some anxiety."
    mco "Hey, Hervé. You know, it's quite alright if we have breaks in our conversations."
    pause 1
    hero -mhappy -eyclosed -eblow "Oh I see..."
    hero msad eblow "I'm used to not speak a lot, it's just I hope I'm not too boring."
    mco "You're not ! I'm not much of a chatterbox either."
    mco "... {color=#9e8b53}{size=27}I quite find your company comforting actually...{/size}{/color}"
    hero -eblow mhappy "Ooh ! Well... Thank you..."
    mco "Hehe."
    mci "Geez, I don't know if I'm doing the right thing... That's kinda stupid to flirt, I should quit that."
    pause 2
    mci "I'm curious about him... He never told that he was living with someone, though this house is so big."
    pause 1
    mco "Say, Hervé what's the story behind the house ?"
    pause 1
    hero eblow eyclosed "I could do you a tour when returning home, you wanna ?"
    mco "Sure !"
    stop sfx1
    
    scene houseOutside 
    camera
    show he hat at middle
    with Fade(1,0,1)
    camera
    her "So."
    her "... How should I start... Well, first, it's an old chalet."
    her eblow "I got it for a pittance, {color=#9e8b53}{size=27}kinda. It was not easy task to restore.{/size}{/color}"
    pause 1
    her msad eblow eyclosed "*ahem* No one wanted it. Too far from cities and no desk work here. The chalet was abandoned and had to be completely redone."
    pause 1
    mco "So, you did the renovations all by yourself ?"
    her "I tried alone for some part like carpentry but for the rest it was sketchy... I ended up asked for help to the neighbors around."
    her -eblow mnormal "By getting closer to them, I found my new job by the way !"
    mco "Forest ranger, woah. I think you're the only one I know. Was this a thing you always wanted to do ?"
    her mhappy "A little childhood dream at some point. I'm not totally sure haha. But now I'm living it, I'm more than happy. It's so diverse, every new season come with its set of work. And I feel helpful to many people around."
    pause 1
    mco "But how did you end up here, nestled deep in the Alps ?"
    stop music fadeout 25
    her -mhappy -eyclosed eblow  "Urh, long story short, when I arrived here, I wanted to start over."   
    her eyclosed msad "I had my reasons, bunch of problems in my life... I needed a break." 
    pause 1
    scene houseLounge 
    hide screen snow_screen1
    hide he
    with Fade(1,0,1) 
    play sfx1 fireplace
    mci "Hervé seemed tired after that. Curiously, like this little conversation unsettled him ?"
    mci "We prefered to sit on the sofa and relax."
    mco "Home sweet home~ so warm in here."
    hero eyclosed eblow "You're melting like an icicle, watch out hehe. Don't worry we we'll stay here now, no need to go outside."
    pause 1
    hero -eyclosed -eblow "Say, we were talking about jobs. What about you-- you told me you were looking for a job, right ?"
    mco "We don't talk about the subjects that upset-- mmh yeah. *sigh* Not much for now unfortunaly."
    hero msad "You don't have to talk about that if you don't want..."
    mci "Arh... I kinda want to now. He's really a guy so easy to talk to."
    pause 1
    mco "Well. Y'know I got my diploma a couple months ago. Though, I haven't told you, but my university is part of a program for helping fresh graduates to find a job abroad."
    mco "I signed up, it was so compelling. They pay us the plane ticket and rent. I never got the chance to go abroad..."
    mco "But I'm nearly at the end of this program, I only have a week to find a job abroad... It's a lot more harder than I expected."
    pause 1
    hero eblow "Oh..."
    hero -eblow -msad "... Why you didn't want to tell me about that ?"
    mco "Uhm... I was a bit stressed since we planned our first meetup too... You're one of my greatest friend, and I was afraid with quite a lot of things at the same time."
    mci "My feelings are all over the place, it's harder to unpack than I expected."
    pause 1
    mco "Are you not upset ?"
    hero eblow "Of course I'm not !"
    hero eyclosed mhappy "First, that's really nice of you to say such things about me, you're a great friend for me too."
    pause 1
    hero msad "I have to say, it wasn't easy for me, invinting you here. I almost wanted to cancel our meeting, but that would have been so rude of me."
    mco "Ooh ?"
    mci "Did I do something wrong ?"
    hero -eblow "... I thought you would be freaked out, I'm quite the ermit. Most of the time I'm working on my own, It's been ages I haven't been to the city or had a real deep interaction with someone."
    pause 1
    mco "B-but you're so chill and caring in the Discord server and all. I see you as quite as social active actually, for real."
    hero eblow mhappy "Ahah that's nice of you... It took me a lot of effort to get there."
    pause 2
    hero mnormal -eblow -eyclosed "... Maybe we can continue the discussion to the kitchen, I would need some hot drink."
    mco "S-sure !"
    stop sfx1 fadeout 15
    scene houseKitchen with Fade(1,0,1) 
    show he at middle with dissolve 
    her eyclosed eblow "There !"
    mco "Thanks Hervé, you're a real bartender."
    mci "He prepared me some chocolate milk. I start drinking it gently."
    pause 1
    mco "... It feels so great."
    her mhappy -eblow "Well, nothing better a hot drink in a wintry day."
    mco "I don't see you as an ermit, you're always full of nice little attentions."
    her -mhappy "Well when I was young, I had more social groups. {color=#9e8b53}{size=27}Though it was never me the first to go to parties.{/color}{/size} That was my boyfriends who made me go out."
    mco "Damn... Hervé. You were hiding a libertine life from me~ ?" 
    her mhappy "I had my good moments, I can say that haha !"

    show screen timerFrame("continue2") # 10 seconds jump to label after: if fail
    menu:
        "Do you miss that ?":
            hide screen timerFrame
            $ affinity += 1
            mco "You don't miss that too much ?"
            her -eyclosed mnormal eblow "... Kinda. But I'm too old now."
            mco "..."
            mco "{color=#9e8b53}{size=27}Though, I think you're pretty handsome.{/size}{/color}"
            her mhappy eblow eyclosed "Rrh shush shush. No flirting. You're too young, you're still a baby to me."
            her -eblow "{color=#9e8b53}{size=27}Our age gap is so large, it just gives me wrinkles thinking about it...{/size}{/color}"
            mco "Aww..."
    label continue2:
        hide screen timerFrame

    pause 2
    mco "Mmh... I'm curious, you said that you were quite active socially before, but now you don't."
    mco "Was it coming to the montains that made you like this ?"
    her -eyclosed mnormal -eblow "For a good part... {color=#9e8b53}{size=27}I've never seen it that way before.{/size}{/color}"
    her "I've always been the shy one with my friends, so I think it was always part in me."
    mci "I feel again that he's avoiding again the why he landed here, I'm not going to push any further."
    her msad eblow "--But I rather think, it's once you grow older it becomes harder to have social interactions."
    mco "Why ?"
    her -eblow "... Mmh. There's less social groups. People of my age already have their friends."
    her "I've never been able to connect deeply with the people around here."
    her eyclosed eblow "{color=#9e8b53}{size=27}... Urrh for the romance part of things, most of the gays are bi dads in heat, that's terrible.{/size}{/color}"
    pause 1
    mco "Oh~ so you had some adventures in the Alps ?"
    her -eyclosed "Over the last 20 years... ? Just two, with old men in retirement. It's either that or rare youngsters here. After a certain age, people go in the city."
    mci "Damn !"
    mco "So, you don't really need a lot of sex ?"
    her mhappy eyclosed -eblow "*chuckles* so curious. No not really."
    her -mhappy eblow "It doesn't interest me anymore. I rarely have libido for all of that now."
    mco "Aaw, that's sad Hervé !"
    her mhappy eyclosed -eblow "Noo... I don't see it that way, it's just I don't need it ! It's rather cumbersome for me."
    her -mhappy "I'm no longer interested in being a one-night stand in a long-term relationship. And body is getting tired too, I don't feel the need anymore. I've come to accept it and that's okay."
    her eblow "I've had my good times, now I prefer to focus on other things in life."
    mci "I find it sad in some way. Though he seems content with it, nearly happy in those last words."
    her -eblow -eyclosed "*ahem* You got so curious, but I'm too now. What about you ? You said me you had a crush on a classmate."
    mco "Well, not long ago. You know, I had my graduation party. Though, I confessed my feelings to him just before we leave. But he left, embarrassed. He hasn't replied me since."
    her msad "Shoot..."
    mco "I was prepared, I did it before we don't see each other, so it's not a big problem. I have the habit."
    pause 2
    mco "... I feel behind others, I never had a girl or boy friend and so many already did. In my class some were already planning to buy a house with their partner, do you believe that ?"
    her ebsad "Oh big guy, don't say harsh things to yourself."
    pause 1
    her eyclosed mnormal "I think you're wonderful and mature person for your age."
    her ebnormal eyopen "Love is a good part of luck, part of takings risks. It's not a race, everyone has a different life. You'll find someone, I'm sure of it."
    her "You already did a big step to come out like this, you can only be proud of yourself, it's no easy task for anyone."
    pause 1
    her eblow mhappy eyclosed "And also, you seem to get on well with some of the members of the Discord server. Some are around your age, and gay too."
    mco "Mmh, yeah."
    mci "I like his optimism, seeing that way, it isn't so bad."
    pause 1
    her -eyclosed -eblow "Hey speaking about them, how about some couch gaming with the server ?"
    mco "With pleasure !"
    play music music3 fadein 1
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play sfx1 fireplace
    scene houseLounge 
    hide he
    with Fade(1,0,1) 
    pause 2
    mar "... Hii Hervé."
    mco "Hi Martin, how are you doing ?"
    mar "Woah [player_name] ? You're with Hervé, you two are in couple now ?"
    mco "..."
    hero eblow eyclosed "Pccht ! ... Of course not ! We just spend the christmas holidays together."
    mar "I see, well I'm surprised [player_name], you managed to get into the big bear's den~"
    mar "... It's okay to be gay, guys, there's nothing to hide~"
    mci "Geez, Martin's always the horny one on our calls."
    hero -eblow eyclosed "*AHEM* {color=#9e8b53}{size=27}Rholala can't be serious for 5 minutes{/size}{/color}..."
    hero mhappy -eyclosed "I think there's only us 3 connected tonight, what game do we play ?"
    pause 1
    mco "Chicken Horse maybe ?"
    pause 1
    mar "I'm in !"
    hero "Let's go !"
    scene houseLounge at tint16dark with Fade(1,1,1) 
    pause 2
    mco "Sapristi !! Your trap got me !"
    mci "Hervé and Martin are really pro ga(y)mers at these kind of platformers. It's like a platformer and party game, we have to place traps to make the parkour harder for others."
    mci "Martin is often ahead but Hervé is never too far behind on the leader board."
    pause 1
    mar "*ahem* I well deserve my pro {i}ga{b}y{/b}mer{/i} status after all."
    hero "*sigh* Alright Martin, you're a real ga(y)mer, we got it."
    mci "Looks like as if Hervé is letting go his 1st position but isn't fully digesting this defeat..."
    pause 1
    mar "Guys, you saw the weather forecast by the way ? It's big snowy day on the whole country tomorrow. Yipee !!"
    hero eblow eyclosed "We've got the habit here, but I'll watch about that, thanks for the info Martin !"
    mar "I love snow, but it's so rare where I am. Like every 2 or 3 years. I'm so excited !"
    hero -eyclosed "Well have fun Martin, I hope at our altitude I won't be too serious."
    pause 2
    define marbf = Character("???", color="#fafafa", kind=calling)
    marbf "{color=#9e8b53}{size=27}My cookie, diners is ready !{/size}{/color}"
    mar "{color=#9e8b53}{size=27}Coming honey !{/size}{/color} Have to go, my maple prepared dinner."
    hero eyclosed mhappy eblow "Have a good meal you two !"
    mco "See ya, have a great night Martin."
    mar "{color=#9e8b53}{size=27}Have a good time in bed guyys~{/size}{/color}"
    play sound phone_endcall
    "*disconnection notification*"
    hero ebeto eyclosed mnormal "Geez..."
    pause 1
    hero ebnormal -eyclosed mnormal "Well... Maybe we could watch a movie together, [player_name] ?" 
    pause 1
    show he at middle with dissolve
    her "I'll reheat some leftovers, you can choose a movie if you want."
    mco "Okay, you have any favorite genres ?"
    her eyclosed "I'm really into cartoons these days."
    mco "It's a good contrast for your age." 
    her eyclosed eblow mhappy "It's late for me worry about that, I've always been a childadult haha."
    hide he with dissolve
    pause 2
    mci "Arrh..."
    pause 1
    mci "... It was just a joke from Martin but I wish it could be real. I thought of it multiple times when we were on the sofa..."
    pause 1
    mci "The more I spend time with Hervé... The more I crave for intimacy and physical contact with him."
    pause 1
    mci "Though... He doesn't seem into me, it kinda breaks my heart but I understand."
    pause 1
    mco "{color=#9e8b53}{size=27}... Maybe just a hug, I could ask ?{/size}{/color}"
    stop sfx1
    stop music fadeout 5
    scene houseBedroom at tint18 with Fade(1,1,1) 
    play sound knockknock
    "*knock knock*"
    her "Hey [player_name] ?"
    play sound light_switch
    scene houseBedroom at tintDimRoom with dissolve
    mco "Come in !"
    show he at middle with dissolve
    pause 1
    her "I just watched the weather forecast, and we are in a snow strom for at least two days. We're going to stay nice and warm at home. Don't hesitate to crank up the heat."
    her eyclosed eblow "... I have spare blankets as well."
    mco "Alrighty, thank you."
    pause 1
    hide he with dissolve
    pause 1
    play sound light_switch
    scene houseBedroom at tint18 with dissolve
    mco "Hervé ... !"
    pause 1
    mco "Have a good night."
    her "You too, sleep tight [player_name]."

    # ================================== day 3
    scene black with Fade(1,0,1)
    pause 1
    play sfx1 snowstorm1
    "*windy outdoor snowstorm*"
    scene houseBedroom at tint16 with Fade(1,1,2)
    pause 1
    show houseLounge at tint16 
    show he eyclosed ebeto msad at middle
    with Fade(1,0,1)
    pause 1
    mco "*yawn* Hi Hervé."
    show he:
        ease 1.0 xpos 0.48
        pause 1
        ease 1.0 xpos 0.52
        pause 1
        repeat
    pause 1    
    mci "It's madhouse this morning, Hervé seems all worried due to the snowstorm." 
    her "{color=#9e8b53}{size=27}The electric meter, with all the machines on, it will trip for sure.{/size}{/color}"
    mci "He's grumbling quietly to himself, while walking in circles. Ke looks clearly laking sleep."
    mci "... Whereas, I'm not very well awake either, I don't even know what time it is."
    pause 1
    her "{color=#9e8b53}{size=27}... I have too turn off all the useless heaters and machines... !{/size}{/color}" 
    her ebsad "{color=#9e8b53}{size=27}... Grr, and I'm really hope the boiler will hold the load this time.{/size}{/color}"
    pause 1 
    mco "Hey, hey Hervé *yawn*."
    mco "Take it easy, I'll take care of it."
    pause 1
    her -eyclosed "... ?"
    show he at middle
    her "Oh sorry [player_name], I didn't even say hello."
    mco "Hervé, we can stay here, near the fireplace ? We wouldn't need to turn on the heat too much if that can."
    her "... That's good idea, I shouldn't stress that much, sorry."
    her "{color=#9e8b53}{size=27}... I haven't slept that well tonight.{/size}{/color}"
    pause 1
    mco "You took care of me the last days, let me take charge of all. I'll do breakfast Rest a bit there on the sofa."
    her eyclosed mnormal "{color=#9e8b53}{size=27}Thank you.{/size}{/color}"
    show houseKitchen at tintDimRoom
    hide he
    with Fade(1,1,1)
    $ renpy.music.set_volume(0.5, delay=5, channel='sfx1')
    mco "Mmh mh mh~ 🎶 *whistling*"
    mci "While waiting for the drinks to heat up in the microwave, I observe the outdoor. It's so dense outside, it's almost like the night in broad day."
    mci "I have a certain feeling of comfortness being indoor right now."
    pause 1
    mci "Hervé surprised me today, he's always so chill and composed. And he should be used to snowstorms..."
    mci "Probably, he carries too much weight on his shoulders and feels obliged to take care of everything ? I haven't realised but from the start, with my car, housing and cooking, he's done a lot." 
    mci "Maybe I can help him relax, and take more the lead to find activities for the day."
    pause 1
    mci "I put my milk and his tea water to the micro wave. Hopefully Hervé doesn't watch me doing breakfast."
    mco "God bless microwaves."
    pause 1
    play sound phone_notification
    "*notification sound*"
    mci "Oh it surprised me ! I thought that was the microwave."
    pause 1
    mci "{i}\"{u}To the attention of Mister [player_name]{/u} - your job application for Seattle.\"{/i}"
    pause 1
    play sound microwave_finish
    "*microwave finishing bell*"
    
    menu:
        "Continue reading the mail":
            $ affinity -= 1
            mco "{i}... After numerous applicants, we have decided that your qualities...{/i}"
            pause 2
            mci "Gosh, why can't say directly I'm not qualified ?"
            pause 1
            mco "{i}... You will be part of the last interview, a homework, for testing your digital marketing skills.{/i}"
            mci "Geez, homework now ? That's new."
            mci "Well I have plenty of time, I'll do that later today."
        "Let that for later":
            mco "Arrh, I'll read that later, breakfast awaits."

    pause 1
    "*Hervé snores*"
    mci "Seems like he managed to find sleep. I'm glad."
    pause 1
    mco "Let's get to work !"
    mci "I'm gonna impress Hervé... Do some the chores, shutdown everything, crank down the heaters, clean up the house. This will take some of the load off Hervé's shoulders, so we'll just have to rest on the sofa and play !"
    scene houseLounge at tint16 with Fade(1,1,1)
    play sound snores
    her "ZzzZzz..."
    pause 2
    mci "...Watching him sleep, I wonder how would be in his age."
    mci "I will not snore like this, right ?"
    pause 1
    mci "That's the first time I see him that way, sleeping at peace."
    mci "For now I've always seen him like a strong figure of some sort... Almost a mentor in some ways, he has quite the experience in a lot of fields."
    play sfx1 snowstorm2 fadein 5
    $ renpy.music.set_volume(1.0, delay=2, channel='sfx1')
    mci "But he has also a sort of naivity in him, I find it rather cute..."
    pause 2
    "*intense outdoor snowstorm wind*"
    mco "Woah... {color=#9e8b53}{size=27}is it me or it's gettin windier outside ?{/size}{/color}"
    mci "Well enough daydreaming, I've work to do. I'll check if the windows are well closed as well."
    show houseLounge at tint16 with Fade(1,1,1)
    mci "... Only left is Hervé's guest room."
    mci "Since I came, I've never been there again, this is where Hervé is sleeping after all..."
    mci "... ! I'm nearly finished so I have to get in."
    show houseGuestroom at tint16 with Fade(1,0,1)
    pause 1
    mci "It's hot in here, he propably needed some heat this night."
    play sound light_switch
    "*heater switch down*"
    mco "Aw poor Hervé, hehe."
    mci "I hope he's getting better, I'll find him some blankets."
    pause 1
    mci "... I remember he told me he had some spare ones, probably I can find them around here..."
    pause 2
    mci "Rummaging around, I can spot a few photos... Is this Hervé ?"
    image youngHerve = "/images/cgs/youngHerve.png"
    show youngHerve:
        xalign 0.5
        yalign 0.5
        zoom 1.25
    with dissolve 
    $ renpy.music.set_volume(0.5, delay=2, channel='sfx1')
    pause 1
    mco "Young Hervé ? He's a stud ! ... ? He's half naked ?!"
    mci "Looks like a cutted photo... I wonder, where would it come from ?"
    mco "Mmmh... A Playboy magazine, who knows... {color=#9e8b53}{size=27}I wonder what Martin could say, for sure he would be astonished.{/size}{/color}"
    pause 2
    mci "He's got the whimsical look. He didn't lose it over the years."
    pause 1
    mci "... I wonder how would we be together, if we were the same age... *long sigh*"
    pause 1
    mci "Oh. Some other photos. With some friends of his ?"
    pause 1
    mco "{i}\"The marais\" Paris, 1990{/i}."
    mci "On it, they all look joyful, and {i}gay{/i}, except Hervé with a quirky smile on it, he seems a little embarrassed."
    pause 2
    mco "And there's a few family photos too..."
    mco "{i}\"Family reunion for mommy\" Amiens, 2018{/i}."
    pause 1
    mci "It's quite the family. Lots of persons on it... Hervé's family certainly. They look like in a retirement house. An old bear lady is in the center, on a wheelchair, surrounded with people of all ages."
    mci "Hervé is a bit hidden just above her, with two relatively older bears of his age. There's also balloons shaped like \"90\", looks like his mom got 90 years old !"
    mci "She seems tired, but with a joyful smile... The nearest bears seem too, except Hervé with a smallest smile."
    mci "Though..."
    mci "What about his father... ? I can't seem to find an older man bear on it."
    hide youngHerve with dissolve
    pause 1
    mci "I wonder why Hervé's so grave on these family photos..."
    pause 2
    mco "{color=#9e8b53}{size=27}... I'll put it back, it's none of my business.{/size}{/color}"
    scene black
    $ renpy.music.set_volume(0.2, delay=2, channel='sfx1')
    play sound light_switch
    "*light switch*"
    mci "?!"
    play sound broken_glass
    "*broken glass*"
    mco "Noo ! Woah ?! What's happening ?"
    mci "I slipped away the photo frame, it's all dark all of the sudden but can't move, I'm going to cut myself."
    pause 1
    mco "Hervé ?? Hervé !"
    pause 2
    mco "Hervé !! Please wake up ! ... I don't like this, I'm scared... !"
    pause 2
    her "?! Nngh, [player_name] ?"
    her "Where are you, are you okay ?"
    mco "Hervé ! It's all dark, I dunno what's happening."
    her "Oh shoot it's probably the electric current that has gone out. Don't move I come for you."
    pause 1
    show houseGuestroom at tint20 with dissolve
    mco "Be careful, there's broken glass... I dropped a frame."
    her "Here I am."
    show he at middle with dissolve
    mci "He brushes away the glass around me with his feets."
    mco "I'm so sorry, I dropped it."
    mci "It's like I'm about to cry, tears well up in my eyes. I really screwed up, it's his stuff, I shouldn't have touched it."
    pause 1
    mci "... Yet he stays so composed and kind."
    mci "He takes the photo on the floor, give a quick a look at it, but doesn't seem upset."
    her ebsad "Are you okay big guy ?"
    pause 1
    mci "He's really close to me. With the intense wind outside and this all dark house, I feel relieved I'm with Hervé right now. So serene, that I would really like..."
    pause 1
    mco "Hervé... {color=#9e8b53}{size=27}I would greatly like to... Hug with you.{/size}{/color}"
    pause 1
    her eblow eyclosed "O-oh sure. Come here {color=#9e8b53}{size=27}be careful with the glass.{/size}{/color}"
    show he:
        xalign 0.5
        yalign 0.0
        ease 2.5 zoom 1.5
    with dissolve
    mci "He envelops me completely with his arms, he's taller so it's easy for him. I had time to cool off a bit, while Hervé was still all warm on his belly due his nap. "
    mci "My arms are all curled up... Though, I would really like to touch him."
    pause 1
    her eyopen "{color=#9e8b53}{size=27}You feeling better ?{/color}{/size}"
    mco "{color=#9e8b53}{size=27}Y-yes.{/color}{/size}"
    her eyclosed "{color=#9e8b53}{size=27}Lemme clean the floor, let's go on the sofa.{/color}{/size}"
    pause 1
    show houseLounge at tint20 
    play sfx1 fireplace
    hide he
    with Fade(1,1,1)
    mci "After the clean, we checked the electric meter, but no luck to put it back on. By calling a neighbor, we got informed that it's a general electric breakdown, and they advised us to stay safe home."
    hero ebsad msad "We'll need to be careful with power, I'll shutdown my phone for now."
    pause 1
    mci "He pauses for a moment with a serious look, I can tell he's planning things, then he looks at me and take a relaxed face again."
    hero eblow mnormal "{color=#9e8b53}{size=27}Arrh{/color}{/size} *sigh*..."
    hero "... Let's just rest a bit on the sofa, come here."
    mci "He taps on the sofa and shows me a place next to him."
    pause 2
    mci "The place quite peaceful, I observe all around me, this immense house in the dark. With the presence this feels more reassuring. We are just the two of us, and safe."
    pause 2
    mci "... Thinking about it, there's not much to do without electricity, except maybe... Waiting..."
    pause 2
    mci "Except... We could continue the hug we were doing ?"
    mci "I slowly make my way towards him..."
    pause 2
    hero eyclosed "Come here, come here..."
    pause 1
    mco "I really needed it."
    hero "... Me too..."
    pause 2
    hero -eyclosed "That was on my mind last night."
    mci "Slowly put my head on his torso and my hand on his belly, so soft. He's petting me too, really gentle to the touch."
    pause 1
    mco "... Hervé."
    mco "Is it okay with your frame ? You're not upset ?"
    hero "No I'm not."
    hero "It's no big deal, it's just a frame."
    pause 1
    mco "There's your mom and your family on it, right ?"
    hero msad eyclosed eblow "Mmh-- yeah."
    mco "You seemed morose on the photo, this is not the Hervé I know... !"
    hero mhappy eyclosed eblow "Mmmh... Haha."
    hero msad "Mmmh, well... Urrh. I've never felt great in my family."
    pause 2
    hero ebsad -eyclosed "I've never been able to find a job and be straight. And quite shy to be frank, due to my sexuality."
    hero ebnormal "Eventhough, I managed to have a couple of friends in Paris, it really helped to know who I was."
    hero "... I was the eldest brother at home late and jobless, my parents weren't too kind with me. It was the hardest times in my life, like roller coasters."
    pause 1 
    hero -eblow "And, after a moment, I just left home ! It was the point of no return, but I just... Needed that !" 
    hero mnormal "... I... Took my car, to the countryside. With very few money, and no idea for a job."
    hero "Until I stamped uppon this valley."
    hero eyclosed mhappy eblow "And quite some time after, I even got my own little house !"
    pause 2
    hero -mhappy "... My family, I recontacted them at some point. I tried to come see mom once in a while, but the mood is so chilly. And I can't find myself to speak. *chuckles* There's an immense snowstorm between us."
    hero msad "Now, I'm just that weird uncle that rarely calls, and leaves family reunions as soon as possible, I don't wanna get involved much."
    mco "... That sounds terrible Hervé."
    pause 1
    hero mhappy "... That's why I prefer to focus on friends."
    pause 2
    hero msad "It was a good part of my fault, but I prefer to think, the problem of everything was my sexuality... There's nothing to be done with my family, that's way too late."
    mco "O-okay, I see."
    pause 2
    mci "I remember yesterday... A good friend's quote..."
    pause 2
    mco "... It's okay to be gay !"
    pause 2
    hero eyopen mhappy "*chuckles* Yeah. Thank you very much."
    show screen timerFrame("continue4") # 10 seconds jump to label after: if fail
    menu:
        "Continue hugging" if affinity > 1:
            hide screen timerFrame
            $ affinity += 1
            mci "I stay in Hervé's arms, petting him, I want to comfort him."
            mco "I really like that."
            hero eyclosed eblow mnormal "... I like it too, it's been a very long time I haven't done that."
            mco "O-oh, there's something the matter ?"
            hero -eblow "Urrh... A tiny thing between us, it's just our ages, again."
            mco "*chuckles* Well, you're about the same age as my dad."
            hero msad "..."
            hero mnormal "*long sigh* My god."
            pause 2
            mci "I'm starting to make circles around his belly, I want to say many things to him, this is a really a good moment..."
            mco "I want to say be franc with you Hervé..."
            mco "Since we exchanged online, you are real a great friend for me. Maybe my best friend."
            mco "... Even my mentor in some ways. You were always kind and there to help me."
            pause 2
            mco "And sometimes, you were so kind, I thought we could be together."
            mco "But I knew it would be weird probably, my family wouldn't agree for sure. So I preferred to not cross the line, and finding someone my age."
            mco "Although, now..."
            pause 2
            mco "... I feel it would be possible for me to love you."
            hero -eyclosed -eblow "Woah there hehe..."
            pause 1
            hero -eblow "I like you're frank and optimistic about it."
            hero eyclosed msad "I don't know... Urrh actually, I thought about it, this night..."
            pause 2
            hero "... I think it would take time for me..."
            pause 1
            hero mnormal -eblow "But I'm into you too."
            mco "Awww ??"
            mci "I do my biggest puppy dog eyes to him."
            hero mhappy "But please, I would need to time. I know you're young and all..."
            mco "Sure !!"
            pause 2
            mco "{color=#9e8b53}{size=27}Could we sleep together this night ?{/color}{/size}"
            hero ebeto mnormal "No, no, sorry. Not now yet."
            mco "Aw."
    label continue4:
        hide screen timerFrame
    pause 2    
    mci "... I kinda have an idea to lighten Hervé's mood..."
    mco "... Besides, what do you think about telling stories to each other Hervé ?"
    mco "I don't know, but you telling me your life, it kinda reminded me of a papa bear telling me some stories."
    hero ebeto -eyclosed "Ruff-- Papa ? Bear ?"
    mco "*chuckles*"
    hero eblow eyclosed "*sigh*, well why not. What's on your mind, some sort of roleplay ?"
    mco "Yeah ! Lemme begin."
    pause 2
    mco "We're together in a strange forest... {color=#9e8b53}{size=27}I'm a great mage and you're...{/color}{/size}"
    pause 1
    scene black with Dissolve(5)
    pause 5
    show screen snow_screen1
    pause 6
    show screen snow_screen6
    pause 6
    mci "Winter after winter..."
    pause 1
    mci "I will always remember this first moment with you, that changed my life."
    hide screen snow_screen2 with dissolve
    hide screen snow_screen6 with dissolve
    define mcc = Character("[player_name]", color="#696fd4", kind=outter)
    play sound phone_call
    pause 6
    stop sound
    if affinity > 2:
        
        play music music3 fadein 2
        mcc "Hey mom ! How are you ?"
        pause 2
        mcc "Yeah, I'm with Hervé !"
        her "{color=#9e8b53}{size=27}... H-hi madam !{/color}{/size}"
        pause 2
        show photo1
        mcc "{i}What are we doing...{/i} ? We are preparing the home for you, for the holidays."
        mcc "*chuckles* of course ! We are quite early, we are sorting out the stuff, well that's Hervé you know..."
        pause 2
        mcc "Mhm yeah, time goes fast... It's been roughly my first year I living here. I've seen all the seasons, it's been so great, I'm glad living here."
        show photo2
        pause 2
        mcc "I'll show you the hiking, the little villages. And the food !"
        mcc "{color=#9e8b53}{size=27}Hervé also wants to make the best impression for you, as always-- He's all tense for real...{/color}{/size}"
        her "{color=#9e8b53}{size=27}H-hey, honey... !{/color}{/size}"
        her "Sorry madam, he's saying nonsense..."
        her "[player_name] is a real naughty boy, for sure Santa Claus won't come for him this winter... I don't know if we will deserve our present..."
        pause 2
        mcc "Heyy ? What ? What are you two up to, there's a gift for me ? "
        her "You'll know the 25th !"
        mcc "..."
        mcc "*ahem* Well, we'll finish to setup everything today. Only a few weeks left, it will be fun together, I'm sure you'll really like the place !"
        show photo3
        pause 1
        mcc "See ya !"
        pause 1
        scene black with Dissolve(5)
    else:

        play music music2 fadein 2
        mcc "Hi mom ! How are you doing ?"
        mci "I'll always "
        pause 1
        scene black with Dissolve(5)
    return

image photo1:
    Image("cgs/PXL_20210824_103510106.jpg")
    xalign 0.2
    yalign 0.3
    zoom 0.15
    alpha 0
    parallel:
        linear 1 rotate -2.5
    parallel:
        linear 1 alpha 1

image photo2:
    Image("cgs/PXL_20210822_183431273.jpg")
    xalign 0.8
    yalign 0.3
    zoom 0.15
    alpha 0
    parallel:
        linear 1 rotate +2.5
    parallel:
        linear 1 alpha 1

image photo3:
    Image("cgs/PXL_20210822_185216451.jpg")
    xalign 0.5
    yalign 0.3
    zoom 0.15
    alpha 0
    parallel:
        linear 1 rotate +2.5
    parallel:
        linear 1 alpha 1
