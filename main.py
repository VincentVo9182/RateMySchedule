# Back-end structure for our project

# RateMySchedule
#   Public forum where users post their schedule and other users can comment/give advice.
#   Schedule is rated by users under feasibility and balance.
#   People have anonymous profiles to comment and post
#   User input information (major)/algorithm more likely to see similar schedules
#   What schedules you see are weighted based on college and major
#   Scrape UT registration for upcoming semester schedule


# Class Variables:
#   First Name, Last Name, UT EID --> If we only get their EID, UT Directory can get first and last name
#   Classification (Year) and Major can be found on UT Directory using EID --> Can we implement this?
#   Classification can be changed because UT can have it wrong
#   Minor, UT Directory cannot grab this for us, prompt user for it
#   Profile Picture?? Display name (adjectiveAnimal for anonymity)

#   Privacy flag
#   Opt into sharing your profile to automatically match with other people in your classes




# Creating an Account
#   User implements their UT EID, scrape UT Directory for the other information if valid EID
#   If valid, EID will become their username, display the Directory information for users to verify
#   If verified, prompt password creation for account (SSO would be better)
#   Prompt user for minor classifications



# Uploading your Schedule
#   User inputs 
#   Store the schedule uploaded as a file
#   Ask user if this is their finalized, already registered schedule
#       If this is their finalized schedule, check privacy flag
#       If privacy flag allows it, automatically match them with others in their class
#       If this is not their finalized schedule, (alternate schedule)



# Credits