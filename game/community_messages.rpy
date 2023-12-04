screen community_messages:
    tag menu

    add "#000000"
 
    vpgrid:
        cols 3
        spacing 10
        draggable True
        mousewheel True

        scrollbars "vertical"

        xsize 1600
        xalign 1.0
        yalign 0.0

        for msg in contributions:
            vbox:
                spacing 5
                xsize 500
                ysize 400

                text "[msg[name]] \n{size=20}{color=#ffae42}([msg[role]]){/color}\n\n[msg[message]]{/size}":
                    font "gui/fonts/Quicksand-Bold.ttf"
                    size 40
                    color "#ffffff"
                    xsize 480

                if "voice_clip" in msg:
                    textbutton "Listen" xalign 0.5 action [Function(set_play_voice, f"audio/messages/{msg['voice_clip']}"), Play("voice", f"audio/messages/{msg['voice_clip']}", selected=True)]

    textbutton "Return" xalign 0.05 yalign 0.5 action [Stop("voice"), Return()]

init python:
    currently_playing = ""

    def set_play_voice(voice):
        currently_playing = voice

    contributions = [
        {
            "name": "DokokanoFry",
            "role": "Artist/VFX",
            "message": """Hi Petra!!! At last we can celebrate you in this way! Happy Birthday!!!
Every time I hear your good Japanese, I get courage to study English harder! Thank you for the miracle of finding you in this Nijisanji! I love you!""",
        },
        {
            "name": "Retko",
            "role": "Writer",
            "message": "Happy birthday Petra! I can't believe it has been three whole years now. During all this time you've always been a big source of inspiration for me and i genuinely admire you a lot. You have so many skills that you've developed and excel at that i couldn't help but want to do something similar as well. I say this every time i have gotten a chance but, from the bottom of my heart, thank you."
        },
        {
            "name": "Xela",
            "role": "Pentomo",
            "message": "Hi Petra! I've only been watching Niji EN for a relatively short while, but you became one of my favorite livers and I'm glad to have discovered you! Happy Birthday and I hope it's a great one!"
        },
        {
            "name": "N.A.T.E.L.S",
            "role": "Pentomo",
            "message": """HAPPY BIRTHDAY PETRA{font=gui/fonts/NotoEmoji.ttf}🎉🎊{/font}
I hope you enjoyed the demo, as I know everyone who was part of it worked hard to make the you have the best experience! I hope you have a wonderful day, have nice food and lots of love{font=gui/fonts/NotoEmoji.ttf}🧡{/font}"""
        },
        {
            "name": "vel/v3llq1a",
            "role": "Pentomo",
            "message": "HAPPY BIRTHDAY PETRA! Don't stress yourself too much with work, keep drinking water, and have a big slice of cake!! -vel :D"
        },
        {
            "name": "BubbyTheBob",
            "role": "Pentomo",
            "message": "HBD Petra! I hope you enjoy(d) the demo too. It's taken so long and pentomos work so hard. Good news is a ton of the work has been waiting for the demo to finish so the rest can be pushed through. Hope to have the final product to you soon. Enjoy your special day and treat yourself!"
        },
        {
            "name": "Mirko D",
            "role": "Pentomo",
            "message": "Happy Birthday Peto! I wish you all the best on your special day. May you always stay happy, healthy and that you will be sucessful in all your activities. Thank you for being such a loveable person who always helps out others whenever she can! Thank you for being an oshi I always can be proud of and that is an enrichment to mine and the lifes of so many Pentomos. Happy Birthday my cute Penguin Princess! Love you!"
        },
        {
            "name": "Co-op",
            "role": "Pentomo",
            "message": """Petra you were the first vtuber and streamer who got me to sit through an entire stream of theirs and i will never not be more grateful to you for introducing me to this wonderful community. I will forever remember you flipping us off during your 2 year anniversary membership stream and be thankful for it.
Thank you petra for being awesome and being one of my oshis.
I wish you the best for the future and hope you have a very happy birthday."""
        },
        {
            "name": "Syntaxe Errour",
            "role": "Pentomo",
            "message": "Hello and happy birthday to my favorite penguin. Congratulations on reaching the age of 3, which is longer than most penguins, so good job on that. Keep it up, I'd like to have you around a little while longer. Anyway, love you... Platonically and non-parasocially, of course. Cheerio.",
            "voice_clip": "syntax_error.mp3"
        },
        {
            "name": "diwa (jengarie)",
            "role": "Artist/VFX",
            "message": "Happy birthday, Petra! I think you're very cool and I love your singing and design sense a lot. I wish you happiness always and that you may achieve your hopes and dreams. Thank you for streaming and for your hard work. {font=gui/fonts/NotoEmoji.ttf}💖{/font}"
        },
        {
            "name": "SordidCaper",
            "role": "Pentomo",
            "message": "Happy Birthday Petra! Your streams always brighten my day which is why you were the first streamer whose membership I ever joined. I can’t wait to see what comes of this game along with your future streams."
        },
        {
            "name": "{font=/gui/fonts/NotoSansTC.ttf}{b}清玄{/b}{/font}",
            "role": "Musician/SFX",
            "message": "Happy birthday Petra-sama!!! You are doing great and hope you have a nice day!!!"
        },
        {
            "name": "dasBente",
            "role": "Programmer",
            "message": """Happy Birthday Petra!
I hope you're having a great day celebrating and another amazing year ahead of you. After this project came to a halt for a while we've finally managed to gain some fresh momentum and produce this little token of our appreciation. I hope you'll enjoy playing it as much as we did making it!"""
        }
    ]
    
    message_screen_width = 1920
    message_screen_height = 1000