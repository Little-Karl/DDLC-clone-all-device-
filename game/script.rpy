label start:

# define name dow now?
# yes it helps later but 
# at the start?
    $ s_name = "???"
    $ y_name = "Girl 1"
    $ n_name = "Girl 2"
    $ m_name = "Girl 3"

# call chapter 0 (real story start)
    call ch0 
return

label ch0:
# stop music with fadeout 2 seconds
    stop music fadeout 2.0
# setup scene bg residental with desolve effect
    scene bg residential with dissolve_scene_full
# in the definition section in the options.rpy
# c2 is being defined as audio.bgm2
    play music bgm2

# story start 
# s is the charactor name, 
# and it's curently defined as ???
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."

# lable s_name as Sayori. 
# This will also labe s as sayori 
# Since sayori is about to show herself
    $ s_name = "Sayori"

# define where to place the girl sayori on the next sayori line
    show sayori 4p at t11
# only have to define "s 4p" once
# the rest will cary on, 
# unless in one of the line have a charactor expression change
    s "Haaahhh...haaahhh..."
    s "I overslept again!"
    s "But I caught you this time!"
    mc "Maybe, but only because I decided to stop and wait for you."

# will look at it again
    show sayori 5c at s11
# story continues
    s "Eeehhhhh, you say that like you were thinking about ignoring me!"
    s "That's mean, [player]!"
    mc "Well, if people stare at you for acting weird then I don't want them to think we're a couple or something."

# change sayory body to 1a
    show sayori 1a at t11
# story continues
    s "Fine, fine."
    s "But you did wait for me, after all."
    s "I guess you don't have it in you to be mean even if you want to~"
    mc "Whatever you say, Sayori..."
# the next dialogue line changed sayori appearence to 1q instead of 1a
    s 1q "Ehehe~"

# make sayori body hide like it's fading away? Kind of
    show sayori at thide
# hide the girl
    hide sayori
# more dialogue
    "We cross the street together and make our way to school."
    "As we draw near, the streets become increasingly speckled with other students making their daily commute."

# show sayori again on the next sayori dialogue
    show sayori 3a at t11
    s "By the way, [player]..."
    s "Have you decided on a club to join yet?"
    mc "A club?"
    mc "I told you already, I'm really not interested in joining any clubs."
    mc "I haven't been looking, either."

# 4h
    show sayori 4j at s11
    s "Eh? That's not true!"
    s "You told me you would join a club this year!"
    mc "Did I...?"
    "I'm sure it's possible that I did, in one of our many conversations where I dismissively go along with whatever she's going on about."
    "Sayori likes to worry a little too much about me, when I'm perfectly content just getting by on the average while spending my free time on games and anime."
    s 4j "Uh-huh!"
    s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
    s "Your happiness is really important to me, you know!"
    s "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
    s 4g "You trust me, right?"
    s "Don't make me keep worrying about you..."
    mc "Alright, alright..."
    mc "I'll look at a few clubs if it makes you happy."
    mc "No promises, though."
    s 1h "Will you at least promise me you'll try a little?"
    mc "Yeah, I guess I'll promise you that."



return