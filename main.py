# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0
count = 0
for height in student_heights:
  # count each number in array
  count += 1
  # Get sum of every number in array
  total += height

# calculate average 
avg = round(total / count)
print(avg)



