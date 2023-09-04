import datetime

x= datetime.datetime.now()   # now method will show current date and time of laptop
print(x)

print(datetime.datetime(2023,4,9))

#datetime symbolls

x= datetime.datetime.now()
m=x.strftime("%H")         # this symbol show time in 24 hours clock
print(m)

x= datetime.datetime.now()
m=x.strftime("%B")         # this symbol shows current month in full
print(m)

x= datetime.datetime.now()
m=x.strftime("%b")         # this symbol shows current month in short spelling
print(m)

x= datetime.datetime.now()
m=x.strftime("%p")         # this symbol shows AM/PM
print(m)


x= datetime.datetime.now()
m=x.strftime("%M")         # this symbol shows minutes
print(m)
