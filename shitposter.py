et project starts with... ENTERPRISE QUALITY.
#
# CODE OF CONDUCT THE SJWS HAVE INVADED
#  * be nice
#  * be accepting
#  * be civil
#  * install gentoo
#
#lets make a shitpost generator
#ok
#great idea
#this quality
 
#limiting this shit to prefixes is terrible we need shitposts generated so real that we could make an OP with them
#how could we do that?
#something along the lines of 'only niggers will use "thing" why are you still using "thing" /tech/?'
#we could remake the prefixes to something where you do like: "only [noun] will use [thing] like that
#that could work
#ill make a list of formats
#more grammar
#how i end a function in python?
#you dont, you just let it be
#that upsets me
#yea python is a bit original with its syntax and it can be hard to get used to but its a really nice language
#i just use ruby and c
# its all fuckin in the tabs man let the tabs do all the work
# drop a tab drop a brace ezpz lemonsqueezy
#it lets you do things a lot of different ways
 
import random, re
 
prefixes = [
    'i hate', 'I hate', 'I fucking hate',
    'Hey guys', 'hey guys', 'hey guise',
    'fucking', 'Fucking', 'FUCKING',
    'the best meme is',
    'kill all',
    'the worst meme is',
    'the real botnet is',
    '>yfw',
    '>yrw',
    '>tfw',
    'DAE le',
    '>implying',
    'Hey faggots,',
    'How do you',
    'It\'s like I\'m really',
    'Do you suck',
    'Slide thread',
    'That',
    'now that the dust has settled, how do we feel about',
    'repost if you'
]
 
formats = [
    '[prefix] [adjective] [noun]',
    'fucking [noun] [noun] [noun] [noun]',
    'Nice try, [noun]',
    'Fucking [noun] fags',
]
 
 
# if the prefix is singular then noun should be plural and vice versa
# could use a dictionary with word type and singularity
#we could just make 2 different prefixes tables, one which needs singular ones and one which needs plural, and with formatting we can just add s at the end idk
#that's probably easier
nouns = [
    'niggers','NIGGERS',
    'kikes','KIKES',
    'maymays',
    'penis','PENIS',
    'shitposts',
    'crash this plane',
    'troll','TROLL',
    'big guys',
    'CIA','NSA','FBI',
    '4chan',
    'cucks','CUCKS',
    'benis','BENIS',
    'shills','SHILLS',
    '/tech/',
    'systemd','SYSTEMD',
    'google chrome',
    'ubuntu',
    'Windows 7',
    'Windows XP',
    'Windows 10',
    'BSD',
    '/g/',
    'SJWs',
    'Gentoo',
    'plebbit',
    '9gag',
    'apple',
    'normie','Normies','NORMIES'
    'm80s',
    'anime',
    'os-tan',
    'CISC',
    'TPP',
    'CISA',
    'Shlomo',
    'RISC',
    'Arch',
    'cancer','CANCER','AIDS',
    'the planet',
    'hacker',
    'hack',
    'anonymous'
    'mint',
    '[number] memers',
    'the [number] that died in the holocaust',
    'loli',
    'VN',
    'Lisp',
    'SICP'
]
 
adjectives = [
    'shitposting',
    'fucking',
    'gay',
    'with no survivors',
    'memeing',
    'ebin',
    'detected',
    'memed',
    'epic',
    'feel',
    'trolling',
    'fat',
    '6,000,000',
    'hack'
]
 
wordfilters = {'':''}
 
#function just in case
def shitpost():
    c = random.choice
    format = c(formats)
    split = format.split(" ")
   
    for index, word in enumerate(split):
        if word == "[prefix]":
            split[index] = c(prefixes)
        elif word == "[adjective]":
            split[index] = c(adjectives)
        elif word == "[noun]":
            noun = c(nouns)
            noun = noun.replace("[number]", str(random.randrange(-1000, 1000)))
            split[index] = noun
        elif word == "[capitalize_noun]":
            noun = c(nouns)
            noun = noun.replace("[number]", str(random.randrange(-1000, 1000)))
            noun = noun.title()
            split[index] = noun
   
    format = " ".join(split)
    return format
 
