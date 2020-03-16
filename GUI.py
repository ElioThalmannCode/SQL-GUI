import pymysql

con = pymysql.connect('localhost', 'in19thel', 
    '1234', 'mydb')

with con:
    
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    
    print("Database version: {}".format(version[0]))


root = Tk()
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
app = Window(root)
# set window title
root.wm_title("Customers")

# show window
root.mainloop()