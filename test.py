import pandas as pd
import math

def binarySearch(arr, start, end, val):
    if(start <= end):
        mid = math.floor((start + end) / 2)
        if arr[mid] > val:
            #we can - 1 since we have just checked the mid index
            return binarySearch(arr, start, mid - 1, val)
        elif arr[mid] < val:
            return binarySearch(arr, mid + 1, end, val)
        else:
            return mid

def getOwidCountry(country):
    row_num = binarySearch(owid["country"], 0, len(owid["country"]) - 1, country)
    year_of_row = owid.iloc[row_num]["year"]
    start_slice = year_of_row - 1900
    end_slice = 2019 - year_of_row
    df = owid.iloc[row_num - start_slice : end_slice + row_num + 1]
    extra = []
    for i in range(df.shape[0]):
        if str(df.iloc[[i]]["country"].values[0]) != country:
            extra.append(df.iloc[[i]].index.values[0])
    
    return df.drop(extra)

owid = pd.read_csv("Macro/owid-energy-data.csv")
test2 = getOwidCountry("Western Sahara")    