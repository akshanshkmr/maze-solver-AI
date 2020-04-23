maze=[
['#','#','#','#','#','B','#'],
['#','#','#','#','#',' ','#'],
['#','#','#','#',' ',' ','#'],
['#','#','#','#',' ','#','#'],
['#','#','#','#',' ',' ','#'],
['#',' ',' ',' ',' ','#','#'],
[' ',' ','#','#','#','#','#'],
['A','#','#','#','#','#','#'],
]

height=0
width=0
walls=[]
solution=[]
start=()
end=()
choices=[]

def initmaze(m):
	global height,width,walls,solution,start,end
	height=len(m)
	width=max([len(line) for line in m])
	for i in range(height):
		for j in range(width):
				if m[i][j]=='#':
					walls.append((i,j))
				elif m[i][j]=='A':
					start=(i,j)
				elif m[i][j]=='B':
					end=(i,j)

def printmaze(m):
	for i in range(height):
		for j in range(width):
			if (i,j) in walls:
				print('█',end='')
			elif (i,j)==start:
				print('A',end='')
			elif (i,j)==end:
				print('B',end='')
			elif (i,j) in solution:
				print('*',end='')
			else:
				print(m[i][j],end='')
		print()

def checkneighbours(i,j):
	actions=[]
	try:
		if maze[i-1][j] ==' ':
			actions.append('UP')
		if maze[i+1][j] ==' ':
			actions.append('DOWN')
		if maze[i][j-1] ==' ':
			actions.append('LEFT')
		if maze[i][j+1] ==' ':
			actions.append('RIGHT')
	except:
		pass
	finally:
		return actions

def solve(m):
	i=start[0]
	j=start[1]
	global solution
	global choices
	while True:
		#terminal condition
		if i==end[0]and j==end[1]:
			break
		#In case of a dead end move back to last choice
		if len(checkneighbours(i,j))==0:
			try:
				temp=choices.pop()
				i=temp[0]
				j=temp[1]
			except:
				return
		#At a point of diversion store the path choices
		elif len(checkneighbours(i,j))>1:
			for x in checkneighbours(i,j):
				if x=='UP':
					choices.append((i-1,j))
				elif x=='DOWN':
					choices.append((i+1,j))
				elif x=='LEFT':
					choices.append((i,j-1))
				elif x=='RIGHT':
					choices.append((i,j+1))
		#Pick a move from chechneighbours function and implement it
		try:
			move=checkneighbours(i,j).pop()
			solution.append((i,j))
			if move=='UP':
				maze[i-1][j]='*'
				i=i-1
				continue
			if move=='DOWN':
				maze[i+1][j]='*'
				i=i+1
				continue
			if move=='LEFT':
				maze[i][j-1]='*'
				j=j-1
				continue
			if move=='RIGHT':
				maze[i][j+1]='*'
				j=j+1
				continue
		except:
			pass

if __name__ == '__main__':
	initmaze(maze)
	print('Maze:')
	printmaze(maze)
	print()
	print('Solution:')
	solve(maze)
	print(solution)
	print()
	printmaze(maze)
	
