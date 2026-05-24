import matplotlib.pyplot as plt
import pandas as pd

# 01: Create a line plot, Add a little and axis labels to graph?
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
# plt.show()

# 02: Write code to create following data frame?
data = {
    'Name': ['Adil', 'Aysha', 'Hamid', 'Alice', 'Ali'],
    'Age': [20, 30, 28, 29, 26],
    'City': ['Karachi', 'Lahore', 'Faisalabad', 'Islamabad', 'Multan'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male']
}
df = pd.DataFrame(data)
# print(df)

# 03: Write a code to create csv file name students.csv?
students_data = {
    'Name': ['Adil', 'Aysha', 'Hamid', 'Alice', 'Ali'],
    'Age': [20, 30, 28, 29, 0],
    'City': ['Karachi', 'Lahore', 'Faisalabad', 'Islamabad', 'Multan'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male']
}
students_df = pd.DataFrame(students_data)
students_df.to_csv('students.csv')
# print("Students data saved to 'students.csv'")
df = pd.read_csv('students.csv')
# print(df)

# 04: Write code to print only the name column from the students.csv file?
students_df = pd.read_csv('students.csv')
# print(students_df['Name'])

# 05: Print student whose males are greater than 28?
students_df = pd.read_csv('students.csv')
filtered_students = students_df[(students_df['Gender'] == 'Male')]
# print(filtered_students)


# 06: Replace missing values with 0?
students_df = pd.read_csv('students.csv')
students_df_filled = students_df.fillna(0)
# print(students_df_filled)

# 07: Create a bar chart?
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 20]
plt.bar(categories, values)
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()