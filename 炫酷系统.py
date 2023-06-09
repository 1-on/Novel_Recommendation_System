import requests
import parsel
import tkinter
import tkinter.messagebox
import webbrowser
import sqlite3

# url_1 = 'http://www.cits0871.com/sort/xuanhuan/'
# response_1 = requests.get(url_1)
# selector_1 = parsel.Selector(response_1.text)
# xuanhuanRank = selector_1.css('.s2 a ::text').getall()  # 玄幻小说排名
# xuanhuanRankLink = selector_1.css('.s2 a::attr(href)').getall()
# xuanhuanDic = {}
# for i in range(len(xuanhuanRankLink)):
#     xuanhuanDic[xuanhuanRank[i]] = 'http://www.cits0871.com' + xuanhuanRankLink[i]
#
# url_2 = 'http://www.cits0871.com/sort/xiuzhen/'
# response_2 = requests.get(url_2)
# selector_2 = parsel.Selector(response_2.text)
# xiuzhenRank = selector_2.css('.s2 a ::text').getall()  # 修真小说排名
# xiuzhenRankLink = selector_2.css('.s2 a ::attr(href)').getall()
# xiuzhenDic = {}
# for i in range(len(xiuzhenRankLink)):
#     xiuzhenDic[xiuzhenRank[i]] = 'http://www.cits0871.com' + xiuzhenRankLink[i]
#
# url_3 = 'http://www.cits0871.com/sort/dushi/'
# response_3 = requests.get(url_3)
# selector_3 = parsel.Selector(response_3.text)
# dushiRank = selector_3.css('.s2 a ::text').getall()  # 都市小说排名
# dushiRankLink = selector_3.css('.s2 a::attr(href)').getall()
# dushiDic = {}
# for i in range(len(dushiRankLink)):
#     dushiDic[dushiRank[i]] = 'http://www.cits0871.com' + dushiRankLink[i]
#
# url_4 = 'http://www.cits0871.com/sort/lishi/'
# response_4 = requests.get(url_4)
# selector_4 = parsel.Selector(response_4.text)
# lishiRank = selector_4.css('.s2 a::text').getall()  # 穿越小说排名
# lishiRankLink = selector_4.css('.s2 a ::attr(href)').getall()
# lishiDic = {}
# for i in range(len(lishiRankLink)):
#     lishiDic[lishiRank[i]] = 'http://www.cits0871.com' + lishiRankLink[i]
#
# url_5 = 'http://www.cits0871.com/sort/wangyou/'
# response_5 = requests.get(url_5)
# selector_5 = parsel.Selector(response_5.text)
# wangyouRank = selector_5.css('.s2 a::text').getall()  # 网游小说排名
# wangyouRankLink = selector_5.css('.s2 a ::attr(href)').getall()
# wangyouDic = {}
# for i in range(len(wangyouRankLink)):
#     wangyouDic[wangyouRank[i]] = 'http://www.cits0871.com' + wangyouRankLink[i]
#
# url_6 = 'http://www.cits0871.com/sort/kehuan/'
# response_6 = requests.get(url_6)
# selector_6 = parsel.Selector(response_6.text)
# kehuanRank = selector_6.css('.s2 a::text').getall()  # 科幻小说排名
# kehuanRankLink = selector_6.css('.s2 a ::attr(href)').getall()
# kehuanDic = {}
# for i in range(len(kehuanRankLink)):
#     kehuanDic[kehuanRank[i]] = 'http://www.cits0871.com' + kehuanRankLink[i]
#
# url_7 = 'http://www.cits0871.com/wanben/sort/'
# response_7 = requests.get(url_7)
# selector_7 = parsel.Selector(response_7.text)
# wanbenRank = selector_7.css('.s2 a::text').getall()  # 完本小说
# wanbenRankLink = selector_7.css('.s2 a ::attr(href)').getall()
# wanbenDic = {}
# for i in range(len(wanbenRankLink)):
#     wanbenDic[wanbenRank[i]] = 'http://www.cits0871.com' + wanbenRankLink[i]

# dict1 = {'玄幻小说': xuanhuanDic, '修真小说': xiuzhenDic, '都市小说': dushiDic, '穿越小说': lishiDic,
#          '网游小说': wangyouDic, '科幻小说': kehuanDic, '完本小说': wanbenDic}
# dict2 = {'玄幻小说': xuanhuanRank, '修真小说': xiuzhenRank, '都市小说': dushiRank, '穿越小说': lishiRank,
#          '网游小说': wangyouRank, '科幻小说': kehuanRank, '完本小说': wanbenRank}
# print(dict1)

