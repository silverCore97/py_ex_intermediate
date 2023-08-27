import     tkinter, tkinter.messagebox
import random
# Game 2048 - Shift the numbers up, down left and right to reach 2048 and win
# [2 2 2 0] <-  => [4 2 0 0]
# [2 2 2 2] <-  => [4 4 0 0]

class Screen:
    def __init__(self):
        self.size=4
        self.window = tkinter.Tk()
        self.window.title("2048 - The Game")
        self.field = tkinter.Frame(self.window)
        self.buttons = []
        self.labels = []
        self.grid = [[0 for i in range(self.size)] for j in range(4)]
        self.arrows = []

        # Labels for field
        for i in range(4):
            rows=[]
            for j in range(4):
                l=tkinter.Label(self.field,text='',width=8,height=4,fg="black",bg="white")
                l.grid(row=i,column=j,padx=5,pady=5)
                rows.append(l)
            self.labels.append(rows)


        # Buttons
        self.text = ['Left','Up', 'Down', 'Right']
        for i in range(4):
            b = tkinter.Button(self.field, text = self.text[i], command = lambda i=i:self.arrow(direction=self.text[i]))
            b.grid(row=4,column=i, padx=5,pady=5)
            self.arrows.append(b)
        self.field.grid()
        self.add_random()
        self.add_random()
        self.redraw()

    # Splitting up arrow() into smaller subfunctions
    def compress(self):
        # Shift towards left
        for i in range(4):
            curr = 0
            for j in range(4):
                if self.grid[i][j] != 0:
                    temp = self.grid[i][j]
                    self.grid[i][j] = 0
                    self.grid[i][curr] = temp
                    curr += 1

    def merge(self):
        # Merge fitting tiles, starting from left
        for i in range(4):
            curr = 0
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j + 1]:
                    self.grid[i][j] *= 2
                    self.grid[i][j + 1] = 0

    # Using transformations of the initial table for different directions
    def arrow(self,direction:str):
        # Left
        if direction == self.text[0]:
            self.compress()
            self.merge()
            self.compress()
        # Up
        elif direction==self.text[1]:
            self.grid=list(map(list,zip(*self.grid)))
            self.compress()
            self.merge()
            self.compress()
            self.grid=list(map(list, zip(*self.grid)))
        # Down
        elif direction == self.text[2]:
            self.grid=list(map(list, zip(*self.grid)))
            self.grid = [[el[self.size-j-1] for j in range(self.size)] for el in self.grid]
            self.compress()
            self.merge()
            self.compress()
            self.grid = [[el[self.size-j-1] for j in range(self.size)] for el in self.grid]
            self.grid=list(map(list, zip(*self.grid)))
        # Right
        elif direction == self.text[3]:
            self.grid = [[el[self.size-j-1] for j in range(self.size)] for el in self.grid]
            self.compress()
            self.merge()
            self.compress()
            self.grid = [[el[self.size - j-1] for j in range(self.size)] for el in self.grid]
        #Add new random element if possible
        self.add_random()
        # Redraw labels for new state of the field
        self.redraw()



    """
    # Requires optimization
    def arrow(self,direction:str):

        if direction == self.text[0]:


            #Shift towards left
            for i in range(4):
                curr = 0
                for j in range(4):
                    if self.grid[i][j]!=0:
                        temp = self.grid[i][j]
                        self.grid[i][j]=0
                        self.grid[i][curr] = temp
                        curr+=1
            # Merge fitting tiles, starting from left
            for i in range(4):
                curr = 0
                for j in range(3):
                    if self.grid[i][j]==self.grid[i][j+1]:
                        self.grid[i][j]*=2
                        self.grid[i][j+1]=0
            # Shift towards left
            for i in range(4):
                curr = 0
                for j in range(4):
                    if self.grid[i][j] != 0:
                        temp = self.grid[i][j]
                        self.grid[i][j] = 0
                        self.grid[i][curr] = temp
                        curr += 1


        elif direction == self.text[1]:

            #Shift towards up
            for j in range(4):
                curr = 0
                for i in range(4):
                    if self.grid[i][j]!=0:
                        temp = self.grid[i][j]
                        self.grid[i][j]=0
                        self.grid[i][curr] = temp
                        curr+=1
            # Merge fitting tiles, starting from up
            for j in range(4):
                curr = 0
                for i in range(3):
                    if self.grid[i][j]==self.grid[i+1][j]:
                        self.grid[i][j]*=2
                        self.grid[i+1][j]=0
            #Shift towards up
            for j in range(4):
                curr = 0
                for i in range(4):
                    if self.grid[i][j]!=0:
                        temp = self.grid[i][j]
                        self.grid[i][j]=0
                        self.grid[i][curr] = temp
                        curr+=1

        elif direction == self.text[2]:
            #Shift towards down
            for j in range(4):
                curr = 3
                for i in range(0,4,-1):
                    if self.grid[i][j]!=0:
                        temp = self.grid[i][j]
                        self.grid[i][j]=0
                        self.grid[curr][j] = temp
                        curr-=1
            # Merge fitting tiles, starting from down
            for j in range(4):
                curr = 3
                for i in range(1,4,-1):
                    if self.grid[i][j]==self.grid[i-1][j]:
                        self.grid[i][j]*=2
                        self.grid[i-1][j]=0
            # Shift towards down
            for j in range(4):
                curr = 3
                for i in range(0,4,-1):
                    if self.grid[i][j] != 0:
                        temp = self.grid[i][j]
                        self.grid[i][j] = 0
                        self.grid[curr][j] = temp
                        curr -= 1

        elif direction == self.text[3]:
            #Shift towards right
            for i in range(4):
                curr = 3
                for j in range(0,4,-1):
                    if self.grid[i][j]!=0:
                        temp = self.grid[i][j]
                        self.grid[i][j]=0
                        self.grid[i][curr] = temp
                        curr-=1
            # Merge fitting tiles, starting from right
            for i in range(4):
                curr = 3
                for j in range(1,4,-1):
                    if self.grid[i][j]==self.grid[i][j-1]:
                        self.grid[i][j]*=2
                        self.grid[i][j-1]=0
            # Shift towards right
            for i in range(4):
                curr = 0
                for j in range(0,4,-1):
                    if self.grid[i][j] != 0:
                        temp = self.grid[i][j]
                        self.grid[i][j] = 0
                        self.grid[i][curr] = temp
                        curr -= 1
        self.add_random()
        self.redraw()
        """


    # Insert
    def add_random(self):
        empty_list = [(i,j) for i in range(4) for j in range(4) if self.grid[i][j]==0 ]
        if len(empty_list)>0:
            rand = random.Random()
            num = 2 + 2*rand.randint(0,1)
            position= rand.randint(0,len(empty_list)-1)
            a = empty_list[position][0]
            b = empty_list[position][1]
            self.grid[a][b] = num

    def redraw(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j]==0:
                    self.labels[i][j].config(text='',width=8,height=4,fg="black",bg="white")
                else:
                    self.labels[i][j].config(text=str(self.grid[i][j]),width=8,height=4,fg="black",bg="white")

game=Screen()
game.window.mainloop()



