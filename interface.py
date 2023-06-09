import tkinter
import csv
import recommend3
import webbrowser

win = tkinter.Tk()
win.title('小说推荐系统')
win.geometry('1000x600')

novel_dict = {}
novel_url = {}

with open('novels1.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        novel_url[row['小说名称']] = row['小说URL']
        novel_name = row['小说名称']
        novel_type = row['小说类型']
        if novel_type not in novel_dict:
            novel_dict[novel_type] = []
        novel_dict[novel_type].append(novel_name)

# for category, novels in novel_dict.items():
#     print(category + ':')
#     print(novels)

l = tkinter.Label(win, text='欢迎进入小说推荐系统', font=('华文行楷', 20), fg='green')
l.place(relx=0.5, rely=0.1, anchor='center')

l2 = tkinter.Label(win, text='选择小说类型', font=('华文行楷', 15))
l2.place(relx=0.5, rely=0.23, anchor='center')

l3 = tkinter.Label(win, text='根据最近的历史记录推荐的小说', font=('华文行楷', 15))
l3.place(relx=0.2, rely=0.23, anchor='center')

ListA = tkinter.Listbox(win)
ListA.place(relx=0.1, rely=0.3, anchor='nw', width=200, height=200)
for item in recommend3.recommendations.index:
    ListA.insert("end", item)

ListB = tkinter.Listbox(win)
ListB.place(relx=0.4, rely=0.3, anchor='nw', width=200, height=200)
for item in novel_dict:
    ListB.insert("end", item)


def show():
    index1 = ListB.curselection()
    for item in index1:
        print(ListB.get(item))

    ListC = tkinter.Listbox(win)
    ListC.place(relx=0.7, rely=0.3, anchor='nw', width=200, height=200)
    yscrollbar = tkinter.Scrollbar(ListC, command=ListC.yview)
    yscrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    ListC.config(yscrollcommand=yscrollbar.set)
    for item in novel_dict[ListB.get(index1[0])]:
        ListC.insert("end", item)

    c = tkinter.Button(win, text='确定', width=5, height=1, bg='gray', command=lambda: show2())
    c.place(relx=0.7, rely=0.75, anchor='sw')

    def show2():
        index2 = ListC.curselection()
        book_name = ListC.get((index2[0]))
        url = novel_url[novel_name]
        print(book_name)
        print(url)
        with open('history.csv', mode='a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([book_name])
        webbrowser.open(url)


b = tkinter.Button(win, text='确定', width=5, height=1, bg='gray', command=lambda: show())
b.place(relx=0.4, rely=0.75, anchor='sw')

win.mainloop()
