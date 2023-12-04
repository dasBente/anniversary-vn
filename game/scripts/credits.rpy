label credits:
    scene black with fade
    play music "bgm/meet_the_characters.mp3" fadein(5.0)

    show screen credit_screen
    pause 100
    pause
    hide screen credit_screen
    return

init python:
    header_size = 40
    content_size = 20
    padding_size = 5

    sections = [
        {
            "title": "Art & VFX",
            "names": [
                "Jangarie", "DokokanoFry", "Nashinoko", "Shizo", "LEI/Mika",
                "LunaNoctuArts", "Zarasaru", "UnfamousRadish", "Alan/Kollin",
                "Shiki", "cottoncandyFRIZZ", "mari", "LuvTheseStuff", "Azuremia",
                "l_yth", "Amechi", "Gitsoone", "Capricious"
            ],
            "size": header_size + 18 * content_size + 18 * padding_size
        },
        {
            "title": "Music & SFX",
            "names": [
                "ozene", "Heko", "sorarara", "Capricious"
            ],
            "size": header_size + 4 * content_size + 4 * padding_size
        },
        {
            "title": "Programming",
            "names": [
                "dasBente", "killbasa", "eientei", "Capricious"
            ],
            "size": header_size + 4 * content_size + 4 * padding_size
        },
        {
            "title": "Writing",
            "names": [
                "Lily", "Retko", "TRIberium", "Capricious"
            ],
            "size": header_size + 4 * content_size + 4 * padding_size
        },
        {
            "title": "Project Management",
            "names": [
                "Lily", "dasBente", "Kollin/Alan", "BubbyTheBob",
                "Thou Holy Wooomy", "Capricious"
            ],
            "size": header_size + 6 * content_size + 6 * padding_size
        },
        {
            "title": "Assets",
            "names": [
                "Made in Ren'Py", "Quicksand Font by Andrew Paglinawan"
            ],
            "size": header_size + 3 * content_size + 3 * padding_size
        },
        {
            "title": "Special Thanks",
            "names": [
                "Petra Gurin", "OBSYDIA", "Eth– uhh", "Peter (from Ninisani)",
                "You (Pentomo)"
            ],
            "size": header_size + 5 * content_size + 5 * padding_size
        }
    ]

screen credit_screen:
    vbox:
        xsize 1000
        ysize 5500

        xalign 0.5
        yalign 0.0

        at transform:
            subpixel True
            easein 100:
                yalign 1.0
        
        vbox:
            ysize 1080 # start with empty screen
        
        vbox:
            ysize 150

            text "A Penguin's Theory of Happiness":
                font "gui/fonts/Quicksand-Bold.ttf"
                color "#ffae42"
                size 100
                xalign 0.5
            
            text "A fan-game made by Petracord":
                font "gui/fonts/Quicksand-Bold.ttf"
                color "#ffae42"
                size 20
                xalign 0.5

        for section in sections:
            vbox:
                ysize section["size"]
                xalign 0.5

                text section["title"]:
                    font "gui/fonts/Quicksand-Bold.ttf"
                    color "#ffffff"
                    size 40
                    xalign 0.5

                for name in section["names"]:
                    text name:
                        font "gui/fonts/Quicksand-Bold.ttf"
                        color "#ffffff"
                        size 20
                        xalign 0.5
        
        vbox:
            ysize 150
            xalign 0.5

            text "Thank you for playing!":
                font "gui/fonts/Quicksand-Bold.ttf"
                color "#ffffff"
                size 80
                xalign 0.5

            text "If you have time, check out the Community Messages section in the main menu!\n\n{size=20}{color=#888888}(Click to return to the main menu){/color}{/size}":
                font "gui/fonts/Quicksand-Bold.ttf"
                color "#ffffff"
                size 40
                xalign 0.5


# https://3dns-2.reddit.com/r/RenPy/comments/16i3kid/rolling_credits_in_renpy_heres_how_you_do_it/