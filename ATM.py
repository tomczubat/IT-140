import sys

# Set the starting blanace
account_balance = float(500.25)

# Function to print the balance
def printbalance():
  print('Your current balance:')
  print(account_balance)

# Function to deposit into the account
def deposit():
  deposit_amount = float(input('How much would you like to deposit today?\n'))
  global account_balance
  # Calcualte the new balance
  account_balance = account_balance +deposit_amount
  # Print the new balance formatted 
  print("Deposit was $%.2f, current balance is $%.2f"%(deposit_amount,account_balance))

# Withfraw function 
def withdrawal():
  global account_balance
  withdrawal_amount =  float(input('How much would you like to withdraw today?\n'))
  # If the withfraal amount is greater than the balance
  if withdrawal_amount > account_balance:
    print('$%.2f is greater than your account balance of $%.2f' %(withdrawal_amount, account_balance))
  else:
    # Calculate the new balance
    account_balance = account_balance - withdrawal_amount
    # Print out the information formatted
    print('Withdrawal amount was $%.2f, current balance is $%.2f'%(withdrawal_amount, account_balance))
    
userchoice = input('What would you like to do?\n')
# Conditionals depending on the user's choice
if(userchoice == 'D'):
   deposit()
elif(userchoice =='W'):
    withdrawal()
elif(userchoice =='B'):
  printbalance()
elif(userchoice =='Q'):
  print('Thank you for banking with us.')
  

