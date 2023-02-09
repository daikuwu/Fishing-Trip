# The script of the game goes in this file.

define f = Character("Father", window_background=Frame("transparent"))
define c = Character("Connor", window_background=Frame("transparent"))

define slowdissolve = Dissolve(2.5)

define crush = False
define girlfriend = False

## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.
## https://www.renpy.org/doc/html/splashscreen_presplash.html

## The animation is boring so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html

image splash_anim_1:

    "gui/renpy-logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0 zoom 2.0

default persistent.firstlaunch = False

label splashscreen:

    scene black

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.firstlaunch:

        ## This screen is at the top of extras.rpy

        call screen splash_settings

        ## This screen will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.firstlaunch = True

    ## Here begins our splashscreen animation.
    show splash_anim_1
    show text "{size=60}Made with Ren'Py [renpy.version_only]{/s}":
        xalign 0.5 yalign 0.8 alpha 0.0
        pause 6.0
        linear 1.0 alpha 1.0

    ## The first time the game is launched, players cannot skip the animation.
    if not persistent.seen_splash:

        ## No input will be detected for the set time stated.
        ## Set this to be a little longer than how long the animation takes.
        $ renpy.pause(8.5, hard=True)

        $ persistent.seen_splash = True

    ## Players can skip the animation in subsequent launches of the game.
    else:

        if renpy.pause(8.5):

            jump skip_splash

    scene black
    with fade

    label skip_splash:

        pass

    return

## The game starts here.

label start:
    scene black

    f "Ah every time I come here I still can’t get over the beautiful view"
    f "The last time we came here together was when you were still a baby."
    c "Dad please that was 2 years ago when I was 18."
    f "Pretty much a baby to me still."
    c "I get it you’re old."
    f "Hehe"
    f "You almost done with that anchor?"
    c "Yup."

    play sound "audio/sound-effect-hd.mp3" volume 2.0

    c "Anchor deployed."
    f "Good now grab that rod and start fishing. Already got a headstart."

    scene base
    with slowdissolve

    play music "audio/湖畔の物語.mp3" fadein 2.0 volume 0.3

    call screen choice1

label dad_school:
    f "How’s school?"
    c "It’s alright. Made some friends and my classes are going well."
    f "Good. You know I was surprised when you said you wanted to go to college."
    f "No one has ever been to college before in our family. Well besides your mother."
    f "Me and my old man were taking bets on whose business you would take over. Mine or his."
    f "Oh course your mom won the bet though. She’s always right."
    c "I know. You were always getting me to help you out at work."
    c "But I always had other plans."
    f "Wait you’re telling me it was always your plan to go to college?"
    c "Pretty much."
    f "Did your mom put you to it so she can win the bet?"
    c "No it was something I wanted to just do for a while."

    pause 1.0

    f "Any girls in your class?"
    c "I mean ya there are obviously some girls in my class."
    f "You know that’s not what I meant. Interested in any of them?"

    pause 1.0

    c "No."

    call screen choicedad_school_reply

    return

label yourschool:
    c " What was your school like?"
    f "Oh don’t get me started."
    f "I was the king of my high school."
    f "Best football player in the area. Went to parties. Started parties. You know the average teenager stuff."
    f "Oh and the ladies all wanted me."
    c "Did mom know about this?"
    f "This was before I met her but she probably did stuff like this too when she was a teenager."

    call screen choice2

    return

label grandpa:
    c "How’s grandpa been?"
    f "Ah, you know his grumpy self."
    c "So he’s fine. Got it."
    f "Yup. When he’s not grumpy you know somethings wrong."
    c "Was he always this grumpy?"
    c "I don’t remember him being grumpy when I was a kid."
    f "Nah he’s grumpy ever since you went to high school."
    c "Oh ya I remember him asking me if I had a girlfriend already."
    f " Ya he was really upset that you went through all of high school without getting a girlfriend."
    f "Honestly I was kind of disappointed too. I had tons of girlfriends throughout high school."
    f "But I know you’ll find her eventually."

    pause 1.0

    c "Sorry..."
    f "Nah it’s ok. Just tell your grandpa to get over it already."

    call screen choicegrandpa_reply

    return

