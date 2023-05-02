from tkinter import *
from funcs import get_response



def user(inp):
    text_area.insert(END, "You: "+inp+'\n\n')

def reply(inp):
    response = get_response(inp)
    text_area.insert(END, "Loki: "+ response +'\n\n')

def combine():
    user_inp = send_Massage.get()
    user(user_inp)
    send_Massage.delete(0,END)
    reply(user_inp)




root = Tk()

# Dimension of app window 
root.geometry("580x680+250+60")

# Title and Background
root.title("Loki the Bot")
root.config( bg = "light blue" )

# Top Label
top_label = Label(root, bg = "light blue", text = "Loki The Bot!!!", font = ('times new roman',25,"bold") , pady=5) 
top_label.pack()

# Center Frame
center_frame = Frame(root, padx= 10, bg= "light blue")
center_frame.pack()

text_area = Text(
                center_frame, 
                font=("times new roman",18,"bold"), 
                height=18, 
                # yscrollcommand= scroll.set,
                wrap= "word",
                padx= 10,
                pady= 5
                )
scroll = Scrollbar(center_frame, orient= "vertical", command = text_area.yview )
text_area.config( yscrollcommand = scroll.set )
scroll.pack( side = RIGHT, fill="y")
text_area.pack(side = LEFT, expand= True)




#Send Message box

send_Massage = Entry(root, font = ("verdena",18, "bold"), width= 43)
send_Massage.pack(pady= 10)

send_button = Button(root, bg="sky blue", text= "Send",font= ("verdana",10,"bold"),
                     command = combine
                     )
send_button.pack()
root.bind('<Return>', lambda event: combine())

root.mainloop()