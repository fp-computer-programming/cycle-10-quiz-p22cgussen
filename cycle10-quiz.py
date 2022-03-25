# Author CCG 3/24/22

prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]

# Question 1

def average(lst):
    sum = 0 # set empty variable for sum of all prices
    num = len(lst) # set variable for number of values
    for value in lst: # for loop to add each price to sum variable
        sum += value
    avg = sum / num # calculate and return average
    return avg
    
print(average(prices))


# Question 2

def discount(lst):
    for index, value in enumerate(lst): # enumerate loop to change each value in the list
        lst[index] = value - 5 # for each price, reduce by 5
    return lst

print(discount(prices))


# Question 3

def fpsales(cost, numb):
    total = 0 # empty variable for output statment
    for index, value in enumerate(cost): # enumerate loop to calculate revenue for each item
        total += (cost[index] * numb[index])   
    return total
        
print(fpsales(prices,sales))


# Question 4

prices = [30, 40, 25, 55, 60, 80, 65]

def discount2(cost2):
    for index, value in enumerate(cost2): # enumerate loop for each price
        if value > 40: # if statment to filter all prices more than 40
            cost2[index] = value - 10 # reduce each selected price by 10
    return cost2

print(discount2(prices))


# Question 5

prices = [30, 40, 25, 55, 60, 80, 65]

def matching(cost3, item):
    items2 = [] # empty list so item list stays intact
    counter = 0 # empty variable so prices list stays matching with nested items list
    for index, value in enumerate(item):
        for index2, value2 in enumerate(value): # enumerate loop inside of enumerate loop to get inside of nested list
            items2.append("{0} ${1}".format(value2, cost3[counter])) # add matching item and price to empty list
            counter += 1 # make sure lists match for each index
    return items2

print(matching(prices,items))

# Question 6 

def counter(number, multiple):
    ai = multiple # variable to start and end count
    while ai <= number: # while loop so the counter ends at chosen number
        print(ai) # print each number in the count
        ai += multiple # continue linear counting

inp1 = int(input("Enter the number to count up to: ")) # user inputs for function
inp2 = int(input("Enter the multiple to count by: "))

counter(inp1,inp2)
