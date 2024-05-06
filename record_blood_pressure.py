#! env python
# -*- coding: utf-8 -*-

import os
import sys
import math
import tkinter as tk
import tkinter.ttk as ttk

# record_blood_pressure.tk-test
# Date: 2024/05/06
# Filename: tk-test 

__author__ = '2bo'
__date__ = "2024/05/06"


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # 変数定義
        # 横幅
        self.width = 340
        # 高さ
        self.height = 340
        # X
        self.xPos = 70
        # y
        self.yPos = 70
        # ボタン
        self.button_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "dot", "del"]
        # ボタンイメージの格納用
        self.button_img = []
        # 血圧とかのデータ
        self.blood_pressure = {"date": "", "max": 0.0, "min": 0.0, "Heart_rate": 0}

        # ウィンドウの設定
        master.geometry(f"{self.width}x{self.height}+{self.xPos}+{self.yPos}")
        master.title("はじめてのtkinter")

        self.pack()
        self.create_widget("収縮期血圧")

    def change_min(self, event):
        self.blood_pressure["max"] = float(self.Static1["text"])
        self.Static0["text"] = "拡張期血圧"
        self.Static1["text"] = ""
        ok_btn = tk.Button(text="決定", font=('MS Gothic', "15", "bold"))
        ok_btn.place(x=170, y=200, anchor=tk.CENTER, width=90, height=30)
        ok_btn.bind('<Button-1>', self.change_Heart_rate)

    def change_Heart_rate(self, event):
        self.blood_pressure["min"] = int(self.Static1["text"])
        self.Static0["text"] = "心拍数"
        self.Static1["text"] = ""
        ok_btn = tk.Button(text="決定", font=('MS Gothic', "15", "bold"))
        ok_btn.place(x=170, y=200, anchor=tk.CENTER, width=90, height=30)
        ok_btn.bind('<Button-1>', self.app_exit)
    def app_exit(self, event):
        self.blood_pressure["Heart_rate"] = float(self.Static1["text"])
        exit()

    def create_widget(self, type=None):
        # 全体の親キャンバス
        self.canvas_bg = tk.Canvas(self.master, width=self.width, height=self.height)
        self.canvas_bg.pack()

        # ボタン作成
        for index, item in enumerate(self.button_list):
            angle = math.radians(index * 30)  # 12個の数字を円周上に均等に配置するために30度ごとに計算
            x = 170 + 120 * math.sin(angle)
            y = 170 - 120 * math.cos(angle)

            self.button_img.append(tk.PhotoImage(file=f"./img/{str(item)}.png"))
            self.canvas_bg.create_image(x, y, image=self.button_img[index], tag=str(item))
        # label
        self.Static0 = tk.Label(text=type, font=("MSゴシック", "20", "bold"), )
        self.Static0.place(x=170, y=120, anchor=tk.CENTER)
        self.Static1 = tk.Label(text="", font=("MSゴシック", "20", "bold"))
        self.Static1.place(x=170, y=160, anchor=tk.CENTER)

        ok_btn = tk.Button(text="決定", font=('MS Gothic', "15", "bold"))
        ok_btn.place(x=170, y=200, anchor=tk.CENTER, width=90, height=30)
        ok_btn.bind('<Button-1>', self.change_min)
        cancel_btn = tk.Button(text="キャンセル", font=('MS Gothic', "15", "bold"))
        cancel_btn.place(x=170, y=230, anchor=tk.CENTER, width=90, height=30)

        """
        self.Static2 = tk.Label(text="決定", font=("MSゴシック", "20", "bold"))
        self.Static2.place(x=170, y=200, anchor=tk.CENTER)
        self.Static3 = tk.Label(text="キャンセル", font=("MSゴシック", "20", "bold"))
        self.Static3.place(x=170, y=230, anchor=tk.CENTER)
        """

        # 0
        self.canvas_bg.tag_bind(self.button_list[0], "<Button-1>", self.button_clicked_0)
        self.canvas_bg.tag_bind(self.button_list[0], "<ButtonRelease-1>", self.button_released_0)
        # 1
        self.canvas_bg.tag_bind(self.button_list[1], "<Button-1>", self.button_clicked_1)
        self.canvas_bg.tag_bind(self.button_list[1], "<ButtonRelease-1>", self.button_released_1)
        # 2
        self.canvas_bg.tag_bind(self.button_list[2], "<Button-1>", self.button_clicked_2)
        self.canvas_bg.tag_bind(self.button_list[2], "<ButtonRelease-1>", self.button_released_2)
        # 3
        self.canvas_bg.tag_bind(self.button_list[3], "<Button-1>", self.button_clicked_3)
        self.canvas_bg.tag_bind(self.button_list[3], "<ButtonRelease-1>", self.button_released_3)
        # 4
        self.canvas_bg.tag_bind(self.button_list[4], "<Button-1>", self.button_clicked_4)
        self.canvas_bg.tag_bind(self.button_list[4], "<ButtonRelease-1>", self.button_released_4)
        # 5
        self.canvas_bg.tag_bind(self.button_list[5], "<Button-1>", self.button_clicked_5)
        self.canvas_bg.tag_bind(self.button_list[5], "<ButtonRelease-1>", self.button_released_5)
        # 6
        self.canvas_bg.tag_bind(self.button_list[6], "<Button-1>", self.button_clicked_6)
        self.canvas_bg.tag_bind(self.button_list[6], "<ButtonRelease-1>", self.button_released_6)
        # 7
        self.canvas_bg.tag_bind(self.button_list[7], "<Button-1>", self.button_clicked_7)
        self.canvas_bg.tag_bind(self.button_list[7], "<ButtonRelease-1>", self.button_released_7)
        # 8
        self.canvas_bg.tag_bind(self.button_list[8], "<Button-1>", self.button_clicked_8)
        self.canvas_bg.tag_bind(self.button_list[8], "<ButtonRelease-1>", self.button_released_8)
        # 9
        self.canvas_bg.tag_bind(self.button_list[9], "<Button-1>", self.button_clicked_9)
        self.canvas_bg.tag_bind(self.button_list[9], "<ButtonRelease-1>", self.button_released_9)
        # dot
        self.canvas_bg.tag_bind(self.button_list[10], "<Button-1>", self.button_clicked_dot)
        self.canvas_bg.tag_bind(self.button_list[10], "<ButtonRelease-1>", self.button_released_dot)
        # del
        self.canvas_bg.tag_bind(self.button_list[11], "<Button-1>", self.button_clicked_del)
        self.canvas_bg.tag_bind(self.button_list[11], "<ButtonRelease-1>", self.button_released_del)

        # ok

        # cancel

    # 0
    def button_clicked_0(self, event):
        self.Static1["text"] += "0"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_0(self, event):
        pass
        #self.canvas_bg.delete("min_button_shadow_img")  # 暗いボタンを消去

    # 1
    def button_clicked_1(self, event):
        self.Static1["text"] += "1"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_1(self, event):
        pass
        #self.canvas_bg.delete("min_button_shadow_img")  # 暗いボタンを消去

    # 2
    def button_clicked_2(self, event):
        self.Static1["text"] += "2"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_2(self, event):
        pass

    # 3
    def button_clicked_3(self, event):
        self.Static1["text"] += "3"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_3(self, event):
        pass

    # 4
    def button_clicked_4(self, event):
        self.Static1["text"] += "4"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_4(self, event):
        pass

    # 5
    def button_clicked_5(self, event):
        self.Static1["text"] += "5"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_5(self, event):
        pass

    # 6
    def button_clicked_6(self, event):
        self.Static1["text"] += "6"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_6(self, event):
        pass

    # 7
    def button_clicked_7(self, event):
        self.Static1["text"] += "7"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_7(self, event):
        pass

    # 8
    def button_clicked_8(self, event):
        self.Static1["text"] += "8"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_8(self, event):
        pass

    # 9
    def button_clicked_9(self, event):
        self.Static1["text"] += "9"
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_9(self, event):
        pass

    # dot
    def button_clicked_dot(self, event):
        self.Static1["text"] += "."
        # 暗いボタンを表示
        #self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        #self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_dot(self, event):
        pass

    # del
    def button_clicked_del(self, event):
        tmp = self.Static1["text"]
        self.Static1["text"] = tmp[:-1]
        # 暗いボタンを表示
        # self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        # self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,tag="min_button_shadow_img")

    def button_released_del(self, event):
        pass
        # self.canvas_bg.delete("min_button_shadow_img")  # 暗いボタンを消去


