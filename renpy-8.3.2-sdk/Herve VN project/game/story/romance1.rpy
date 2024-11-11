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

label romance1:
    mco "Aww, why ?"
    her "toto"
    return
