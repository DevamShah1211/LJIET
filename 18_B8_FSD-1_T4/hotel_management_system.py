import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("600x600")
        self.root.config(bg="#dfe4ea")

        # Background Image (if you have one)
        self.bg_image = Image.open("hotel_bg.jpg")  # Make sure to have a background image
        self.bg_image = self.bg_image.resize((600, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Start with Login Page
        self.show_login_page()

    def show_login_page(self):
        # Clear window and show login page
        for widget in self.root.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.root, text="Hotel Management System", font=("Arial", 24, 'bold'), bg="#2f3542", fg="white")
        self.heading.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Username", font=("Arial", 14), bg="#dfe4ea")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Arial", 14))
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password", font=("Arial", 14), bg="#dfe4ea")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        self.password_entry.pack(pady=5)

        self.login_btn = tk.Button(self.root, text="Login", font=("Arial", 14, 'bold'), command=self.show_main_page)
        self.login_btn.pack(pady=20)

    def show_main_page(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            # If the login is successful, show the main page
            self.show_booking_page()
        else:
            messagebox.showerror("Error", "Invalid credentials, please try again!")

    def show_booking_page(self):
        # Clear window and show booking page
        for widget in self.root.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.root, text="Book Your Room", font=("Arial", 24, 'bold'), bg="#2f3542", fg="white")
        self.heading.pack(pady=20)

        # Room Type Selection
        self.room_label = tk.Label(self.root, text="Select Room Type", font=("Arial", 14), bg="#dfe4ea")
        self.room_label.pack(pady=5)
        
        self.room_var = tk.StringVar(value="single")
        self.room_options = ["Single", "Double", "Suite"]
        self.room_menu = tk.OptionMenu(self.root, self.room_var, *self.room_options)
        self.room_menu.config(font=("Arial", 14))
        self.room_menu.pack(pady=10)

        # Dates (Check-in, Check-out)
        self.checkin_label = tk.Label(self.root, text="Check-in Date (DD/MM/YYYY)", font=("Arial", 14), bg="#dfe4ea")
        self.checkin_label.pack(pady=5)
        self.checkin_entry = tk.Entry(self.root, font=("Arial", 14))
        self.checkin_entry.pack(pady=5)

        self.checkout_label = tk.Label(self.root, text="Check-out Date (DD/MM/YYYY)", font=("Arial", 14), bg="#dfe4ea")
        self.checkout_label.pack(pady=5)
        self.checkout_entry = tk.Entry(self.root, font=("Arial", 14))
        self.checkout_entry.pack(pady=5)

        # Book Now Button
        self.book_btn = tk.Button(self.root, text="Book Now", font=("Arial", 14, 'bold'), command=self.show_confirmation_page)
        self.book_btn.pack(pady=20)

    def show_confirmation_page(self):
        room_type = self.room_var.get()
        checkin_date = self.checkin_entry.get()
        checkout_date = self.checkout_entry.get()

        if not checkin_date or not checkout_date:
            messagebox.showerror("Error", "Please enter valid check-in and check-out dates!")
            return

        if room_type == "Single":
            room_rate = 1000
        elif room_type == "Double":
            room_rate = 2000
        else:
            room_rate = 3000

        # Confirm the booking
        confirmation_message = f"Room Type: {room_type}\nCheck-in: {checkin_date}\nCheck-out: {checkout_date}\nRate: ₹{room_rate}"
        confirmation_message += "\n\nDo you want to confirm the booking?"

        confirmation_response = messagebox.askyesno("Confirm Booking", confirmation_message)
        
        if confirmation_response:
            self.show_billing_page(room_type, room_rate)

    def show_billing_page(self, room_type, room_rate):
        # Show the billing page
        for widget in self.root.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.root, text="Booking Confirmation", font=("Arial", 24, 'bold'), bg="#2f3542", fg="white")
        self.heading.pack(pady=20)

        self.bill_label = tk.Label(self.root, text=f"Room Type: {room_type}", font=("Arial", 16), bg="#dfe4ea")
        self.bill_label.pack(pady=5)

        self.rate_label = tk.Label(self.root, text=f"Room Rate: ₹{room_rate}", font=("Arial", 16), bg="#dfe4ea")
        self.rate_label.pack(pady=5)

        self.total_label = tk.Label(self.root, text=f"Total Amount: ₹{room_rate}", font=("Arial", 16, 'bold'), bg="#dfe4ea")
        self.total_label.pack(pady=20)

        self.exit_btn = tk.Button(self.root, text="Exit", font=("Arial", 14, 'bold'), command=self.root.quit)
        self.exit_btn.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()