"""
def main():
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

    window = tk.Tk()
    window.title("はじめてのtkinter")
    # 横幅
    width = 340
    # 高さ
    height = 340
    # X
    xPos = 70
    # y
    yPos = 70
    window.geometry(f"{width}x{height}+{xPos}+{yPos}")

    canvas = tk.Canvas(window, width=width, height=height)
    button_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "dot", "del"]
    button_img = []
    for index, item in enumerate(button_list):
        angle = math.radians(index * 30)  # 12個の数字を円周上に均等に配置するために30度ごとに計算
        x = 170 + 120 * math.sin(angle)
        y = 170 - 120 * math.cos(angle)
#        button = tk.Button(window, text=str(item)).place(x=x, y=y)
#        canvas.create_text(x, y, text=str(i), font=("Arial", 12, "bold"))
        # Minボタン
        button_img.append(tk.PhotoImage(file=f"./img/{str(item)}.png"))
        canvas.create_image(x, y, image=button_img[index], tag=str(item))
        canvas.tag_bind(str(item), "<Button-1>", min_button_clicked)
        canvas.tag_bind(str(item), "<ButtonRelease-1>", min_button_released)

        # Minボタン
        self.min_button_img = tk.PhotoImage(file="./img/min_button.png")
        self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_img, tag="min_button_img")
        self.canvas_bg.tag_bind("min_button_img", "<Button-1>", min_button_clicked)
        self.canvas_bg.tag_bind("min_button_img", "<ButtonRelease-1>", min_button_released)

    canvas.pack()



    # ウィンドウの表示
    window.mainloop()

    return


def min_button_clicked(event):

    # 暗いボタンを表示
    self.min_button_shadow_img = tk.PhotoImage(
        file="./img/min_button_shadow.png")  # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
    self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img,
                                tag="min_button_shadow_img")


def min_button_released(self, event):
    self.canvas_bg.delete("min_button_shadow_img")  # 暗いボタンを消去

"""


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
