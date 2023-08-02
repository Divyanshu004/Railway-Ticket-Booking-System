import tkinter as tk
from tkinter import ttk

class Train:
    def __init__(self, train_id, name, source, destination, seats):
        self.train_id = train_id
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats

class Booking:
    def __init__(self, booking_id, train_id, name, age, gender):
        self.booking_id = booking_id
        self.train_id = train_id
        self.name = name
        self.age = age
        self.gender = gender

class TrainBookingSystem:
    def __init__(self):
        self.trains = []
        self.bookings = []
        self.booking_id_counter = 1
    
    def add_train(self, train_id, name, source, destination, seats):
        train = Train(train_id, name, source, destination, seats)
        self.trains.append(train)
        print("Train added successfully!")
    
    def book_train(self, train_id, name, age, gender):
        for train in self.trains:
            if train.train_id == train_id:
                if train.seats > 0:
                    booking = Booking(self.booking_id_counter, train_id, name, age, gender)
                    self.bookings.append(booking)
                    self.booking_id_counter += 1
                    train.seats -= 1
                    print("Booking successful!")
                    return
                else:
                    print("No seats available!")
                    return
        print("Train not found!")
    
    def display_trains(self):
        if len(self.trains) == 0:
            print("No trains found!")
            return
        for train in self.trains:
            print(f"Train ID: {train.train_id}, Name: {train.name}, Source: {train.source}, Destination: {train.destination}, Seats: {train.seats}")
    
    def display_bookings(self):
        if len(self.bookings) == 0:
            print("No bookings found!")
            return
        for booking in self.bookings:
            train_name = None
            for train in self.trains:
                if train.train_id == booking.train_id:
                    train_name = train.name
                    break
            print(f"Booking ID: {booking.booking_id}, Train Name: {train_name}, Name: {booking.name}, Age: {booking.age}, Gender: {booking.gender}")

class TrainBookingApp:
    def __init__(self, train_booking_system):
        self.train_booking_system = train_booking_system
        self.window = tk.Tk()
        self.window.title("Train Booking Management System")
        
        self.train_id_label = ttk.Label(self.window, text="Train ID:")
        self.train_id_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.train_id_entry = ttk.Entry(self.window)
        self.train_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.name_label = ttk.Label(self.window, text="Name:")
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.source_label = ttk.Label(self.window, text="Source:")
        self.source_label.grid(row=2, column=0, padx=5, pady=5)
        
        self.source_entry = ttk.Entry(self.window)

