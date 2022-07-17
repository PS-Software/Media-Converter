import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkm
from PIL import Image, ImageTk
import os

global tasks
tasks = []
global videoformats
videoformats = ["mp4", "avi", "mkv", "mov", "wmv", "flv", "mpg", "mpeg", "mts", "gif"]
global audioformats
audioformats = ["mp3", "wav", "flac", "ogg", "aac", "wma", "m4a"]
global rasterimageformats
rasterimageformats = ["jpg", "jpeg", "jfif", "gif", "png", "bmp", "tiff", "tif", "heic", "webp"]
global vectorimageformats
vectorimageformats = ["svg"]

window = tk.Tk()
#make the window size 50% screen resolution
window.geometry("%dx%d+%d+%d" % (window.winfo_screenwidth()/2, window.winfo_screenheight()/2, window.winfo_screenwidth()/4, window.winfo_screenheight()/4))
#maximize the window
#window.state('zoomed')
window.title("PizzaSoft Media Converter v22.0.1")
#set icon to icon.png
try:
    img = tk.Image("photo", file="./assets/icon.png")
    window.iconphoto(False, img)
except:
    pass

style = ttk.Style()
styles = style.theme_names()
menu = tk.Menu(window)

fileMenu = tk.Menu(menu, tearoff=0)
fileMenu.add_command(label="Open")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.quit)

tasksMenu = tk.Menu(menu, tearoff=0)
tasksMenu.add_command(label="Run All Tasks", state="disabled")
tasksMenu.add_command(label="Cancel All Tasks", state="disabled")
tasksMenu.add_command(label="Remove All Tasks", state="disabled")

themesSub = tk.Menu(tasksMenu, tearoff=0)
#add all available themes to the themes submenu
for theme in styles:
    themesSub.add_command(label=theme, command=lambda theme=theme: style.theme_use(theme))

viewMenu = tk.Menu(menu, tearoff=0)
viewMenu.add_cascade(label="Theme", menu=themesSub)

editMenu = tk.Menu(menu, tearoff=0)
editMenu.add_command(label="Preferences")

window.config(menu=menu)
menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="Edit", menu=editMenu)
menu.add_cascade(label="Tasks", menu=tasksMenu)
menu.add_cascade(label="View", menu=viewMenu)
menu.add("command", label="Help", command=lambda: os.startfile("https://pizzasoft.us/helpcenter/"))

#make a frame for the buttons at the top
buttons = tk.Frame(window)
buttons.pack(side="top", fill="x")

def import_file():
    #open a file dialog and get the file
    file = tkfd.askopenfilename(filetypes=[("Video Files", videoformats), ("Audio Files", audioformats), ("Raster Image Files", rasterimageformats), ("Vector Image Files", vectorimageformats)])
    #if the file is not empty, add it to the list
    if file != "":
        return file

def add_task():
    file = import_file()
    # make a popup window to get info about the task
    popup = tk.Toplevel(window)
    popup.title("Add Task")
    popup.geometry("%dx%d+%d+%d" % (popup.winfo_screenwidth()/8, popup.winfo_screenheight()/8, popup.winfo_screenwidth()/4, popup.winfo_screenheight()/16))
    popup.resizable(False, False)
    # the popup will have a dropdown menu to select the task type
    # the dropdown menu will have the following options:
    # - file type conversion ("Convert")
    # - transcoding ("Transcode")
    
    # the content of the popup will change depending on the task type
    
    # create a frame for the dropdown menu
    dropdown = tk.Frame(popup)
    dropdown.pack(side="top", fill="x")
    # create a label for the dropdown menu
    dropdown_label = tk.Label(dropdown, text="Task Type")
    dropdown_label.pack(side="top")
    # create a dropdown menu
    dropdown_menu = ttk.Combobox(dropdown, values=["Convert", "Transcode"])
    dropdown_menu.pack(side="top")
    # create a frame for the content of the popup
    contentConvert = tk.Frame(popup)
    contentConvert.pack(side="bottom", fill="x")
    
    # if the option selected is "Convert", the content of the popup will be:
    # - new file type dropdown menu
    # - output file directory selection button
    
    # no matter what the option selected is, there will be an "Add Task" button
    
    # content of the file type dropdown menu: video files array (videoformats)
    # add the file type dropdown menu to the content frame
    file_type_dropdown = ttk.Combobox(contentConvert, values=videoformats)
    file_type_dropdown.pack(side="right")
    # create a label for the file type dropdown menu
    file_type_dropdown_label = tk.Label(contentConvert, text="Output File Type")
    file_type_dropdown_label.pack(side="left")
    # create a button to select the output file directory
    global outdir
    outdir = ""
    def output_file_directory():
        output_file_directory = tkfd.askdirectory()
        return output_file_directory
    def select_output_file_directory():
        output_file_directory = output_file_directory()
        global outdir
        outdir = output_file_directory
    output_file_directory_button = tk.Button(contentConvert, text="Select Output File Directory", command=select_output_file_directory)
    output_file_directory_button.pack(side="left")
    
    # wait for a selection to be made for the task type
    def dropdown_menu_selection():
        # if the option selected is "Convert", the content of the popup will be:
        # - new file type dropdown menu
        # - output file directory selection button
        if dropdown_menu.get() == "Convert":
            # add the file type dropdown menu to the content frame
            file_type_dropdown.pack(side="right")
            # create a label for the file type dropdown menu
            file_type_dropdown_label.pack(side="left")
        # if the option selected is "Transcode", the content of the popup will be:
        # - new file type dropdown menu
        # - output file directory selection button
        elif dropdown_menu.get() == "Transcode":
            # add the file type dropdown menu to the content frame
            file_type_dropdown.pack(side="right")
            # create a label for the file type dropdown menu
            file_type_dropdown_label.pack(side="left")
        
    dropdown_menu.bind("<<ComboboxSelected>>", dropdown_menu_selection)

#make the buttons
importButton = ttk.Button(buttons, text="Import", command=add_task)

rat = ttk.Button(buttons, text="Run All Tasks", state="disabled") #you can tell who made this variable name (it was me, lewolfyt)
cat = ttk.Button(buttons, text="Cancel All Tasks", state="disabled")
rmat = ttk.Button(buttons, text="Remove All Tasks", state="disabled")

importButton.pack(side="left")
rat.pack(side="left")
cat.pack(side="left")
rmat.pack(side="left")

#make the task list frame
tasklframe = tk.Frame(window)
tasklframe.pack(side="top", fill="both", expand=True)
tasklist = tk.Listbox(tasklframe, selectmode="extended")

window.mainloop()