import tkinter as tk
from tkinter import ttk
from UI import BlockTradeInterface, FutureInterface, HSGTInterface, TopInsInterface


class RootWindow:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('数据终端 v2.0')

        tabName_arr = ['活跃期货成交统计', '机构大宗交易买入', '沪深港通资金', '游资机构共同']
        self.tabObject_arr = []
        tabControl = ttk.Notebook(self.win)
        for tabName in tabName_arr:
            tab = ttk.Frame(tabControl)
            tabControl.add(tab, text=tabName)
            self.tabObject_arr.append(tab)
        tabControl.pack(expand=1, fill='both')

        FutureInterface.FutureTab(self.tabObject_arr)
        BlockTradeInterface.LTTab(self.tabObject_arr)
        HSGTInterface.HSGTTab(self.tabObject_arr)
        TopInsInterface.TITab(self.tabObject_arr)

        self.win.mainloop()
