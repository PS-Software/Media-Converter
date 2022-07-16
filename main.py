import tkinter as tk
import tkinter.ttk as ttk
import os

wndw = tk.Tk()
#make the window size 50% screen resolution
wndw.geometry("%dx%d+%d+%d" % (wndw.winfo_screenwidth()/2, wndw.winfo_screenheight()/2, wndw.winfo_screenwidth()/4, wndw.winfo_screenheight()/4))
#maximize the window
#wndw.state('zoomed')
wndw.title("PizzaSoft Media Converter v22.0.1")
#set icon to icon.png
try:
    img = tk.Image("photo", file="./assets/icon.png")
    wndw.iconphoto(False, img)
except:
    pass

style = ttk.Style()
styles = style.theme_names()
menu = tk.Menu(wndw)

fileMenu = tk.Menu(menu, tearoff=0)
fileMenu.add_command(label="Open")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=wndw.quit)

tasksMenu = tk.Menu(menu, tearoff=0)
tasksMenu.add_command(label="Run All Tasks", state="disabled")
tasksMenu.add_command(label="Pause All Tasks", state="disabled")
tasksMenu.add_command(label="Resume All Tasks", state="disabled")
tasksMenu.add_command(label="Cancel All Tasks", state="disabled")
tasksMenu.add_command(label="Remove All Tasks", state="disabled")

themesSub = tk.Menu(tasksMenu, tearoff=0)
#add all available themes to the themes submenu
for theme in styles:
    themesSub.add_command(label=theme, command=lambda: style.theme_use(theme))

viewMenu = tk.Menu(menu, tearoff=0)
viewMenu.add_cascade(label="Theme", menu=themesSub)

editMenu = tk.Menu(menu, tearoff=0)
editMenu.add_command(label="Preferences")

wndw.config(menu=menu)
menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="Edit", menu=editMenu)
menu.add_cascade(label="Tasks", menu=tasksMenu)
menu.add_cascade(label="View", menu=viewMenu)
menu.add("command", label="Help", command=lambda: os.startfile("https://ps-software.github.io/helpcenter/"))

button = ttk.Button(wndw, text="test")
button.place(relx=0.5, rely=0.5, anchor="center")

wndw.mainloop()