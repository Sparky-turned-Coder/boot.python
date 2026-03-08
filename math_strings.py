# When working with strings the + operator performs a "concatenation", which is a fancy word that means "joining two strings". Generally speaking, it's better to use string interpolation with f-strings over + concatenation.

first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
print(full_name)
# prints "Lane Wagner"

# full_name now holds the value "Lane Wagner"


# NOTE Multi-Variable Declaration

sword_name, sword_damage, sword_length = "Excalibur", 10, 200

# is the same as:

sword_name = "Excalibur"
sword_damage = 10
sword_length = 200
