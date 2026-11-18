def hotel_reservation_system():
    inventory = {"Single": 5, "Double": 3, "Suite": 2}
    prices = {"Single": 100.0, "Double": 180.0, "Suite": 350.0}

    while True:
        print("\n" + "="*40 + "\n       HOTEL RESERVATION SYSTEM\n" + "="*40)
        print("Current Room Availability & Prices:")
        for room, count in inventory.items():
            print(f"- {room} Room: {count} available | Price/Night: ${prices[room]:.2f}")
        print("-" * 40)

        guest_name = input("Enter guest name: ").strip()

        # Room Type Validation
        while True:
            room_type = input("Enter room type (Single, Double, Suite): ").strip().capitalize()
            if room_type in inventory: break
            print("❌ Invalid room type. Please choose from Single, Double, or Suite.")

        # Optional Room Change
        if input("Would you like to change your room type? (yes/no): ").strip().lower() == 'yes':
            while True:
                room_type = input("Enter new room type (Single, Double, Suite): ").strip().capitalize()
                if room_type in inventory: break
                print("❌ Invalid room type. Try again.")

        # Helper function for positive integer inputs
        def get_positive_int(prompt, err_msg):
            while True:
                try:
                    val = int(input(prompt))
                    if val > 0: return val
                    print(err_msg)
                except ValueError:
                    print("❌ Please enter a valid integer.")

        num_rooms = get_positive_int("Enter number of rooms to reserve: ", "❌ Number of rooms must be greater than 0.")

        # Availability Check
        if num_rooms > inventory[room_type]:
            print(f"\n⚠️ Sorry! Only {inventory[room_type]} {room_type} room(s) available. Reservation failed.")
            if input("\nWould you like to process another reservation? (yes/no): ").strip().lower() != 'yes':
                print("\nThank you for using the Hotel Reservation System. Goodbye!")
                break
            continue

        num_nights = get_positive_int("Enter number of nights: ", "❌ Number of nights must be greater than 0.")

        # Membership Validation
        while True:
            membership = input("Enter membership type (Gold, Silver, Bronze, None): ").strip().capitalize()
            if membership in ["Gold", "Silver", "Bronze", "None"]: break
            print("❌ Invalid membership. Choose Gold, Silver, Bronze, or None.")

        # Calculations
        base_cost = prices[room_type] * num_rooms * num_nights
        
        mem_disc = {"Gold": 0.5, "Silver": 0.3, "Bronze": 0.2, "None": 0.0}[membership]
        night_disc = 0.1 if num_nights > 5 else 0.0
        final_cost = base_cost * (1 - mem_disc) * (1 - night_disc)
        total_discount = base_cost - final_cost

        # Update Inventory
        inventory[room_type] -= num_rooms

        # Invoice Output
        print("\n" + "="*42 + "\n              FINAL INVOICE\n" + "="*42)
        print(f" Guest Name        : {guest_name}\n Room Type         : {room_type}\n Rooms Reserved    : {num_rooms}\n Nights            : {num_nights}\n Membership        : {membership}")
        print("-" * 42)
        print(f" Base Cost         : ${base_cost:.2f}\n Total Discount    : -${total_discount:.2f}\n Final Total Cost  : ${final_cost:.2f}")
        print("="*42 + f"\n Remaining {room_type} inventory: {inventory[room_type]}\n" + "="*42)

        if input("\nWould you like to process another reservation? (yes/no): ").strip().lower() != 'yes':
            print("\nThank you for using the Hotel Reservation System. Goodbye!")
            break

if __name__ == "__main__":
    hotel_reservation_system()
