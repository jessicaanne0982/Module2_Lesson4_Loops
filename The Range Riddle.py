# Task 1
 
import random
 
mood = ["happy", "sad", "energetic", "tired", "excited"]
 
for day in range(7):
  mood_today = random.choice(mood)
  if day == 0:
    print(f"Your mood on Sunday was {mood_today}.")
  elif day == 1:
    print(f"Your mood on Monday was {mood_today}.")
  elif day == 2:
    print(f"Your mood on Tuesday was {mood_today}.")
  elif day == 3:
    print(f"Your mood on Wednesday was {mood_today}.")
  elif day == 4:
    print(f"Your mood on Thursday was {mood_today}.")
  elif day == 5:
    print(f"Your mood on Friday was {mood_today}.")
  elif day == 6:
    print(f"Your mood on Saturday was {mood_today}.")