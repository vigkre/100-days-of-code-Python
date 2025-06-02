
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
names: pandas.DataFrame = pandas.read_csv("nato_phonetic_alphabet.csv")

names_dict = {row.letter: row.code for (_, row) in names.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
text = input("Enter the word: ").upper()

# phonetic_words = [code for alphabet in text for (letter, code) in names_dict.items() if letter == alphabet]
phonetic_words = [names_dict[letter] for letter in text]
print(phonetic_words)
