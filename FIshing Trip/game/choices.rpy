screen test():
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "testing" action Jump("no_fussy")

        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "testing" action Jump("L_father")

screen imgtest:
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        imagebutton:
            idle "button1.png"
            action Jump("no_fussy")

        imagebutton:
            idle "button2.png"
            action Jump("L_father")

screen choice1:
    hbox:
        xalign 0.5
        yalign 0.4
        spacing 300

        imagebutton:
            idle "dadtalk.png"
            action Jump("dad_school")

        imagebutton:
            idle "ctalk.png"
            action Jump("grandpa")

screen choicedad_school_reply:
    hbox:
        xalign 0.5
        yalign 0.4
        spacing 300

        imagebutton:
            idle "dadtalk.png"
            action Jump("workingout")

        imagebutton:
            idle "ctalk.png"
            action Jump("yourschool")

screen choicegrandpa_reply:
    hbox:
        xalign 0.5
        yalign 0.4
        spacing 300

        imagebutton:
            idle "dadtalk.png"
            action Jump("visiting")

        imagebutton:
            idle "ctalk.png"
            action Jump("fishing")

screen choice2:
    hbox:
        xalign 0.5
        yalign 0.4
        spacing 300

        imagebutton:
            idle "dadtalk.png"
            action Jump("workingout")

        imagebutton:
            idle "ctalk.png"
            action Jump("fishing")

screen choice3:
    hbox:
        xalign 0.5
        yalign 0.4
        spacing 300

        imagebutton:
            idle "dadtalk.png"
            action Jump("girlfriend")

        imagebutton:
            idle "ctalk.png"
            action Jump("firstcrush")

screen choicegirlfriend_reply:
    hbox:
        xalign 0.7
        yalign 0.4
        spacing 300
        imagebutton:
            idle "ctalk.png"
            action Jump("meetmom")
