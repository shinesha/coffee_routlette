import win32com.client as win32
import pandas as pd
import random
import csv


df = pd.read_csv(r'C:\Users\GOHILV\OneDrive - FUJITSU\Documents\Coffee_Rout\NewPair.csv', header = None)

df.columns = ['Email1', 'Email2']
df = df.dropna(axis = 0, how = 'all')

for index, row in df.iterrows():
    a1 = row['Email1']
    b1 = row['Email2']


    print(df)

    x1= "viran.gohil@fujitsu.com"
    x2 = "jodrew_hotmail.com"
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
 
    #change this to a1
    mail.To = a1
    mail.Subject = 'Coffee Roulette'
    mail.Body = a1
    mail.HTMLBody = "Hi, " +  str(a1)  + "  and  " +  str(b1) + " have been paired for coffee networking, please do reach out to each other and arrange a time " #this field is optional

    # To attach a file to the email (optional):
    # attachment  = "Path to the attachment"
    # mail.Attachments.Add(attachment)

    mail.Send()

for index, row in df.iterrows():
    a1 = row['Email1']
    b1 = row['Email2']

    x1= "viran.gohil@fujitsu.com"
    x2 = "jodrew_7@hotmail.com"

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)


    # change this to b1 
    mail.To = b1
    mail.Subject = 'Coffee Roulette'
    mail.Body = b1
    mail.HTMLBody = "Hi, " +  str(a1)  + "  and  " +  str(b1) + " have been paired for coffee networking, please do reach out to each other and arrange a time " #this field is optional

    # To attach a file to the email (optional):
    # attachment  = "Path to the attachment"
    # mail.Attachments.Add(attachment)

    mail.Send()


