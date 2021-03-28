#Create lists for pizza toppings as well as corresponding prices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#Count the number of occurrences of $2 slices
number_of_2s = prices.count(2)
print(number_of_2s)

#Find the length of the toppings list, store it in a variable, and print it in a string
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Convert toppings and prices lists into a new two-dimensional list and print it
pizza_and_prices = [list(a) for a in zip(prices, toppings)]
print(pizza_and_prices)

#Sort pizza_and_prices so that the pizzas are in the order of increasing price
pizza_and_prices.sort()

#Store the first and last elements of pizza_and_prices in new variables
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

#Somebody bought priciest_pizza. Remove it from the pizza_and_prices list.
pizza_and_prices.pop()

#Since there is no longer an "anchovies" pizza, add a new topping to pizza_and_prices and sort it correctly.
pizza_and_prices.insert(4, [2.5, "peppers"])

#Three customers with little money come in and each want different pizzas. Slice pizza_and_prices, store the 3 cheapest pizzas in a new list, and print it.
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)