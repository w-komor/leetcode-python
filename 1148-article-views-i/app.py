# 1148. Article Views I
# https://leetcode.com/problems/article-views-i/

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_views = views[views['author_id'] == views['viewer_id']]
    result = pd.DataFrame(self_views['author_id'].unique(), columns=['id']).sort_values(by='id')
    return result
