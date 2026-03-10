# Enchant spells with bonus damage


def enchant_spell(target_health, damage, spell):
    enchanted_spell = f"enchanted {spell}"
    enchanted_damage = damage * 1.5
    new_health = target_health - enchanted_damage
    return new_health, enchanted_spell


def test(target_health, damage, spell, monster, monster_attack):
    print(f"Current health of {monster} is {target_health}.")
    print(f"Base damage of {spell} is {damage}. Casting an enchantment on it...")
    new_health, enchanted_spell = enchant_spell(target_health, damage, spell)
    print(f"The player casts {enchanted_spell} on {monster}!")
    # This if statement handles if the spell becomes strong enough to kill the target.
    if new_health > 0:
        print(f"The {monster} snarls angrily. It has {new_health} health remaining.")
        print(f"{monster} {monster_attack}, hitting you for 1200 damage!")
    elif new_health <= 0:
        print(f"The {monster} has been slain! 1,245 Exp. Gained!")
    print("==================================================\n")


def main():
    test(
        3000, 1234, "Thunderclap", "Green Dragon", "spews Green Fire in all directions"
    )
    test(
        4235,
        2036,
        "Earthquake",
        "Cave Troll",
        "slams the ground with his club, splitting the earth",
    )
    test(
        7500,
        4200,
        "Ultima",
        "Magma Wyrm",
        "slashes a mighty sword, throwing lava across the battlefield",
    )
    test(4000, 3000, "Arcane Blast", "Bully Goat", "throws horns at you")


main()
