# 1757. Recyclable and Low Fat Products
# https://leetcode.com/problems/recyclable-and-low-fat-products/

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    selected_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    selected_products = selected_products[['product_id']]
    return selected_products