label visiting:
    f "You planning on visiting grandpa anytime soon?"
    c "Umm I probably shouldn’t. The last time we spoke he told me not to come back until I had a girlfriend."
    f "I’m sure he was just joking."
    f "We can go there together next week how about that?"

    pause 1.0

    c "Sure I probably should talk to him."

    call screen choice2

    return

label workingout:
    f "Been working out lately? Can see you're growing some muscles."
    c "I guess. My friends pretty much force me to go to the gym."
    f "Good on them. If they didn’t I would have."
    f "Play any sports?"
    c "‘Not really. Some of my friends play volleyball and are part of the college’s team."
    c "I play with them sometimes."
    f "You should join the team. Women love an athletic man. I can tell you from experience."
    f "Wait is that why you started working out? To get the ladies?"

    pause 1.0

    c "No I just felt I need to do some form of physical activity."
    c "But mostly because friends force me to. If I had a say I would just do it at home."
    f "Hmm…"
    f "If that’s what you say."
    f "Remember I’m your father so you can trust me. I can give you a hand if you need me to help wingman."
    f "Ah, but it would probably be better for your mates to be wingmen for you."

    call screen choice3

    return

label fishing:
    c "Hey dad have you always liked fishing?"
    f "Yup have been fishing since I was 5 when my old man used to take me."
    c "Didn’t you also start taking me fishing when I was 5?"
    f "Huh I guess I did. I guess It’s becoming some sort of tradition."
    f "Guess you gotta do this when your kid turns 5."

    pause 1.0

    c "I never enjoyed fishing so I won’t make any promises."
    f "How about I take them for you?"
    f "Ah but that would mean you gotta have kids before I’m gone."
    f "So you better get on that."

    pause 1.0

    c "Again no promises."

    pause 1.0

    f "Wait I just realized what you said."
    f "You telling me you don’t like these fishing trips? :("
    c "How did you just sad face verbally?"
    c "Anyways ya never really enjoyed them."
    c "Just not my thing I guess."

    call screen choice3

    return

label girlfriend:
    $ girlfriend = True

    f "How’s your girlfriend been? You rarely talk about her?"
    c "Oh.. well"
    c "We… broke up last year."
    f "What!"
    f "What did she do?"
    c "Nothing! It wasn’t their fault."
    f "Ah I see."
    f "Son, it’s very wrong to cheat on your girlfriend. You have to respect and be loyal to her."
    c "What no dad I didn’t cheat on them!"
    f "Oh sorry that were vibes I was getting."
    c "Don’t ever say vibes again."
    c "It was…"

    pause 1.0

    c "I didn’t feel the same way she felt with me."
    f "Then why did you get with her in the first place?"
    c "Well... I thought what I felt with them the same way she felt."

    pause 1.0

    f "Don’t worry Connor you'll find that special someone."

    call screen choicegirlfriend_reply

    return

label meetmom:
    c "Hey dad how did you meet mom?"
    f "Oh now that’s a story."
    f "I met her at a bar."
    f "Tried asking her out but you know what she did?"
    c "She slapped you didn’t she?"
    f "What?! How did you know?"
    f "Did your mom tell you?"
    c "No it was just obvious."
    f "Well ya she did."
    f "And as a true gentleman, I backed off."
    f "But you wouldn’t believe it the next day I met her at the same bar."
    f "She apologized for slapping me."
    f "She then took up my offer to go on a date."
    f "And the rest is history."
    f "I hope the story for when you find a wife is just as interesting."
    f "You’ll get to tell your kids when you go fishing with them."
    f "Oh I should tell you grandpa’s story on how he met grandma."
    f "Maybe he’ll know his old man’s story."
    f "We can hear stories up the family roots."
    c "Ya that sounds nice."
    f "Let’s make this a tradition. Tell your kids my story too."

    pause 1.0

    c "No promises."
    f "Bah you better."

    jump ending

    return

