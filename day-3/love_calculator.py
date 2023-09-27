print("Welcome to love calculator")

name1 = input("Enter your name: ").lower()
name2 = input("Enter name of your partner: ").lower()
names = name1 + name2


def count_character(name, char):
    return name.count(char)


count_true = (count_character(names, "t") +
              count_character(names, "r") +
              count_character(names, "u") +
              count_character(names, "e"))

count_love = (count_character(names, "l") +
              count_character(names, "o") +
              count_character(names, "v") +
              count_character(names, "e"))

value = str(count_true) + str(count_love)

print(f"your love score is {value}")
