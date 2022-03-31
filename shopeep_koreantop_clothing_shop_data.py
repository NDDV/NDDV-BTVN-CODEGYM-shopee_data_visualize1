#%%
import matplotlib.pyplot as plt
import pandas as pd
import datetime
#%%
df = pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
df.info()

# %%
df=df.dropna()

# %%
#Vẽ biểu đồ so sánh số lượng shop gia nhập theo các năm.
d1 = df.groupby(by=df['join_year']).count()
d1

# %%
x = d1.index.get_level_values(0)

plt.bar(x, d1['pk_shop'])
plt.xlabel('năm gia nhập', fontsize = 14)
plt.ylabel('số lượng shop', fontsize = 14)
plt.show()
# %%
#Vẽ biểu đồ thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt.
plt.scatter(df['response_rate'].dt.second,df['rating_good'])
plt.xlabel('đánh giá tốt', fontsize = 14)
plt.ylabel('tỉ lệ được đánh giá', fontsize = 14)
plt.show()

# %%
#Vẽ biểu đồ thể hiện mối quan hệ giữa thời gian phản hồi (đơn vị giây) với số lượt khách hàng đánh giá xấu.
df
#%%
# %%
plt.bar(df['response_time'].dt.seconds,df['rating_good'])
plt.xlabel('đánh giá tốt', fontsize = 14)
plt.ylabel('tỉ lệ được đánh giá', fontsize = 14)
plt.show()

#%%
#Vẽ biểu đồ thể hiện xu hướng của số lượng shop gia nhập theo thời gian.