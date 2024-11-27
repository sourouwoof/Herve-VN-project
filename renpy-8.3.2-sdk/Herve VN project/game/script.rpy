# The script of the game goes in this file.
default timer_current = 0
default timer_max = 0
default affinity = 0

screen timerFrame(missed_event, timer_max=7):
    on "hide" action SetVariable("timer_current", 0)
    frame:
        xalign 0.5
        yalign 0.6
        hbox:
            timer 0.1 action If(timer_current > timer_max, false = SetVariable("timer_current", timer_current + 0.1), true = [Hide("timerscreen"),Jump(missed_event)]) repeat True

            bar:
                value AnimatedValue(value=timer_current, range=timer_max, delay= 0.5)
                xalign 0.0
                yalign 0.0
                xmaximum 250

"""
jour 1:
MC se réveille dans le chalet de RV. RV lui donne un en cas et chocolat chaud. MC demande ce que fait RV comme travail en ce moment. RV lui propose de lui montrer demain
MC se rendors. Il reçoit un appel d'une des candidatures à l'international qui est à Vancouver et fait une interview.
jour 2:
RV et MC font un tour dehors. RV lui montre comment il balise les chemins. Il lui fait un tour de sa maison.
MC se demande de l'histoire de RV, sa famille, pourquoi il vit seul ici
Ils terminent la journée à regarder des films/jouer aux jv. Il y a de grosses neiges prévues demain
MC reçoit un avis positif pour sa candidature à Vancouver et lui proposent de travailler au plus tôt
jour 3: 
RV fait un tour des dernières pièces de la maison, grenier. Découverte de photos de famille de RV. Photos de l'ancien petit-ami de RV
Journée chill au chaud à jouer aux jv. Mais MC se pose de + en + de questions sur la vie de RV et arrive à lui demander directement
Bouleversé MC fait un calin à RV
Ils continuent à jouer aux jv mais plus proches qu'avant
(Pour la novembear je pense arriver jusque là 🙏 petit cliff hanger peut-être)
Pour la suite:
jour 4: 
MC a de + en + de sentiments pour RV. Mais le joueur a un choix entre répondre au job et simplement rester amis avec RV. Ou bien ne pas répondre et avancer plus vers ses sentiments pour RV
Comme buts il y a:
La vie de RV (comment était sa famille, pourquoi il est ici, son ancien petit-ami, sa sexualité)
Le problème de la candidature de MC à avouer à RV
La vie de MC (pourquoi il est ici, son rêve de partir loin)
"""

# The game starts here.
label start:
    stop music fadeout 30.0
    call story1

label end:
    "The end.{w=2}{nw}"
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