import tkinter as tk
from tkinter import ttk
import  openpyxl
import  pandas as pd
import test as t
import  F1_Fomula as ss
from PIL import  Image,ImageTk
from openpyxl import load_workbook
from collections import defaultdict
from tkinter import messagebox


class DangKyThiDau:
    def __init__(self,root):
        self.master = root
        self.master.title('Trang chủ giải đấu')
        self.master.geometry('800x600+150+150')

        # self.style = ttk.Style(self.master)
        # self.master.tk.call('source', 'forest-light.tcl')
        # self.master.tk.call('source', 'forest-dark.tcl')
        # self.style.theme_use('forest-light')

        self.frametop = tk.Frame(self.master, bg='#ff1e00', height=200)
        self.frametop.pack(fill=tk.X)
        self.sms = tk.Label(self.frametop, text='F1 Fomula', bg='#ff1e00', fg='white', font=('tahoma', 30), pady=20)
        self.sms.grid(row=0,column=0)
        self.imgF = Image.open('Images/F1-logo.jpg')
        self.imgF.thumbnail((200, 200))
        self.new_imgF = ImageTk.PhotoImage(self.imgF)

        self.logo = tk.Label(self.frametop, image= self.new_imgF)
        self.logo.grid(row=0,column=1)

        self.frametop.grid_columnconfigure(0, weight=1)
        self.frametop.grid_columnconfigure(1, weight=1)
        ###### Frame Top End ###########

        ###### Frame Center Start Here ###########
        self.centerFrame = tk.Frame(self.master, height=200)
        self.centerFrame.pack(fill=tk.X)
        ###### Frame Center End Here ###########

        ###### Frame Dang ky thi dau ###########
        self.dangKyThiDau = tk.Frame(self.centerFrame, pady=100, padx=100)
        self.dangKyThiDau.grid(row=0, column=0)

        self.img = Image.open('Images/pngegg (1).png')
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)

        self.imgdangKyThiDau = tk.Label(self.dangKyThiDau, image=self.new_img)
        self.imgdangKyThiDau.pack()
        self.butdangKyThiDau = tk.Button(self.dangKyThiDau, text='Đăng ký thi đấu', bg='#e10600', fg='white', padx=5
                                      , pady=5,command= self.comDangKyThiDau)
        self.butdangKyThiDau.pack(pady=20)

        ###### Frame Thong tin giai dau ###########
        self.thongTinGiaiDau = tk.Frame(self.centerFrame, pady=100, padx=100)
        self.thongTinGiaiDau.grid(row=0, column=1)

        self.img2 = Image.open('Images/1.png')
        self.img2.thumbnail((200, 200))
        self.new_img2 = ImageTk.PhotoImage(self.img2)

        self.imgthongTinGiaiDau = tk.Label(self.thongTinGiaiDau, image=self.new_img2)
        self.imgthongTinGiaiDau.pack()
        self.butthongTinGiaiDau = tk.Button(self.thongTinGiaiDau, text='Thông tin giải đấu', bg='#e10600', fg='white',
                                         padx=5,pady=5, command= self.show_alert)

        self.butthongTinGiaiDau.pack(pady=20)

        ########### Frame End #############
        self.frameEnd = tk.Frame(self.master, bg='#000', height=200)
        self.frameEnd.pack(fill=tk.X, side=tk.BOTTOM)
        self.butQuayLai = tk.Button(self.frameEnd, text='Quay lại', bg='#e10600', fg='yellow', padx=10,
                                 pady=5)
        self.butQuayLai.pack(side=tk.RIGHT)

        self.centerFrame.grid_columnconfigure(0, weight=1)
        self.centerFrame.grid_columnconfigure(1, weight=1)

    def show_alert(self):
        messagebox.showinfo("Alert", "Mục đang bảo trì")
    def comDangKyThiDau(self):
          std= ss.F1_Fomula()



if(__name__=='__main__'):
    df = pd.read_excel(t.csvLichThiDau)
    df.drop_duplicates(inplace=True)
    df.to_excel(t.csvLichThiDau, index=False)
    root = tk.Tk()
    std = DangKyThiDau(root)
    tk.mainloop()