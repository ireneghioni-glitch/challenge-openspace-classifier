from utils.openspace import Openspace

def main():
    # definition of function that extracts names from the txt file 
    # returns the names in a list, one per line
    strings = []
    with open("new_colleagues.txt", "r") as colleagues:
        strings = colleagues.read().split("\n")

    # declaration of openspace type obj room
    room = Openspace()

    # disposition of people in colleagues in the room, tabel per table
    room.organize(strings)

    # print room status
    print(room)

if __name__ == "__main__":
    main()