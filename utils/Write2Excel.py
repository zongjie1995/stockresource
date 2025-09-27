import pandas as pd

class Write2Excel:
    def write2Excel(self,data):
        df = pd.DataFrame(data)
        # df.to_excel('pandas_output.xlsx', index=False)
        with pd.ExcelWriter('pandas_output.xlsx', engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
            worksheet = writer.sheets['Sheet1']
            for col in worksheet.columns:
                for cell in col:
                    cell.number_format = '@'
    pass

