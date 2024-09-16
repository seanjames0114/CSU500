# Completion : Print total_months and avg_rain_per_month

# Need total rain, num_years, num_months
total_rain = 0
num_years = int(input('Give the number of years : '))
num_months = 12
x = 1

#outer loop needs to be counting for years x is year 1 and will continue until it is equal to the number of years
while x <= num_years:
    y = 1
    print(f'Year {x}')
    #inner is the number of months loop, it is starting at the first month and will continue until it is equal until the number of months 
    while y <= num_months : 
        #takes the input of the rainfall
        rainfall = int(input(f'Give the Rainfall in Inches for month {y}: '))
        #calc total rain, total rain = total rain + rainfall of the nonth 
        total_rain += rainfall
        print(f"Total Rainfall as of month {y} : {total_rain}")
        #add one to y becasue you are counting up in months 
        y += 1
    #add one to the years because you are counting up in years
    x += 1
    

#calc the avg rain per month, avg rain = total rain / number of months * num_years
avg_rain_per_month = total_rain/(num_months * num_years)

print(f"Total Number of months : {(num_months * num_years)}, Total Rainfall : {total_rain}, Average Rain / Month : {avg_rain_per_month}")

# Get the number of books from the user 
num_books = int(input("Insert Number of books purchased this month : "))

# if statements for all the conditions, the number of books must be between the constraints in order to give the points 

if num_books >=0 and num_books < 2:
    points = 0
elif num_books >=2 and num_books < 4:
    points = 5
elif num_books >=4 and num_books < 6:
    points = 15
elif num_books >=6 and num_books < 8:
    points = 30
elif num_books >=8:
    points = 60

print(f'Points Awarded : {points}')