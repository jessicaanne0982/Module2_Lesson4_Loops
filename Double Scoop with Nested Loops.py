# Task 1: Your Mood Tracker 
 
import random
 
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["morning", "afternoon", "evening"]
mood = ["happy", "sad", "energetic", "tired", "excited", "content", "overwhelmed", "angry"]
 
# the outer loop should iterate over the days
for day in range(7):
  # the inner loop should iterate over the times of the day
  for time in time_of_day:
    current_mood = random.choice(mood)
    print("On " + days[day] + " " + time + ", you were " + current_mood + ".")