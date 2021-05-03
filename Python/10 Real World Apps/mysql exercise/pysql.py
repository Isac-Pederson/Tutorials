import mysql.connector

#Not putting in a .env folder for this short tutorial 

cursor = con.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    print("no word found")