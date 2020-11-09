import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm
import stats_calculator as sc
import json

main_win = tk.Tk()
main_win.title('ポケモン実数値計算')
main_win.geometry('500x500')


label1 = tk.Label(text='ポケモン名 : ')
label1.place(x=100, y=140)

entry1 = tk.Entry(width=21)
entry1.place(x=400, y=140)

label2 = tk.Label(text='(種族値) : ')
label2.place(x=100, y=400)

entry2h = tk.Entry(width=4)
entry2h.place(x=320, y=400)

entry2a = tk.Entry(width=4)
entry2a.place(x=430, y=400)

entry2b = tk.Entry(width=4)
entry2b.place(x=540, y=400)

entry2c = tk.Entry(width=4)
entry2c.place(x=650, y=400)

entry2d = tk.Entry(width=4)
entry2d.place(x=760, y=400)

entry2s = tk.Entry(width=4)
entry2s.place(x=870, y=400)


label3 = tk.Label(text='Lv : ')
label3.place(x=100, y=560)

entry3 = tk.Entry(width=4)
entry3.place(x=205, y=560)
entry3.insert(0,'50')

label4 = tk.Label(text='性格 : ')
label4.place(x=380, y=560)

listarray = list(json.load(open('./data/nature_data.json', 'r')))
txt = tk.StringVar()
entry4 = ttk.Combobox(width=16, height=10, value=listarray, textvariable=txt)
entry4.place(x=530, y=560)

label5 = tk.Label(text='個体値 : ')
label5.place(x=100, y=660)

entry5h = tk.Entry(width=3)
entry5h.place(x=300, y=660)
entry5h.insert(0,31)

entry5a = tk.Entry(width=3)
entry5a.place(x=400, y=660)
entry5a.insert(0,31)

entry5b = tk.Entry(width=3)
entry5b.place(x=500, y=660)
entry5b.insert(0,31)

entry5c = tk.Entry(width=3)
entry5c.place(x=600, y=660)
entry5c.insert(0,31)

entry5d = tk.Entry(width=3)
entry5d.place(x=700, y=660)
entry5d.insert(0,31)

entry5s = tk.Entry(width=3)
entry5s.place(x=800, y=660)
entry5s.insert(0,31)


label6 = tk.Label(text='努力値 : ')
label6.place(x=100, y=760)

entry6h = tk.Entry(width=3)
entry6h.place(x=300, y=760)
entry6h.insert(0,0)

entry6a = tk.Entry(width=3)
entry6a.place(x=400, y=760)
entry6a.insert(0,0)

entry6b = tk.Entry(width=3)
entry6b.place(x=500, y=760)
entry6b.insert(0,0)

entry6c = tk.Entry(width=3)
entry6c.place(x=600, y=760)
entry6c.insert(0,0)

entry6d = tk.Entry(width=3)
entry6d.place(x=700, y=760)
entry6d.insert(0,0)

entry6s = tk.Entry(width=3)
entry6s.place(x=800, y=760)
entry6s.insert(0,0)


label7 = tk.Label(text='計算結果 : ')
label7.place(x=100, y=1030)

entry7 = tk.Entry(width=23)
entry7.place(x=350, y=1030)


def bsget():
	pokemon_name = entry1.get()
	bs = sc.Bsfind(pokemon_name)
	entry2h.delete(first=0, last=100)
	entry2a.delete(first=0, last=100)
	entry2b.delete(first=0, last=100)
	entry2c.delete(first=0, last=100)
	entry2d.delete(first=0, last=100)
	entry2s.delete(first=0, last=100)
	entry2h.insert(0,bs[0])
	entry2a.insert(0,bs[1])
	entry2b.insert(0,bs[2])
	entry2c.insert(0,bs[3])
	entry2d.insert(0,bs[4])
	entry2s.insert(0,bs[5])


def calculate():
	bs = [int(entry2h.get()),int(entry2a.get()),int(entry2b.get()),int(entry2c.get()),int(entry2d.get()),int(entry2s.get())]
	strnt = str(entry4.get())
	striv = [entry5h.get(),entry5a.get(),entry5b.get(),entry5c.get(),entry5d.get(),entry5s.get()]
	ev = [int(entry6h.get()),int(entry6a.get()),int(entry6b.get()),int(entry6c.get()),int(entry6d.get()),int(entry6s.get())]
	
	if not (bool(bs) and bool(strnt) and bool(ev)):
		tkm.showinfo('info', '必要な値が抜けています')
	
	else:
		iv = [int(s) for s in striv]
		lv = int(str(entry3.get()))
		nt = sc.Ntfind(strnt)
		
		if not bool(nt):
			tkm.showinfo('info','性格名が間違っています')
			
		else:
			st = sc.stats_calculate(bs, iv, ev, lv, nt)
			entry7.delete(first=0, last=100)
			entry7.insert(0,'{}-{}-{}-{}-{}-{}'.format(st[0],st[1],st[2],st[3],st[4],st[5]))


button1 = tk.Button(text='確定', command=bsget)
button1.place(x=760, y=240)

button2 = tk.Button(text='計算', command=calculate)
button2.place(x=760, y=880)



main_win.mainloop()