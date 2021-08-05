from tkinter import *


class Jalil:
	# -----------------------نافذة البرنامج-------------
	def __init__(self, calc):
		self.calc = calc
		self.calc.geometry('800x173+1+1')
		self.calc.configure(bg='#b4b0b0')
		self.calc.resizable(False, False)
		self.calc.title('ألة حاسبة')
		tile = Label(self.calc, text='<<<Dumb Casio FX-1ES Plus>>> by Abdeljalil', bg='orange', font=('Liquid Crystal', 14, 'bold'), fg='#eeeeee')
		tile.pack(fill=X)
		# ------------------ المتغيرات-----------------
		self.var_x = DoubleVar()
		self.var_y = DoubleVar()
		# ----- الفريمات وبرمجة الادخال والاخراج ---------
		frame_btn = Frame(self.calc, bg='#FFC300')
		frame_btn.place(x=588, y=25, width=210, height=145)
		frame_entry = Frame(self.calc, bg='#fefefe')
		frame_entry.place(x=2, y=25, width=210, height=145)
		frame_result = Frame(self.calc, bg='#DAF7A6')
		frame_result.place(x=214, y=25, width=373, height=145)
		first_value = Label(frame_entry, text='A value:', bg='#abfc9e', font=('', 19, 'bold'), fg='black')
		first_value.pack(side='top', fill='x')
		first_entry = Entry(frame_entry, textvariable=self.var_x, bd='5', bg='black', font=('', 9), justify='center', fg='orange')
		first_entry.pack(side='top', fill='x')
		second_entry = Entry(frame_entry, textvariable=self.var_y, bd='5', bg='black', font=('', 9), justify='center', fg='orange')
		second_entry.pack(side='bottom', fill='x')
		second_value = Label(frame_entry, text='B value:', bg='#a6f1e1', font=('', 19, 'bold'), fg='black')
		second_value.pack(side='bottom', fill='x')
		result_label2 = Label(frame_result, text='', bg='#DAF7A6', font=('', 18, 'bold'))
		result_label2.pack(side='top', fill='x')
		result_label = Label(frame_result, text='=', bg='#DAF7A6', font=('', 18, 'bold'))
		result_label.pack(side='top', fill='x')
		help_label = Label(frame_result, text='<<Enter A value and B Value, then press a Calculations button>>', bg='#DAF7A6', font=('', 8,))
		help_label.pack(side='bottom', fill='x')
		# ------------- برمجة العمليات الحسابية-------------

		def calp():
			x = self.var_x.get()
			y = self.var_y.get()
			result_label.config(text=x + y)
			result_label2.config(text='A   +   B   =')

		def calm():
			x = self.var_x.get()
			y = self.var_y.get()
			result_label.config(text=x - y)
			result_label2.config(text='A   -   B   =')

		def cals():
			x = self.var_x.get()
			y = self.var_y.get()
			result_label.config(text=x * y)
			result_label2.config(text='A   *   B   =')

		def cald():
			x = self.var_x.get()
			y = self.var_y.get()
			result_label.config(text=x / y)
			result_label2.config(text='A   /   B   =')

		# ------------- برمجة أزار العمليات الحسابية ------------
		btnp = Button(frame_btn, text='+', font=('', 9, 'bold'), command=calp,)
		btnp.pack(side='top', fill='x')
		btnm = Button(frame_btn, text='-', font=('', 9, 'bold'), command=calm)
		btnm.pack(side='top', fill='x')
		btnd = Button(frame_btn, text='/', font=('', 9, 'bold'), command=cald)
		btnd.pack(side='top', fill='x')
		btns = Button(frame_btn, text='*', font=('', 9, 'bold'), command=cals)
		btns.pack(side='top', fill='x')
		btnexit = Button(frame_btn, text='exit', bg='red', font=('', 9, 'bold'), command=exit)
		btnexit.pack(side='top', fill='x')


root = Tk()
ob = Jalil(root)
root.mainloop()