label firstcrush:
    $ crush = True

    c "Who was your first crush?"
    f "What with that question? It feels like we’re playing truth or dare."
    f "Let’s see… There was a girl in my class when I was in elementary school."
    c "Do I know them?"
    f "Probably not, haven’t seen them since elementary school."
    f "I remember having the biggest crush on her when I was young."
    f "Always trying to be with her. Trying to impress and get her attention"
    f "What about you? Who was your first crush?"

    pause 1.0

    c "I don’t think I ever had one from what I can remember."
    c "I know a lot of my classmates talked about it a lot."
    c "Actually some of my current classmates still talk about it."
    f "You’re young of course you'll still talk about it."
    f "None at all?"
    c "Nope none that I can think of."
    f "Maybe you just didn't know at the time."

    pause 1.0

    c "Well, I didn’t understand my feelings before but now I'm certain."

    jump ending

label ending:
    pause 1.0

    scene cgetsup
    with slowdissolve

    c "Hey dad…"

    scene dadgetsup
    with slowdissolve

    f "Ya Connor. What’s up?"
    c "There’s something I need to tell you."

    pause 1.0

    c "I…"
    c "I don’t plan on having a girlfriend."
    c "or kids either."
    c "I’m aromantic and asexual."

    pause 1.5

    f "That’s not gay."
    f "What is that?"
    c "Well, aromantic basically means I feel little to no romantic feelings towards anyone."
    c "And asexual means I feel no desire to be intimate with someone."

    if crush:
        c "Remember how you felt towards your first crush."
        c "I never felt that with anyone."
        c "I thought I did but turns out it wasn’t the same feeling."

    if girlfriend:
        f "What about your girlfriend?"
        c "Ya well this is the reason why we broke up."
        c "When I first met her I thought I had a crush on them."
        c "I thought she was so cool."
        c "I wanted to be just like them."
        c "I didn’t know what having a crush was supposed to be like at the time so I thought the feelings I had for them were a crush."
        c "Turns out feeling like you wanted to be like someone isn’t the same as wanting to be with someone."

    pause 1.0

    c "Everyone expects everyone to get married, have kids, then die."
    c "And I’m not meeting that expectation."
    c "I’m sorry it ends with me."
    f "Connor!"

    scene hug
    with slowdissolve

    f "It’s ok."
    f "Roots don’t grow forever."
    f "I don't care if it ends with you or my grandkids or whatever."
    f "I never meant to make you feel forced."

    pause 1.0

    c "I know."

    scene black
    with slowdissolve

    c "Thanks dad."





    return


## End Credits
label credits:

    ## We hide the quickmenu for the last part of the game so they don't
    ## appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things
    window hide

    scene black with fade

    ## Find "End Credits Scroll" in extras.rpy to change text.
    call screen credits(15.0)

    $ persistent.credits_seen = True

    scene black
    with fade

    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:

        pass

    centered "Fin"

    if persistent.game_clear:

        pass

    ## Do you want to leave some author's notes or a hidden message for your dedicated fans?
    ## This will check if they've seen all that the game has to offer.
    else:

        if readtotal == 100:

            #$ achievement.grant("Completionist")

            ## Due to the way that $ percent() works, we need to make this a text displayable
            ## or else it'll try to count it too.
            show text "{size=60}{color=#ffffff}You've unlocked a special message.\nAccess it through the Extras Menu.{/color}{/s}":
                xalign 0.5 yalign 0.5 alpha 0.0
                linear 1.0 alpha 1.0

            $ persistent.game_clear = True

            ## The game will show our text displayable so the player can read it
            ## And only continue when there is input
            pause

    ## We re-enable the quickscreen as the credits are over.
    $ quick_menu = True

    # This ends the game.
    return
