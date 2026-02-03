 #Just input the Amount of an item you want, and how many you get per run, and it will tell you how many runs you need to do to get that amount

#Variables
total_needed = int(input("Enter the total amount of the resource you want: \n"))
per_run = int(input("Enter how many you get per run: \n"))
runs = -(-total_needed // per_run)  # Ceiling division so it rounds up
print(f"You need to do {runs} runs to get at least {total_needed} resources.")
