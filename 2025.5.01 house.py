name = input("What's your name? ")

match name:
    case"Harry"|"Nigel":
        print("Gryffindor")
    case"Hermione":
        print("Gryffindor")
    case _:
        print("Who?")

        
