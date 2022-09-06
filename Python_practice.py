
#What is the score?
score = int(input("what is your test score?"))

#Determine the grade 
if score >= 90:
    print('Your grade is an A')
elif score >= 80:
    print('Your grade is a B')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

#Loop Practice 

x=0
while x <= 5:
    print(x)
    x=x+1
    
# List practice 
counties=["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
    print("El Pas is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

for county in counties:
    print(county)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

voting_data=[{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 43238}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county, voters in counties_dict.items():
    print(county + "county has" + str(voters) + "registered voters.")

my_votes=int(input("How many votes did you get in the election?"))
total_votes=int(input("What is the total votes in the election?"))
percentage_votes=(my_votes/total_votes)*100
print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes=int(input("How many votes did you get in the election?"))
total_votes= int(input("What is the total votes in the election?"))
print(f"I received {my_votes/total_votes *100}% of the total votes.")

counties_dict={"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes= int(input("How many votes did the candidate get in the election?"))
total_votes= int(input("What is the total number of votes in the election?"))
message_to_candidate= (
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes/ total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")


# Import the datetime class from the datetime module

import datetime as dt

# Use the now() attribute on the datetime class to get the present time 
now = dt.datetime.now()

# Print the present time 
print("The time right now is ", now)

