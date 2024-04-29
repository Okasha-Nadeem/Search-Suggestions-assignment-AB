from tkinter import *

root = Tk()
root.title('Search Suggestions')

root.geometry('500x300')

def update(data):
    my_list.delete(0,END)
    for item in data:
        my_list.insert(END, item)
def fillout(e):
    my_entry.delete(0,END)
    my_entry.insert(0,my_list.get(ACTIVE))

def check(e):
    typed = my_entry.get()

    if typed == '':
        data = suggestions
    else:
        data = []
        for item in suggestions:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)

my_label = Label(root, text='Start Typing..',font=('Helvetica',14),fg='grey')
my_label.pack(pady=20)

my_entry = Entry(root,font=('Helvetica',20))
my_entry.pack()

my_list = Listbox(root,width=50)
my_list.pack(pady=40)

suggestions = ['Zain noob','Okasha','Huraira','Mustafa','Sherry','Abudl rehman','affan bhai'
               ,'behari','Coding','Dog','Eifel Tower','fishing','greetings','Impossible ways to die']

update(suggestions)

my_list.bind('<<ListboxSelect>>',fillout)

my_entry.bind('<KeyRelease>',check)

root.mainloop()
