name = "asegid shegaw"
print(name.title())

print(name.upper())

kilkil = "AsEgId ShEgAw"
swapped = ""
for char in kilkil:
    if(char.isupper()):
        swapped += char.lower()
    elif(char.islower()):
        swapped += char.upper()
    else:
        swapped += char

print(swapped)

print("Please enter your first name: ")
first_name = input()
print("please enter your last name: ")
last_name = input()
full_name = f"{first_name} {last_name}"

print(f"Hello {first_name.title()}, would you like to learn some Python today?")

message = "One of Python's strengths is its diverse community"
print(message)

file_name = "    python_notes.txt    "
print(f"The file name is: {file_name.strip().removesuffix('.txt')}")

quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new.'

print(quote)

# how to edit a string
print("Let's update the name of the person who said the above quote")
quote = quote.split(" ")
quote[0] = 'Mike'
quote[1] = 'Tyson'
quote = " ".join(quote)
print(quote)

# popping by index and removing an item by its value
quote = quote.split(" ")
name = quote.pop(0)
print(f"\nI don't think {name} said that.")
name += " " + quote.pop(0)
print(f"So we need to remove {name}'s name from the quote.")

name = quote.insert(0, 'Albert Einstein')
quote = " ".join(quote)
print(quote)

