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

quote = 'Albert Eintein once said, "A person who never made a mistake never tried anything new.'

print(quote)

# how to edit a string
print("Let's update the name of the person who said the above quote")
quote = quote.split(" ")
quote[0] = 'Mike'
quote[1] = 'Tyson'
quote = " ".join(quote)
print(quote)

# removing an item by its value
quote = quote.split(" ")
print(quote)
name = quote.remove('new.')
print(name)
print(f"\nI don't think {quote.remove('Mike')} said that.")

