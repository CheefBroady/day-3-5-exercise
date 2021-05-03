# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


T_counter = name1.lower().count("t")
T_counter += name2.lower().count("t")
# print(f"T occurs {T_counter} times")
R_counter = name1.lower().count("r")
R_counter += name2.lower().count("r")
# print(f"R occurs {R_counter} times")
U_counter = name1.lower().count("u")
U_counter += name2.lower().count("u")
# print(f"U occurs {U_counter} times")
E_counter = name1.lower().count("e")
E_counter += name2.lower().count("e")
# print(f"E occurs {E_counter} times")




L_counter = name1.lower().count("l")
L_counter += name2.lower().count("l")
# print(f"L occurs {L_counter} times")
O_counter = name1.lower().count("o")
O_counter += name2.lower().count("o")
# print(f"O occurs {O_counter} times")
V_counter = name1.lower().count("v")
V_counter += name2.lower().count("v")
# print(f"V occurs {V_counter} times")
E_counter = name1.lower().count("e")
E_counter += name2.lower().count("e")
# print(f"E occurs {E_counter} times")

true_sum = T_counter + R_counter + U_counter + E_counter
# print(f"True-Buchstaben sind {true_sum}")
love_sum = L_counter + O_counter + V_counter + E_counter
# print(f"Love-Buchstaben sind {love_sum}")


sumup = str(true_sum) + str(love_sum)
sumup = int(sumup)


if sumup < 10 or sumup > 90:
  print(f"Your score is {sumup}, you go together like coke and mentos.")
elif sumup >= 40 and sumup <= 50:
  print(f"Your score is {sumup}, you are alright together.")
else:
  print(f"Your score is {sumup}.")


