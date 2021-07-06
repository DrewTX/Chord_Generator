from tkinter import *
from tkinter.ttk import *

def chordGen(note,mode):
    notesList = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    custNotesList = []
    for i in notesList[notesList.index(note):]:
        custNotesList.append(i)
    for i in notesList[:notesList.index(note)]:
        custNotesList.append(i)
    modeChords = []
    #Ionian - W W H W W W H
    if mode == 'Ionian':
        ionian = [0,2,4,5,7,9,11]
        ionianChords = ['Maj','min','min','Maj','Maj','min','dim']
        n = 0
        for i in ionian:
            modeChords.append(custNotesList[i])
            modeChords[n] = modeChords[n] + ionianChords[n]
            n+=1
    #Dorian - W H W W W H W
    if mode == 'Dorian':
        dorian = [0,2,3,5,7,9,10]
        dorianChords = ['min','min','Maj','Maj','min','dim','Maj']
        n = 0
        for i in dorian:
            modeChords.append(custNotesList[i])
            modeChords[n] = modeChords[n] + dorianChords[n]
            n+=1
    #Phrygian - H W W W H W W
    if mode == 'Phrygian':
        phrygian = [0,1,3,5,7,8,10]
        phrygianChords = ['min','Maj','Maj','min','dim','Maj','min']
        n = 0
        for i in phrygian:
            modeChords.append(custNotesList[i])
            modeChords[n] = modeChords[n] + phrygianChords[n]
            n+=1
    #Lydian - W W W H W W H
    if mode == 'Lydian':
        lydian = [0,2,4,6,7,9,11]
        lydianChords = ['Maj','Maj','min','dim','Maj','min','min']
        n = 0
        for i in lydian:
            modeChords.append(custNotesList[i])
            modeChords[n] = modeChords[n] + lydianChords[n]
            n+=1
    #Mixolydian - W W H W W H W
    if mode == 'Mixolydian':
        mixolydian = [0,2,4,5,7,9,10]
        mixolydianChords = ['Maj','min','dim','Maj','min','min','Maj']
        n = 0
        for i in mixolydian:
            modeChords.append(custNotesList[i])
            modeChords[n] = modeChords[n] + mixolydianChords[n]
            n+=1
    #Aeolian - W H W W H W W
    if mode == 'Aeolian':
        aeolian = [0,2,3,5,7,8,10]
        aeolianChords = ['min','dim','Maj','min','min','Maj','Maj']
        n = 0
        for i in aeolian:
            modeChords.append(custNotesList[i])
            modeChords[n] = modeChords[n] + aeolianChords[n]
            n+=1
    #Locrian - H W W H W W W
    if mode == 'Locrian':
        locrian = [0,1,3,5,6,8,10]
        locrianChords = ['dim','Maj','min','min','Maj','Maj','min']
        n = 0
        for i in locrian:
            modeChords.append(custNotesList[i])
            modeChords[n] = modeChords[n] + locrianChords[n]
            n+=1
    return modeChords

def popOutputLbl():
    if notesCombo.get() and modesCombo.get():
        outputLbl.configure(text=chordGen(notesCombo.get(),modesCombo.get()))
        chord1Combo.configure(state="readonly")
        chord2Combo.configure(state="readonly")
        chord3Combo.configure(state="readonly")
        chord4Combo.configure(state="readonly")
        chord1Combo.set("")
        chord2Combo.set("")
        chord3Combo.set("")
        chord4Combo.set("")
        chord1Lbl.configure(text="")
        chord2Lbl.configure(text="")
        chord3Lbl.configure(text="")
        chord4Lbl.configure(text="")
        instructionsLbl2.configure(foreground="Black")
        chordProgBtn.configure(state="normal")

def popChordNbrLbl():
    chordNbrDict = {'I':0,'II':1,'III':2,'IV':3,'V':4,'VI':5,'VII':6}
    if chord1Combo.get() in chordNbrDict.keys():
        chord1Lbl.configure(text=chordGen(notesCombo.get(),modesCombo.get())[chordNbrDict[chord1Combo.get()]])
    if chord2Combo.get() in chordNbrDict.keys():
        chord2Lbl.configure(text=chordGen(notesCombo.get(),modesCombo.get())[chordNbrDict[chord2Combo.get()]])
    if chord3Combo.get() in chordNbrDict.keys():
        chord3Lbl.configure(text=chordGen(notesCombo.get(),modesCombo.get())[chordNbrDict[chord3Combo.get()]])
    if chord4Combo.get() in chordNbrDict.keys():
        chord4Lbl.configure(text=chordGen(notesCombo.get(),modesCombo.get())[chordNbrDict[chord4Combo.get()]])
    chordProgClearBtn.configure(state="normal")

