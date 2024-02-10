def aggregate_level1(df):
    '''writing a function to get item and store level summary metrics for a specific year'''

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

