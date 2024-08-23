import pandas as pd

def transform_data():

    print('im here ')
    df = pd.read_csv(r"C:\Users\hp\Desktop\RedditDataEngineering\data\output\reddit_20240821.csv")
    print(df.head)
    # Remove commas from the 'city' column
    print(df.info())
    # print(df['city'].head)
    
    # df['city'] = df['city'].str.replace(',', '')
    # cols = ['period_begin','period_end','period_duration', 'region_type', 'region_type_id', 'table_id',
    # 'is_seasonally_adjusted', 'city', 'state', 'state_code', 'property_type', 'property_type_id',
    # 'median_sale_price', 'median_list_price', 'median_ppsf', 'median_list_ppsf', 'homes_sold',
    # 'inventory', 'months_of_supply', 'median_dom', 'avg_sale_to_list', 'sold_above_list', 'parent_metro_region_metro_code', 'last_updated']
   
    # df = df[cols]

    print(df.head)

   # df = df.dropna()

    #let's change the period_begin and period_end to date time object and extract years and month.
    # df['period_begin'] = pd.to_datetime(df['period_begin'])
    # df['period_end'] = pd.to_datetime(df['period_end'])

    # df["period_begin_in_years"] = df['period_begin'].dt.year
    # df["period_end_in_years"] = df['period_end'].dt.year
    
    # df["period_begin_in_months"] = df['period_begin'].dt.month
    # df["period_end_in_months"] = df['period_end'].dt.month
    
    # #let's map the month number to their respective month name.
    # month_dict = {
    #     "period_begin_in_months": {
    #         1 : "Jan",
    #          2 :  "Feb",
    #          3: "Mar",
    #          4: "Apr",
    #          5: "May",
    #          6: "Jun",
    #          7: "Jul",
    #          8: "Aug",
    #          9: "Sep",
    #          10: "Oct",
    #          11: "Nov",
    #          12: "Dec",
    #     },
    #     "period_end_in_months": {
    #         1 : "Jan",
    #          2 :  "Feb",
    #          3: "Mar",
    #          4: "Apr",
    #          5: "May",
    #          6: "Jun",
    #          7: "Jul",
    #          8: "Aug",
    #          9: "Sep",
    #          10: "Oct",
    #          11: "Nov",
    #          12: "Dec"
    #     }}
    
    # df = df.replace(month_dict)
    print('Num of rows:', len(df))
    print('Num of cols:', len(df.columns))
        
    # Convert DataFrame to CSV format
    csv_data = df.to_csv(index=False)
    print('csv format done')
    # Upload CSV to S3

transform_data()