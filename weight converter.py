print("=== Weight Converter ===")

while True:
    try:
        weight = float(input("\nEnter your weight (number only): "))
        unit = input("Enter unit (K for kilograms, L for pounds): ").strip().upper()

        if unit == "K":
            print(f"\n{weight} kg = {weight * 2.20462:.2f} lbs")
        elif unit == "L":
            print(f"\n{weight} lbs = {weight / 2.20462:.2f} kg")
        else:
            print("Please enter only 'K' or 'L' for the unit.")
            continue

        another = input("\nConvert another? (Y/N): ").strip().upper()
        if another != 'Y':
            print("\nGoodbye!")
            break

    except ValueError:
        print("Invalid weight. Please enter a number.")