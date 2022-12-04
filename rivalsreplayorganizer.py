from tkinter import *
import os
from tkinter.font import Font
import shutil
from tkinter.filedialog import askdirectory
from functools import partial
__version__ = '1.0.2'


'''
Dear person reading the code (imagine?),
sorry its a mess i just want to get it finished, maybe ill finish later







'''


def savereplay(match):
    player1butdifferent = match[0]
    player2butdifferent = match[1]
    matchbutdifferent = match[2:]
    newfilelist = []
    count = 0

    directoryplayer1 = player1butdifferent.replace('.', '')
    directoryplayer2 = player2butdifferent.replace('.', '')

    for replaybutdifferent in matchbutdifferent:
        count += 1
        newfilelist.append([replaybutdifferent, count])
    try:
        date = newfilelist[0][0][:10]
        date = date[5:9] + date[9:] + '-' + date[0:4]
        os.makedirs(directory + '\\' + date + ' ' +
                    directoryplayer1 + ' v.s. ' + directoryplayer2)
    except FileExistsError:
        # wait if this just passes it works? idk
        pass

    for replay, gamecount in newfilelist:
        shutil.copy2(os.getenv('LOCALAPPDATA') + "\RivalsofAether\Replays\\" + replay, directory + '\\' + date + ' ' + directoryplayer1 +
                     ' v.s. ' + directoryplayer2 + '\\' + player1butdifferent + " v.s. " + player2butdifferent + ' Game ' + str(gamecount) + '.roa')
        shutil.make_archive(directory + '\\' + date + ' ' + directoryplayer1 + ' v.s. ' + directoryplayer2,
                            'zip', directory + '\\' + date + ' ' + directoryplayer1 + ' v.s. ' + directoryplayer2)
    shutil.move(directory + '\\' + date + ' ' + directoryplayer1 + ' v.s. ' + directoryplayer2 + '.zip', directory + '\\' + date + ' ' +
                directoryplayer1 + ' v.s. ' + directoryplayer2 + '\\' + date + ' ' + directoryplayer1 + ' v.s. ' + directoryplayer2 + '.zip')


def main():
    global frame
    frame = Frame(root, width=390, height=160)
    frame.place(x=10, y=100)
    canvas = Canvas(frame, bg='#FFFFFF', width=440, height=160)
    global directory
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
    playerlist = [[], []]
    masterlist = []
    for replay in filelist:
        if replay[-4:] == '.roa':
            f = open(os.getenv('LOCALAPPDATA') + "\RivalsofAether\Replays\\" +
                     replay, 'r', encoding='utf-8')  # .readlines()

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
                            remove_punctuation_map = dict(
                                (ord(char), None) for char in '\/*?:"<>|')
                            realplayer1 = player1
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
                            remove_punctuation_map = dict(
                                (ord(char), None) for char in '\/*?:"<>|')
                            realplayer2 = player2
                            player2 = player2.translate(remove_punctuation_map)
                            break
                if fileread[char] == 'H' and fileread[char-1] == '\n':
                    readflag = True
            masterlist.append([replay, player1, player2])
            if (len(playerlist[0]) == 1 and len(playerlist[1]) == 1):
                manimaginebeingabletocodecompetently = 0
            elif len(set(playerlist[0])) > 1 or len(set(playerlist[1])) > 1:

                break
    global masterlist2
    masterlist2 = []
    for item in masterlist:
        if item == masterlist[0]:
            masterlist2.append([item[1], item[2], item[0]])
        elif item[1] == previousitem[1] and item[2] == previousitem[2]:
            masterlist2[-1].append(item[0])
        else:
            masterlist2.append([item[1], item[2], item[0]])
        previousitem = item

    masterlist2 = masterlist2[::-1]

    couriernew = Font(font='TkDefaultFont')
    for match in masterlist2:
        player1length = couriernew.measure(match[0])
        player2length = couriernew.measure(match[1])
        datelength = couriernew.measure(match[2][:10])
        textlength = max([player1length, player2length, datelength])
        if masterlist2.index(match) == 0:
            previouslength = 0
        canvas.create_rectangle(10+previouslength, 10,
                                10+previouslength+textlength+5, 75)
        canvas.create_text(12 + previouslength, 16, text=match[0], anchor=NW)
        canvas.create_text((10 + previouslength + 10 +
                           previouslength + textlength)/2, 28, text='v.s.', anchor=N)
        canvas.create_text(12 + previouslength, 40, text=match[1], anchor=NW)
        date = match[2][:10]
        date = date[5:9] + date[9:] + '-' + date[0:4]
        canvas.create_text(12 + previouslength, 52, text=date, anchor=NW)
        tkinterisdumb = partial(savereplay, match)
        button = Button(root, command=tkinterisdumb, text='Save Replay')
        canvas.create_window(12 + previouslength, 80, window=button, anchor=NW,
                             width=10+previouslength+textlength+5 - 10 - previouslength - 2)
        previouslength = 10+previouslength+textlength
    global hbar
    hbar = Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=TOP, fill=X)
    hbar.config(command=canvas.xview)

    canvas.config(xscrollcommand=hbar.set)
    canvas.pack(side=LEFT, expand=True, fill=BOTH)
    canvas.config(scrollregion=canvas.bbox(ALL))


