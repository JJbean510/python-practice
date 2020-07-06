def lyrics(genre):
    if genre == "rock":
        return "I will follow you into the dark"
    elif genre == "rap":
        return "Gangster, gangster, gangster, G!"
    elif genre == "country":
        return "Rock me baby like wagon wheel"
    else:
        return "Do you not have a favorite genre?"

print(lyrics(""))

def multiplicaton(a,b,c):
    print(a * b * c)
    return "Multiplied"

print(multiplicaton(10, 20, 30))
