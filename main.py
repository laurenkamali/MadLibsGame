'''
Name: Lauren Kamali
Date: 10/04/2024
Description: This is an interactieve Mad Libs game where users put in inputs that are later added into a story.
'''

print("Welcome to this Mads Libs Game!".center(60,"-"))

#user name + date
username = input("What is your name? ")
print(username.title())
date = input("What is today's date? (eg: xx/xx/xx) ")



#user input for mad lib
verb1 = str(input("Choose a verb: "))
noun4 = str(input("Choose a noun: "))
verb2 = str(input("Choose a verb that ends in 'ed': "))
occupation2 = str(input("Choose an occupation: "))
noun5 = str(input("Choose a noun: "))
verb3 = str(input("Choose a third verb: "))
adjective1 = str(input("Choose an adjective: ")) 
adjective2 = str(input("Choose a another adjective : "))
name1 = str(input("Choose a name: "))
noun = str(input("Choose a noun: "))
noun2 = str(input("Choose another noun: "))
adjective3 = str(input("Choose an adjective: ")) 
adverb2 = str(input("Choose an adverb: "))
noun3 = str(input("Choose a noun: "))
adjective4 = str(input("Choose an adjective: ")) 
animal = str(input("Choose an animal: "))
verb4 = str(input("Choose a verb: "))
noun6 = str(input("Choose a noun: "))
adjective5 = str(input("Choose an adjective: ")) 
place = str(input("Choose a place: "))
adverb1 = str(input("Choose an adverb: "))
verb5 = str(input("Choose a verb: "))
occupation = str(input("Choose another occupation: "))
noun7 = str(input("Choose a noun: "))
sillyword = str(input("Choose a silly word: "))

#output of story
print(f"""One day, {name1} decided to go on an adventure to the {adjective1} land of {noun}.
      They packed their favorite {noun2} and set off. Along the way, they encountered a {adjective2} {animal} who offered them a {noun3}.
      Excited, they {adverb1} accepted and continued their journey until they reached a {adjective3} {place}.
      There, they met a {adjective4} {occupation} who was in desperate need of a {noun4}.
      Without hesitation, {name1} handed over their trusty {noun5}.
      In return, the {occupation2} gave them a magical {noun6} that could {verb1} whenever {name1} said the word {sillyword}.
      Thrilled with their new gift, they {adverb2} {verb5} and {verb4} all the way back home, where they shared the story of their {adjective5} adventure with everyone.
      And from that day on, they always remembered to carry a {noun7} in case they needed to {verb3}.""")