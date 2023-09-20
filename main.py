message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isupper(): 
        ch_index = ord(ch) - ord('A')
            # зсув даного символа на позицію offset
        ch_shifted = (ch_index + offset) % 26 
        ch_new = chr(ch_shifted + ord('A'))
        encoded_message += ch_new
    elif ch.islower(): # перевірка чи є символ в нижньому регістрі
            # вирахувати юнікод 'a', щоб отримати індекс в діапазоні [0-25)
        ch_index = ord(ch) - ord('a')
        ch_shifted = (ch_index + offset) % 26 
        ch_new = chr(ch_shifted + ord('a'))
        encoded_message += ch_new
    elif ch.isdigit():
        ch_og = (int(ch) + offset) % 10
        encoded_message += str(ch_og)
    else:
            # якщо ні буква ні числоБ залишаємо,як є
        encoded_message += ch
print("Your message:",message)
print("Your encoded message:",encoded_message) 

 # Функція дешифрування
# coded_message = ""
# for ch in crip_message:
#     if ch.isupper():
#             ch_index = ord(ch) - ord('A')
#             ch_og_pos = (ch_index - offset) % 26 + ord('A')
#             ch_og = chr(ch_og_pos)
#             coded_message += ch_og
#     elif ch.islower():
#             ch_index = ord(ch) - ord('a')
#             ch_og_pos = (ch_index - offset % 26 + ord('a')
#             ch_og = chr(ch_og_pos)
#             coded_message += ch_og
#     elif ch.isdigit():
#             ch_og = (int(ch) - offset) % 10
#             coded_message += str(ch_og)
#     else:
#             coded_message += ch
    