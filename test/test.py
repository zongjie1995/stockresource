import akshare as ak


# stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20220101", end_date='20220201', adjust="qfq")
# print(stock_zh_a_hist_df)


# stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
# print(stock_sh_a_spot_em_df)
#
# for i in stock_sh_a_spot_em_df:
#     print(i)

# stock_individual_info_em_df = ak.stock_individual_info_em(symbol="301316")
# print(stock_individual_info_em_df)


# stock_individual_basic_info_xq_df = ak.stock_individual_basic_info_xq(symbol="SH301316")
# s=stock_individual_basic_info_xq_df.to_json
# print(s)

stock_df = ak.stock_info_a_code_name()
print(stock_df)