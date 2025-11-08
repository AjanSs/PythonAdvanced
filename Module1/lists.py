to_do_list = ["math homework","clean the room", "research for history", "fun"]
print(to_do_list[0])
print(to_do_list[1])
print(to_do_list[2])
print(to_do_list[3])

shopping_list = ["apples","bananas",3,4.5]
shopping_list.append("oranges")
print(shopping_list)

shopping_list.insert(2,"lemons")
print(shopping_list)

to_do_list.remove("research for history")
print(to_do_list)

del to_do_list[2]
print(to_do_list)

to_do_list[0] = "physics homework"
print(to_do_list)

to_do_list[1] = 3
print(to_do_list)