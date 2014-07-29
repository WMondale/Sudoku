"""
Sudoko Solver
July 29, 2014
Description: Accepts a sudoku puzzle and iteratively adds to it where it is
certain a number fits in a certain cell.  +If this does not complete the
puzzle, backtracking is performed until the puzzle has reached a valid solution.

Changelog
+Waits for input to end program, program can now be run with double-clicning
+Added backtracking functionality.
"""
from copy import deepcopy

#initialize blank 2D 9x9 array
puzzle=[[0 for x in range(9)] for x in range(9)]

#set up blank variable to "catch" the solution ("straight shot" recursive
#returns didn't work out)
sol=[]

def fillPuzzle(puzzle):
	"""Systematically accepts input from the user to get a puzzle."""
	for i in range(9):
		for j in range(9):
			needsinput=True
			while needsinput:
				try:
					print("Please input an integer between 1 and 9,\nor 0 for a blank space: ", "[", i+1, ", ", j+1, "]")
					puzzle[i][j]=int(input())
				except ValueError:
					print("Invalid input, try again.")
					continue
				if puzzle[i][j]>=0 and puzzle[i][j]<=9:
					needsinput=False
				print()
	return puzzle

def isValid(puz, point, number):
	"""Checks the row, column, and square of the given point in the given
	puzzle for the given number.  If it's found, return False, else return
	true."""
	valid=True
	blocka=(0,1,2)
	blockb=(3,4,5)
	blockc=(6,7,8)
	for i in puz[point[0]]: #checks row
		if i==number:
			valid=False
			break
	if valid:
		for i in puz: #checks column
			if i[point[1]]==number:
				valid=False
				break
	if valid:
		if point[0]>=0 and point[0]<=2: #determine row range of block
			r=blocka
		elif point[0]>=3 and point[0]<=5:
			r=blockb
		elif point[0]>=6 and point[0]<=8:
			r=blockc

		if point[1]>=0 and point[1]<=2: #determine column range of block
			c=blocka
		elif point[1]>=3 and point[1]<=5:
			c=blockb
		elif point[1]>=6 and point[1]<=8:
			c=blockc

		for i in r: #check 3x3 block
			for j in c:
				if puz[i][j]==number:
					valid=False
					break
		return valid

def certainSolver(puz):
	"""Checks each blank space in the puzzle for numbers that are valid
	fits.  If one and only one number fits, that number is placed in that
	space in the puzzle."""
	changes=True
	while changes: #keeps the function going as long as a cell is filled in
		changes=False
		for i in range(9):
			for j in range(9):
				numlst=[]
				if puz[i][j]==0:
					for k in range(1, 10):
						if isValid(puz, (i, j), k):
							numlst.append(k)
					if len(numlst)==1:
						puz[i][j]=numlst[0]
						changes=True
	return puz

def backtracker(puz):
	"""Creates a clone of the inputted puzzle, adds a valid number to each
	blank space of the clone, and inputs said clone into a recursive call
	of this function."""
	global sol #allows function to use this global variable to return
	clone=deepcopy(puz)
	clone=certainSolver(clone)
	#try removing the above from this function and running separately
	#before running this, I am unsure if repeatedly running this quickens
	#or slows things
	done=True
	for i in range(9):
		for j in range(9):
			possible=False
			if clone[i][j]==0:
				done=False
				for k in range(1, 10):
					if isValid(clone, (i, j), k):
						possible=True
						clone[i][j]=k
						backtracker(clone)
				if not possible:
					return
	if done:
		sol=clone

			

puzzle=fillPuzzle(puzzle)
backtracker(puzzle)
for i in sol:
	print(i)
#puzzle=certainSolver(puzzle)
#for i in puzzle:
#	print(i)

input("\nPress Enter to close.")
