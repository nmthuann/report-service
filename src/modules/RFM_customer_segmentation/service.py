import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# df = pd.read_excel('D:\\CODE\\Project_Download\\python_project_miAI\\MIAI_Customer_Segmentation\\data.xlsx')
#
# # Loai bo gia tri nan
# df_not_nan = df[df['CustomerID'].notna()]
# df_not_nan = df_not_nan.sample(1000, random_state=42)
# df_not_nan.to_csv('data_1000.csv', index=False)
# print(df_not_nan.head(10))



def readData(file_name):
    data_frame = pd.read_csv(file_name)
    print("%n IN 10 dong::::", data_frame.head(10))

def removeNaNValue(data_frame, field):
    df_not_nan = data_frame[data_frame[field].notna()]
    return df_not_nan


"""
    1. Tính R - Recency
    2. Tinh M - MoneytaryValue
    3. Tính F - Frequency 
    
"""
def calculateRFM(data_frame):
    titles = ['InvoiceDate', 'Quantity', 'TotalPay', 'CustomerID']
    print("titles:::", titles)

    # Loại bỏ giá trị NaN


    # Chuyen tu string -> date
    data_frame['InvoiceDate'] = pd.to_datetime(data_frame['InvoiceDate'], format='%Y-%m-%d %H:%M:%S')

    # Lay ngay lon nhat trong InvoiceDate + 1
    current_date = max(data_frame['InvoiceDate']) + datetime.timedelta(days=1)

    # -------- Tinh M - MoneytaryValue
    data_frame['TotalPay'] = data_frame['Quantity'] * data_frame['UnitPrice']

    # Group by CustomerID de tinh R, F, M
    df_customers = data_frame.groupby(['CustomerID']).agg(
        {'InvoiceDate': lambda x: (current_date - x.max()).days,
         'InvoiceNo': 'count',
         'TotalPay': 'sum'
         }
    )
        
    df_customers.rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'TotalPay': 'MonetaryValue'},
                        inplace=True)

if __name__ == "__main__":
    df = pd.read_csv('data_1000.csv')
    print("%n IN 10 dong::::", df.head(10))