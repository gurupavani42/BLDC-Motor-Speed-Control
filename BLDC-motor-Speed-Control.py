# BLDC-Motor-Speed-Control
# Simple BLDC Motor Speed Control Simulation

target_speed = 1000  # RPM

while True:
    print("\nBLDC Motor Speed Control")
    print("1. Increase speed")
    print("2. Decrease speed")
    print("3. Show speed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        target_speed += 100
        print("Motor speed:", target_speed, "RPM")

    elif choice == "2":
        target_speed -= 100

        if target_speed < 0:
            target_speed = 0

        print("Motor speed:", target_speed, "RPM")

    elif choice == "3":
        print("Current motor speed:", target_speed, "RPM")

    elif choice == "4":
        print("Motor stopped.")
        break

    else:
        print("Invalid choice")
