import random

player = 0
monster = 0
tries = 3

print("There are 3 doors try to find the correct one")

while tries > 0 and player < 20 and monster < 20:
    door = random.randint(1, 3) 
    choice = int(input("Choose a door (1, 2, or 3): "))

    if choice == door:
        player = player + 5
        print("Correct! Player score:", player)
    else:
        monster = monster + 5
        tries = tries - 1
        print("Wrong! Monster score:", monster)
        print("Tries left:", tries)

print(" Game Over ")
print("Player score:", player)
print("Monster score:", monster)

if player >= 20:
    print("Player wins")
elif monster >= 20:
    print("Monster wins")
else:
    print("No more tries. Game over!")


