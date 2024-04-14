from pytrends.request import TrendReq
from newsapi import NewsApiClient
from config import NEWS_API_KEY

pytrends = TrendReq(hl='it-IT')
newsapi = NewsApiClient(api_key=NEWS_API_KEY)


print(pytrends.trending_searches(pn='italy'))

trending_searches = pytrends.trending_searches(pn='italy')

for trend in trending_searches[0]:
    print(trend)
    news = newsapi.get_everything(q=trend,
                                  language='it',
                                  sort_by='relevancy')
    print(news)
