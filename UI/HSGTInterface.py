import tkinter as tk
from tkinter import ttk
from Data import HSGT


class HSGTTab(object):
    def __init__(self, tabObject_arr):
        # ---------------------------- data object ----------------------------
        self.data_object = HSGT.HSGT()
        # ---------------------------- root window ----------------------------
        frame = ttk.LabelFrame(tabObject_arr[2])
        frame.grid(column=0, row=0)

        # ---------------------------- Tree views ----------------------------
        # # HGT tree view
        hgt_labels = ['交易日期', '港股通(SH)/百万', '沪股通/百万']
        hgt_treeview = ttk.Treeview(frame, columns=list(range(len(hgt_labels))), show='headings', height=25)
        for i in range(len(hgt_labels)):
            hgt_treeview.heading(i, text=hgt_labels[i])
            hgt_treeview.column(i, width=111, anchor='center')
        hgt_treeview.grid(column=1, row=0, padx=5, pady=5)

        # # SGT tree view
        sgt_labels = ['交易日期', '港股通(SZ)/百万', '深股通/百万']
        sgt_treeview = ttk.Treeview(frame, column=list(range(len(sgt_labels))), show='headings', height=25)
        for i in range(len(sgt_labels)):
            sgt_treeview.heading(i, text=sgt_labels[i])
            sgt_treeview.column(i, width=111, anchor='center')
        sgt_treeview.grid(column=2, row=0, padx=10, pady=5, )

        # # flows tree view
        flows_labels = ['交易日期', '北向/百万', '南向/百万', '北向较上日/百万']
        flows_treeview = ttk.Treeview(frame, column=list(range(len(flows_labels))), show='headings', height=25)
        for i in range(len(flows_labels)):
            flows_treeview.heading(i, text=flows_labels[i])
            flows_treeview.column(i, width=120, anchor='center')
        flows_treeview.grid(column=3, row=0, padx=5, pady=5)

        # ---------------------------- control pad ----------------------------
        control_frame = ttk.LabelFrame(frame, text='日期格式: YYYYMMDD')
        control_frame.grid(column=0, row=0)
        ttk.Label(control_frame, text='开始日期').grid(column=0, row=0)
        ttk.Label(control_frame, text='停止时间').grid(column=0, row=1)

        start_date = tk.StringVar()
        ttk.Entry(control_frame, width=10, textvariable=start_date).grid(column=1, row=0)
        end_date = tk.StringVar()
        ttk.Entry(control_frame, width=10, textvariable=end_date).grid(column=1, row=1)

        # # button function
        def load_data_action():

            dfs_arr = self.data_object.load_data(start_date=start_date.get(), end_date=end_date.get())
            treeviews_arr = [hgt_treeview, sgt_treeview, flows_treeview]

            for idx, treeview in enumerate(treeviews_arr):
                for j in treeview.get_children():
                    treeview.delete(j)
                for j in range(dfs_arr[idx].shape[0]):
                    treeview.insert('', 'end', values=list(dfs_arr[idx].iloc[j]))
                print(dfs_arr[idx])

        ttk.Button(control_frame, text='提取数据', command=load_data_action).grid(column=0, row=2)
