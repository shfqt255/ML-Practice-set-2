from pandas_profiling import Profile_Report
import pandas as pd
data_frame=pd.read_csv('EDA/train.csv')
prof=Profile_Report(df)
prof.to_file(output_file='Output.html')