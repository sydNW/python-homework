class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        self.items.append((name, quantity, price))

    def remove_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def show_cart(self):
        print("Cart Items:")
        for name, qty, price in self.items:
            print(f"{name}: {qty} pcs @ Ksh {price:.2f}")
        print(f"Subtotal: Ksh {self.calculate_total():.2f}\n")


class DiscountedCart(ShoppingCart):
    def __init__(self, discount_rate):
        super().__init__()
        self.discount_rate = discount_rate

    def calculate_total(self):
        original = super().calculate_total()
        discount = original * self.discount_rate
        return original - discount


class TaxedCart(ShoppingCart):
    def __init__(self, tax_rate):
        super().__init__()
        self.tax_rate = tax_rate

    def calculate_total(self):
        base = super().calculate_total()
        tax = base * self.tax_rate
        return base + tax


def checkout(cart):
    cart.show_cart()
    print(f"Final Total: Ksh {cart.calculate_total():.2f}")
    print("-" * 30)


# Demo usage
if __name__ == "__main__":
    print(">> Normal Cart <<")
    cart1 = ShoppingCart()
    cart1.add_item("Banana", 10, 5.00)
    cart1.add_item("Apple", 5, 8.50)
    checkout(cart1)

    print(">> Discount Cart (10%) <<")
    disc_cart = DiscountedCart(0.10)
    disc_cart.add_item("Banana", 10, 5.00)
    disc_cart.add_item("Apple", 5, 8.50)
    checkout(disc_cart)

    print(">> Taxed Cart (12%) <<")
    tax_cart = TaxedCart(0.12)
    tax_cart.add_item("Banana", 10, 5.00)
    tax_cart.add_item("Apple", 5, 8.50)
    checkout(tax_cart)