def refresh():
    frame.place_forget()
    main()


def saveall():
    for i in masterlist2:
        savereplay(i)


''' doesnt work with win32gui cxfreeze :( use separate file
def update():



    soup = BeautifulSoup(requests.get('https://github.com/CheesyPotato/Rivals-Replay-Organizer/releases/latest').text, 'html5lib')
    downloadzipfile = 'https://github.com'+soup.find_all('li', {'class': 'd-block py-2'})[0].a['href']

    if downloadzipfile[-9:-4] == __version__:
        global savedlabel
        savedlabel = Label(root, text = 'Already current version!', fg = 'green')
        savedlabel.place(x=305, y=65)
        root.after(5000, saved)
        return

    response = requests.get(downloadzipfile, stream=True)
    tempdirectory = os.getcwd()
    os.chdir(os.path.dirname(os.getcwd()))



    with open("Rivals Replay Organizer " + downloadzipfile[-9:], "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    zip_ref = zipfile.ZipFile(os.getcwd() + '\\Rivals Replay Organizer ' + downloadzipfile[-9:-4] + '.zip', 'r')
    zip_ref.extractall(os.getcwd())
    zip_ref.close()
    os.remove(os.getcwd() + '\\Rivals Replay Organizer ' + downloadzipfile[-9:])
    os.chdir(tempdirectory)
    global donelabel
    donelabel = Label(root, text = 'Done! (Check directory above current install)', fg = 'green')
    donelabel.place(x=200, y=65)
    root.after(5000, done)
    return'''


def numbercheck(numberinput):
    if numberinput == '':
        return True
    try:
        int(numberinput)
        return True
    except ValueError:
        return False


def browse():
    choosedirectory = askdirectory(
        initialdir=os.path.expanduser(r"~\\Desktop"), )
    changedestinationentry.delete(0, END)
    changedestinationentry.insert(0, choosedirectory)
    save()


def done():
    donelabel.destroy()


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


def errorupdate():
    errorupdatelabel.destroy()


def success():
    successlabel.destroy()


def default():
    if not os.path.exists(os.path.expanduser(r"~\\Desktop\\Rivals Replays")):
        os.makedirs(os.path.expanduser(r"~\Desktop\Rivals Replays"))
    changedestinationentry.delete(0, END)
    changedestinationentry.insert(
        0, os.path.expanduser(r"~\Desktop\Rivals Replays"))
    save()


def start():
    '''if not numbercheck(matchentry.get()):
        global errormatchlabel
        errormatchlabel = Label(root, text = 'Error: Select how many matches you played', fg = 'red')
        errormatchlabel.place(x=115,y=250)
        root.after(2000, errormatch)'''
    # else:
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
    '''kindanewfilelist = []
    for anyfile in filelist:
        if anyfile[-4:] == '.roa':
            kindanewfilelist.append(anyfile)
    newfilelist = []
    count = 0
    kindanewfilelist = kindanewfilelist[-(int(matchentry.get())):]
    for replay in kindanewfilelist:
        count += 1
        newfilelist.append([replay, count])
    for i in newfilelist:
        i[1] = (len(newfilelist) - i[1]) + 1'''
    playerlist = [[], []]
    masterlist = []
    for replay in filelist:
        f = open(os.getenv('LOCALAPPDATA') +
                 "\RivalsofAether\Replays\\" + replay, 'r')  # .readlines()
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
                        remove_punctuation_map = dict(
                            (ord(char), None) for char in '\/*?:"<>|')
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
                        remove_punctuation_map = dict(
                            (ord(char), None) for char in '\/*?:"<>|')
                        player2 = player2.translate(remove_punctuation_map)
                        break
            if fileread[char] == 'H' and fileread[char-1] == '\n':
                readflag = True
        masterlist.append([replay, player1, player2])

    '''
    if (len(playerlist[0]) == 1 and len(playerlist[1]) == 1):
        manimaginebeingabletocodecompetently = 0
    elif len(set(playerlist[0])) > 1 or len(set(playerlist[1])) > 1:
        global errorplayerlabel
        errorplayerlabel = Label(root, text = 'Error: Matches are not a full set', fg = 'red')
        errorplayerlabel.place(x=115,y=250)
        root.after(2000, errorplayer)
        return

    directoryplayer1 = player1.replace('.', '')
    directoryplayer2 = player2.replace('.', '')'''
    try:

        os.makedirs(directory + '\\' + newfilelist[0][0][:10] +
                    ' ' + directoryplayer1 + ' v.s. ' + directoryplayer2)
    except FileExistsError:
        # wait if this just passes it works? idk
        pass
        # global errorfilelabel
        # errorfilelabel = Label(root, text = 'Error: Folder already exists', fg = 'red')
        # errorfilelabel.place(x=115,y=250)
        # root.after(2000, errorfile)
    for replay, gamecount in newfilelist:
        shutil.copy2(os.getenv('LOCALAPPDATA') + "\RivalsofAether\Replays\\" + replay, directory + '\\' +
                     newfilelist[0][0][:10] + ' ' + directoryplayer1 + ' v.s. ' + directoryplayer2 + '\\' + player1 + " v.s. " + player2 + ' Game ' + str(gamecount) + '.roa')
    shutil.make_archive(directory + '\\' + newfilelist[0][0][:10] + ' ' + directoryplayer1 + ' v.s. ' + directoryplayer2,
                        'zip', directory + '\\' + newfilelist[0][0][:10] + ' ' + directoryplayer1 + ' v.s. ' + directoryplayer2)
    global successlabel
    successlabel = Label(root, text='Success!', fg='green')
    successlabel.place(x=205, y=250)
    root.after(2000, success)


