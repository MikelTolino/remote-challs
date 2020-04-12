#! /usr/bin/python3

import sys

def error(n_arg):
	if n_arg <= 1 or n_arg > 21:
		print("usage: ./mmateo-t.py <1-9 squared_rows...>")
		return(True)
		sys.exit(1)

	for i in range(1,n_arg):
		if len(sys.argv[i]) != (n_arg - 1) or not sys.argv[i].isnumeric() or sys.argv[i].find('0') >= 0:
			print("usage: ./mmateo-t.py <1-9 squared_rows...>")
			return(True)
			sys.exit(1)


def snail(matrix):
	l = len(matrix)
	e_col = e_row = l - 1
	s_col = s_row = 0
	while s_col <= e_col and s_row <= e_row:
		for i in range(s_col, e_col + 1):
			print(matrix[s_row][i], end= " ")
		s_row+=1
		for i in range(s_row, e_row + 1):
			print(matrix[i][e_col], end= " ")
		e_col -=1
		for i in range(e_col, s_col - 1, -1):
			print(matrix[e_row][i], end= " ")
		e_row-=1
		for i in range(e_row, s_row - 1, -1):
			print(matrix[i][s_col], end= " ")
		s_col+=1
		
			


def main():
	matrix = []
	n_arg = len(sys.argv)
	if error(n_arg):
		sys.exit(1)
	
	for i in range(1, n_arg):
		matrix.append([])
		for j in range(n_arg - 1):
			matrix[i - 1].append(int(sys.argv[i][j]))
	snail(matrix)
	print()
	sys.exit()	

main()


