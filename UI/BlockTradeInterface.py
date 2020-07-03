import tkinter as tk
from tkinter import ttk
from Data import BlockTrade


class LTTab(object):
    def __init__(self, tabObject_arr):

        # ------ data object ------
        self.dataObject = BlockTrade.BlockTrade()
        # ------ draw widgets ------
        frame = ttk.LabelFrame(tabObject_arr[1])
        frame.grid(column=0, row=0)

        control_frame = ttk.LabelFrame(frame, text='数据日期格式 YYYYMMDD\n证券代码 XXXXXX')
        control_frame.grid(column=0, row=0)

        ttk.Label(control_frame, text='开始时间').grid(column=0, row=0)
        ttk.Label(control_frame, text='终止时间').grid(column=0, row=1)
        start_date = tk.StringVar()
        ttk.Entry(control_frame, width=10, textvariable=start_date).grid(column=1, row=0)
        end_date = tk.StringVar()
        ttk.Entry(control_frame, width=10, textvariable=end_date).grid(column=1, row=1)

        # select company
        ttk.Label(control_frame, text='证券代码').grid(column=0, row=2)
        stock_code = tk.StringVar()
        ttk.Entry(control_frame, width=10, textvariable=stock_code).grid(column=1, row=2)

        # result display view
        col_labels = ['证券代码', '交易日期', '成交价', '成交量(万)', '成交金额(万)', '买方营业部', '卖方营业部', '机构合计(万)']

        res_treeview = ttk.Treeview(frame, columns=list(range(len(col_labels))), show='headings', height='25')
        res_treeview.grid(column=1, row=0, pady=5)
        # res_treeview.pack(fill = 'x') # adjust the treeview to the frame
        col_widths = [90, 90, 70, 80, 80, 350, 350, 80]
        for i in range(len(col_labels)):
            res_treeview.heading(i, text=col_labels[i])
            res_treeview.column(i, width=col_widths[i], anchor='center')

        def display_data():
            display_df = self.dataObject.load_data(ts_code=stock_code.get(),
                                                   start_date=start_date.get(),
                                                   end_date=end_date.get())
            print(display_df)
            for idx in res_treeview.get_children():
                res_treeview.delete(idx)
            for idx in range(display_df.shape[0]):
                res_treeview.insert('', 'end', values=list(display_df.iloc[idx]))

        display_data_btn = ttk.Button(control_frame, text='提取数据', command=display_data)
        display_data_btn.grid(column=0, row=3)
