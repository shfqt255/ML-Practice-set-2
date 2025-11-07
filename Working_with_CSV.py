import pandas as pd

df=pd.read_csv("placement.csv")
print(df.head())

# What if the data is not separated by comma, if the data separated by tab.
print(pd.read_csv("placement.csv", sep="/t"))

#if sometimes rows displayed in columns and columns in rows. 
print(pd.read_csv("placement.csv", sep="", names=["Column1", "Column2..."]))

# Index_col Parameter, sets which column to use as row index
print(pd.read_csv("placement.csv", index_col="column name"))

# Header problem: controls which row(s) are used as column names
print (pd.read_csv("placement.csv", header="1"))

#use specific columns
print(pd.read_csv("placement.csv", usecols=["cgpa", "iq"]))

# squeeze is used to convert a DataFrame with only one column or one row into a simpler (lower-dimensional) object, 
# usually a Series (or sometimes a scalar).
print(pd.read_csv("placement.csv", usecols=["cgpa", "iq"], squeeze=True))

# Skip rows
print(pd.read_csv("placement"), skiprows=[1,3])
# N-rows
print(pd.read_csv("placement"), nrows=100)

#Encoding Parameter
print(pd.read_csv("placement.csv"), encoding=1)

# skip Bad lines: if lines contains 8 values but other contains 7 and columns are also 7. In short, if any of lines containes extra values.
print(pd.read_csv("placement.csv"), encoding=1, error_bad_lines=False)

#dtype parameter
print(pd.read_csv("placement.csv"), dtype={"cgpa": int})

# parse dates:  change the data type of the column to date. You can use list, and double, check documentation.
print(pd.read_csv("placement.csv"), parse_dates=["column1","column2"])

#converter

#na_values": In general we can find null values but is there is unnecessary hiphen or comma. To make them null
print(pd.read_csv("placement.csv"), na_values=["attribute name"])

#chunk size: 
print(pd.read_csv("placement.csv"), chunk_size=33)

