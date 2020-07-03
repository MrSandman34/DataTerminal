import pandas as pd
from Tool import TushareAPI, TsCodeTransform


class BlockTrade:
    def __init__(self):
        self.api = TushareAPI.TushareAPI().pro

    def load_data(self, start_date, end_date, ts_code):
        df = self.api.block_trade(ts_code=TsCodeTransform.ts_code_trans(ts_code), start_date=start_date, end_date=end_date)
        df.ts_code = df.ts_code.apply(lambda x:x[:6])
        df.dropna(inplace=True)
        df['ref'] = df.index

        insbuy_df = df[df['buyer'].str.contains('营业部') == False].copy()
        insbuy_df['ins_buy'] = insbuy_df.amount

        inssell_df = df[df['seller'].str.contains('营业部') == False].copy()
        inssell_df['ins_sell'] = -inssell_df.amount

        df = pd.merge(df, insbuy_df[['ref', 'ts_code', 'trade_date', 'ins_buy']], how='left',
                      on=['ref', 'ts_code', 'trade_date'])
        df = pd.merge(df, inssell_df[['ref', 'ts_code', 'trade_date', 'ins_sell']], how='left',
                      on=['ref', 'ts_code', 'trade_date'])
        df.fillna(0, inplace=True)
        df['ins_change'] = (df.ins_buy + df.ins_sell).round(2)
        df.drop(columns=['ref', 'ins_buy', 'ins_sell'], inplace=True)

        df.trade_date = pd.to_datetime(df.trade_date, format='%Y-%m-%d')
        return df
