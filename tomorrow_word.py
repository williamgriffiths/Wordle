from datetime import datetime

start_date = datetime(2021,6,19)
today = datetime.today()
delta = (today - start_date).days

f = open('words.txt','r')
lines= f.readlines()
print(lines[delta+1].strip())