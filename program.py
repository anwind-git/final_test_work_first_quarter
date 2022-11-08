text1 = str(input("Введите первую строку: "))
text2 = str(input("Введите вторую строку: "))
text3 = str(input("Введите третью строку: "))
text4 = str(input("Введите четвертую строку: "))

array1 = [text1, text2, text3, text4]
array2 = []
i = 0

while i < len(array1):
    if len(array1[i]) <= 3:
        array2.append(array1[i])
    i += 1

print(f"Исходный массив: {array1}")
print(f"Строки, в которых три или меньше символов: {array2}")