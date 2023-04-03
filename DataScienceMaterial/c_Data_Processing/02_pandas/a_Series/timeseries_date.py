import pandas as pd

datetime_series_1 = pd.Series(pd.date_range("2015-12-01 01:00:00", periods=7, freq="h"))
datetime_series_2 = pd.Series(
    pd.date_range("2015-12-01 07:30:00", periods=29, freq="30min")
)
datetime_series_3 = pd.Series(pd.date_range("2015-12-01 22:00:00", periods=3, freq="h"))

datetime_series = pd.concat([datetime_series_1, datetime_series_2, datetime_series_3])

datetime_series.reset_index(inplace=True, drop=True)

# loop through the number of days and use a day delta adding to list
list_dates = [datetime_series] * 366  # 2016 was leap year :)
for i in range(0, 366):
    list_dates[i] = datetime_series + pd.Timedelta("{0} days".format(i))

# concat that list at the end
datetime_series = pd.concat(list_dates)
print(datetime_series)
