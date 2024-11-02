# Cart and checkout system
class Cart:

    def __init__(self):
        self.cart = {} # {item: (quantity, price)}

    # Add items (item, quantity, price)
    def add_items(self, item, quantity=1, price=0):
        if item in self.cart:
            # grab current value of item in cart
            current_quantity, current_price = self.cart[item]
            # update the value w new quantity
            self.cart[item] = (current_quantity + quantity, current_price)
        else:
            self.cart[item] = (quantity, price)
        print(f"Added {quantity} x {item} to the cart.")

    # Remove items

    def remove_item(self, item, quantity=1):
        if item in self.cart:
            current_quantity, current_price = self.cart[item]
            new_quantity = current_quantity - quantity
            if new_quantity <= 0:
                del self.cart[item]
            else:
                self.cart[item] = (new_quantity, current_price)
            print(f"Removed {quantity} x {item} from the cart.")
        else:
            print(f"{item} is not in the cart.")

    # Total Cost

    def total_cost(self):
        total = sum(quantity * price for quantity, price in self.cart.values())
        print(f"Total cost before discounts and taxes: ${total:.2f}")
        return total

    # Checkout

    def checkout(self):
        total = self.total_cost()
        print(f"Final total cost: ${total:.2f}")
        self.cart.clear()
        # self.cart = {}

class DiscountCart(Cart):
    def __init__(self, discount=0):
        super().__init__()
        self.discount = discount

    def discount_total(self):
        # discount total = total * discount
        total = self.total_cost()
        discount = total * self.discount
        total = total - discount
        return total

    def checkout(self):
        total = self.discount_total()
        print(f"Final total cost: ${total:.2f}")
        self.cart.clear()

# discount_cart = DiscountCart(0.10)
# discount_cart.add_items("orange", 4, 1.00)
# discount_cart.add_items("mango", 1, 2.00)
# total = discount_cart.discount_total()
# print(total)
# discount_cart.checkout()


# Sales Tax

class TaxCart(Cart):
    def __init__(self, tax_rate=0):
        super().__init__()
        self.tax_rate = tax_rate

    def apply_tax(self, total):
        tax = total * self.tax_rate
        taxed_total = total - tax
        print(f"Applying a tax of {self.tax_rate * 100}%, adding ${tax:.2f}.")
        return taxed_total
    
    # def tax_total(self):
    #     total = self.total_cost()
    #     tax = total * self.tax_rate
    #     total = total + tax
    #     return total

    # def checkout(self):
    #     total = self.tax_total()
    #     print(f"Final total cost: ${total:.2f}")
    #     self.cart.clear()

tax_cart = TaxCart(0.07)
tax_cart.add_items("orange", 4, 1.00)
tax_cart.add_items("mango", 1, 2.00)
tax_cart.checkout()


class SpecialCart(DiscountCart, TaxCart):
    def __init__(self, discount, tax_rate):
        super().__init__()
        self.discount = discount
        self.tax_rate = tax_rate
        # DiscountCart.__init__(self, discount=0.10)
        # TaxCart.__init__(self, tax_rate=0.07)

    def checkout(self):
        # final_total = total - discounts + taxes
        # total = self.total_cost()
        # apply taxes on a discounted total
        tax_applied_total = self.apply_tax(self.discount_total())
        print(f"Total after applying tax on discounted amount: ${tax_applied_total:.2f}")
        return tax_applied_total

special_cart = SpecialCart(discount=0.10, tax_rate=0.07)
special_cart.add_items("orange", 4, 1.00)
special_cart.add_items("mango", 1, 2.00)
special_cart.checkout()