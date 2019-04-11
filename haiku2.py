#!/bin/python3

import random

def remHeShe(sentence):
    # Converts he, she and I into him, her and me where appropriate
    words = sentence.split()
    for i in range(2, len(words)):
        #print(words[i])
        if words[i] == "he":
            words[i] = "him"
        elif words[i] == "she":
            words[i] = "her"
        elif words[i] == "I" and words[i-1] != "and":
            #print("FOUND I")
            words[i] = "me"
    #print(words)
    finalSentence = " ".join(words)
    #print(finalSentence)
    return finalSentence

def addArticle(items):
    # Adds the correct article to nouns
    vowels = ["a", "e", "i", "o", "u"]
    finalItems = ["an " + item for item in items if item[0] in vowels] + ["a "  + item for item in items if item[0] not in vowels] + ["the " + item for item in items]
    return finalItems

def combine(list1, list2):
    # Combines nouns for multiple people as the subject
    comList = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] != list2[j]:
                comList.append([list1[i], "and", list2[j]])
                if list1 != list2:
                    comList.append([list2[j], "and", list1[i]])
    for i in range(len(comList)):
        if comList[i][-1] == "he":
            comList[i] = comList[i][0:-1] + ["him"]
        elif comList[i][-1] == "she":
            comList[i] = comList[i][0:-1] + ["her"]
        comList[i] = " ".join(comList[i])
    return comList

def senFormat(sentence):
    # Gives the sentence a capital letter and full stop
    words = sentence.split()
    words[0] = words[0].capitalize()
    finalSentence = " ".join(words) + "."
    return finalSentence

def cap(sentence):
    # Will just capitalise a sentence
    words = sentence.split()
    words[0] = words[0].capitalize()
    finalSentence = " ".join(words)
    return finalSentence

def plural(word):
    # Will convert a word into its plural form e.g. "puppy" to "puppies"
    if word[-1] == "y":
        return word[0:-1] + "ies"
    elif word[-1] == "h":
        return word[0:-1] + "hes"
    else:
        return word + "s"

def pluralise(verb):
    # Turns a verb "plural" for 
    sep = verb.split()
    if len(sep) == 0:
        return plural(verb)
    else:
        sep[0] = plural(sep[0])
        final_verb = " ".join(sep)
        return final_verb

def actionise(items):
    # Turns standalone verbs into something which can be used on an object
    finalItems = []
    for word in (" on", " with"):
        finalItems += [item + word for item in items]
    return finalItems

def applyAdj(nouns, adjs):
    # Adds adjectives to nouns
    #print(nouns)
    #print(adjs)
    combined = []
    for noun in nouns:
        for adj in adjs:
            if len(noun.split()) == 1:
                combined.append(adj + " " + noun)
    #print(combined)
    return combined

def applyAdv(verbs, advs):
    # Adds an adverb to a verb
    combined = []
    for verb in verbs:
        for adv in advs:
            combined.append(verb + " " + adv)
    return combined

def adjust3(syls):
    # Adjusts for randomly assigned syllables that the dictionaries can't accommodate
    #print("syllables", syls)
    newSyls = []
    if syls[0] >= 6:
        #print(1)
        newSyls.append(syls[1])
        newSyls.append(syls[0])
        newSyls.append(syls[2])
    elif syls[2] >= 6:
        #print(2)
        newSyls.append(syls[0])
        newSyls.append(syls[2])
        newSyls.append(syls[1])

    if len(newSyls) == 0:
        return syls
    else:
        return newSyls

def adjust2(syls):
    # As above
    newSyls = []
    if syls[1] >= 5:
        newSyls.append(syls[0] + 1)
        newSyls.append(syls[1] - 1)
    if len(newSyls) == 0:
        return syls
    else:
        return newSyls
    

nouns = {"pAni":{1:["cat", "dog", "mouse", "ape", "duck"], 2:["donkey", "giraffe", "lion", "monkey"]},
         "pPerson":{1:["nurse", "tech", "man", "kid", "lord"], 2:["builder", "pirate", "doctor", "lady"]},
         "npVague":{1:["I", "you"]},
         "pVague":{1:["he", "she"]},
         "pName":{1:["Bob", "Sue"], 2:["Sarah", "Peter"]},
         "pObj":{1:["chair", "mat", "lamp"], 2:["table", "cupboard", "beer can"]},
         "pLand":{1:["sky", "sea", "beach", "field"], 2:["sunset", "landscape"]}}

#print("Noun", nouns["pAni"][1])

adjs = {1:["bad", "good"],
        2:["pretty", "happy", "tasty"],
        3:["beautiful", "disgusting"]}

advs = {2:["coyly", "quickly", "slowly", "happily"],
        3:["intensely", "viciously", "angrily"]}

verbs = {1:["eat", "sleep", "fly", "cry", "die", "run", "talk"],
         2:["travel", "study"],
         3:["celebrate", "concentrate", "meditate", "suffocate"],
         4:["misunderstand", "investigate", "collaborate"],
         5:[]}

aVerbs = {1:["eat", "kill", "pet", "cut", "watch"],
          2:["murder", "select", "carry", "disect"],
          3:[],
          4:[],
          5:[]}

for i in range(1, 5):
    # Add to the action verbs using the other list of verbs
    aVerbs[i+1] += actionise(verbs[1])

