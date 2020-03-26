
def chord(root):
    if root == ("A") or root == ("a"):
        print("\nA major = \n\tA - C# - E\n")
    elif root == ("B") or root == ("b"):
        print("\nB major = \n\tB - E♭ - F#\n")
    elif root == ("C") or root == ("c"):
        print("\nC major = \n\tC - E - G\n")
    elif root == ("D") or root == ("d"):
        print("\nD major = \n\tD - F# - A\n")
    elif root == ("E") or root == ("e"):
        print("\nE major = \n\tE - G# - B\n")
    elif root == ("F") or root == ("f"):
        print("\nF major = \n\tF - A - C\n")
    elif root == ("G") or root == ("g"):
        print("\nG major = \n\tG - B - D\n")



    elif root == ("A#") or root == ("a#") or root == ("Bb") \
            or root == ("bb") or root == ("B♭") or root == ("b♭"):
        print("\nA#/B♭ major = \n\tA#/B♭ - D - F\n")

    elif root == ("B#") or root == ("b#"):
        print("\nB#/C major = \n\tC - E - G\n")

    elif root == ("C#") or root == ("c#") or root == ("Db") \
            or root == ("db") or root == ("D♭") or root == ("d♭"):
        print("\nC#/D♭ major = \n\tC#/D♭ - E# - G#\n")

    elif root == ("D#") or root == ("d#") or root == ("Eb") \
            or root == ("eb") or root == ("E♭") or root == ("e♭"):
        print("\nD#/E♭ major = \n\tD#/E♭ - G - B♭\n")

    elif root == ("E#") or root == ("e#"):
        print("\nE#/F major = \n\tF - A - C\n")

    elif root == ("F#") or root == ("f#") or root == ("Gb") \
            or root == ("gb") or root == ("G♭") or root == ("g♭"):
        print("\nF#/G♭ major= \n\tF#/G♭ - B♭ - C#\n")

    elif root == ("G#") or root == ("g#") or root == ("Ab") \
            or root == ("ab") or root == ("A♭") or root == ("a♭"):
        print("\nG#/A♭ major = \n\tG#/A♭ - C - E♭\n")


root = input("Type your root note: ")
print(chord(root))




