label night1_start:

    $ meet = _("none")

    scene bg room night
    show Georgie at left
    show Archie at right
    with fade

    g "—and it said that if I don't do this I'm gonna have to stay a magical girl indefinitely!"

    r "Awww. I'm so sorry Georgie... That must be so hard for you"

    r "My sector is great tho, I get a pension plan"

    g "Thank you for your very sympathetic input, Archie"

    r "Ofc"

    g "And because of this, I won't be able to transition!"

    r "And go to college."

    g "...and go to college."

    r "So, who are the lucky kids that get to be mentored by the Top☆Magical☆Girl?" 

    g "You know I hate you, right?"

    r "Love you too, babe."

    r "But seriously, who are the kids?"

    ## *sound of paper being moved*

    g "Let's see..."

    g "Charlie, the athlete"

    r "Aww, an athlete! Always exciting to have those"

    g "What do you mean by that?"

    r "I don't know, they can do parkour and shit maybe"

    g "Okay..."

    g "There's Persephone, the punk"

    r "Such a sweet name, is she really a punk?"

    g "Are you seriously judging people by their names?"

    g "Your name is Archie, but you feel more like a Veronica"

    r "Fair point"

    g "Next is Aspen, the girl scout"

    r "Oh! I was in the girl scout. Must be a diligent and hard working girl"

    g "Are you saying you're all that?"

    r "..."

    r "Next girl"

    g "Wren, the smart one"

    r "..."

    r "The... smart one?"

    g "Okay, she's a nerd."

    r "You're saying it like it's a bad thing!"

    g "Well..."

    r "Rude."

    r "So. Who are you going to check out first for tomorrow morning?"

    g "Hm..."


    menu:

        "Who to check out?"

        "Charlie":
            jump night1_charlie

        "Persephone":
            jump night1_persephone

        "Aspen":
            jump night1_aspen

        "Wren":
            jump night1_wren


label night1_charlie:

    $ meet = _("Charlie")

    r "I'd like to see some parkour, let's go with Charlie!"

    g "You're not even gonna be there"

    r "But you'll take videos for me right? (ㅅ´ ˘ `)"

    g "I think that's illegal, actually"

    r "Since when do you care about that?"

    g "Since this conversation"

    r "Oh come on!"

    r "Fine! You don't have to take videos, just tell me how cool she is later!"

    g "Urgh, the things I do for you"

    jump night1_end


label night1_persephone:

    $ meet = _("Persephone")

    r "I can tell you really want to start with Persephone"

    g "It's not like I want to"

    g "but if I have to, and I DO have to"

    g "she sounds the most interesting"

    r "Of course you'd think that. I still remember your emo phase"

    g "First of all, emo and punk are 2 different things"

    g "And second of all, if you're gonna be like that maybe I shouldn't pick her"

    r "No, come on Georgie, you can reconnect with your angsty 15 year old self!"

    g "Next time we hang out I'm gonna strangle you to death"

    r "Just pick her already!"

    g "Fine."

    jump night1_end


label night1_aspen:

    $ meet = _("Aspen")

    r "I think you should pick Aspen, fellow girl scouts should stick together!"

    g "YOU'RE the girl scout, not me!"

    r "But girl scouts are dependable and action oriented! You like those, right?"

    g "I only like it when YOU do it"

    r "Aww, you love me >:3<"

    g "I am never speaking to you ever again"

    r "Since you love me so much, pick her for me"

    g "I NEVER SAID I LOVE YOU"

    r " You just did!!"

    jump night1_end


label night1_wren:

    $ meet = _("Wren")

    g "I don't really want to go with Wren"

    r "You're so mean! I think you SHOULD pick her first as compensation!"

    g "Why are you defending her? You also don't like nerds"

    r "But I don't say it out loud! You haven't even met her!"

    r "Plus it'll make you nicer or something"

    g "How would that work?"

    r "I don't know, I'm not a psychologist. Power of friendship or whatever."

    g "Sure, at least I'll get her out of the way first"

    jump night1_end


label night1_end:

    "Picked [meet]!"

    g "Wait a minute, why do I feel like you're the one picking for me?"

    r "Because you love me and I'm your bestie"

    g "Oh whatever, I guess that's settled"

    r "Oh by the way, can I come over?"

    g "It's 11 pm!"

    r "Yeah but my boyfriend just broke up with me and I need a friend and some cuddles"

    g "And ice cream"

    r "Yes, you know me so well, bby <3"

    g "Gross."

    g "You're just gonna rob me"

    r "Nooooo. I'll wait for you patiently at home like a good housewife when you go do your Top☆Magical☆Girl work"

    g "Whatever, just come over before it gets too late"

    r "You can just say no"

    g "You're gonna do it anyway no matter what I say, might as well"

    g "Give me your location, I'll pick you up"

    r "This is why we're besties"

    return