def save():
    if not os.path.exists(changedestinationentry.get()):
        global errorsavedlabel
        errorsavedlabel = Label(root, text='Error: Path Invalid', fg='red')
        errorsavedlabel.place(x=205, y=35)
        root.after(2000, errorsaved)
        return
    f = open('config', 'w')
    f.write(changedestinationentry.get())
    f.seek(0)
    f.close()
    global savedlabel
    savedlabel = Label(root, text='Saved!', fg='green')
    savedlabel.place(x=305, y=65)
    root.after(2000, saved)


chardict = {
    '01': 'Random',
    '02': 'Zetterburn',
    '03': 'Orcane',
    '04': 'Wrastor',
    '05': 'Kragg',
    '06': 'Forsburn',
    '07': 'Maypul',
    '08': 'Absa',
    '09': 'Etalus',
    '10': 'Ori and Sein',
    '11': 'Ranno',
    '12': 'Clairen',
    '13': 'Sylvanos',
    '14': 'Elliana'
}

stagedict = {
    '00': 'Random',
    '01': 'Treetop Lodge',
    '02': 'Fire Capitol',
    '03': 'Air Armada',
    '04': 'Rock Wall',
    '05': 'Merchant Port',
    '07': 'Blazing Hideout',
    '08': 'Tower of Heaven',
    '09': 'Tempest Peak',
    '10': 'Frozen Fortress',
    '11': 'Aethereal Gates',
    '12': 'The Endless Abyss',
    '14': 'The Ceo Ring',
    '15': 'Spirit Tree',
    '17': 'Neo Fire Capitol',
    '18': 'Swampy Estuary'
}
root = Tk()
Button(text="Default", command=default).place(x=345, y=35)
Button(text="Save", command=save).place(x=305, y=35)
Button(text="Browse", command=browse).place(x=400, y=35)
changedestination = Label(root, text='Change destination folder: ')
changedestination.place(x=10, y=10)
changedestinationentry = Entry(root, width=45)
changedestinationentry.place(x=160, y=10)
#Label(root, text = 'Number of matches:').place(x=175, y=75)
Label(text='To update: \n run "update.exe"',
      height=4, width=12).place(x=18, y=33)
Button(text='Refresh', command=refresh, height=3, width=10).place(x=110, y=35)
Button(text='Save All', command=saveall, height=3, width=10).place(x=200, y=35)

'''
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


vcmd = (root.register(numbercheck))
matchentry = Entry(root, width = 5, validate='key', validatecommand=(vcmd, '%P'))
matchentry.place(x=215, y=100)
bigfont = Font(size=24)
startbutton = Button(text='START', command=start, height = 2, width = 14, font = bigfont)
startbutton.place(x=100, y=150)'''


Label(root, text='By CheesyPotato (PM at CheesyPotato#5378 for bugs/suggestions)').place(x=85, y=280)

f = open('config', 'r')
if f.read() == 'DEFAULT':
    f.seek(0)
    if not os.path.exists(os.path.expanduser(r"~\Desktop\Rivals Replays")):
        os.makedirs(os.path.expanduser(r"~\Desktop\Rivals Replays"))
    changedestinationentry.insert(
        0, os.path.expanduser("~\Desktop\Rivals Replays"))
else:
    f.seek(0)
    changedestinationentry.insert(0, f.read())
f.close()
root.geometry("450x300")
root.title("Rivals Replay Organizer GUI")
root.iconbitmap("kragg icon.ico")


main()


root.mainloop()
