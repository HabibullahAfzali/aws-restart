stock_burger = 10  # initial variable

while stock_burger > 0: #this condition is true for stock_burger is not equal to zero (0)
    client_order = int(input("How many burgers do you want to order? : ")) # here we ask the client to put their orders using input function, using keyboard
    
    if stock_burger < client_order: # this line check if the client order is more than the burger left in our stock, the should display the below message
        print("There are not enough burgers left")
    if stock_burger >=client_order: # this line check if client order is equal or less than our stock then put the order and do print the remaing stock minus client order
        stock_burger -= client_order
        print("Order placed. Remaining burgers in stock:", stock_burger)
