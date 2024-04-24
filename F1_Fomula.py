import tkinter as tk
from tkinter import ttk
import  openpyxl
import  pandas as pd
import test as t
from PIL import  Image,ImageTk
class F1_Fomula:
    def __init__(self):
        self.root = tk.Toplevel()
        self.style = ttk.Style(self.root)
        self.root.title('Đăng ký thi đấu')
        # self.root.tk.call('source', 'forest-light.tcl')
        # self.root.tk.call('source', 'forest-dark.tcl')
        # self.style.theme_use('forest-light')

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        listChangDua = list(t.csvChangDua['Race'])
        listDoiDua = list(t.csvDoiDua['RacingTeam'])



        ############# phan 1 ###############
        self.widgets_frame = ttk.LabelFrame(self.frame, text='Chọn chặng đua')
        self.widgets_frame.grid(row=0, column=0, padx=20, pady=10)

        self.name_ChangDua = ttk.Combobox(self.widgets_frame, values=listChangDua)  ####################################
        self.name_ChangDua.current(0)
        self.name_ChangDua.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.ngay_dua_data = t.csvChangDua.loc[t.csvChangDua['Race'] == self.name_ChangDua.get(), 'Time']
        self.ngay_dua_data = self.ngay_dua_data.to_string(index=False)
        self.ngayDua = ttk.Entry(self.widgets_frame)  ##########################################
        self.ngayDua.insert(0, self.ngay_dua_data)
        self.ngayDua.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.button = ttk.Button(self.widgets_frame, text='Xác nhận', command=self.displayDangKyThiDau)
        self.button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        ########## phan 2 #####################
        self.widgets_frame2 = ttk.LabelFrame(self.frame, text='            ')
        # widgets_frame2.grid(row=0,column=1, padx=20, pady=10)

        self.labelDoiDua = ttk.Label(self.widgets_frame2, text='Đội đua')
        self.labelDoiDua.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.name_DoiDua = ttk.Combobox(self.widgets_frame2, values=listDoiDua)  ########################
        self.name_DoiDua.current(0)
        self.name_DoiDua.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        self.butDoiDua = ttk.Button(self.widgets_frame2, text='Xác nhận', command=self.comTayDua)  ##############
        self.butDoiDua.grid(row=0, column=2, sticky='ew', padx=5, pady=5)

        self.labelTayDua = ttk.LabelFrame(self.widgets_frame2, text='Tay đua')
        self.labelTayDua.grid(row=2, column=0, columnspan=2, padx=20, pady=10) #------------------

        tay_dua_data = t.csvDoiDua.loc[t.csvDoiDua['RacingTeam'] == self.name_DoiDua.get(), 'Racer']
        tay_dua_data = tay_dua_data.to_string(index=False)
        tay_dua_data = tay_dua_data.split(',')
        tay_dua_data = [string.strip() for string in tay_dua_data]

        self.boxTayDua = ttk.Combobox(self.widgets_frame2, values=tay_dua_data)  ##########################
        self.boxTayDua.current(0)
        self.boxTayDua.grid(row=2, column=2, padx=5, pady=5, sticky='ew')

        self.label1 = ttk.Label(self.labelTayDua, text='    ')
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        self.label2 = ttk.Label(self.labelTayDua, text='    ')
        self.label2.grid(row=0, column=1, padx=20, pady=10)

        #------------------------------------#

        self.label1_rank = ttk.Label(self.labelTayDua, text='Xếp hạng')
        self.label1_rank.grid(row=1, column=0, padx=20, pady=10)
        self.label2_rank = ttk.Label(self.labelTayDua, text='Xếp hạng')
        self.label2_rank.grid(row=1, column=1, padx=20, pady=10)

        self.label1_diem = ttk.Label(self.labelTayDua, text='Điểm số')
        self.label1_diem.grid(row=2, column=0, padx=20, pady=10)
        self.label2_diem = ttk.Label(self.labelTayDua, text='Điểm số')
        self.label2_diem.grid(row=2, column=1, padx=20, pady=10)

        self.label1_so = ttk.Label(self.labelTayDua, text='Số xe')
        self.label1_so.grid(row=3, column=0, padx=20, pady=10)
        self.label2_so = ttk.Label(self.labelTayDua, text='Số xe')
        self.label2_so.grid(row=3, column=1, padx=20, pady=10)

        #------------------------------------#

        self.butDangKy = ttk.Button(self.widgets_frame2, text='Đăng ký', command=self.insert_row)
        self.butDangKy.grid(row=3, column=2, padx=5, pady=5, sticky='ew')

        self.treeFrame = ttk.Frame(self.frame)
        self.treeFrame.grid(row=0, column=3, pady=10)
        self.treeScroll = ttk.Scrollbar(self.treeFrame)
        self.treeScroll.pack(side='right', fill='y')

        cols = ("ChangDua", "DoiDua", "TayDua", "NgayDua")
        self.treeview = ttk.Treeview(self.treeFrame, show='headings',
                                yscrollcommand=self.treeScroll.set, columns=cols, height=13)
        self.treeview.column('ChangDua', width=100)
        self.treeview.column('DoiDua', width=100)
        self.treeview.column('TayDua', width=100)
        self.treeview.column('NgayDua', width=100)

        self.treeview.pack()
        self.treeScroll.config(command=self.treeview.yview())
        self.load_data()



    def load_data(self):
        path = 'C://Users//ADMIN//PycharmProjects//GUI_csv//tkinter-excel-app//LichThiDau.xlsx'
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active

        list_value = list(sheet.values)
        # print(list_value)
        for col_name in list_value[0]:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in list_value[1:]:
            self.treeview.insert('', tk.END, values=value_tuple)

    def insert_row(self):
        self.changdua = self.name_ChangDua.get()
        self.ngaydua = self.ngayDua.get()
        self.doidua = self.name_DoiDua.get()
        self.taydua = self.boxTayDua.get()

        print((self.changdua, self.ngaydua, self.doidua, self.taydua))

        path = 'C://Users//ADMIN//PycharmProjects//GUI_csv//tkinter-excel-app//LichThiDau.xlsx'
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        row_values = [self.changdua, self.doidua, self.taydua, self.ngaydua]

        sheet.append(row_values)
        workbook.save(path)

        self.treeview.insert('', tk.END, values=row_values)

    def displayDangKyThiDau(self):
        self.widgets_frame2.grid(row=0, column=1, padx=20, pady=10)
        self.widgets_frame2.config(text=self.name_ChangDua.get())

        ngay_dua_data = t.csvChangDua.loc[t.csvChangDua['Race'] == self.name_ChangDua.get(), 'Time']
        ngay_dua_data = ngay_dua_data.to_string(index=False)
        self.ngayDua.delete(0, 'end')
        self.ngayDua.insert(0, ngay_dua_data)  #########################################

    def comTayDua(self):
        tay_dua_data = t.csvDoiDua.loc[t.csvDoiDua['RacingTeam'] == self.name_DoiDua.get(), 'Racer']
        tay_dua_data = tay_dua_data.to_string(index=False)
        tay_dua_data = tay_dua_data.split(',')
        tay_dua_data = [string.strip() for string in tay_dua_data]
        self.label1.config(text=tay_dua_data[0])
        self.label2.config(text=tay_dua_data[1])
        self.boxTayDua.set(tay_dua_data[0])
        self.boxTayDua.config(values=tay_dua_data)

        df = pd.read_csv('C://Users//ADMIN//PycharmProjects//GUI_csv//tkinter-excel-app//BXH.csv')
        other_columns_values1 = df.loc[df['TayDua'] == tay_dua_data[0], ['Rank', 'Diem', 'SoXe']]
        first_row_values1 = other_columns_values1.iloc[0].tolist()
        self.label1_rank.config(text='Xếp hạng: '+str(first_row_values1[0]))
        self.label1_diem.config(text='Điểm số: '+ str(first_row_values1[1]))
        self.label1_so.config(text='Số xe: '+ str(first_row_values1[2]))

        other_columns_values2 = df.loc[df['TayDua'] == tay_dua_data[1], ['Rank', 'Diem', 'SoXe']]
        first_row_values2 = other_columns_values2.iloc[0].tolist()
        self.label2_rank.config(text='Xếp hạng: '+str(first_row_values2[0]))
        self.label2_diem.config(text='Điểm số: '+str(first_row_values2[1]))
        self.label2_so.config(text='Số xe: '+str(first_row_values2[2]))


    # csvChangDua = pd.read_csv('C://Users//ADMIN//PycharmProjects//GUI_csv//tkinter-excel-app//ChangDua.csv')


    # root.geometry('1200x741+100+25')
