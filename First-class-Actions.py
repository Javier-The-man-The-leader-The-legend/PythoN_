def shout(text):
    return text.upper()
def wisper(text):
    return text.lower()
# yell = shout
def person_does(name, func):
    return name + " says " + func("How hAs YoUr beEN?")
message = person_does("Javi", wisper)
print(message)
º