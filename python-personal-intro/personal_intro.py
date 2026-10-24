
# Project: Personal Introduction Program
# Week 1 - Python Basics

print("=" * 40)
print("PERSONAL INTRODUCTION PROGRAM")
print("=" * 40)

# Collect user information
name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
city = input("Enter your city: ").strip()
hobby = input("Enter your favorite hobby: ").strip()
food = input("Enter your favorite food: ").strip()

# Store interests in a list
interests = [hobby, food]

# welcome message
print("\n" + "=" * 40)
print(f"* Welcome, {name}! *")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print(f"Favorite food: {food}")

print(f"\nYour interests are: {interests}")
print(f"Next year, you will be {age + 1} years old.")

print("\nThank you for using my program!")
