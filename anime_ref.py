from random import choice, randint

def jojo_ref():
    # Have it print the dict name, and the tenor link :)
    
    #When the bot returns a random moment, have the title, and image be censored for spoilers

    refrences = {"Leddle Leddle" : "https://tenor.com/view/kakyoin-cherry-lick-gif-14970220",
                 "Ok Master Let's kill da ho! Beechhh" : "https://tenor.com/view/jojo-koichi-ok-master-lets-kill-da-hoe-koichi-act3-jojo-renatojxd-gif-16057969",
                 "MUDA MUDA MUDA MUDA!":"https://tenor.com/view/dio-jojo-muda-dio-br-gif-26351721",
                 "WRRRYYYY" : "https://tenor.com/view/wryyyy-dio-brando-gif-21122961",
                 "ORA ORA ORA ORA" : "https://tenor.com/view/ora-star-platinum-jo-jos-bizarre-adventure-jojo-gif-5505650",
                 "NIGERUNDAYO!!!!" : "https://media1.tenor.com/m/Ll--oAklMr0AAAAd/nigerundayo-joestar.gif",
                 "CAESARRRR" : "https://tenor.com/view/caesar-anthonio-zeppeli-jo-jos-bizarre-mad-angry-pissed-gif-15097694",
                 "Giorno Piss" : "https://tenor.com/view/jojo-sip-drink-giorno-giovanna-bruno-bucciarati-gif-16024006",
                 "Part 5 Gang Jump" : "https://tenor.com/view/jojo-kick-jjba-gif-13894493",
                 '"Hayato"':"https://tenor.com/view/jojo-anime-jojos-bizarre-adventure-show-cartoon-gif-14672131",
                 "????" : "https://tenor.com/view/jojo-meme-gif-25722148",
                 "Dio Walk 1" : "https://tenor.com/view/dio-brando-walking-fabulous-epic-gif-14680976",
                 "ZA WARDUOOOO" : "https://tenor.com/view/za-warudo-zawarudo-the-world-gif-10578246",
                 "Josuke Gun" : "https://tenor.com/view/jojo-gun-jojos-josuke-meme-gif-18019715",
                 "Doppio Phone" : "https://tenor.com/view/jojo-froggy-phone-frog-phone-frog-froggy-gif-19529980",
                 "MUDA MUDA MUDA MUDA MUDA MUDA" : "https://tenor.com/view/muda-muda-giorno-giovanna-jo-jo-gold-experience-muda-gif-14208660",
                 "Kars Pose" : "https://tenor.com/view/bright-light-flowing-hair-jojos-bizarre-adventure-anime-gif-17398510",
                 "Jotaro Trauma" : "https://tenor.com/view/jojo-jotaro-scream-panic-knives-gif-27298743",
                 "Polpo Death" : "https://tenor.com/view/polpo-jojo-banana-jjba-gun-gif-13644198",
                 "Zeppeli Frog" : "https://tenor.com/view/jo-jos-bizarre-adventure-frog-fist-gif-11650164",
                 "How many breads have you eaten in your life?" : "https://tenor.com/view/jojosbizarreadventure-jojo-diobrando-dio-phantomblood-gif-18657170",
                 "Torture Dance" : "https://tenor.com/view/torture-dance-gif-14760311",
                 "Giorno Tweak" : "https://tenor.com/view/giorno-giorno-giovanna-giorno-jojo-giorno-in-pain-giorno-rolling-around-gif-25364667",
                 "Giorno and Mista..." : "https://tenor.com/view/narancia-surprised-shock-shocked-anime-gif-16863620",
                 "Bucciarati Lick" : "https://tenor.com/view/bruno-bucciarati-giorno-giovanna-lick-jojos-bizarre-adventure-anime-gif-17755384"
                 }
    
    x = randint(0, len(refrences) - 1)

    first_key = list(refrences.keys())[x]
    first_value = list(refrences.values())[x]
    
    return f'Censored for spoiler purposes! \n || {first_key} || \n || {first_value} ||'
    
def onepiece_ref():
    pass