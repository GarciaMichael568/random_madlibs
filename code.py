#method for madlib
def madlib():
    verb = input("Verb: ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    noun1 = input("Noun (plural): ")
    noun2 = input ("Noun (plural): ")

    madlib = f"{noun1} is a {adj1} monkey. He lives in a {adj2} forest. He likes {verb} and climbing trees. He is {adj3} every day. But he has a shortcoming. He is curious.\
One day an old man named {noun2} goes by the forest. He carries a lot of straw hats. {noun1} sees the man, and the man sees {noun1}, too. The man says to himself, 'What a {adj4} monkey! I will catch him. I will take him home.'\
The man sits down and thinks over. {noun1} sees and also sits down. The man has an idea. He puts a hat on his head, and puts other hats on the ground. Then he pretends to sleep.\
{noun1} is curious and looks at the hats. 'I will be nice if I put a hat on my head.' {noun1} thinks. Then he climbs down from the tree, picks up a hat and puts it on. The hat is too big, and covers {noun1}'s eyes.\
{noun1} can't see. And the man gets up at once, rushes out and catches him quickly.\
Poor {noun1}!"

    print(madlib)