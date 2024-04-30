#Task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


#Task 2

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
facilities = "audio system and a projector" if attendees > 50 else "projector"

print(venue)
print(facilities)


#Task 3

preference = input("Do you want vegetarian food? (Yes/No)")

if preference == "Yes":
    print("The Veggie Delight Caterers have great reviews.")
else:
    print("Gourmet Meals Caterers are good too.")