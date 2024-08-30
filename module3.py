#18% top 7% tax
#calc total

#Get Price
item_price = int(input('Insert the price of the meal : '))

#first thing to do is set them in decimal form
tip_amnt = .18
tax = .07

#create function
#calcTotal
#total price is item_price then need to add tax and tip
#tip_price is item_price * tip
#tax_price is item_price  * tax
#total = item_price + tip_price + tax_price

def calcTotal(item_price):
    tip_price = (item_price* tip_amnt)
    print("Tip Amount : ", tip_price)
    tax_price = (item_price* tax) 
    print("Tax amount : ", tax_price)

    total_price = item_price + tip_price + tax_price
    return total_price

print(calcTotal(item_price))


#to calculate the future time you can modulo by 24
# alarm_time = (countdown + time_now) %24  
# print the alarm time

time_now = int(input('Enter Current Time : '))
countdown = int(input('Hours until timer : '))

print('Alarm will go off at : ', (countdown + time_now) %24 )