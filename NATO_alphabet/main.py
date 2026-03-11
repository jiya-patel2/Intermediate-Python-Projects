import pandas

data = pandas.read_csv("NATO_alphabet\\nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        # Attempt to create the list
        nato_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        # If a character isn't found in the dictionary
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic() # Restart the function
    else:
        # If no errors occurred, print the result
        print(nato_list)

generate_phonetic()