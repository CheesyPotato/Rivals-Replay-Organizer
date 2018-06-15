from tkinter import *
import os
from tkinter.font import Font
import shutil
from tkinter.filedialog import askdirectory


def browse():
    choosedirectory = askdirectory(initialdir = os.path.expanduser(r"~\\Desktop"), )
    changedestinationentry.delete(0, END)
    changedestinationentry.insert(0, choosedirectory)
    save()
def saved():
    savedlabel.destroy()
def errorsaved():
    errorsavedlabel.destroy()
def errormatch():
    errormatchlabel.destroy()
def errorplayer():
    errorplayerlabel.destroy()
def errorfile():
    errorfilelabel.destroy()
def success():
    successlabel.destroy()
def default():
    if not os.path.exists(os.path.expanduser(r"~\\Desktop\\Rivals Replays")):
        os.makedirs(os.path.expanduser(r"~\Desktop\Rivals Replays"))
    changedestinationentry.delete(0, END)
    changedestinationentry.insert(0, os.path.expanduser(r"~\Desktop\Rivals Replays"))
    save()
def start():
    if v.get() == 0:
        global errormatchlabel
        errormatchlabel = Label(root, text = 'Error: Select how many matches you played', fg = 'red')
        errormatchlabel.place(x=115,y=250)
        root.after(2000, errormatch)
    else:
        f = open('config', 'r')
        if f.read() == 'DEFAULT':
            f.seek(0)
            directory = os.path.expanduser("~\Desktop\Rivals Replays")
        else:
            f.seek(0)
            directory = f.read()
            f.seek(0)
        f.close()

        filelist = os.listdir(os.getenv('LOCALAPPDATA') + '\RivalsofAether\Replays')
        kindanewfilelist = []
        for anyfile in filelist:
            if anyfile[-4:] == '.roa':
                kindanewfilelist.append(anyfile)
        newfilelist = []
        count = 0
        kindanewfilelist = kindanewfilelist[-v.get():]
        for replay in kindanewfilelist:
            count += 1
            newfilelist.append([replay, count])
        for i in newfilelist:
            i[1] = (len(newfilelist) - i[1]) + 1
        playerlist = [[],[]]
        for replay, gamecount in newfilelist:
            f = open(os.getenv('LOCALAPPDATA') + "\RivalsofAether\Replays\\" + replay, 'r')#.readlines()
            '''player1 = ''                               small brain solution thats broken
            player2 = ''
            filteredlist = []
            for i in f:
                if i[0] == 'H':
                    filteredlist.append(i[1:])
                if i[0] == 'H':
                    filteredlist.append(i[1:])

            for char in filteredlist[0]:
                player1 += char
                if char == ' ':
                    spaceflag += 1
                if char != ' ':
                    spaceflag = 0
                if spaceflag == 5:
                    player1 = player1[:-5]
                    spaceflag = 0
                    flag = True
                    break
            for char in filteredlist[1]:
                player2 += char
                if char == ' ':
                    spaceflag += 1
                if char != ' ':
                    spaceflag = 0
                if spaceflag == 5:
                    player2 = player2[:-5]
                    spaceflag = 0
                    break

            print(player1)


            big brain solution
            '''
            f.seek(0)
            fileread = f.read()
            f.seek(0)
            f.close()
            readflag = False
            player1 = ''
            player2 = ''
            player1done = False
            spaceflag = 0

            for char in range(len(fileread)):
                if readflag == True:
                    if player1done == False:
                        player1 += fileread[char]

                        if fileread[char] == ' ':
                            spaceflag += 1
                        if fileread[char] != ' ':
                            spaceflag = 0
                        if spaceflag == 5:
                            player1 = player1[:-5]
                            remove_punctuation_map = dict((ord(char), None) for char in '\/*?:"<>|')
                            player1 = player1.translate(remove_punctuation_map)
                            readflag = False
                            player1done = True
                            spaceflag = 0
                    else:
                        player2 += fileread[char]
                        if fileread[char] == ' ':
                            spaceflag += 1
                        if fileread[char] != ' ':
                            spaceflag = 0
                        if spaceflag == 5:
                            player2 = player2[:-5]
                            remove_punctuation_map = dict((ord(char), None) for char in '\/*?:"<>|')
                            player2 = player2.translate(remove_punctuation_map)
                            break
                if fileread[char] == 'H' and fileread[char-1] == '\n':
                    readflag = True
            playerlist[0].append(player1)
            playerlist[1].append(player2)
        if (len(playerlist[0]) == 1 and len(playerlist[1]) == 1):
            manimaginebeingabletocodecompetently = 0
        elif len(set(playerlist[0])) > 1 or len(set(playerlist[1])) > 1:
            global errorplayerlabel
            errorplayerlabel = Label(root, text = 'Error: Matches are not a full set', fg = 'red')
            errorplayerlabel.place(x=115,y=250)
            root.after(2000, errorplayer)
            return
        try:
            os.makedirs(directory + '\\' + newfilelist[0][0][:10] + ' ' + player1 + ' v.s. ' + player2)
        except FileExistsError:
            #wait if this just passes it works? idk
            pass
            # global errorfilelabel
            # errorfilelabel = Label(root, text = 'Error: Folder already exists', fg = 'red')
            # errorfilelabel.place(x=115,y=250)
            # root.after(2000, errorfile)
        for replay, gamecount in newfilelist:
            shutil.copy2(os.getenv('LOCALAPPDATA') + "\RivalsofAether\Replays\\" + replay, directory + '\\' + newfilelist[0][0][:10] + ' ' + player1 + ' v.s. ' + player2 + '\\' + player1 + " v.s. " + player2 + ' Game ' + str(gamecount) + '.roa')
        shutil.make_archive(directory + '\\' + newfilelist[0][0][:10] + ' ' + player1 + ' v.s. ' + player2, 'zip', directory + '\\' + newfilelist[0][0][:10] + ' ' + player1 + ' v.s. ' + player2)
        global successlabel
        successlabel = Label(root, text = 'Success!', fg = 'green')
        successlabel.place(x=205,y=250)
        root.after(2000, success)