dict1 = {'玄幻小说': "玄幻", '修真小说': "修真", '都市小说': '都市', '穿越小说': '穿越',
         '网游小说': "网游", '科幻小说': "科幻", '完本小说': "完本"}

dict2 = {'玄幻小说': "玄幻", '修真小说': "修真", '都市小说': '都市', '穿越小说': '穿越',
         '网游小说': "网游", '科幻小说': "科幻", '完本小说': "完本"}

print(dict1)

win = tkinter.Tk()
win.title('小说推荐系统')
win.geometry('500x300')


def show():
    index1 = ListB.curselection()

    def webopen():
        index2 = Listc.curselection()
        webbrowser.open(dict1[ListB.get(index1)][Listc.get(index2)])

    def add():
        index3 = Listc.curselection()

        def addfavor(name, novellink):
            f.execute('insert into novel values(?,?)', (name, novellink))

        addfavor(dict2[ListB.get(index1)][index3[0]], dict1[ListB.get(index1)][Listc.get(index3)])
        winadd = tkinter.Toplevel()
        winadd.title('提示框')
        winadd.geometry('200x200')
        ladd = tkinter.Label(winadd, text='添加成功', font=('华文行楷', 15))
        ladd.place(relx=0.5, rely=0.4, anchor='center')

    win2 = tkinter.Toplevel()
    win2.title('小说推荐系统')
    win2.geometry('500x300')
    l2 = tkinter.Label(win, text='请选择你喜欢的小说类型', font=('华文行楷', 15))
    l2.place(relx=0.5, rely=0.23, anchor='center')
    Listc = tkinter.Listbox(win2)
    Listc.place(relx=0.3, rely=0.3, anchor='nw', width=200, height=100)
    for item in dict1[ListB.get(index1)]:
        Listc.insert("end", item)
    yscrollbar = tkinter.Scrollbar(Listc, command=Listc.yview)
    yscrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    Listc.config(yscrollcommand=yscrollbar.set)
    c = tkinter.Button(win2, text='确定', width=5, height=1, bg='gray', command=lambda: webopen())
    c.place(relx=0.3, rely=0.75, anchor='sw')
    e = tkinter.Button(win2, text='加入收藏', width=7, height=1, bg='gray', command=lambda: add())
    e.place(relx=0.6, rely=0.75, anchor='sw')


l = tkinter.Label(win, text='欢迎进入小说推荐系统', font=('华文行楷', 20), fg='green')
l.place(relx=0.5, rely=0.1, anchor='center')

l2 = tkinter.Label(win, text='请选择你喜欢的小说类型', font=('华文行楷', 15))
l2.place(relx=0.5, rely=0.23, anchor='center')

ListB = tkinter.Listbox(win)
ListB.place(relx=0.3, rely=0.3, anchor='nw', width=200, height=100)
for item in dict1:
    ListB.insert("end", item)

yscrollbar = tkinter.Scrollbar(ListB, command=ListB.yview)
yscrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
ListB.config(yscrollcommand=yscrollbar.set)

b = tkinter.Button(win, text='确定', width=5, height=1, bg='gray', command=lambda: show())
b.place(relx=0.3, rely=0.75, anchor='sw')

d = tkinter.Button(win, text='我的书架', width=7, height=1, bg='gray', command=lambda: bookshelf())
d.place(relx=0.6, rely=0.75, anchor='sw')

conn = sqlite3.connect('info.db')
f = conn.cursor()


# f.execute("create table novel(name char(10), novellink char(100))")

def serch():
    f.execute('select * from novel')
    li = f.fetchall()
    print(li)
    return li


def bookshelf():
    win3 = tkinter.Toplevel()
    win3.title('我的书架')
    win3.geometry('500x300')
    ListD = tkinter.Listbox(win3)
    ListD.place(relx=0.3, rely=0.3, anchor='nw', width=200, height=100)
    li1 = serch()
    for i in li1:
        ListD.insert('end', i[0])
    yscrollbar = tkinter.Scrollbar(ListD, command=ListD.yview)
    yscrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    ListD.config(yscrollcommand=yscrollbar.set)

    def enter():
        index4 = ListD.curselection()
        webbrowser.open(li1[index4[0]][1])

    enterbutton = tkinter.Button(win3, text='进入小说', width=7, height=1, bg='gray', command=lambda: enter())
    enterbutton.place(relx=0.3, rely=0.75, anchor='sw')


win.mainloop()
conn.commit()
conn.close()
