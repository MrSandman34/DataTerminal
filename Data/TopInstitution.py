import pandas as pd
from datetime import date, timedelta
from Tool import TushareAPI
import threading


class TopInsThread(threading.Thread):
    def __init__(self, thread_id, status_label, progressbar):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.data_instance = TopIns(progressbar=progressbar)
        self.status_label = status_label

    def run(self):
        print(f'start {self.thread_id} thread')
        data_date = self.data_instance.pre_load_data()
        self.status_label.config(text=f'更新完毕\n当前更新日期{data_date}')
        print(f'end {self.thread_id} thread')


def load_data_from_local(trade_date, ts_code):
    data = pd.read_csv('50days_TopIns_data.csv', dtype={'trade_date':str, 'ts_code':str})

    if (trade_date == '') and (ts_code == ''):
        output_df = data
        print('no date, no code')
    elif (trade_date == '') and (ts_code != ''):
        output_df = data[data.ts_code == ts_code]
        print('no date, have code')

    elif (trade_date != '') and (ts_code == ''):
        output_df = data[data.trade_date == trade_date]
    else:
        output_df = data[(data.ts_code == ts_code)]
        output_df = output_df[output_df.trade_date == trade_date]
        print('have date, have code')

    return output_df


class TopIns:
    def __init__(self, progressbar):
        self.api = TushareAPI.TushareAPI().pro
        self.progressbar = progressbar
        # create date_range for preload data
        self.date_range = []
        today = date.today()
        delta = timedelta(days=5)  # length of period
        for i in range(delta.days + 1):
            day = today - timedelta(days=i)
            self.date_range.append(day.strftime('%Y%m%d'))

    def pre_load_data(self):
        # load 60-days data
        data = self.api.top_inst(trade_date=self.date_range[0])
        for idx, trade_date in enumerate(self.date_range):
            if idx == 0:
                try:
                    data = self.api.top_inst(trade_date=self.date_range[0])
                except:
                    data = self.api.top_inst(trade_date=self.date_range[0])
            else:
                try:
                    df = self.api.top_inst(trade_date=trade_date)
                except:
                    df = self.api.top_inst(trade_date=trade_date)
                data = data.append(df)
                print(f'preloading data ... {trade_date}')
            if idx == len(self.date_range) - 1:
                self.progressbar['value'] = 100
                self.progressbar.update_idletasks()
            else:
                self.progressbar['value'] = idx / len(self.date_range) * 100
                self.progressbar.update_idletasks()
        data.ts_code = data.ts_code.apply(lambda x:x[:6])
        data.to_csv('50days_TopIns_data.csv', index=False)
        print(data)
        return str(int(data.trade_date.head(1).values))
