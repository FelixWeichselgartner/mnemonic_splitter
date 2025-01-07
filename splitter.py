import random
from tabulate import tabulate


with open('phrase.txt') as file:
    phrases = file.readlines()
    for i, phrase in enumerate(phrases):
        phrases[i] = phrase[:-1]
    print("original phrases")
    print(phrases)

amount_of_phrases = 12
amount_of_sheets = 3
amount_of_sheets_recover = 2

sheets = [[] for i in range(amount_of_sheets)]
phrases_per_sheet = int(amount_of_phrases * amount_of_sheets_recover / amount_of_sheets)
missing_phrases = amount_of_phrases - phrases_per_sheet
#print(phrases_per_sheet)

first_sheet_phrases = list()
for i in range(phrases_per_sheet):
    a = random.randint(1, 12)
    while a in first_sheet_phrases:
        a = random.randint(1, 12)
    first_sheet_phrases.append(a)
first_sheet_phrases = list(sorted(first_sheet_phrases))
#print(first_sheet_phrases)


def find_missing_phrases(phrases):
    missing = list()
    for i in range(1, amount_of_phrases + 1):
        if i not in phrases:
            missing.append(i)
    return missing


first_sheet_missing_phrases = find_missing_phrases(first_sheet_phrases)
#print(first_sheet_missing_phrases)


def numbers_to_phrases(numbers, phrases):
    phrase_list = ['' for i in range(len(phrases))]
    for n in numbers:
        phrase_list[n - 1] = phrases[n - 1]
    return phrase_list


def pprint_sheet(sheet, number):
    print(f'sheet {number}:')
    for i, s in enumerate(sheet):
        print(f'{i}: {s}')


sheets[0] = numbers_to_phrases(first_sheet_phrases, phrases)
#pprint_sheet(sheets[0], 0)


additional_second_phrases = first_sheet_phrases.copy()
for i in range(missing_phrases):
    random_item_from_list = random.choice(additional_second_phrases)
    additional_second_phrases.remove(random_item_from_list)
second_sheet_phrases = list(sorted(first_sheet_missing_phrases + additional_second_phrases))

sheets[1] = numbers_to_phrases(second_sheet_phrases, phrases)
#pprint_sheet(sheets[1], 1)


second_sheet_missing_phrases = find_missing_phrases(second_sheet_phrases)
#print(first_sheet_missing_phrases)
#print(second_sheet_missing_phrases)
third_sheet_phrases = list(sorted(first_sheet_missing_phrases + second_sheet_missing_phrases))
sheets[2] = numbers_to_phrases(third_sheet_phrases, phrases)
#pprint_sheet(sheets[2], 2)


l = [list(range(1, 13))] + sheets
print()
print('your sheets:')
print(tabulate(list(map(list, zip(*l))), headers=['number', 'sheet 1', 'sheet 2', 'sheet 3'], tablefmt="grid"))


# test sheets against each other
for i in range(amount_of_phrases):
    allowed_amount_of_empty_slots = amount_of_sheets - amount_of_sheets_recover
    amount_of_empty_slots = 0
    for s in range(amount_of_sheets):
        sheet = sheets[s]
        slot = sheet[i]
        if slot == '':
            amount_of_empty_slots += 1
    if amount_of_empty_slots != allowed_amount_of_empty_slots:
        print('DO NOT USE THIS. THERE HAS BEEN SOME ERROR')
        exit()
print('no errors, you can use this on your own risk. please check the code yourself, since your money is on risk.')
print()
input('enter anything to close')
