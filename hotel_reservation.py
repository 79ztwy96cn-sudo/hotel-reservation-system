# Hotel Reservation System


def hotel_reservation_system():
    """Run the interactive hotel reservation system."""

    # Starting inventory and nightly prices for each room type.
    inventory = {"Single": 5, "Double": 3, "Suite": 2}
    prices = {"Single": 100.0, "Double": 180.0, "Suite": 350.0}

    # Track successful reservations so a summary receipt can be shown at exit.
    reservations = []

    def get_choice(prompt, choices, error_message):
        """Prompt until the user enters one of the allowed choices."""
        while True:
            value = input(prompt).strip().capitalize()
            if value in choices:
                return value
            print(f"❌ {error_message}")

    def get_yes_or_no(prompt):
        """Prompt until the user enters yes or no."""
        while True:
            value = input(prompt).strip().lower()
            if value in ("yes", "no"):
                return value
            print("❌ Please enter 'yes' or 'no'.")

    def get_positive_int(prompt, error_message):
        """Prompt until the user enters a positive whole number."""
        while True:
            try:
                value = int(input(prompt).strip())
                if value > 0:
                    return value
                print(f"❌ {error_message}")
            except ValueError:
                print("❌ Please enter a valid whole number.")

    try:
        while True:
            print("\n" + "=" * 40)
            print("       HOTEL RESERVATION SYSTEM")
            print("=" * 40)
            print("Current Room Availability & Prices:")

            for room, count in inventory.items():
                print(
                    f"- {room} Room: {count} available | "
                    f"Price/Night: ${prices[room]:.2f}"
                )
            print("-" * 40)

            guest_name = input("Enter guest name: ").strip()
            if not guest_name:
                print("❌ Guest name cannot be empty.")
                continue

            room_type = get_choice(
                "Enter room type (Single, Double, Suite): ",
                inventory,
                "Invalid room type. Choose Single, Double, or Suite.",
            )

            # Allow guests to change their selection after initial validation.
            if get_yes_or_no("Would you like to change your room type? (yes/no): ") == "yes":
                room_type = get_choice(
                    "Enter new room type (Single, Double, Suite): ",
                    inventory,
                    "Invalid room type. Try again.",
                )

            num_rooms = get_positive_int(
                "Enter number of rooms to reserve: ",
                "Number of rooms must be greater than 0.",
            )

            # Prevent a reservation if it would exceed remaining inventory.
            if num_rooms > inventory[room_type]:
                print(
                    f"\n⚠️ Sorry! Only {inventory[room_type]} {room_type} "
                    "room(s) available. Reservation failed."
                )
                if get_yes_or_no(
                    "\nWould you like to process another reservation? (yes/no): "
                ) == "no":
                    break
                continue

            num_nights = get_positive_int(
                "Enter number of nights: ",
                "Number of nights must be greater than 0.",
            )

            membership = get_choice(
                "Enter membership type (Gold, Silver, Bronze, None): ",
                ("Gold", "Silver", "Bronze", "None"),
                "Invalid membership. Choose Gold, Silver, Bronze, or None.",
            )

            # Calculate discounts, then update inventory only after success.
            base_cost = prices[room_type] * num_rooms * num_nights
            membership_discounts = {
                "Gold": 0.50,
                "Silver": 0.30,
                "Bronze": 0.20,
                "None": 0.00,
            }
            membership_discount = membership_discounts[membership]
            night_discount = 0.10 if num_nights > 5 else 0.00

            final_cost = (
                base_cost * (1 - membership_discount) * (1 - night_discount)
            )
            total_discount = base_cost - final_cost

            inventory[room_type] -= num_rooms

            reservation = {
                "Guest Name": guest_name,
                "Room Type": room_type,
                "Rooms": num_rooms,
                "Nights": num_nights,
                "Membership": membership,
                "Base Cost": base_cost,
                "Total Discount": total_discount,
                "Final Cost": final_cost,
            }
            reservations.append(reservation)

            print("\n" + "=" * 42)
            print("              FINAL INVOICE")
            print("=" * 42)
            print(
                f" Guest Name        : {guest_name}\n"
                f" Room Type         : {room_type}\n"
                f" Rooms Reserved    : {num_rooms}\n"
                f" Nights            : {num_nights}\n"
                f" Membership        : {membership}"
            )
            print("-" * 42)
            print(
                f" Base Cost         : ${base_cost:.2f}\n"
                f" Total Discount    : -${total_discount:.2f}\n"
                f" Final Total Cost  : ${final_cost:.2f}"
            )
            print("=" * 42)
            print(f" Remaining {room_type} inventory: {inventory[room_type]}")
            print("=" * 42)

            if get_yes_or_no(
                "\nWould you like to process another reservation? (yes/no): "
            ) == "no":
                break

    except KeyboardInterrupt:
        print("\n\n⚠️ Reservation process interrupted by the user.")

    except EOFError:
        print("\n\n⚠️ Input ended unexpectedly.")

    finally:
        print("\n" + "=" * 42)
        print("             SUMMARY RECEIPT")
        print("=" * 42)

        if not reservations:
            print(" No reservations were completed.")
        else:
            grand_total = 0.0
            print(f" Reservations Completed: {len(reservations)}")
            print("-" * 42)

            for number, reservation in enumerate(reservations, start=1):
                print(
                    f" {number}. {reservation['Guest Name']} | "
                    f"{reservation['Room Type']} | "
                    f"{reservation['Rooms']} room(s) x {reservation['Nights']} night(s) | "
                    f"${reservation['Final Cost']:.2f}"
                )
                grand_total += reservation["Final Cost"]

            print("-" * 42)
            print(f" Grand Total       : ${grand_total:.2f}")

        print("=" * 42)
        print(" Thank you for using the Hotel Reservation System.")
        print(" Goodbye!")


if __name__ == "__main__":
    hotel_reservation_system()
