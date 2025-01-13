import tkinter as tk
from tkinter import messagebox

class Pizza:
    def __init__(self, size, toppings, cheese):
        self.size = size
        self.toppings = toppings
        self.cheese = cheese
        
    def price(self):
        cost = 0
        if self.size == 'small':
            cost += 50
        elif self.size == 'medium':
            cost += 100
        else:
            cost += 200
        topping_prices_20 = ['corn', 'tomato', 'onion', 'capsicum']
        topping_prices_50 = ['mushroom', 'olives', 'broccoli']
        for topping in self.toppings:
            if topping in topping_prices_20:
                cost += 20
            else:
                cost += 50
        cost += 50 * len(self.cheese)
        return cost

class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def total_bill(self):
        total = sum([p.price() for p in self.pizzas])
        return total


class PizzaOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Ordering System")
        self.root.geometry("500x700")
        
        self.order = Order()
        
        self.create_widgets()

    def create_widgets(self):
        self.heading = tk.Label(self.root, text="Pizza Ordering System", font=("Arial", 20))
        self.heading.pack(pady=20)

        # Pizza customization frame
        self.pizza_frame = tk.Frame(self.root)
        self.pizza_frame.pack(pady=20)

        # Pizza size selection
        self.size_label = tk.Label(self.pizza_frame, text="Select Pizza Size (small/medium/large):")
        self.size_label.grid(row=0, column=0, padx=10, pady=5)
        self.size_var = tk.StringVar(value="small")
        self.size_menu = tk.OptionMenu(self.pizza_frame, self.size_var, "small", "medium", "large")
        self.size_menu.grid(row=0, column=1, padx=10, pady=5)

        # Toppings selection
        self.toppings_label = tk.Label(self.pizza_frame, text="Select Toppings (corn, tomato, onion, capsicum, mushroom, olives, broccoli):")
        self.toppings_label.grid(row=1, column=0, padx=10, pady=5)
        self.toppings_entry = tk.Entry(self.pizza_frame, width=40)
        self.toppings_entry.grid(row=1, column=1, padx=10, pady=5)

        # Cheese selection
        self.cheese_label = tk.Label(self.pizza_frame, text="Enter Cheese Types (mozzarella, feta, cheddar):")
        self.cheese_label.grid(row=2, column=0, padx=10, pady=5)
        self.cheese_entry = tk.Entry(self.pizza_frame, width=40)
        self.cheese_entry.grid(row=2, column=1, padx=10, pady=5)

        # Add Pizza button
        self.add_pizza_btn = tk.Button(self.root, text="Add Pizza", command=self.add_pizza)
        self.add_pizza_btn.pack(pady=10)

        # View bill button
        self.view_bill_btn = tk.Button(self.root, text="View Bill", command=self.view_bill)
        self.view_bill_btn.pack(pady=10)

    def add_pizza(self):
        size = self.size_var.get()
        toppings = [t.strip() for t in self.toppings_entry.get().split(',')]  # Comma separated toppings
        cheese = [c.strip() for c in self.cheese_entry.get().split(',')]  # Comma separated cheeses
        
        if not toppings or not cheese:
            messagebox.showerror("Error", "Toppings and Cheese cannot be empty!")
            return
        
        pizza = Pizza(size, toppings, cheese)
        self.order.add_pizza(pizza)
        
        messagebox.showinfo("Success", "Pizza Added Successfully!")
        
        # Reset fields for next pizza
        self.toppings_entry.delete(0, tk.END)
        self.cheese_entry.delete(0, tk.END)

    def view_bill(self):
        if not self.order.pizzas:
            messagebox.showerror("Error", "No pizzas ordered!")
            return

        bill_details = ""
        total = 0
        for i, pizza in enumerate(self.order.pizzas, 1):
            bill_details += f"Pizza {i} - Size: {pizza.size}, Toppings: {', '.join(pizza.toppings)}, Cheese: {', '.join(pizza.cheese)}\n"
            total += pizza.price()
        
        bill_details += f"\nTotal Bill: ₹{total}"
        messagebox.showinfo("Bill", bill_details)


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaOrderApp(root)
    root.mainloop()
