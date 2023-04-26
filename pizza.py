class TextbasedPizzaOrder:
    available_pizza = ["margarita", "pollo", "4cheese", "bolognese", "vegetarian"]
    available_toppings = ["pepperoni", "mushroom", "extra_cheese", "sausage", "onion"]
    pizza_prices = {"margarita": 8, "pollo": 5, "4cheese": 10, "bolognese": 12, "vegetarian": 7}
    topping_prices = {"pepperoni": 1, "mushroom": 3, "extra_cheese": 4, "sausage": 2, "onion": 3}

    def __init__(self):
        self.sub_total = []
        self.final_order = {}
        self.customer_address = {}

    def start_order(self):
        print("Hi, welcome to our text based pizza ordering")

        for pizza in self.available_pizza:
            print(pizza)

        while True:
            print()
            pizza = input("Which pizza you would like to order? ")
            global pizza_count
            pizza_count = int(input("How many pizza you want to order? "))

            if pizza:
                if pizza.lower() in self.available_pizza:
                    print(f"You have ordered {pizza_count} {pizza}")
                    self.sub_total.append(self.pizza_prices[pizza] * pizza_count)
                    break
                else:
                    print(f"I am sorry, we currently do not have {pizza}.")
                    select_again = input("if want to choose above available pizza type 'yes' to continue : ")
                    if select_again.lower() == "yes":
                        continue
                    else:
                        print("Thank you")
                        break
            else:
                print("Please give correct information to take your orders")
                continue
       
        print()
        print("This is the list of extra toppings:")
        for topping in self.available_toppings:
            print(topping)

        extra_topping = input("Would you like an extra toppings ? yes or no?")

        if extra_topping.lower() == "yes":
            print()
            topping = input("Which one would you like to add : ")

            if topping in self.available_toppings:
                self.final_order.setdefault(pizza, [])
                self.final_order[pizza].append(topping)
                print(f"I have ordered {topping}.")
                self.sub_total.append(self.topping_prices[topping]*pizza_count)
            else:
                print(f"I am sorry, we don't have {topping} available.")
        print()
        self.review_order()

    def review_order(self):
        for pizza, toppings in self.final_order.items():
            print(f"\n You have order {pizza_count} {pizza} pizza with {toppings}")
        order_correct = input("Is this order is correct? yes/no")

        if order_correct == 'no':
            add_remove = input("Would you like to add or remove?")
            if add_remove == "remove":
                remove = input("Which pizza you want to remove?")
                del self.final_order[remove]
                print("Your order details are deleted..")
            elif add_remove == 'add':
                add = input("Which pizza you want to add?")
                # self.final_order[add] =
        self.finalize_order()

    def finalize_order(self):
        print(f"\n Your total order price is : ${sum(self.sub_total)}")
        while True:
            print()
            print("Enter your Details to deliver your pizzas")
            self.customer_address['Name'] = input("Enter your name : ")
            self.customer_address["Phone.no"] = input("Enter your phone number : ")
            self.customer_address["Address"] = input("Enter your address : ")
            print()
            print("We will send your orders in below address ASAP")
            print()
            for key,value in self.customer_address.items():
                print(f"{key} : {value}")

            confirm_details = input("Confirm your details.. IS all ok then type 'place order' :")
            if confirm_details == "place order":
                print("Your order is confirmed.☻")
                print("Thank you!")
                break

            else:
                print()
                print("ok.. Please enter your details again:")
                continue
            print()

if __name__ == "__main__":
    order_now = TextbasedPizzaOrder()
    order_now.start_order()