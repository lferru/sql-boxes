import sqlite3

conn = sqlite3.connect('boxes.db')
cur = conn.cursor()

cur.execute("create table if not exists boxes(name TEXT, colour TEXT, length INTEGER, width INTEGER, height INTEGER)")

menu = "\nMENU\n"\
	"Type \"d\" to delete a row\n"\
	"Type \"i\" to insert a row\n"\
	"Type \'s\' to show all rows\n"\
	"Type \"q\" to quit\n"
ans = input(menu)

while ( ans != "q" ):
	
	if ( ans == "d" ):
		
		n = input("\nEnter the name of the box that you wish to delete: ")
		cur.execute(f"delete from boxes where name = \"{n}\";")
		#conn.commit()
	elif ( ans == "i" ):

		n = input("\nEnter the new box's name: ")
		c = input("Enter the new box's colour: ")
		l = int(input("Enter the new box's length: "))
		w = int(input("Enter the new box's width: "))
		h = int(input("Enter the new box's height: "))
		cur.execute(f"insert into boxes values (\"{n}\", \"{c}\",{l},{w},{h});")
		#conn.commit()
	elif ( ans == "s" ):

                print("\n")
                for row in cur.execute("select * from boxes"):
                    print(row)
                print("\n")
	ans = input(menu)
conn.commit()
conn.close()
print("Thank you and goodbye :)")
