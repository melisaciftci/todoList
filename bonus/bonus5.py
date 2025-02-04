waiting_list = ["sen", "ben", "john"]
waiting_list.sort()


for index, name in enumerate(waiting_list):
    print(f"{index + 1}.{name.capitalize()}")