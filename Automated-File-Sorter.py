from customtkinter import *
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog
import os,shutil

#file_Sorting
def automatic_file_sorting(path):
    path = path+'\\'
    file_list = os.listdir(path)
    new_folder = ['csv files', 'Images files', 'Text files', 'Excel files', 'pdf files','Video files','Applications','JSON Files','Powerpoint Presentations','Word Documents','Other']
    for i in new_folder:
        if not os.path.exists(path + i):
            os.makedirs(path + i)
        else:
            continue


    extension_images = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".heic", ".heifs", ".avif", ".svg", ".ai", ".eps", ".pdf", ".raw", ".arw", ".cr2", ".nef", ".sr2"]
    extensions_video = [".mp4", ".mov", ".avi", ".wmv"]

    for file in file_list:
        if '.csv' in file and not os.path.exists(path+'csv files\\'+file):
            shutil.move(path+file, path+'csv files\\'+file)
        elif '.pdf' in file and not os.path.exists(path+'pdf files\\'+file):
            shutil.move(path+file, path+'pdf files\\'+file)
        elif '.xlsx' in file and not os.path.exists(path+'Excel files\\'+file):
            shutil.move(path+file, path+'Excel files\\'+file)
        elif any(ext in file for ext in extension_images) and not os.path.exists(path+'Images files\\'+file):
            shutil.move(path+file, path+'Images files\\'+file)
        elif any(ext2 in file for ext2 in extensions_video) and not os.path.exists(path+'Video files\\'+file):
            shutil.move(path+file, path+'Video files\\'+file)
        elif '.txt' in file and not os.path.exists(path+'Text files\\'+file):
            shutil.move(path+file, path+'Text files\\'+file)
        elif '.exe' in file and not os.path.exists(path+'Text files\\'+file):
            shutil.move(path+file, path+'Applications\\'+file)
        elif '.json' in file and not os.path.exists(path+'Text files\\'+file):
            shutil.move(path+file, path+'JSON files\\'+file)
        elif '.pptx' in file and not os.path.exists(path+'Text files\\'+file):
            shutil.move(path+file, path+'Powerpoint Presentations\\'+file)
        elif '.docx' in file and not os.path.exists(path+'Text files\\'+file):
            shutil.move(path+file, path+'Word Documents\\'+file)
        else:
            shutil.move(path+file, path+'Other\\'+file)


#GUI
window = CTk()
window.geometry("600x350")
window.title("Automatic Folder Sorter")
#setting theme of GUI to dark
set_appearance_mode("Dark")

folder_location=''
def ask_folder():
    global folder_location
    folder_location = filedialog.askdirectory()
    folder_path.delete(0, 'end')
    folder_path.insert(0, folder_location)

def show_success():
    if CTkMessagebox(message="Sorting Completed!", 
                  icon="check", 
                  option_1="OK",title="Completion Message"):
            os.startfile(folder_location)
            folder_path.delete(0, 'end')
    

def Final_call():
    automatic_file_sorting(folder_location)
    show_success()
    
    
folder_path_label = CTkLabel(window,text="Select Source Directory",font=CTkFont(size=15),text_color='#E0E0E0')
folder_path = CTkEntry(window,width=300,text_color='#E0E0E0',fg_color='#33373D')
browse_btn =CTkButton(window,command=ask_folder,text="Browse",text_color='white',width=30,fg_color='#454A4E')

sort_btn = CTkButton(window,text='Sort Files',text_color='White',fg_color='green',command=Final_call)



folder_path_label.place(x=22,y=70)
folder_path.place(x=200,y=70)
browse_btn.place(x=510,y=70)
sort_btn.place(x=250,y=140)

window.mainloop()