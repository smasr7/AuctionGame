# student_score = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione" : 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
# for key in student_score:
#     value = student_score[key]
#     grade = ""
#     if value > 90:
#         grade = "Outstanding"
#     elif 80 < value <= 90:
#         grade = "Excellent"
#     elif 70 < value <= 80:
#         grade = "Critical"
#     else:
#         grade = "Failed"
#     student_grades[key] = grade
# print(student_grades)
##############################################
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country, visits, cities):
#     travel_log.append({"country": country, "visits": visits, "cities": cities})
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# add_new_country("Brazil", 4, ["Brasil", "Rio de Janeiro"])
# print(travel_log[3]["cities"][0])
#####################################################################################3
#Secret Auction Program
from art import logo

print(logo)
print("Welcome to the Auction Program")
auction = {}
name = input("What is your name?\n")
bid = input("What is your bid?\n$")
auction[name] = bid
while True:
    ans = input("Type 'yes' to continue, or 'no' to quit\n")
    if ans == "yes":
        name = input("What is your name?\n")
        bid = input("What is your bid?\n$")
        auction[name] = bid
    if ans == "no":
        break
BB = 0
winner = ""
for name in auction:
    if int(auction[name]) > BB:
        BB = int(auction[name])
        winner = name
print(f"{winner} won with the value of ${BB}.")
