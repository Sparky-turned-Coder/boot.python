# This one was really cool. We defined a function that can alter the amount of damage an enemy's weapon can deal if it is afflicted with a "lesser curse" or a "greater curse".

# This is really cool, because I can see how I might define some functions that can handle "buffs" and "debuffs"!  Fucking awesome!
print()
print()
print("////////////////////////////////////////")
print("/////////// CURSE WEAPON ///////////////")
print("////////////////////////////////////////")


def curse(weapon_damage):
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * 0.25
    return lesser_cursed, greater_cursed


# Don't modify below this line


def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")


def main():
    test(100)
    print()
    test(500)
    print()
    test(1000)


main()
print()
print()

#  Let's do something similar of our own. Apply an attack debuff to the target.
print("/////////////////////////////////////////")
print("/////////// ATTACK DEBUFF ///////////////")
print("/////////////////////////////////////////")


# define a function to apply our logic for debuffing a target's attack stat
def attack_debuff(attack_stat):
    atk_decrease = attack_stat * 0.75
    severe_atk_decrease = attack_stat * 0.5
    return atk_decrease, severe_atk_decrease


# Define a TEST func that will test our attack_debuff function logic.
def test2(attack_stat):
    print("Player's attack stat is: ", float(attack_stat))
    print("Ennemy casts an attack debuff...")
    atk_decrease, severe_atk_decrease = attack_debuff(
        attack_stat
    )  # You'll notice, this is where we use the values that are returned from the "attack_debuff" function by calling it on (attack_stat)
    print(
        "Hit with an attack debuff, our physical attack drops to: ", float(atk_decrease)
    )
    print(
        "Hit with a severe attack debuff, our physical attack drops to: ",
        float(severe_atk_decrease),
    )
    print("======================================")


# Define a main func that calls our TEST func on some values(arguements) we will provide for our parameters above
def main2():
    test2(120)
    print()
    test2(300)
    print()
    test2(432)


# Call our main function
main2()
