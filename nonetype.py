# The None keyword is used to define an "empty" variable.

# For instance, we set a username = None early in the code because we don't have anything to assin to it yet
username = None

# Then later in the code, once the user has entered their name, you can assign it to the username variable:
username = input("What's your name?")

# Remember, it's crucial to recognize that None is not the same as the string "None". The look the same when printed, but they are different data types. If you use "None" instead of None, you will end up with code that looks correct when it's printed but fails the tests. In that case, printing the type would distinguish between the two values.
str_none = "None"
none_keyword = None

print(str_none)  # None
print(none_keyword)  # None

print(type(str_none))  # <class 'str'>
print(type(none_keyword))  # <class 'NoneType'>


# NOTE Python is dynamically typed, which means a variable can store any type, and that type can change.

# Example:
speed = 5
speed = "five"

# More often than not, it's a BAD IDEA to change the type of a variable. The 'proper' thing to do is to just create a new one:
speed = 5
speed_description = "five"

# NOTE What is Non-Dynamic typing?

# Languages that aren't dynamically typed are 'statically typed', such as Go. In a statically typed language, if you try to assign a value to a variable of the wrong type, you'll get a compile-time error and the program won't run.
