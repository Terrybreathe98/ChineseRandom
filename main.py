import tkinter as tk
from random import randint
import json
import demjson
import codecs
import datetime
import re

hitStatus = False

#def readJson(fileName):
#    with codecs.open(fileName,'r','utf-8') as data:
#        dataDic = demjson.decode(data)
#        return dataDic

#def writeJson(dataDic,fileName):
#    with codecs.open(fileName, 'w', 'utf-8') as f:
#        f=demjson.encode(dataDic)

#def getDate():
#    date=datetime.date.today()
#    year=date.year
#    month=date.month
#    day=date.day
#    formedDate=year+"/"+month+"/"+day
#    return formedDate

#def decodeDate(formedDate):
#    reDate=re.findall(r"\d+",formedData)
#    year=reDate[0]
#    month=reDate[1]
#    day=reDate[2]
#    return year,month,day

def getNum():
    #dataDic=readJson("data.json")
    #DATE = datetime.date.today()
    #for i in range(len(dataDic.keys())):
    #    date=dataDic[i]["date"]
    #    year,month,day=decodeDate(date)
    #    if year==DATE.year and month==DATE.month and day==DATE.day:
    #        numli=dataDic[i]["num"]
    #        ord=i
    #        break
    #else:
    #    numli=[]
    #    dataDic[len(dataDic.keys())]={
    #        "date":getDate(),
    #        "num":numli
    #    }


    while True:
        num = randint(1, 53)
        if num != 47 and (num not in numli):
            numli.append(num)
            #升级时记得删
            #print(numli)
            #dataDic[ord]["num"]=numli
            #writeJson(dataDic,"data.json")
            return num

def display():
    global out
    val=getNum()
    out.delete('1.0','end')
    out.insert('end',val)

if __name__ == "__main__":
    win = tk.Tk()
    win.title("语文课抽学号v1.0")
    win.geometry("1000x500")

    ti = tk.Label(win,
                  text="抽学号",
                  font=("Microsoft JhengHei", 40),
                  width=24,
                  height=2)
    ti.pack()

    # 升级时记得删
    numli = []

    # txt = tk.StringVar()
    # no = tk.Label(win,
    #              textvariable=txt,
    #              font=("Microsoft JhengHei", 20),
    #              width=15,
    #              height=2)
    # no.pack()

    out = tk.Text(
        win,
        height=2,
        width=30
    )
    #out.tag_config('font',font=("STKaiti", 15))
    out.pack()

    warn = tk.Label(
        win,
        text="抽学号到51次后程序有概率会死掉，重启下就好(不过应该也不会有人抽51吧...)",
        height=2,
        width=100
    )
    #warn.place(x=10,y=40)
    warn.pack(side="bottom")

    choose = tk.Button(win,
                       text="生死有命，富贵在天",
                       font=("STKaiti", 15),
                       width=20,
                       height=2,
                       command=display)
    choose.pack()

    win.mainloop()
