# Example Input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

# Example Output
# 171

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# averageHeight = sum(student_heights) / len(student_heights)

# print(round(average_of_height))
total_height = 0
number_of_students = 0

for heights in student_heights:
  total_height += heights
  number_of_students += 1

average_height = total_height / number_of_students
print(round(average_height))
