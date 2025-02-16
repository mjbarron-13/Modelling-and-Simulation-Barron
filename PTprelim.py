# Electricity Cost Estimator with Appliance Editing AFTER Displaying Consumption

def calculate_electricity_cost(appliances, tariff):
    total_energy_kwh = 0  
    appliance_details = []  

    for appliance in appliances:
        name, power_watts, hours_per_day = appliance
        energy_kwh = (power_watts * hours_per_day) / 1000  
        cost = energy_kwh * tariff  
        total_energy_kwh += energy_kwh  
        appliance_details.append((name, power_watts, hours_per_day, energy_kwh, cost))  
    
    total_cost = total_energy_kwh * tariff  
    return total_energy_kwh, total_cost, appliance_details

# Get electricity rate
electricity_tariff = float(input("Enter electricity rate (cost per kWh in PHP): "))

# User enters multiple appliances
print("\nEnter appliance details in the format: Name Power(W) Hours_per_day, separated by commas.")
print("Example: TV 100 5, Aircon 1800 8, Refrigerator 160 24\n")
user_input = input("Enter all appliances: ")

# Process input string
appliances = []
entries = user_input.split(",")

for entry in entries:
    data = entry.strip().split()
    name = " ".join(data[:-2])  
    power_watts = float(data[-2])  
    hours_per_day = float(data[-1])  
    appliances.append((name, power_watts, hours_per_day))  

while True:  
    # Compute and display the results
    total_energy, estimated_cost, appliance_details = calculate_electricity_cost(appliances, electricity_tariff)

    print("\nElectricity Consumption per Appliance:")
    for i, (name, power, hours, energy_kwh, cost) in enumerate(appliance_details):
        print(f"{i + 1}. {name}: {energy_kwh:.2f} kWh, Cost: ₱{cost:.2f}")

    print("\nTotal Energy Consumption:", f"{total_energy:.2f} kWh")
    print("Estimated Monthly Cost:", f"₱{estimated_cost * 30:.2f}")  

    # Ask if the user wants to modify an appliance AFTER showing consumption
    edit_choice = input("\nDo you want to modify an appliance? (yes/no): ").strip().lower()

    if edit_choice != "yes":
        break  

    appliance_index = int(input("Enter the number of the appliance to modify: ")) - 1

    if 0 <= appliance_index < len(appliances):
        name, power_watts, hours_per_day, _, _ = appliance_details[appliance_index]

        new_power = input(f"Enter new power for {name} in watts (or press Enter to keep {power_watts}W): ").strip()
        new_hours = input(f"Enter new daily usage for {name} in hours (or press Enter to keep {hours_per_day}h): ").strip()

        power_watts = float(new_power) if new_power else power_watts  
        hours_per_day = float(new_hours) if new_hours else hours_per_day  

        appliances[appliance_index] = (name, power_watts, hours_per_day)
