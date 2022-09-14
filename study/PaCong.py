import pandas as pd
from Get_Text_Link import get_text_link_from_sel
url = 'https://www.jianshu.com/p/85f4624485b9'
sel = '#__next > div._21bLU4._3kbg6I > div > div._gp-ck > section:nth-child(1) > article > p > a'
df = pd.DataFrame(get_text_link_from_sel(url, sel))
df.columns = ['Text', 'link']
df.to_csv('output.csv', encoding='gbk', index=False)
print(df)
