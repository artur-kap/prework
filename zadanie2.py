directory_path = "words"


def read_file(file_name):
    out = None
    try:
        with open(file_name, 'r') as file:
            out = file.read().lower()
    except FileNotFoundError as e:
        print("Podany plik nie istnieje!", e)
    except Exception as e:
        print("Wystąpił błąd.", e)
    finally:
        file.close()
    return out


dane = []
for i in range(0, 30):
    dane.extend(read_file(directory_path + '\\' + "word_{}.txt".format(i)))

all_letters, counter = len(dane), 0
used_letters = set(dane)
for letter in used_letters:
    number = dane.count(letter)
    counter = counter + number
    print('litera {} występuje {} razy w plikach '.format(letter, number))
print('Wszystkich liter w plikach {} łączna suma wystąpień {}'.format(all_letters, counter))
