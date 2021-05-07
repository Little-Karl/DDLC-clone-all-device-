# READ BEFORE BRAGING ABOUT NOT ABLE TO FIND ANYTHING IN THE CODE
# All parmairtors(s, y, n, m, mc, music, residental, bgm2) are defined in parm.rpy 

# label start: is what the enginge will look for when the game launches and starts here  
label start:
    # naming before the story starts
    $ s_name = "???"
    $ y_name = "Girl 1"
    $ n_name = "Girl 2"
    $ m_name = "Girl 3"

    # teleport to lable ch0
    call ch0 

# tell the enginge this is the end of this lable
return



# tell the enginge this the the ch0 section
label ch0:
# scene setup (residental)
    # use residential scene with transistion "dissolve_scene_full"
    scene bg residential with dissolve_scene_full
    # Start playing the story background music bgm2
    play music bgm2
    # end of scene setup

# Use S at the front of the dialogue to define the sayer of that dialogue
    s "Heeeeeeeyyy!!"
    # lines without sayer defined(blank) will defaulted as narrator
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."

# change the S sayer to Sayori
    $ s_name = "Sayori"

# show sayori at positions "t1"
    show sayori at t1
    # the "4p" next to s is the body expressions and type
    s 4p "Haaahhh...haaahhh..."
    s "I overslept again!"
    s "But I caught you this time!"
    # mc is the player themself
    # yes forcing words into your mouth.
    mc "Maybe, but only because I decided to stop and wait for you."

# change sayori positions from "t1" to "s1" on the next dialogue line
    show sayori at s1
    # change sayori body from "4p" to "5c"
    s 5c "Eeehhhhh, you say that like you were thinking about ignoring me!"
    # [] is a definitions showing box, it can be anyhting as long as it's defined
    s "That's mean, [player]!"
    mc "Well, if people stare at you for acting weird then I don't want them to think we're a couple or something."

# change sayori positions to "t1" 
    show sayori at t1
    #
    s 1a "Fine, fine."
    s "But you did wait for me, after all."
    s "I guess you don't have it in you to be mean even if you want to~"
    mc "Whatever you say, Sayori..."
    # this is a clean body type change without any effect
    s 1q "Ehehe~"

# make sayori body hide like it's fading away with "thide"
    show sayori at thide
    # hide the charactor 
    hide sayori
    #
    "We cross the street together and make our way to school."
    "As we draw near, the streets become increasingly speckled with other students making their daily commute."

# 39
    show sayori at t1
    s 3a "By the way, [player]..."
    s "Have you decided on a club to join yet?"
    mc "A club?"
    mc "I told you already, I'm really not interested in joining any clubs."
    mc "I haven't been looking, either."

# 45
    show sayori at s1
    #
    s 4h "Eh? That's not true!"
    s "You told me you would join a club this year!"
    mc "Did I...?"
    "I'm sure it's possible that I did, in one of our many conversations where I dismissively go along with whatever she's going on about."
    "Sayori likes to worry a little too much about me, when I'm perfectly content just getting by on the average while spending my free time on games and anime."
    #
    s 4j "Uh-huh!"
    s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
    s "Your happiness is really important to me, you know!"
    s "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
    #
    s 4g "You trust me, right?"
    s "Don't make me keep worrying about you..."
    mc "Alright, alright..."
    mc "I'll look at a few clubs if it makes you happy."
    mc "No promises, though."
    #
    s 1h "Will you at least promise me you'll try a little?"
    mc "Yeah, I guess I'll promise you that."

# 62
    show sayori at t1
    #
    s 4r "Yaay~!"
    "Why do I let myself get lectured by such a carefree girl?"
    "More than that, I'm surprised I even let myself relent to her."
    "I guess seeing her worry so much about me makes me want to ease her mind at least a little bit - even if she does exaggerate everything inside of her head."

# scene setup (classroom)
    scene bg classroom with wipeleft_scene
    # end of screen setup

# 71
    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    #
    mc "Clubs..."
    "Sayori wants me to check out some clubs."
    "I guess I have no choice but to start with the anime club..."
    # show sayori charactor, just dialogue
    # since it's a new scene
    s "Hellooo?"

# 77
    show sayori 1b at t1
    #
    mc "Sayori...?"
    "Sayori must have come into the classroom while I was spacing out."
    "I look around and realize that I'm the only one left in the classroom."
    #
    s 1a "I thought I'd catch you coming out of the classroom, but I saw you just sitting here and spacing out, so I came in."
    s "Honestly, you're even worse than me sometimes... I'm impressed!"
    mc "You don't need to wait up for me if it's going to make you late to your own club."
    #
    s 1y "Well, I thought you might need some encouragement, so I thought, you know..."
    mc "Know what?"
    #
    s 1a "Well, that you could come to my club!"
    mc "Sayori..."
    #
    s 4r "Yeah??"
    mc "...There is no way I'm going to your club."

# 90
    show sayori at s1
    #
    s 5d "Eeeehhhhh?! Meanie!"
    "Sayori is vice president of the Literature Club."
    "Not that I was ever aware that she had any interest in literature."
    "In fact, I'm 99%% sure she only did it because she thought it would be fun to help start a new club."
    "Since she was the first one to show interest after the one who proposed the club, she inherited the title \"Vice President\"."
    "That said, my interest in literature is guaranteed to be even less."
    mc "Yeah. I'm going to the anime club."

# 98
    show sayori at t1
    #
    s 1g "C'mon, please?"
    mc "Why do you care so much, anyway?"
    #
    s 5b "Well..."
    s "I kind of told the club yesterday I would bring in a new member..."
    s "And Natsuki made cupcakes and everything..."
    s "Ehehe..."
    mc "Don't make promises you can't keep!"
    "I can't tell if Sayori is really that much of an airhead, or if she's so cunning as to have planned all of this out."
    "I let out a long sigh."
    mc "Fine... I'll stop by for a cupcake, okay?"
    


return