import tkinter as tk
from tkinter import ttk
from Data import TopInstitution


class TITab():
    def __init__(self, tabObject_arr):



        frame = ttk.LabelFrame(tabObject_arr[3])
        frame.grid(column=0, row=0)
        control_pad = ttk.LabelFrame(frame, text='数据日期格式 YYYYMMDD\n证券代码 XXXXXX')
        control_pad.grid(column=0, row=0)
        self.pre_load_state = ttk.Label(control_pad, text='正在导入数据......')
        self.pre_load_state.grid(column=0, row=2)
        # pre loading process bar
        bar = ttk.Progressbar(control_pad, orient='horizontal', length=150, mode='determinate')
        bar.grid(column=0, row=3)

        # data object
        self.data_object = TopInstitution

        # pre-loading data with thread
        TopInstitution.TopInsThread(thread_id=1, status_label=self.pre_load_state, progressbar=bar).start()
        print('skipped thread')

        # draw the UI
        input_frame = ttk.LabelFrame(control_pad)
        input_frame.grid(column=0, row=1, pady=1)
        ttk.Label(input_frame, text='交易时间').grid(column=0, row=0)
        ttk.Label(input_frame, text='证券代码').grid(column=0, row=1)
        trade_date = tk.StringVar()
        ttk.Entry(input_frame, width=10, textvariable=trade_date).grid(column=1, row=0)
        ts_code = tk.StringVar()
        ttk.Entry(input_frame, width=10, textvariable=ts_code).grid(column=1, row=1)

        # action UI
        def load_data():
            date = trade_date.get()
            code = ts_code.get()
            print(f'click {date}, {code}')
            df = self.data_object.load_data_from_local(trade_date=date, ts_code=code)
            # ready for input
            print(df)
            for idx in res_treeview.get_children():
                res_treeview.delete(idx)
            for idx in range(df.shape[0]):
                res_treeview.insert('', 'end', values=list(df.iloc[idx]))

        ttk.Button(control_pad, text='提取数据', command=load_data).grid(column=0, row=4)

        # table UI
        col_labels = ['交易日期', '证券代码', '交易席位', '买入金额', '买入占比', '卖出金额', '卖出占比', '净买入']

        res_treeview = ttk.Treeview(frame, columns=list(range(len(col_labels))), show='headings', height='25')
        res_treeview.grid(column=1, row=0, pady=5)
        col_widths = [100, 100, 500, 95, 95, 95, 95, 95]
        for i in range(len(col_labels)):
            res_treeview.heading(i, text=col_labels[i])
            res_treeview.column(i, width=col_widths[i], anchor='center')

