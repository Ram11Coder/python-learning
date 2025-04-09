# Weight converter program

weight = float(input("Enter the weight : "))
units = input("Killograms or Pounds? (K or L) : ")

if units == "K":
    weight *= 2.205
    units = "lbs."
    print(f"Your weight is : {round(weight,1)} {units}")
elif units == "L":
    weight /=2.205
    units = "kgs."
    print(f"Your weight is : {round(weight, 1)} {units}")
else:
    print(f"Enter the {units} is not valid!")