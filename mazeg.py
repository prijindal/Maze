from random import shuffle,randrange
import os
import time

from getchFix import _Getch
#A Maze

def system_clear():
	clean = 'cls' if os.name == 'lt' else 'clear'
	os.system(clean)

def display(i):

	system_clear()
	print("This is level no. ",i)
	print("Time elapsed %.0f"%(time.time()-start_time))
	print("\nYour Maze looks like this\n")
	for (a,b) in zip(hori_wall,vert_wall):
		print(''.join(a+['\n']+b))
	print("Move your Character")


def make_maze(width,height):

	global vert_wall
	global hori_wall
	global start_time
	start_time=time.time()

	fill=[[0]*width+[1] for i in range(height)] +[[1]*(width+1)]

	vert_wall=[["|  "]* width +['|'] for i in range(height)]+[[]]

	hori_wall=[["---"]* width+['+'] for i in range(height+1)]

	def point(x,y):
		fill[y][x]=1

		dir=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
		shuffle(dir)
		for (i,j) in dir:

			if fill[j][i]:
				continue
			if i==x:
				hori_wall[max(y,j)][x]="+  "
			if j==y:
				vert_wall[y][max(x,i)]="   "
			point(i,j)

	point(randrange(width),randrange(height))

def change_position(d,n):

	global pos
	posible=True
	d=d.upper()

	if d=='W':

		if pos[1]==0:
			if hori_wall[pos[0]][pos[1]]=="+  ":

				vert_wall[pos[0]-1][pos[1]]="| O"
				vert_wall[pos[0]][pos[1]]="|  "
				pos=[pos[0]-1,pos[1]]

			else:


				posible=False

		else:

			if hori_wall[pos[0]][pos[1]]=="+  ":
				if vert_wall[pos[0]-1][pos[1]]=="|  " and vert_wall[pos[0]][pos[1]]==" O ":
					vert_wall[pos[0]-1][pos[1]]="|O "
					vert_wall[pos[0]][pos[1]]="   "
					pos=[pos[0]-1,pos[1]]

				elif vert_wall[pos[0]-1][pos[1]]=="   " and vert_wall[pos[0]][pos[1]]==" O ":
					vert_wall[pos[0]-1][pos[1]]=" O "
					vert_wall[pos[0]][pos[1]]="   "
					pos=[pos[0]-1,pos[1]]

				elif vert_wall[pos[0]-1][pos[1]]=="|  " and vert_wall[pos[0]][pos[1]]=="|O ":
					vert_wall[pos[0]-1][pos[1]]="|O "
					vert_wall[pos[0]][pos[1]]="|  "
					pos=[pos[0]-1,pos[1]]

				elif vert_wall[pos[0]-1][pos[1]]=="   " and vert_wall[pos[0]][pos[1]]=="|O ":
					vert_wall[pos[0]-1][pos[1]]=" O "
					vert_wall[pos[0]][pos[1]]="|  "
					pos=[pos[0]-1,pos[1]]
			else:


				posible=False


	elif d=='A':

		if pos[1]==1:
			if vert_wall[pos[0]][pos[1]-1]=="|  ":
				if vert_wall[pos[0]][pos[1]]==" O ":

					vert_wall[pos[0]][pos[1]-1]="| O"
					vert_wall[pos[0]][pos[1]]="   "
					pos=[pos[0],pos[1]-1]

				#elif vert_wall[pos[0]][pos[1]]=="|O ":

				#	vert_wall[pos[0]][pos[1]-1]="| O"
				#	vert_wall[pos[0]][pos[1]]="|  "
				#	pos=[pos[0],pos[1]-1]

				else:
					print("ERROR")

			else:


				posible=False

		else:

			if vert_wall[pos[0]][pos[1]]==" O ":

				if vert_wall[pos[0]][pos[1]-1]=="   ":

					vert_wall[pos[0]][pos[1]-1]=" O "
					vert_wall[pos[0]][pos[1]]="   "
					pos=[pos[0],pos[1]-1]

				elif vert_wall[pos[0]][pos[1]-1]=="|  ":

					vert_wall[pos[0]][pos[1]-1]="|O "
					vert_wall[pos[0]][pos[1]]="   "
					pos=[pos[0],pos[1]-1]

				else:
					print("ERROR")
			else:

				posible=False

	elif d=='S':


		if pos[1]==0:
			if hori_wall[pos[0]+1][pos[1]]=="+  ":

				vert_wall[pos[0]+1][pos[1]]="| O"
				vert_wall[pos[0]][pos[1]]="|  "
				pos=[pos[0]+1,pos[1]]

			else:

				posible=False

		elif pos==[n-2,2*n-1]:

			if hori_wall[pos[0]+1][pos[1]]=="+  ":

				if vert_wall[pos[0]][pos[1]]==" O ":

					vert_wall[pos[0]+1][pos[1]]=" O "
					vert_wall[pos[0]][pos[1]]="   "
					pos=[pos[0]+1,pos[1]]
					print("You Won")

				elif vert_wall[pos[0]][pos[1]]=="|O ":

					vert_wall[pos[0]+1][pos[1]]=" O "
					vert_wall[pos[0]][pos[1]]="|  "
					pos=[pos[0]+1,pos[1]]
					print("You Won")

				else:
					print("ERROR")

		else:

			if hori_wall[pos[0]+1][pos[1]]=="+  ":
				if vert_wall[pos[0]+1][pos[1]]=="|  " and vert_wall[pos[0]][pos[1]]==" O ":
					vert_wall[pos[0]+1][pos[1]]="|O "
					vert_wall[pos[0]][pos[1]]="   "
					pos=[pos[0]+1,pos[1]]

				elif vert_wall[pos[0]+1][pos[1]]=="   " and vert_wall[pos[0]][pos[1]]==" O ":
					vert_wall[pos[0]+1][pos[1]]=" O "
					vert_wall[pos[0]][pos[1]]="   "
					pos=[pos[0]+1,pos[1]]

				elif vert_wall[pos[0]+1][pos[1]]=="|  " and vert_wall[pos[0]][pos[1]]=="|O ":
					vert_wall[pos[0]+1][pos[1]]="|O "
					vert_wall[pos[0]][pos[1]]="|  "
					pos=[pos[0]+1,pos[1]]

				elif vert_wall[pos[0]+1][pos[1]]=="   " and vert_wall[pos[0]][pos[1]]=="|O ":
					vert_wall[pos[0]+1][pos[1]]=" O "
					vert_wall[pos[0]][pos[1]]="|  "
					pos=[pos[0]+1,pos[1]]
			else:

				posible=False

	elif d=='D':

		if vert_wall[pos[0]][pos[1]+1]=="   ":

			if pos[1]==0:
				vert_wall[pos[0]][pos[1]+1]=" O "
				vert_wall[pos[0]][pos[1]]="|  "
				pos=[pos[0],pos[1]+1]


			else:

				if vert_wall[pos[0]][pos[1]]==" O ":
					vert_wall[pos[0]][pos[1]+1]=" O "
					vert_wall[pos[0]][pos[1]]="   "
					pos=[pos[0],pos[1]+1]

				elif vert_wall[pos[0]][pos[1]]=="|O ":
					vert_wall[pos[0]][pos[1]+1]=" O "
					vert_wall[pos[0]][pos[1]]="|  "
					pos=[pos[0],pos[1]+1]

				else:
					print("ERROR")

		elif pos==[n-1,2*n-2]:

			if vert_wall[pos[0]][pos[1]]==" O ":
				vert_wall[pos[0]][pos[1]+1]=" O "
				vert_wall[pos[0]][pos[1]]="   "
				pos=[pos[0],pos[1]+1]

			elif vert_wall[pos[0]][pos[1]]=="|O ":
				vert_wall[pos[0]][pos[1]+1]=" O "
				vert_wall[pos[0]][pos[1]]="|  "
				pos=[pos[0],pos[1]+1]

			else:
				print("ERROR")

			print("You Won")

		else:
			posible=False

	elif d=='P':

		print("Alright,you will be taken out of this Game")
		print("Better luck,next Time")
		input()
		exit(0)

	else:

		print("Invalid Input")

	return posible


def is_win(n):
	if pos==[n-1,2*n-1]:
		return True
	else:
		return False


system_clear()
print("We will Play Maze\n")
print("\nYou need to walk your character represented by 'O'")
print("through the maze and reach your target 'T'\n")
print("Move with the help of w,a,s,d\n")
print("And press e to quit")
print("You know, if it seemed too tough for you\n")
print("All The Best")
print("Press enter to start ")

input()

for i in range(1,8):
	system_clear()

	n=3*i
	make_maze(2*n,n)
	pos=[0,0]
	vert_wall[0][0]="| O"
	vert_wall[n-1][2*n-1]=" T "

	display(i)
	while is_win(n)==False:

		cur_time=time.time()-start_time
		if cur_time-int(cur_time)==0.0:
			display(i)
		inptData=_Getch()
		inpt = inptData.impl.__call__()
		b=change_position(inpt,n)
		display(i)

		if b==False:
			print("Can't Move")

	display(i)
	print("You Won this Round")
	input("Press Enter to move to the next Level")

system_clear()
print("Congrats, You cleared all the Levels")
print("Made by-")
print("Priyanshu Jindal")
input("Enter To Exit")
