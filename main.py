# ─── BASE ───────────────────────────────────────────────────────────────────────

def words():
    """
        Сколько слов в файле
    """
    file_name = input('File name: ')
    file = open(file_name, 'r')
    # Тут будут все символы в файле
    all_words = file.read().split() # в лист по проб.
    # ['Qwerty', 'lorem', 'loop', '|', '|', '|', '___', 'Hello', 'Python']
    word_dict = {}

    for word in all_words:
        word_dict[word] = word_dict.get(word, 0) + 1
        # Если нет, создать, а если есть - добавить
    
    print(file_name)
    print('Words in file: {}'.format(len(all_words)))
    print('Result: \n {}'.format(word_dict))

    return word_dict


if __name__ == '__main__':
    words()

