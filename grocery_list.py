# Grocery List - Tom Czubat

# Create an empty dictionary
grocery_item = {}

# Create an empty list
grocery_history = []
# Variable to control the while loop
stop = "go"

# Loop until user inputs 'q'
while stop != 'q':
  
  # Prompt the user for item name
  item_name = input("Item name:\n")
  # Prompt the user for Quantity purchased
  quantity = int(input("Quantity purchased:\n"))
  # Prompt the user for the Price per item
  cost = float(input("Price per item:\n"))
  
  # Add the 3 inputs to the dicitonary
  grocery_item = {'name':item_name, 'quan': quantity, 'cost': cost}
  
  # Add the dictionary to the grocery history list
  grocery_history.append(grocery_item)
  
  # Ask the user if they want another item
  stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
  # declare a variable to hold the grand total
  grand_total = 0
# for loop to step thourgh the grocery_history list
for grocery_item in grocery_history:
    # Print the infp fpr each item
    print("%d %s @ $%.2f ea $%.2f " %(grocery_item['quan'], grocery_item['name'], grocery_item['cost'], (grocery_item['cost'] * grocery_item['quan'])))
    #Compute grand total
    grand_total += (grocery_item['cost'] * grocery_item['quan'])
  
#Print grand total  
print("Grand total: $%.2f \n" %(grand_total))