from tkinter import *
from tkinter import ttk
from tkinter import StringVar, messagebox


root = Tk()
root.geometry('500x600')
root.title('Length Converter')
root.configure(bg = '#993399')



def answer():
    
    num1 = num_from.get()
    Unit_from = Unit_frm.get()
    Unit_to = Unit_too.get()
    try:
        number1 = float(num1)
    except:
        messagebox.showerror('Error','Term not recognised!') 

    # Length
    if Unit_from == 'Kilometer' and Unit_to == 'Kilometer':
        calculate = number1
        result.cget('text')
        result.configure(text = (f"{calculate:,}", "km")) 
    

    elif Unit_from == 'Kilometer' and Unit_to == 'Meter':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (f"{calculate:,}","m"))

    elif Unit_from == 'Kilometer' and Unit_to == 'Centimeter':
        calculate = number1*100000
        result.cget('text')
        result.configure(text = (f"{calculate:,}","cm"))

    elif Unit_from == 'Kilometer' and Unit_to == 'Foot':
        calculate = number1*3280.839895
        result.cget('text')
        result.configure(text = (f"{calculate:,}","ft"))

    elif Unit_from == 'Kilometer' and Unit_to == 'Inch':
        calculate = number1*39370.07874 
        result.cget('text')
        result.configure(text = (f"{calculate:,}","in"))

    elif Unit_from == 'Meter' and Unit_to == 'Meter':
        calculate = number1
        result.cget('text')
        result.configure(text = (f"{calculate:,}","m"))

    elif Unit_from == 'Meter' and Unit_to == 'Kilometer':
        calculate = number1*0.001
        result.cget('text')
        result.configure(text = (f"{calculate:,}","km"))

    elif Unit_from == 'Meter' and Unit_to == 'Centimeter':
        calculate = number1*100
        result.cget('text')
        result.configure(text = (f"{calculate:,}","cm"))

    elif Unit_from == 'Meter' and Unit_to == 'Foot':
        calculate = number1*3.28084
        result.cget('text')
        result.configure(text = (f"{calculate:,}","ft"))

    elif Unit_from == 'Meter' and Unit_to == 'Inch':
        calculate = number1*39.370079
        result.cget('text')
        result.configure(text = (f"{calculate:,}","in"))

    elif Unit_from == 'Centimeter' and Unit_to == 'Centimeter':
        calculate = number1
        result.cget('text')
        result.configure(text = (f"{calculate:,}","cm"))

    elif Unit_from == 'Centimeter' and Unit_to == 'Kilometer':
        calculate = number1*0.00001
        result.cget('text')
        result.configure(text = (f"{calculate:,}","km"))

    elif Unit_from == 'Centimeter' and Unit_to == 'Meter':
        calculate = number1*0.01
        result.cget('text')
        result.configure(text = (f"{calculate:,}","m"))

    elif Unit_from == 'Centimeter' and Unit_to == 'Foot':
        calculate = number1*0.032808
        result.cget('text')
        result.configure(text = (f"{calculate:,}","ft"))
    
    elif Unit_from == 'Centimeter' and Unit_to == 'Inch':
        calculate = number1*0.393701
        result.cget('text')
        result.configure(text = (f"{calculate:,}","in"))

    elif Unit_from == 'Foot' and Unit_to == 'Foot':
        calculate = number1
        result.cget('text')
        result.configure(text = (f"{calculate:,}","ft"))

    elif Unit_from == 'Foot' and Unit_to == 'Kilometer':
        calculate = number1*0.000305
        result.cget('text')
        result.configure(text = (f"{calculate:,}","km"))

    elif Unit_from == 'Foot' and Unit_to == 'Meter':
        calculate = number1*0.3048
        result.cget('text')
        result.configure(text = (f"{calculate:,}","m"))

    elif Unit_from == 'Foot' and Unit_to == 'Centimeter':
        calculate = number1*30.48
        result.cget('text')
        result.configure(text = (f"{calculate:,}","cm"))

    elif Unit_from == 'Foot' and Unit_to == 'Inch':
        calculate = number1*12
        result.cget('text')
        result.configure(text = (f"{calculate:,}","in"))

    elif Unit_from == 'Inch' and Unit_to == 'Inch':
        calculate = number1
        result.cget('text')
        result.configure(text = (f"{calculate:,}","in"))

    elif Unit_from == 'Inch' and Unit_to == 'Kilometer':
        calculate = number1*0.0000254
        result.cget('text')
        result.configure(text = (f"{calculate:,}","km"))
    
    elif Unit_from == 'Inch' and Unit_to == 'Meter':
        calculate = number1*0.0254
        result.cget('text')
        result.configure(text = (f"{calculate:,}","m"))

    elif Unit_from == 'Inch' and Unit_to == 'Centimeter':
        calculate = number1*2.54
        result.cget('text')
        result.configure(text = (f"{calculate:,}","cm"))

    elif Unit_from == 'Inch' and Unit_to == 'Foot':
        calculate = number1*0.083333
        result.cget('text')
        result.configure(text = (f"{calculate:,}","ft"))

    

# Creating the num_from entry label
title_lbl = Label(root,text = 'Length Converter ', fg = 'white', bg='#993399', font=("Courier", 20))
# label_from['font'] = font2
title_lbl.place(relx = '0.25',rely = '0.1')

# Creating the num_from entry label
label_num_from = Label(root,text = 'Value ',bg = '#df9fdf', fg = 'black')
# label_from['font'] = font2
label_num_from.place(relx = '0.15',rely = '0.25')


# Creating the num_from entry
num_from = Entry(root,width = '56')
num_from.place(relx = '0.15',rely = '0.29', height=40)


# Creating the unit label
label_unit = Label(root,text = 'Unit ',bg = '#df9fdf', fg = 'white')
label_unit.place(relx = '0.15',rely = '0.37', width = 40.5)

unit = ttk.Combobox(root, width = '45', values= ['Length'])
unit.place(relx = '0.238', rely = '0.37')
unit.current(0)




# Creating the from label
label_from = Label(root,text = 'From ',bg = '#df9fdf', fg = 'white')
label_from.place(relx = '0.15',rely = '0.42', width = 40)

# Creating the unit to convert from box
f = StringVar()
Unit_frm = ttk.Combobox(root, width = 15, textvariable = f)
Unit_frm['values'] = ('Kilometer',
                      'Meter',
                      'Centimeter',
                      'Foot',
                      'Inch')

Unit_frm.place(relx = '0.238',rely = '0.42')
Unit_frm.current(0)



# Creating the To label
to = Label(root,text = 'To   ',bg = '#df9fdf', fg = 'white')
to.place(relx = '0.5',rely = '0.42', width = 40)

# Creating the unit to convert to box
t = StringVar()
Unit_too = ttk.Combobox(root,width = 16, textvariable = t)
Unit_too['values'] = ('Kilometer',
                      'Meter',
                      'Centimeter',
                      'Foot',
                      'Inch')

Unit_too.place(relx = '0.59',rely = '0.42')
Unit_too.current(0)



# Creating the result label
result = Label(root,text = '', width = 30, font=1)
result.place(relx = '0.2',rely = '0.62',height=30)


# Creating the get answer button
get_answer = Button(root,
                    text = 'Convert',
                    bg = '#660066',
                    command = answer,
                    fg = 'white'
                    )

get_answer.place(relx = '0.36',rely = '0.7', width=100, height=30
)

root.mainloop()



