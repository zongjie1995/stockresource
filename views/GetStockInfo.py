import akshare as ak
import sys

from pandas import DataFrame

sys.path.append('..')
from controllers.GetStock import GetStock
from utils.Write2Excel import Write2Excel
import pandas as pd

if __name__ == '__main__':
    ##获取所有股票代码和名称
    stock_df1 = ak.stock_info_a_code_name()
    ##获取代码
    code_list=stock_df1.get("code")
    # stockInfo=pd.DataFrame
    # stockInfo.columns=['最新', '股票代码', '股票简称','总股本','流通股','总市值','流通市值','行业','上市时间']
    stockInfo=pd.DataFrame(columns=['最新', '股票代码', '股票简称','总股本','流通股','总市值','流通市值','行业','上市时间'])
    # print(stockInfo)
    ##循环获取股票信息
    for i in code_list:
        stock_df2 = ak.stock_individual_info_em(symbol=i).drop("item",axis=1).transpose()
        # stock_df2=stock_df2[['最新', '股票代码', '股票简称','总股本','流通股','总市值','流通市值','行业','上市时间']]
        stock_df2.columns=['最新', '股票代码', '股票简称','总股本','流通股','总市值','流通市值','行业','上市时间']
        # stock_df2=stock_df2.values[1]
        # print(stock_df2)
        stock_df2["总股本"]=stock_df2["总股本"].astype(str)
        stock_df2["流通股"]=stock_df2["流通股"].astype(str)
        stock_df2["总市值"]=stock_df2["总市值"].astype(str)
        stock_df2["流通市值"]=stock_df2["流通市值"].astype(str)

        stockInfo = pd.concat([stockInfo, stock_df2], ignore_index=True)

    # ss=GetStock()
    # data=ss.getallstock(stock_df)
    we=Write2Excel()
    we.write2Excel(stockInfo)


    # print(code_list)