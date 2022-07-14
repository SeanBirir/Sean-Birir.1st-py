"""it is a structure in python which allows us to store information in key value pairs.
first step in creating a dictionary is give it a name,
the information stored has to be enclosed in {} and the values inside must be diffferent
they should be separated by commas"""

months = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep":"september",
    "oct":"october",
    "nov":"nivember",
    "dec":"december"
}

print(months["aug"])
print(months.get("jan"))

#you can put out a default value in the dictionary using the .get()

print(months.get("asd","not a valid key."))
