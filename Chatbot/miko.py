import datetime
age = int(input("Hey, how old are you? "))
#hometown = input("So where are you from? ")
#favorite_color = input("What's your favorite color? ")

# Add conditionals for hometown/favorite color
# Think of more basic questions Miko can ask
# Make a song title guessing game with lyrics & while loops

if age < 18:
    print("Sorry, but you must be at least 18 years old to talk to me.")
if age == 18:
    print("Aren't you a little young to be in to this kind of thing? Go Tik-Tok or something.")
elif age in range(19, 29):
    print("Hmmm, you're almost at the peak of this rollercoaster you call life. Must suck to have to do life, ha, ha!")
elif age in range(30, 45):
    print("You are in the prime of your life, after this season comes the Fall.")
elif age in range(46, 60):
    print("It is never to late to be who you were supposed to be, someone needs to hear that...")
elif age in range(61, 90):
    print("I'm surprised this is your kind of thing. Well, welcome, I'm Miko.")
elif age in range(91, 110):
    print("Let's talk about the last hundred years, I'm pretty well versered.")

#Notes to update source code
