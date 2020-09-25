"""24/09/2020 - Thursday
Dictionary Exercise
Type a sequence of numbers and at the end
transcript each element.
In case of typing a character, show ! """
digits_mapping = {"1": "One", "2": "Two", "3": "Three",
                 "4": "Four", "5": "Five", "6": "Six",
                 "7": "Seven", "8": "Eight", "9": "Nine",
                 "0": "Zero"}

digits = input("Type your phone number: ")
output = ""

for ch in digits:
    output += digits_mapping.get(ch, "!") + " "

print(output)