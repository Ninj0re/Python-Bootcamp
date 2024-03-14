import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {value.letter: value.code for (letter, value) in data.iterrows()}

name = input("Enter your name: ").upper()
nato_code = [data_dict[letter] for letter in name if data_dict.get(letter) is not None]
print(nato_code)
