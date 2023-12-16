H = int(input("Enter the height of Person in cm: "))
W = int(input("Enter the weight of Person in kg : "))
H_in_meters = H * 0.01
BMI = W / (H_in_meters)**2
print(f'Body Mass of person is {BMI}')
if BMI > 24.9:
    print("Start Working Out! You Lazy")
elif BMI < 18.5:
    print("Work Hard! Build Some Strength")
else:
    print("Keep it Up Buddy!")
