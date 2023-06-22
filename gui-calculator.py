from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = Tk()
root.title("Wykresy")
root.geometry("1000x650")
root.resizable(0,0)

expression = ""

def press(item):
    """
    when the button with item is pressed enters the input field

    arguments:
    item -- string
    """
    global expression
    expression = expression + str(item)
    equation.set(expression)
    
def make_graph():
    """
    makes an empty graph
    """
    fr_plot = Frame(root)
    fr_plot.grid(row=3, column=8, sticky=N+S, rowspan=20)
    figure1 = plt.figure(figsize=(5,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    plt.xlabel('x')  
    plt.ylabel('y')
    canvas = FigureCanvasTkAgg(figure1, fr_plot)
    canvas.get_tk_widget().pack(fill=BOTH)

make_graph()

def clear():
    """
    clears the main input field, the graph, max values and min values
    """
    global expression
    expression = ""
    equation.set("")
    make_graph()
    x_min_val.delete(0, END)
    x_max_val.delete(0, END)
    y_min_val.delete(0, END)
    y_max_val.delete(0, END)

equation = StringVar()

label0 = Label(root, text='\t').grid(row=0,column=0)
headlabel = Label(root, text='Graphs', font=(30)).grid(row=1,column=2)
label0 = Label(root, text='\t').grid(row=2,column=0)
mainlabel = Label(root, text='y: ').grid(row=3, column=0)
expression_field = Entry(root, textvariable=equation).grid(column=1, row=3, columnspan=4, 
                            ipadx=68)

symbols_math = {'\u03C0': 'np.pi', 'e': 'np.e', 'ln' : 'np.log', '^' : '**', 'sin' : 'np.sin', 'cos' : 'np.cos', 
                    'ctg' : '1/np.tan', 'tg' : 'np.tan'}
symbols = ['1','2','3','4','5','6','7','8','9','0','(', ')', '+', '-', '*', '/', '.', ',', 'x', 'abs']
symbols = symbols+(list(symbols_math.keys()))

button_dict = {}
label0 = Label(root, text='\t').grid(row=3,column=6)
for j in range(len(symbols)):
    button_dict[symbols[j]]=Button(root, text=symbols[j], fg='white', bg='black',
                    command=lambda j=j: press(symbols[j]), height=1, 
                    width=7).grid(row=int(j/4)+6, column=int(j%4)+1)

label0 = Label(root, text='\t').grid(row=13,column=0)
clear_button = Button(root, text='clear', fg='white', bg='dark red',
                    command=lambda: clear(), height=1, 
                    width=7).grid(row=14, column=2)

label0 = Label(root, text='\t').grid(row=0,column=7)
label0 = Label(root, text='\t').grid(row=0,column=8)

row1=16
label0 = Label(root, text='\t').grid(column=0, row=row1)
x_min_label = Label(root, text='xmin: ').grid(column=1, row=row1+1)
x_min_val = Entry(root, width=13)
x_min_val.grid(column=2, row = row1+1, sticky=W, columnspan=2)
x_max_label = Label(root, text='xmax: ').grid(column=1, row=row1+2)
x_max_val = Entry(root, width=13)
x_max_val.grid(column=2, row = row1+2, sticky=W, columnspan=2) 
y_min_label = Label(root, text='ymin: ').grid(column=1, row=row1+3)
y_min_val = Entry(root, width=13)
y_min_val.grid(column=2, row = row1+3, sticky=W, columnspan=2) 
y_max_label = Label(root, text='ymax: ').grid(column=1, row=row1+4)
y_max_val = Entry(root, width=13)
y_max_val.grid(column=2, row = row1+4, sticky=W, columnspan=2) 

legend_val = IntVar()
label0 = Label(root, text='\t').grid(column=0, row=row1+5)
legend_button = Checkbutton(root, text='legenda', variable=legend_val, 
                                onvalue=1, offvalue=0).grid(column=3, row=row1+6, columnspan=2)

fr_plot = Frame(root)
fr_plot.grid(row=3, column=8, sticky=N+S, rowspan=20)

def math_plot():
    """
    function takes an expression from main input field and makes a graph based on it
    """
    global expression
    functions_1 = expression.split(',')
    for key, value in symbols_math.items():
            expression = expression.replace(key, value)
    functions = expression.split(',')
    xmin = int(x_min_val.get())
    xmax = int(x_max_val.get())
    ymin = int(y_min_val.get())
    ymax = int(y_max_val.get())
    fr_plot = Frame(root)
    fr_plot.grid(row=3, column=8, sticky=N+S, rowspan=20)
    figure1 = plt.figure(figsize=(5,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([xmin,xmax,ymin,ymax])
    canvas = FigureCanvasTkAgg(figure1, fr_plot)
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
    i=0
    for function in functions:
        xs = np.linspace(xmin, xmax, (xmax-xmin)*10)
        ys = [eval(function) for x in xs]
        ax1.plot(xs,ys, label=f'{functions_1[i]}')
        i=i+1
    if legend_val.get() == 1:
        plt.legend()

label0 = Label(root, text='\t').grid(row=13,column=0)
plot_button = Button(root, text='graph', fg='white', bg='dark red',
                    command=lambda: [math_plot()], height=1, 
                    width=7).grid(row=14, column=3)

root.mainloop()