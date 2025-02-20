# Day 1, Part 1

label intro_day_1:
    # [open the VN on flashback of Rosemi asking Petra if she wants to live among humans in human society; clip from OG lore video of the debut stream] 
    scene bg bedroom
    show petra default at left

    petra "(Now that I think about it... Did I even have a choice then?)" 
    petra "(What would they have done, if I had said no....?)" 
    petra "(... do I even know how to say no…?)" 
    petra "(I don't think I've said no to anything they've asked so far...)"
    petra "(I guess everything they've suggested has been for my own good... I think... so I really didn't need to…?)" 
    petra "(As long as they don't hurt me if I cooperate…)"
    petra "(They wouldn't do that.)"
    petra "(They… They've been nice after all.)"
 
    # flip Petra's sprite horizontally back and forth to indicate her looking around her room

    petra "(Well… Either way, I shouldn't stay in bed all day.)"

    window hide
    play sound "sfx/sheets_rustling.mp3"
    
    show petra default at flip, left
    pause 1
    show petra default at flip, left
    show petra default:
        xoffset 0
        linear 1.0 xoffset 400

    pause 2

    show petra default at flip, left
    pause 1

    play sound "sfx/door_open.wav"
    show petra with dissolve
    pause 1

    show bg bedroom with fade

    show petra default at left
    play sound "sfx/door_knock.wav"
    pause 2

    petra "Huh?!"
    petra "(Oh, it must be–)"

    play sound "sfx/door_open.wav"
    pause 2

    stop music
    play music "bgm/meet_the_characters.mp3" fadein 1.0 volume 0.75 # TODO: this isn't playing for me for some reason when I run it
    show petra at left
    show nina excited at right
    
    # Nina greeting sfx

    nina "Good morning, Honey!"

    show petra default

    # Petra Greeting (shy) sfx
    petra "G-Good morning, Nina…"
    petra "(What's the point of knocking if you're just going to let yourself in…?)"
    petra "(And here I thought being given my own room was a sign of respect towards my privacy…)"

    show nina happy

    nina "Are you ready? Wanna grab breakfast together?" #fixed typo
    petra "..." 
    nina  "..."
    nina "It's okay, there's no rush~"
    petra "(I still don't know how to say no…)"
    petra "O-Okay…"

    show nina excited

    nina "Great!" 

    show nina happy

    nina "Oh, guess what, Honey, I heard the cafeteria is serving toast and omurice for breakfast today."
    nina "Mmm… Nothing beats good old toast with eggs, right?" 

    petra "..."
    petra "Y-Yeah…"
    petra "(...how is she so energetic this early in the morning?)" 

    scene bg hallway with fade

    show petra default at left
    show nina happy at right

    petra "(... it's so bright…)" 
    petra "(Is this really the same sun I used to see back in antarctica? Somehow, it feels different…)" 
    petra "..." 
    petra "(Everything here feels different…)"
    petra "(It feels... warm.)"

    show nina default

    nina "..." 

    show nina happy

    nina " I see you've been staring outside for a while, would you like to take a stroll today, Honey?" 
    petra "..."
    nina "Well, we've already told you this but you're free to roam the facility, any time you want."
    nina "This place is safe, no need to worry."

    show petra softsadsmile

    petra " ... thanks... I'll think about it."
    nina "Of course, take your time, dear."
    petra "..." 
    petra "(Nina is warm too)"

    scene bg hallway with fade
    play sound "ambient/clock_ticking.wav" volume 0.5 # TODO: this sound effect is getting cut short too after playing for a breif moment

    # flip sprites to face left
    show petra default at center, flip
    show nina default at right

    mystery "Hey!" 
    mystery "Nina! Petra!" 

    # Scene: Selen Intro CG START
    # Selen greeting sfx
    scene cg selen_intro with fade
    hide nina
    hide petra #hiding sprites for the sake of the CG

    selen "Good morning!" 
    nina "Good morning, Selen!" 
    petra "... good morning." 

    play sound "sfx/ember_bark.wav"
    ember "Gawr!!"
    
    nina "Haha, good morning to you too, Ember!"
    
    # Scene: Selen Intro CG END. Return to Hallways (day) BG
    # Moved the end of the CG to after the dialogue and right before Selen sprite pops on screen
    scene bg hallway with fade
    show petra default at slightright, flip
    show nina default at outer_right 

    # add some proper offset
    show selen happy at slightleft, flip

    selen "Have you two had breakfast yet?" 
    nina "Not yet, we're going to the cafeteria now!" 
    selen "Phew, I'm not late then! Let's go!"

    scene bg cafeteria with fade

    show petra default at center
    show nina happy at right
    show selen default at left, flip 

    nina "Alright Honey, anything else you'd like?"
    petra "Hmm..." 
    petra "(Except for some of the strange ones, everything else looks good..)" 
    petra "Can…"
    petra "Can I have the– Fweh?"

    play sound "sfx/ember_chomp.wav" volume 0.75
    ember "*chomp chomp*"

    show petra shocked
    
    petra "FWEEEHH??!!!"

    show selen excited
    show nina laugh

    # Nina laugh sfx
    selen "Haha! Looks like Ember's already decided what he wants for breakfast!"

    petra "Ember... P-Please! This is my emergency food!"

    show nina happy
    show selen happy

    nina "That's right, Ember please pick a food from the table not from Petra's hair."

    play sound "sfx/ember_whimper.wav" volume 0.5
    ember "Oouuff" 

    show petra shocked

    petra "Ah, my hair clip!"

    show petra default

    petra "..."

    show petra softsadsmile

    petra "... I-it's fine…"
    petra "(Haaa… Even Ember's walking all over me… Did they pick me up as a rescue or as a doormat…?)"
    petra "(I guess I shouldn't get upset at it for not knowing better…)"

    # Petra Sigh sfx

    mystery "Hey guys! Over here!"
    mystery "I saved a few seats!"

    show selen default at center, flip
    show nina default at outer_right

    # this works but "slightright, flip" makes petra huge so at this point i'll leave this untouched
    show petra at slightright
    show petra at flip

    nina "Aww Honey! Thank you!" 
    selen "Thanks, Rosemi." 
    petra "T-Thank you…"

    # Rosemi greeting sfx

    # move in from left
    show rosemi happy:
        zoom 1.5
        yoffset -150
        anchor (0.0, 0.65)
        ypos 1.0
        xpos -0.1
        easein 0.5 xpos 0.1

    rosemi "Don't mention it"

    show nina happy
    show rosemi default 
    nina "Ooh, is that omurice? It looks so cute!"

    scene cg rosemi_intro with fade

    # Scene: Rosemi Intro CG START
    rosemi "Close, it's Pomurice! It's like omurice…"
    rosemi "But better!"

    # Rosemi laugh sfx
    rosemi "The omelet is fluffy and cooked just right!" 
    rosemi "The rice tastes great and the garnish is so pretty~"
    rosemi "I heard the theme for the dish was ''Forest Fairies''! Isn't that cute?"

    # Scene: Rosemi Intro CG END 
    scene bg cafeteria with fade #transition back out of Rosemi CG

    show rosemi default at spread(4, 1), rosemi_bump
    show selen default at spread(4, 2)
    show nina excited at spread(4, 3)
    show petra default at spread(4, 4)

    nina "That sounds amazing!"
    
    show nina happy
    nina "I'll have to try some Pomurice too!" 

    show rosemi happy
    rosemi "Yes, please do! I'm sure you'll like it!"

    show nina proud
    nina "As expected of my son~ He really did become a pro chef!"
    nina "I'm so proud of him!"

    show selen excited
    # selenLaugh sfx
    selen "Haha, yeah, he wasn't joking!"

    show selen happy
    selen "Ever since he joined, the menus have become so fancy!"

    show rosemi default
    rosemi "And there's more types of dishes to pick from too!"

    show petra deadpan
    petra "(Well having variety is nice but... Peter has some... weird food tastes…)" 
    petra "(... he keeps saying that cooking school taught him those recipes, but I wonder how much of it he actually follows…)"
    petra "(At least it's easy to tell the good ones apart from the weird ones…)"

    show nina happy
    nina "I'm so glad he came back as a cook. It's so nice to see my baby again!"

    rosemi "It is nice to see him again."
    rosemi "But I'm still not used to seeing him in the kitchen staff uniform." 
    rosemi "It was quite the surprise the first time I saw him like that!" 

    show selen excited
    selen "Haha, same here!" 
    selen "It was a surprise for sure!" 

    show selen happy
    # Turn Selen's sprite to face Petra
    selen "And speaking of surprises..." 
    selen "Don't we have our own little surprise prepared?" 

    # Turn everyone else's sprite to face Petra too

    show nina smug
    nina "Ooh right, we do have one~" 

    show rosemi excited
    rosemi "Yep, I think it's time!" 

    show petra shocked
    petra "Fweh?"

    selen "Petra…"
    selen "You've probably already noticed, but it's been a month since you've joined the Rehab center…"
    selen "And to commemorate that…"
    selen "We've prepared a special present for you!"

    petra "(A present…?)"

    show nina happy
    nina "Well, it's more like Rosemi made the present, and we just helped."

    show rosemi worried
    rosemi "Nooo! Don't say that! We worked on this together!" 

    show petra default
    petra "You guys made a present..."

    show petra shocked
    petra "... for me?!" 

    show rosemi excited
    rosemi "Yes, of course!"
    rosemi "We wanted to celebrate you being here with us!"

    show nina excited
    nina "Of course Honey! You've been such a dear and an absolute joy to work with!" 

    show nina happy
    nina "You deserve a present." 

    selen "We're glad to have you here, Petra. Is that so surprising?" 

    show petra default
    petra "(Th-They got me a present…?)"
    petra "I-I- ..."
    petra "(What could they have gotten me?)"
    petra "(What kind of present do you even get for… a one-month anniversary… at a rehab center…?)"
    petra "(I don't know what to say…)"

    menu present_choices:
        # This option does not increase or decrease Petra's affection with any character! The dialogues triggered by this option are in [Day 1, part 1.a]. 
        "Th-Thank you…":
            jump intro_day_1_good
        
        # This option does not increase or decrease Petra's affection with any character either, but it does change what dialogue appears in future scenes! The dialogues triggered by this option are in [Day 1, part 1.b].
        "I-I'm not a little kid, you know!":
            $ prologue_rejection_flag = True
            jump intro_day_1_bad
