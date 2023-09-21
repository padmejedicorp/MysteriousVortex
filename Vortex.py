import time

def introduction():
    print("Welcome to the Mysterious Vortex Adventure!")
    print("You find yourself trapped in a swirling vortex of mystery.")
    print("Your goal is to navigate through the vortex and uncover its secrets.")
    print("Choose your path carefully, and beware of the unknown.")

def dark_tunnel():
    print("\nYou enter the dark tunnel, and it becomes pitch black.")
    print("You hear strange whispers all around you.")
    time.sleep(2)

    print("\nSuddenly, you see a faint light up ahead.")
    print("Do you want to continue towards the light?")
    print("1. Yes")
    print("2. No, go back")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        mysterious_cave()
    elif choice == '2':
        choose_path()
    else:
        print("Invalid choice. Try again.")
        dark_tunnel()
def choose_path():
    print("\nYou stand at a crossroads. Which path will you choose?")
    print("1. Go left into a dark tunnel.")
    print("2. Go right towards a glowing light.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        dark_tunnel()
    elif choice == '2':
        glowing_light()
    else:
        print("Invalid choice. Try again.")
        choose_path()

def glowing_light():
    print("\nAs you approach the glowing light, it intensifies.")
    print("You find yourself in a beautiful, serene garden.")
    time.sleep(2)

    print("\nIn the center of the garden, there's a mysterious door.")
    print("Do you want to enter the door?")
    print("1. Yes")
    print("2. No, go back")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        secret_chamber()
    elif choice == '2':
        choose_path()
    else:
        print("Invalid choice. Try again.")
        glowing_light()

def mysterious_cave():
    print("\nYou enter a vast, underground cave filled with glowing crystals.")
    print("You feel a strange energy in the air.")
    time.sleep(2)

    print("\nYou come across two tunnels: one leading deeper into the cave and another going upward.")
    print("1. Go deeper into the cave.")
    print("2. Go upward.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        deeper_cave()
    elif choice == '2':
        choose_path()
    else:
        print("Invalid choice. Try again.")
        mysterious_cave()

def deeper_cave():
    print("\nYou venture deeper into the cave and discover a hidden chamber.")
    print("Inside the chamber, you find a treasure chest.")
    print("Do you want to open the chest?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("\nCongratulations! You've found the hidden treasure.")
        print("You have successfully navigated the Mysterious Vortex.")
    elif choice == '2':
        print("\nYou decide to leave the chest untouched and return to the vortex.")
        choose_path()
    else:
        print("Invalid choice. Try again.")
        deeper_cave()

def secret_chamber():
    print("\nYou enter the mysterious door and find yourself in a dimly lit chamber.")
    print("Strange symbols cover the walls, and there's a pedestal in the center.")
    time.sleep(2)

    print("\nOn the pedestal, you see an ancient book.")
    print("Do you want to open the book and read its contents?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("\nThe book contains ancient knowledge that unlocks the secrets of the vortex.")
        print("You have successfully navigated the Mysterious Vortex.")
    elif choice == '2':
        print("\nYou decide not to meddle with the book and return to the garden.")
        choose_path()
    else:
        print("Invalid choice. Try again.")
        secret_chamber()

if __name__ == "__main__":
    introduction()
    choose_path()
