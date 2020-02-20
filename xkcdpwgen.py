import argparse
import secrets
import random

with open('words.txt', 'r') as f:
    wordlist = f.readlines()

nums = range(0, 9)
symbs = ["~,", "!",  "@", "#", "$", "%", "^", "&", "*", ";", ":"]
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--words", type=int, help="include WORDS words in the password", default=4)
parser.add_argument("-c", "--caps", type=int, help="capitalize the first letter of CAPS random words", default=0)
parser.add_argument("-n", "--numbers", type=int, help="insert NUMBERS random numbers in the password", default=0)
parser.add_argument("-s", "--symbols", type=int, help="insert SYMBOLS random symbols in the password", default=0)
args = parser.parse_args()

password = []

for num_words in range(args.words):
    password.append(secrets.choice(wordlist).replace("\n", ""))

cap_indexes = random.sample(range(0, len(password)), args.caps)
for i in cap_indexes:
    password[i] = password[i].capitalize()

for num_nums in range(args.numbers):
    password.insert(random.randint(0, len(password)), str(secrets.choice(nums)))

for num_symbs in range(args.symbols):
    password.insert(random.randint(0,len(password)), secrets.choice(symbs))

print("".join(password))
