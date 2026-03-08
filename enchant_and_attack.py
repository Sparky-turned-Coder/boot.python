#  Think of your favorite fantasy games. In any of them worth their salt, a weapon can be enchanted to do bonus damage.

# NOTE  *** IF YOU NEED TO BRUSH UP ON FUNCTIONS, I have included an overly complicated explanation of the code used in this script below ***

# TODO
#  Think of other ways you could apply python concepts to further improve the functions mechanics you've created below...
#       - What if an attack brings a target's health down to zero?
#       - What if a target has an increased evasion stat?
#       - Can you calculate a hit-rate mechanic that applies to spells or weapons with lower values of accuracy?


# First, we define a function that will include all of our logic necessary to calculate: the target's health after taking damage, the "enchanted" name of the player's weapon, and the "bonus" damage dealt by an enchanted weapon
def enchant_and_attack(target_health, damage, weapon):
    #  create a new variable that returns a string, renaming the "weapon" value passed to it
    enchanted_weapon = f"enchanted {weapon}"
    #  create a new variable that calculates the bonus damage dealt using the "damage" value passed to it
    enchanted_damage = damage + 10
    #  create a new variable that calculates the target's health after being hit with an "enchanted attack"
    new_health = target_health - enchanted_damage
    return enchanted_weapon, new_health


def test(target_health, damage, weapon):
    print(f"The target has {target_health} health.")
    print(f"{weapon} base damage: {damage}... Enchanting and attacking.")

    # NOTE - on line 23 - We call our function above, "enchant_and_attack". We pass the values in paranthesis to this function.
    #  The "enchant_and_attack" function then uses these values to perform the instructions we gave it.
    #  The "enchant_and_attack" function then returns the new values and we store them in the variables we have declared here.
    #  We used the same variable names above as we did here (enchanted_weapon, new_health) to make our code easier to read and understand. Aside from that, there is no relation between the two. They are in two different function scopes. We simply used the same variable names for ease of understanding.
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"The target has been attacked with the {enchanted_weapon}.")
    print(f"The target has {new_health} health remaining.")
    print("=====================================")


# NOTE - Our "main()" function below provides the values we need. We passed those values into the test function, which then passes them into the enchant_and_attack function. The enchant_and_attack function returns the modified values back to the test function, where we have included "print" statements for printing all the output to the console.


# Define our main function, which will provide the values needed by the functions above to perform their job
def main():
    #  Call the test function on the values provided
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


# Call our main function
main()

# Below, let's write a script that tests enchanted magic attacks!


def enchant_spell_attack(target_health, damage, spell):
    enchanted_spell = f"enchanted {spell}"
    enchanted_damage = damage * 1.5
    new_health = target_health - enchanted_damage
    return enchanted_spell, new_health


def test2(target_health, damage, spell):
    print(f"The Cave Troll has {target_health} health!")
    print(f"{spell} base damage: {damage}... Enchanting spells...")
    enchanted_spell, new_health = enchant_spell_attack(target_health, damage, spell)
    print(f"[Player Name] attacks Cave Troll with {enchanted_spell}...")
    print(f"Cave Troll stumbles, its health has dropped to {new_health}!")
    print("================================================")


def main2():
    test2(450, 200, "Fireball")
    test2(500, 250, "Ice Blast")
    test2(600, 400, "Thunderclap")


main2()
