import pandas as pd 

def aggregate_level1(df):
    sale_day_store_level = df.groupby(['Year', 'Month', 'Day', 'store_nbr'], as_index=False)[
        'unit_sales'].agg(['sum', 'count'])
    sale_day_store_level = sale_day_store_level.reset_index().rename(
        columns={'sum': 'store_sales', 'count': 'item_variety'})
    sale_day_item_level = df.groupby(['Year', 'Month', 'Day', 'item_nbr'], as_index=False)[
        'unit_sales'].agg(['sum', 'count'])
    sale_day_item_level = sale_day_item_level.reset_index().rename(
        columns={'sum': 'item_sales', 'count': 'store_spread'})
    sale_store_item_level = df.groupby(['Year', 'store_nbr', 'item_nbr'], as_index=False)[
        'unit_sales'].agg(['sum', 'count'])
    sale_store_item_level = sale_store_item_level.reset_index().rename(
        columns={'sum': 'item_sales', 'count': 'entries'})

    return sale_day_store_level, sale_day_item_level,sale_store_item_level


def classification(ts):
    adi = len(ts) / len(ts[ts > 0]) if len(ts[ts > 0]) > 0 else float('inf')
    cv_squared = (sum(((ts - ts.mean())**2) / len(ts)) / ts.mean())
    f_type = 'Smooth'
    if (adi > 1.32 and cv_squared < 0.49):
        f_type = 'Intermittent'
    elif (adi > 1.32 and cv_squared > 0.49):
        f_type = 'Lumpy'
    elif (adi < 1.32 and cv_squared > 0.49):
        f_type = 'Erratic'              
    return adi, cv_squared

def to_dateTime(df):
    df['date'] = pd.to_datetime(df['date'])