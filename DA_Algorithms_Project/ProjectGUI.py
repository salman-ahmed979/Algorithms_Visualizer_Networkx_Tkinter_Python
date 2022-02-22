from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from AlgoProject import GraphRunnerAlgorithm

win = Tk()
win.title("Graphs Visualization")
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)

# Label

fileLabel = Label(win, text="Select file")
fileLabel.place(x=30, y=30)

algoLabel = Label(win, text="Select Algorithm")
algoLabel.place(x=30, y=90)

# FileComboBox
fileSelection = StringVar()

fileComboBox = ttk.Combobox(win, width=25, textvariable=fileSelection)
fileComboBox['state'] = 'readonly'
fileComboBox['values'] = ('input10.txt', 'input20.txt', 'input30.txt', 'input40.txt', 'input50.txt', 'input60.txt', 'input70.txt', 'input80.txt', 'input90.txt', 'input100.txt')
fileComboBox.place(x=150, y=30)


# AlgorithmsComboBox
algoSelection = StringVar()

algoComboBox = ttk.Combobox(win, width=25, textvariable=algoSelection)
algoComboBox['state'] = 'readonly'
algoComboBox['values'] = ('Prims', 'Kruskal', 'Dijsktra', 'BellmanFord', 'FloydWarshall', 'Boruvka', 'ClusteringCoefficient')
algoComboBox.place(x=150, y=90)

# Controller Function
def runAlgo():
    if algoSelection.get() == '' or fileSelection.get() == '':
        messagebox.showerror('Error', 'Fill all Fields')
    else:
        GraphRunnerAlgorithm(fileSelection.get(), algoSelection.get())

# Button
btn = Button(win, text="Show Graph", bg='lightblue', command=runAlgo)
btn.place(x=150, y=150)

win.mainloop()