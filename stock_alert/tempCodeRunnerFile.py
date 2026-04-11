 # # to send email
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL,password=PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=MY_EMAIL,
    #         msg=f"Subject:ALERT!\nRELAINCE STOCK\n\n{news}.",
    #         )
    #     connection.close()