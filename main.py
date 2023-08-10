def censor_invalid_words(input_filename, output_filename, forbidden_words):
    with open(input_filename, 'r') as input_file:
        content = input_file.read()
        words = content.split()

    replaced_words = []
    word_changes = 0

    for word in words:
        if word.lower() in forbidden_words:
            replaced_words.append('***')
            word_changes += 1
        else:
            replaced_words.append(word)

    replaced_text = ' '.join(replaced_words)

    with open(output_filename, 'w') as output_file:
        output_file.write(replaced_text)

    return word_changes

forbidden_words = {'die'}
changes = censor_invalid_words('input.txt', 'output_censored.txt', forbidden_words)
print(f"Статистика: {changes} заміни слів.")