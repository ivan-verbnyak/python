# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

count_wat = int(input('--> '))

min_wat = int(input('water_1: '))
max_wat = min_wat

for i in range(count_wat - 1):
    wat = int(input(f'water_{i + 2}: '))
    if wat > max_wat:
        max_wat = wat
    elif wat < min_wat:
        min_wat = wat

print(min_wat, max_wat)