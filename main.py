
PLACEHOLDER = "[name]"

with open("input/names/invited_names.txt") as name_file:
    names = name_file.readlines()
    print(names)

with open("./input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)
        with open("./output/ready_to_send/letter_for_{}.txt".format(stripped_name), mode='w') as final_letter:
            final_letter.write(new_letter)

