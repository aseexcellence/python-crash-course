# A way to define multiline dictionary
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'rust',
	'phil': 'python', # best practice
	}
# permanently delete key-value pair
del favorite_languages['sarah']

# Using get() to access values
favorite_language = favorite_languages.get('sarah', 'No language assigned.')
'''
If the key 'sarah' exists in the dictionary, get() returns the corresponding
value. If it doesn't, returns the default value given as the second argument.
If the second argument is left out in the call to get() and the key doesn't exist,
Python will return the value None.
'''

print(favorite_language) # Prints 'No language assigned.'

'''
Looping through dictionary can be done: through all of dictionary's key-value
pairs, through its keys, or through its values.
'''
# 1 Iterate through key-value pairs
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

'''
# 2 Iterate through the keys using keys() method. The keys() method isn't just for
looping: it actually returns a sequence of all the keys as list. For example,
we can use sorted() method to loop through the dictionary in a sorted manner.
'''
for name in favorite_languages.keys():
	language = favorite_languages[name]
	print(f"{name.title()}'s favorite language is {language.title()}.")

# 3 Iterate through the values
for language in favorite_languages.values():
	print(language.title())
	