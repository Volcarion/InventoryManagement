import datetime
amountLettuce = 90
num = amountLettuce
num2 = 60
date1 = datetime.date(2022,2,7)
date2 = datetime.date(2022,2,11)
lettucePerDay = 0
def estimateUsed (num,num2,date1,date2):

  lettuceUsed = num - num2
  daysPassed = date2 - date1
  lettucePerDay = lettuceUsed/(daysPassed.days - 1)
  return lettucePerDay

print(estimateUsed (num,num2,date1,date2))