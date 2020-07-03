from Tool import TushareAPI
import pandas as pd

class HSGT(object):
    def __init__(self):
        self.pro = TushareAPI.TushareAPI().pro

    def load_data(self, start_date, end_date):
        raw_df = self.pro.moneyflow_hsgt(start_date=start_date, end_date=end_date)

        hgt_df = raw_df[['trade_date', 'ggt_ss', 'hgt']].copy()
        # for SGT
        sgt_df = raw_df[['trade_date', 'ggt_sz', 'sgt']].copy()
        # for flows
        flows_df = raw_df[['trade_date', 'north_money', 'south_money']].copy()
        flows_df['north_change'] = flows_df.north_money.diff(-1).round(2)

        return [hgt_df, sgt_df, flows_df]
