import psycopg2

# Update this part according to your own database!!!
connection = psycopg2.connect(database="***", user="postgres", password="***", host="127.0.0.1", port="5432")

cursor = connection.cursor()

# This part is given as an example for the query of the first question. 
# For other questions, please add the necessary code pieces to the specified places!!!

# Question-1
print str('Question-1')
cursor.execute("Write your query here.")

rows = cursor.fetchall()
print ('ORDERID\t TotalPrice\t TotalwithDiscountPrice')
for row in rows:
    print(str(row[0]) + " \t " + str(row[1]) + " \t " + str(row[2]))

# Question-2
print str('Question-2')

# Write your piece of code as in Question-1

# Question-3
print str('Question-3')

# Write your piece of code as in Question-1

# Question-4
print str('Question-4')

# Write your piece of code as in Question-1

# Question-5
print str('Question-5')

# Write your piece of code as in Question-1

# Question-6
print str('Question-6')

# Write your piece of code as in Question-1

# Question-7
print str('Question-7')

# Write your piece of code as in Question-1

# Question-8
print str('Question-8')

# Write your piece of code as in Question-1
	
connection.commit()
connection.close()