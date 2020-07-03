from Tool import TushareAPI
import pandas as pd


class Future(object):
    def __init__(self):
        self.pro = TushareAPI.TushareAPI().pro

    #  col_labels = ['日期', '合约', '多头', '多头前20增减', '空头', '空头前20增减', '前20多空净差']
    def load_data(self, symbol, start_date, end_date):
        df = self.pro.fut_holding(symbol=symbol, start_date=start_date, end_date=end_date)
        df = df.groupby(['trade_date', 'symbol']).sum().reset_index()
        print(df)
        df['longChg_minus_shortChg'] = df.long_chg - df.short_chg
        df.drop(columns=['vol', 'vol_chg'], inplace=True)
        print(df)
        df.trade_date = pd.to_datetime(df.trade_date, format='%Y-%m-%d')
        return df
