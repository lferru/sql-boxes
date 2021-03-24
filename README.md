# sql-touhou
An SQL demo

This is a script that interfaces with a simple SQLite database, touhou.db, which contains one table, CHARACTERS.
CHARACTERS has the columns name, colour, age, height, image, music.
There are six operations: delete a single row, add a single row, display all rows, display an image, play a music file, and quit the script.

To run the script, enter the following in your shell:

python3 sql-touhou.py

As of now, this script requires the PIL, sqlite3, and subprocess modules. It also assumes you have the vlc and display (a part of ImageMagick) commands available on your terminal.

The characters in this database are from the Touhou video game series.
