import sqlite3
#import vlc
import subprocess
from PIL import Image
conn = sqlite3.connect('touhou.db')
cur = conn.cursor()

cur.execute("create table if not exists character(name TEXT, colour TEXT, height INTEGER, image TEXT, music TEXT)")

menu = "\nMENU\n"\
	"Type \"d\" to delete a row\n"\
	"Type \"D\" to delete all rows\n"\
	"Type \"i\" to insert a row\n"\
	"Type \"s\" to show all rows\n"\
	"Type \"p\" to display an image\n"\
	"Type \"m\" to play a music file\n"\
	"Type \"q\" to quit\n"
ans = input(menu)

while ( ans != "q" ):
	
	if ( ans == "d" ):
		
		n = input("\nEnter the name of the character that you wish to delete: ")
		cur.execute(f"delete from character where name = \"{n}\";")
		#conn.commit()
	elif ( ans == "D" ):
		
		cur.execute("delete from character;")
		print("All characters have been deleted.")
	elif ( ans == "i" ):

		n = input("\nEnter the new character's name: ")
		c = input("Enter the new character's hair colour: ")
		h = int(input("Enter the new character's height (cm): "))
		p = input("Enter the new character's image's filename: ")
		m = input("Enter the new character's theme music's filename: ")
		cur.execute(f"insert into character values (\"{n}\", \"{c}\",{h},\"{p}\",\"{m}\");")
		#conn.commit()
	elif ( ans == "s" ):

                print("\n")
                for row in cur.execute("select * from character"):
                   		print(row)
                print("\n")
	elif ( ans == "p" ):
		
		n = input("\nEnter the name of the character whose picture you'd like to see: ")
		displaying = []
		for row in cur.execute(f"select image from character where name == \"{n}\""):
			#m = Image.open(row[0])
			p = subprocess.Popen(["display", row[0]])
			displaying.append(p)
			#m.show()
		print("Press Enter to close the picture")
		n = input()
		for i in displaying:
			#i.close()
			i.kill()
	elif ( ans == 'm' ):
		
		n = input("\nEnter the name of the character whose theme music you'd like to listen to: ")
		playing = []
		for row in cur.execute(f"select music from character where name == \"{n}\""):
			#m = vlc.MediaPlayer(f"{row[0]}")
			#m.play()
			m = subprocess.Popen(["vlc", row[0]])
			playing.append(m)
		print("Press Enter to stop the music")
		n = input()
		for i in playing:
			#i.stop()
			i.kill()
	ans = input(menu)
conn.commit()
conn.close()
print("Thank you and goodbye :)")
