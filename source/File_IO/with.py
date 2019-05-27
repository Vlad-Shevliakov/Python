
# ─── CONTEXT MANAGER - WITH ─────────────────────────────────────────────────────

def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line)
# сам закроет поток чтения, даже с ошибкой

read_file('some.txt')


# Тоже, что и ...
try:
    f = open('some.txt', 'r')
    for line in f:
        print(f)
except Exception as err:
    raise err
finally:
    f.close()