for item in ("pAni", "pObj", "pLand", "pPerson"):
    nouns[item][2] += applyAdj(nouns[item][1], adjs[1])
    nouns[item][3] = (applyAdj(nouns[item][2], adjs[1]) + applyAdj(nouns[item][1], adjs[2]))
    nouns[item][4] = (applyAdj(nouns[item][2], adjs[2]) + applyAdj(nouns[item][1], adjs[3]))

verbs[3] += applyAdv(verbs[1], advs[2])
verbs[4] += applyAdv(verbs[1], advs[3])
verbs[4] += applyAdv(verbs[2], advs[2])
verbs[5] += applyAdv(verbs[2], advs[3])

subs = {}

subs[1] = [nouns["npVague"][1], nouns["pVague"][1] + nouns["pName"][1]]
subs[2] = [[], nouns["pName"][1]]
subs[3] = [[], applyAdj(nouns["pName"][1], adjs[2])]
subs[4] = [[], applyAdj(nouns["pName"][1], adjs[3]) + applyAdj(nouns["pName"][2], adjs[2])]
subs[5] = [[], applyAdj(nouns["pName"][2], adjs[3])]

for item in ("pAni", "pPerson"):
    for i in range(1, 5):
        #print("i", i)
        #print(subs[i+1][1])
        #print(nouns["pAni"][i])
        subs[i+1][1] += addArticle(nouns[item][i])

subs[3][0] += combine(subs[1][0] + subs[1][1], subs[1][0] + subs[1][1])
subs[4][0] += combine(subs[1][0], subs[2][1])
subs[5][0] += combine(subs[1][0] + subs[1][1], subs[3][1])
subs[5][0] += combine(subs[2][1], subs[2][1])

objs = {}

objs[1] = [nouns["npVague"][1], nouns["pVague"][1] + nouns["pName"][1]]
objs[2] = [[], nouns["pName"][1]]
objs[3] = [[], applyAdj(nouns["pName"][1], adjs[2])]
objs[4] = [[], applyAdj(nouns["pName"][1], adjs[3]) + applyAdj(nouns["pName"][2], adjs[2])]
objs[5] = [[], applyAdj(nouns["pName"][2], adjs[3])]

for item in ("pAni", "pObj", "pLand", "pPerson"):
    for i in range(1, 5):
        objs[i+1][1] += addArticle(nouns[item][i])

objs[3][0] += combine(subs[1][0] + subs[1][1], subs[1][0] + subs[1][1])
objs[4][0] += combine(subs[1][0], subs[2][1])
objs[5][0] += combine(subs[1][0] + subs[1][1], subs[3][1])
objs[5][0] += combine(subs[2][1], subs[2][1])
  
def getSub(syl):
    # This generates a random subject for a particular number of syllabes
    theBools = [False, True]
    subNum = random.randint(0, 1)
    theBool = theBools[subNum]
    if len(subs[syl][subNum]) == 0:
        sub = random.choice(subs[syl][(subNum+1)%2])
        theBool = not theBool
    else:
      sub = random.choice(subs[syl][subNum])

    return sub, theBool

def getObj(syl):
    # Same as above for an object
    obj = random.choice(objs[syl][0] + objs[syl][1])
    return obj
  
def getVerb(syl, plur):
    # Same as above for a verb
    verb = random.choice(verbs[syl])
    if plur:
        verb = pluralise(verb)
    return verb

def getActionVerb(syl, plur):
    # Same as above for an action verb (can be performed on an object)
    verb = random.choice(aVerbs[syl])
    if plur:
        verb = pluralise(verb)
    return verb

def makeLine(groupNo, valuesNo):
    # Randomly generates a line of syllables
    groupList = []

    for i in range(0, groupNo-1):
        item = random.randint(1, (valuesNo-(groupNo-i)))
        groupList.append(item)
        valuesNo -= item

    groupList.append(valuesNo)
    random.shuffle(groupList)
    
    return groupList
  
def writeLine(group):
    # Creates the line from subjects, verbs and objects
    #print(group)
    if len(group) == 2:
        group = adjust2(group)
        sub, plur = getSub(group[0])
        verb = getVerb(group[1], plur)
        if sum(group) == 6:
            start = "while"
        else:
            start = ""
        sentence = " ".join([start, sub, verb])
    elif len(group) == 3:
        #print(group)
        group = adjust3(group)
        #print("adjusted", group)
        sub, plur = getSub(group[0])
        verb = getActionVerb(group[1], plur)
        obj = getObj(group[2])
        if sum(group) == 6:
            start = "while"
        else:
            start = ""
        sentence = " ".join([start, sub, verb, obj])
    return sentence
  
def allWriteLine(words, syllables, sen):
    # Writes the total line, formatting words as appropriate
    group = makeLine(words, syllables)
    sentence = writeLine(group)
    sentence = remHeShe(sentence)
    if sen == True:
        sentence = senFormat(sentence)
    elif sentence[0:5] == "while":
        sentence += "."
    else:
        sentence = cap(sentence)
    return sentence

if __name__ == "__main__":
    for i in range(10):
        print(allWriteLine(2, 5, False))
        print(allWriteLine(3, 6, False))
        print(allWriteLine(2, 5, True))
        print("")
  
"""print(makeLine(random.randint(2, 3), 5))
print(makeLine(random.randint(3, 5), 7))
print(makeLine(random.randint(2, 3), 5))"""

