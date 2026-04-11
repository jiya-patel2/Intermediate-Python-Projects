import requests
import smtplib
import os

STOCK = "RELIANCE.BSE"
COMPANY_NAME = "RELIANCE"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

PARAMETERS_STOCK = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY
}

# check stock trend
response = requests.get(STOCK_API_ENDPOINT,params=PARAMETERS_STOCK)
response.raise_for_status()
data = response.json()
print(data)
time_series = data["Time Series (Daily)"]
data_list = [values for (key,values) in time_series.items()]

yesterday = data_list[0]
yesterday_closing_price = float(data_list[0]['4. close'])

day_before = data_list[1]
day_before_closing_price = float(data_list[1]['4. close'])

difference = abs(yesterday_closing_price - day_before_closing_price)
diff_percent = (difference/yesterday_closing_price)*100
print(diff_percent)


if  diff_percent > 5:
    # to get news
    PARAMETERS_NEWS = {
      "q" : COMPANY_NAME,
      "language": "en",
      "pageSize": 3,
      "apiKey" : NEWS_API_KEY,
      }
    
    news_response = requests.get(NEWS_API_ENDPOINT,params=PARAMETERS_NEWS)
    news_response.raise_for_status()
    news_report = news_response.json()["articles"]

    for news in news_report:
        headline = news["title"]
        brief = news["description"]
        report = f"HEADLINE: {headline}\n\nBreif: {brief}"

        # to send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:ALERT!\nRELAINCE STOCK {int(diff_percent)}%\n\n{report}.",
                )
            connection.close()


