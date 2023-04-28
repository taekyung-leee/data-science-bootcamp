swimming = int(input("Enter minutes you have taken for swimming:"))
cycling = int(input("Enter minutes you have taken for cycling:"))
running = int(input("Enter minutes you have taken for running:"))

total_time = int(swimming + cycling + running)

print (total_time)

if (total_time <= 100):
    print("You have finished within qualifying time. You are awarded Provincial Colours.")

elif total_time <= 105 and total_time > 100:
    print("You have finished within 5 minutes of qualifying time. You are awarded Provincial Half Colours")

elif total_time <= 110 and total_time > 105:
    print("You have finished within 10 minutes of qualifying time. You are awarded Provincial Scroll.")

elif total_time > 110:
    print("You have finished 10 minutes past qualifying time. You have no award.")   