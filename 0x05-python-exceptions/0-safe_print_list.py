#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	try:
		len_my_list = 0
		for i in range(x):
			print(my_list[i], end="")
			len_my_list += 1
		print("")
		return len_my_list
	except IndexError:
		print("")
		return len_my_list
