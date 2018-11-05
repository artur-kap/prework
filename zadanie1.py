# Zadanie 1 - suma kontrolna z pliku
file_path = "input.txt"


def get_checksum_for_row(row):
    tmp = list(map(int, row))
    return max(tmp) - min(tmp)


try:
    rows_checksum = []
    with open(file_path, 'r') as file:
        for line in file:
            row = line.replace('\n', '').split('\t')
            rows_checksum.append(get_checksum_for_row(row))
    print('Suma kontrolna pliku {} wynosi {}'.format(file_path, sum(rows_checksum)))

except FileNotFoundError as e:
    print("Podany plik nie istnieje!", e)
except Exception as e:
    print("Wystąpił błąd.", e)
finally:
    if file: file.close()