def save():
    if not os.path.exists(changedestinationentry.get()):
        global errorsavedlabel
        errorsavedlabel = Label(root, text = 'Error: Path Invalid', fg = 'red')
        errorsavedlabel.place(x=205, y=35)
        root.after(2000, errorsaved)
        return
    f = open('config', 'w')
    f.write(changedestinationentry.get())
    f.seek(0)
    f.close()
    global savedlabel
    savedlabel = Label(root, text = 'Saved!', fg = 'green')
    savedlabel.place(x=255, y=35)
    root.after(2000, saved)



root = Tk()
Button(text="Default", command = default).place(x=345,y=35)
Button(text="Save", command = save).place(x=305,y=35)
Button(text="Browse", command = browse).place(x=400,y=35)
changedestination = Label(root, text='Change destination folder: ')
changedestination.place(x=10,y=10)
changedestinationentry = Entry(root, width = 45)
changedestinationentry.place(x=160, y=10)
Label(root, text = 'Number of matches:').place(x=175, y=75)
MODES = [
('1', 1, 50),
('2', 2, 125),
('3', 3, 200),
('4', 4, 275),
('5', 5, 350)
]
v = IntVar()

for text, mode, xvar in MODES:
    Radiobutton(root, text=text, variable=v, value = mode, width = 8, indicatoron = False).place(x=xvar, y=100)
bigfont = Font(size=24)
startbutton = Button(text='START', command=start, height = 2, width = 14, font = bigfont)
startbutton.place(x=100, y=150)
Label(root, text='By CheesyPotato (PM at CheesyPotato#5378 for bugs/suggestions)').place(x=85,y=280)

f = open('config', 'r')
if f.read() == 'DEFAULT':
    f.seek(0)
    if not os.path.exists(os.path.expanduser(r"~\Desktop\Rivals Replays")):
        os.makedirs(os.path.expanduser(r"~\Desktop\Rivals Replays"))
    changedestinationentry.insert(0, os.path.expanduser("~\Desktop\Rivals Replays"))
else:
    f.seek(0)
    changedestinationentry.insert(0, f.read())
f.close()
root.geometry("450x300")
root.title("Rivals Replay Organizer GUI")
root.iconbitmap("kragg icon.ico")
root.mainloop()
