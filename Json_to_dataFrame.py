import pandas as pd
import requests as rq

response=rq.get("https://jsonplaceholder.typicode.com/posts")
# print(response.json())

df=pd.DataFrame(response.json())
print(df.head())
print(df.shape)


