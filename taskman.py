from main import tkfd, tk, ttk, videoformats, audioformats, imageformats, window, tasks, update_tasklist
def import_file():
    #open a file dialog and get the file
    file = tkfd.askopenfilename(filetypes=[("Video Files", videoformats), ("Audio Files", audioformats), ("Image Files", imageformats)])
    return file

def add_directory(pchooserlb):
    #open a file dialog and get the file
    directory = tkfd.askdirectory()
    pchooserlb.config(text=directory)

def add_task():
    file = import_file()
    if file == "":
        return
    
    #make a popup window to get info like the output file name and the conversion format
    popup = tk.Toplevel(window)
    popup.geometry("500x100")
    #add the icon to the popup
    try:
        img = tk.Image("photo", file="./assets/icon.png")
        window.iconphoto(False, img)
    except:
        pass
    popup.title("Add Task")
    
    pathchooser_frame = tk.Frame(popup)
    pathchooser_frame.pack(side="top", fill="x")
    
    pathchooser_label = ttk.Label(pathchooser_frame, text="No directory chosen", background="white")
    pathchooser = ttk.Button(pathchooser_frame, text="Choose Directory", command=lambda: add_directory(pathchooser_label))
    pathchooser.pack(side="left")
    
    pathchooser_label.pack(side="left")
    
    btframe = tk.Frame(popup)
    btframe.pack(side="bottom", fill="x")
    
    if file.split(".")[-1] in videoformats:
        filetype = "video"
        typechooser = ttk.Combobox(btframe, values=videoformats)
    elif file.split(".")[-1] in audioformats:
        filetype = "audio"
        typechooser = ttk.Combobox(btframe, values=audioformats)
    elif file.split(".")[-1] in imageformats:
        filetype = "image"
        typechooser = ttk.Combobox(btframe, values=imageformats)
    else:
        return
    
    typechooser.pack(side="left")
    
    def add_task_to_list():
        #get the info from the popup
        outputdir = pathchooser_label.cget("text")
        format = typechooser.get()
        #add the task to the list
        tasks.append([file, filetype + " ➔ " + format, outputdir, "Queued"])
        #close the popup
        popup.destroy()
        #update the listbox
        update_tasklist()
    addbtn = ttk.Button(btframe, text="Add Task", command=lambda: add_task_to_list())
    addbtn.pack(side="right")