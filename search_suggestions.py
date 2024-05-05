import tkinter as tk
import pyodbc

try:
    cnxn = pyodbc.connect("Driver={SQL Server};"
                          "Server=DESKTOP-EHVKD7M;"
                          "Database=student;"
                          "Trusted_Connection=yes;")
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM Suggestions')
    suggestions = []
    for row in cursor:
        # Process each cell in the row to remove brackets and commas
        cleaned_row = [str(cell).replace('{', '').replace('}', '').replace(',', '') for cell in row]
        for i in cleaned_row:
            suggestions.append(i)
except pyodbc.Error as e:
    print("Database connection error:", e)
    

def update_listbox(data):
    my_list.delete(0, tk.END)
    if data:
        for item in data:
            my_list.insert(tk.END, item)
    else:
        my_list.insert(tk.END, "No suggestions found")

def fillout(e):
    my_entry.delete(0, tk.END)
    selected_item = my_list.get(tk.ACTIVE)
    if selected_item != "No suggestions found":
        my_entry.insert(0, selected_item)

def check(e):
    typed = my_entry.get().lower()  # Convert typed text to lowercase for case-insensitive matching
    if typed == '':
        data = suggestions
    else:
        data = [row for row in suggestions if typed in row.join(map(str,row)).lower()]
    update_listbox(data)

root = tk.Tk()
root.title('Search Suggestions')
root.geometry('500x300')

my_label = tk.Label(root, text='Start Typing..', font=('Helvetica', 14), fg='grey')
my_label.pack(pady=20)

my_entry = tk.Entry(root, font=('Helvetica', 20))
my_entry.pack()

my_list = tk.Listbox(root, width=50)
my_list.pack(pady=40)

update_listbox(suggestions)

my_list.bind('<<ListboxSelect>>', fillout)
my_entry.bind('<KeyRelease>', check)

root.mainloop()
