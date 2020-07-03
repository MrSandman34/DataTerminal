import tkinter as tk
from tkinter import ttk
from Data import Future


class FutureTab(object):
    def __init__(self, tabObject_arr):
        # data object
        self.dataObject = Future.Future()
        self.chart_size = (4.8, 6.5)

        frame = ttk.LabelFrame(tabObject_arr[0])
        frame.grid(column=0, row=0)

        # treeview for displaying data
        col_labels = ['日期', '合约', '多头', '多头前20增减', '空头', '空头前20增减', '前20多空净差']
        tree_view = ttk.Treeview(frame, columns=list(range(len(col_labels))), show='headings', height='25')
        tree_view.grid(column=1, row=0, pady=5)
        for i in range(len(col_labels)):
            tree_view.heading(i, text=col_labels[i])
            tree_view.column(i, width=170, anchor='center')

        # control pad
        control_frame = ttk.LabelFrame(frame, text='时期格式 YYYYMMDD\n合约代码 IF2009')
        control_frame.grid(column=0, row=0)

        ttk.Label(control_frame, text='开始时间').grid(column=0, row=0)
        ttk.Label(control_frame, text='终止时间').grid(column=0, row=1)
        ttk.Label(control_frame, text='合约代码').grid(column=0, row=2)
        start_date = tk.StringVar()
        ttk.Entry(control_frame, width=10, textvariable=start_date).grid(column=1, row=0)
        end_date = tk.StringVar()
        ttk.Entry(control_frame, width=10, textvariable=end_date).grid(column=1, row=1)
        symbol = tk.StringVar()
        ttk.Entry(control_frame, width=10, textvariable=symbol).grid(column=1, row=2)

        def btn_action():
            print(symbol)
            try:
                data_df = self.dataObject.load_data(symbol=symbol.get(), start_date=start_date.get(),
                                                    end_date=end_date.get())
                for idx in tree_view.get_children():
                    tree_view.delete(idx)
                for idx in range(data_df.shape[0]):
                    tree_view.insert('', 'end', values=list(data_df.iloc[idx]))

            except AttributeError as msg:
                print(msg)
            except Exception as msg:
                print(msg)

        ttk.Button(control_frame, text='提取数据', command=btn_action).grid(column=0, row=3)
