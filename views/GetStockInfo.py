import akshare as ak
import sys
sys.path.append('..')
from Controllers.GetStock import GetStock

if __name__ == '__main__':
    stock_df = ak.stock_info_a_code_name()
    ss=GetStock()
    ss.getallstock(stock_df)


    # print(stock_df)