#excuse my shitty code
#im gonna do a raw_input thing
#function this and pass input
def shitpost_by_amount(amount):
    for i in range(amount): # fucking py3 whatever
        print(shitpost())
 
use_input = True
 
if use_input:
    amount = -1
   
    while amount == -1:
        try:
            amount = int(input("Amount of shitposts: "))
        except ValueError:
            amount = -1
   
    shitpost_by_amount(amount)
 
   
# SHIT TALK, DISCUSSION, AND DESIGN:
# ----------------------------------
 
#we should hook this up to twitter
#we could if this supported pip
#fug. Maybe we should write our own version of this designed to run in a disposable VM
#we could just upload this to a repository site
#someone back it up right now
#brand new innovative way to make the average imageboard post
# THE AVERAGE WHAT?!                  ^^^^^^^
# the average quality of life improve for all involved
# you mean i dont have to jump?
 
# TODO:
# post numbers
# quoting
# botnet implementation
 
 
 
#      .'"".      I LIKE PYTHON BECAUSE I ENJOY HOMOSEXUAL
#     c' )"/      S/M. OH GUIDO MAKE ME USE THAT FUCKING
#    __>  /_      INDENTATION. OH BABY I'M CUMMING.
# .-`_    ._'-.
#( -' \  :/  )/   THERE IS ONLY ONE WAY TO DO IT: GUIDO'S
# \\._|  (  //    WAY! THAT MEANS YOU CAN'T USE ALL
#  '-/)   \(,     CONTROL STRUCTURES. IF YOU NEED A DO-
#     /  ) )      WHILE LOOP, A SWITCH OR BREAK OUT OF A
#    / .'\ |      NESTED LOOP, TOO BAD. GUIDO SAYS IT'S TO
#   /.'   \|      KEEP THE LANGUAGE CLEAN, BUT IT'S ACTUALLY
#  ||     ||      TO PUNISN HIS SLAVES. THIS DOESN'T MEAN
#__|/     |/__    THAT PYTHON IS FLAWED, JUST WORK AROUND IT.
#_._)     (,__;                       FUCK I'M CUMMING AGAIN.
 
 
#this code is 72% comment.
 
#kys ascii spamming literal autist
 
#what we could do is make a website where you put in a GET request parameter so the REPL spams it, and the key is private (and also we dont need pip)
 
#wait, i have a better idea.
#why not just make a bot that spams /tech/?
#we could have it spam some small board with no captcha on it besides the DNS bypass and someone run it on their box
# someone can run it from home machine which has captcha solved
##if only hotwheels wasnt a faggot and didnt require a captcha only once a day, physiclly do it everyday
#ah true
 
#dont think it needs JS since tor users can do it
#does the captcha require js?
#i dont think it needs it, but its google recaptcha so
#if not we can just curl the captcha page
 
#wat, since when does 8chan use reca
#isnt it google recaptcha? no its hotwheels own thing <---
#oh then we can just read 8chan's code
#It's still a picture. there's a package for captcha decipher (ocr?)
 
# we only need to solve it once, we can do it ourselves
#how will we solve it from this codepad though
 
#nah red
# nvrmind
#and just like input() what it says or somethin?
#TIME TO WRITE AN ASCII ART RENDERER <---- please dont
#what's good my dudes
 
# can't we just get the public ip of this thing, then someone spoofs the ip and does the captcha?
# ^ Interesting. I don't know shit about that sort of thing. could it work?
 
#that sounds way more complicated
#
 
# wait
#idea
# it curls the page then uploads its captcha image to some site like 0x01.st then we view it and make it send the post with the cpatcha
#yeah but 0x01.st you can just send it to uhhh
#like you can just do it with a post send command iirc
#pomf.cat has an api iirc
 
#make it grab the image then send post to image hoster than we know captcha?????
