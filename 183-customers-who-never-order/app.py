# 183. Customers Who Never Order
# https://leetcode.com/problems/customers-who-never-order/

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')

    no_order_customers = merged[merged['id_y'].isnull()]
    no_order_customers = no_order_customers[['name']]
    no_order_customers.rename(columns={'name': 'Customers'}, inplace=True)

    return no_order_customers
