from random import shuffle,randrange
import os

def make_maze(width,height):
	
	global vert_wall
	global hori_wall
	global start_time
	#start_time=time.time()
	
	fill=[[0]*width+[1] for i in range(height)] +[[1]*(width+1)]
	
	vert_wall=[["|  "]* width +['|'] for i in range(height)]+[[]]
	
	hori_wall=[["---"]* width+['+'] for i in range(height+1)]
	display(0);
	
	def point(x,y):
		fill[y][x]=1
		
		display(2);
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

def display(i):
	
	#os.system('cls')
	print "This is level no. ",i
	#print "Time elapsed %.0f"%(time.time()-start_time)
	print "\nYour Maze looks like this\n"
	for (a,b) in zip(hori_wall,vert_wall):		
		print ''.join(a+['\n']+b)
	print "Move your Character"

make_maze(6,3);
display(1);