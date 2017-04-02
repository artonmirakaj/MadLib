import random

def yourname():
    nameList = ['Arton', 'Carlo', 'Mike', 'Kenny', 'Eddie', 'Kyle', 'Ron', 'Kris', 'Lou']
    return nameList[random.randint(0, len(nameList)-1)]



def adjective():
    adjList = ['ashamed', 'alcoholic', 'bat-shit-crazy', 'mentally impaired',
               'zombie like', 'slap happy', 'duck-like', 'insanely creepy', 'fat',
               'homeless', 'mammoth', 'repulsive', 'fluffy','scrawny', 'squealing',
               'yummy', 'ugliest', 'naked', 'bonkers', ]

    return adjList[random.randint(0, len(adjList)-1)]



def number():
    return random.randint(0, 100)



def verb():
    verbList = ['stab', 'bazinga', 'bumfuzzle', 'doohickey', 'manscape', 'wombat',
                'pantaloons', 'hornswoggle', 'snoop', 'splatter', 'medicate', 'flap']
    return verbList[random.randint(0, len(verbList) - 1)]



def place():
    placeList = ['The Giant\'s Causeway', 'Thor\'s well', 'The Lost City of Atlantis', 'Lake Hillier',
                 'The Bermuda Triangle', 'Chocolate Hills of Bohol Island', 'Whale Bone Valley',
                 'The Catacombs', 'The Door to Hell', 'Island of the Dolls', 'Area 51']
    return placeList[random.randint(0, len(placeList) - 1)]



def plural_noun():
    pluralList = ['babies', 'dwarves', 'elves', 'hippopotami', 'hooves', 'cacti',
                  'octopuses', 'Cul-de-Sacs', 'low lifes', 'potatoes', 'geese']
    return pluralList[random.randint(0, len(pluralList) - 1)]



def noun():
    nounList = ['idiot', 'sandwich', 'friendly grandma', 'anit-depressant drug',
                'corn cake', 'candelstick maker', 'mad cow disease', 'hairy legs',
                'dingle berry', 'smooth criminal', 'dog poop', 'striped hyena']
    return nounList[random.randint(0, len(nounList) - 1)]




print "My name is %s and Ive known the %s couple for %d years, " % (yourname(), adjective(), number())
print "I %s all the way from %s to celebrate this day." % (verb(), place())
print "I am so %s that Mary & John have tied the Knot!" % (adjective())
print "They are the most %s %s that I know, and I wish them %s %s for many years to come!" % (adjective(), plural_noun(), adjective(), noun())
print "My best advice? Dont forget to %s before you %s and %s after the %s." % (verb(), verb(), verb(), noun())
print "Mary, you should always %s Johns %s, and John, you should always %s Marys %s." % (verb(), noun(), verb(), noun())
print "One last thing, always remember to %s your %s before bedtime. I wish you a lifetime of health, happiness and %s!" % (verb(), noun(), noun())

