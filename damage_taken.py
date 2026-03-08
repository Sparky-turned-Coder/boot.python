#  In this lesson, we defined functions that we could call and calculate the damage of two different types of attacks: Punches and Slashes.

#  This was particularly cool, because if you are given a "weapon type", "player health", and "player armor", you can define a function that handles the amount of damage you recieve and simply returnthe player's new health amount!


def get_punched(health, armor=0):
    damage = 50 - armor
    new_health = health - damage
    return new_health


def get_slashed(health, armor=0):
    damage = 100 - armor
    new_health = health - damage
    return new_health


# Don't touch below this line


def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)