def clearChordProg():
    chord1Combo.set("")
    chord2Combo.set("")
    chord3Combo.set("")
    chord4Combo.set("")
    chord1Lbl.configure(text="")
    chord2Lbl.configure(text="")
    chord3Lbl.configure(text="")
    chord4Lbl.configure(text="")
    chordProgClearBtn.configure(state="disabled")

#-------------
#-----GUI-----
#-------------

#Window config.
window = Tk()
window.title("Chord Generator")

#Instruction label
instructionsLbl = Label(window, text="Select a key:")
instructionsLbl.grid(column=0, row=0)

#Notes drop-down list
notesCombo = Combobox(window, state="readonly", width=12)
notesCombo['values']= ('C','C#','D','D#','E','F','F#','G','G#','A','A#','B')
notesCombo.grid(column=0, row=1)
notesCombo.set("")

#Modes drop-down list
modesCombo = Combobox(window, state="readonly", width=12)
modesCombo['values']= ('Ionian','Dorian','Phrygian','Lydian','Mixolydian','Aeolian','Locrian')
modesCombo.grid(column=0, row=2, padx=5, pady=8)
modesCombo.set("")

#Generate scale button
genBtn = Button(window, text="Generate Chords", command=popOutputLbl)
genBtn.grid(column=1, row=1, padx=5)

#Output chords label
outputLbl = Label(window, width=50, background="light gray", foreground="dark blue",anchor=CENTER)
outputLbl.grid(column=1, row=2, sticky=E,padx=5)

#Instruction label 2
instructionsLbl2 = Label(window, text="Select a progression:", width=24, anchor=CENTER, foreground="Gray")
instructionsLbl2.grid(column=0, row=4)

#Chord 1 drop-down list
chord1Combo = Combobox(window, state="disabled", width=8)
chord1Combo['values']= ('I','II','III','IV','V','VI','VII')
chord1Combo.grid(column=0, row=5, sticky=W, padx=5)
chord1Combo.set("")

#Chord 2 drop-down list
chord2Combo = Combobox(window, state="disabled", width=8)
chord2Combo['values']= ('I','II','III','IV','V','VI','VII')
chord2Combo.grid(column=1, row=5, sticky=W)
chord2Combo.set("")

#Chord 1 label
chord1Lbl = Label(window, width=11, background="light gray", foreground="dark blue", anchor=CENTER)
chord1Lbl.grid(column=0, row=6, sticky=W, padx=5, pady=5)

#Chord 2 label
chord2Lbl = Label(window, width=11, background="light gray", foreground="dark blue", anchor=CENTER)
chord2Lbl.grid(column=1, row=6, sticky=W)

#Chord 3 drop-down list
chord3Combo = Combobox(window, state="disabled", width=8)
chord3Combo['values']= ('I','II','III','IV','V','VI','VII')
chord3Combo.grid(column=0, row=7, sticky=W, padx=5)
chord3Combo.set("")

#Chord 4 drop-down list
chord4Combo = Combobox(window, state="disabled", width=8)
chord4Combo['values']= ('I','II','III','IV','V','VI','VII')
chord4Combo.grid(column=1, row=7, sticky=W)
chord4Combo.set("")

#Chord 3 label
chord3Lbl = Label(window, width=11, background="light gray", foreground="dark blue", anchor=CENTER)
chord3Lbl.grid(column=0, row=8, sticky=W, padx=5, pady=7)

#Chord 4 label
chord4Lbl = Label(window, width=11, background="light gray", foreground="dark blue", anchor=CENTER)
chord4Lbl.grid(column=1, row=8, sticky=W)

#Chord progression button
chordProgBtn = Button(window, state="disabled", text="Generate Progression", command=popChordNbrLbl)
chordProgBtn.grid(column=1, row=5, padx=5)

#Chord progression clear button
chordProgClearBtn = Button(window, state="disabled", text="Clear Progression", command=clearChordProg)
chordProgClearBtn.grid(column=1, row=6, padx=5)
