AM2302-MySQL-Logger
===================

Log data captured from AM2302 into a MySQL database using a Raspberry Pi

This script is based heavily on the Adafruit scripts found at:
https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview

Follow of the the Adafruit instructions to make your newly-minted temperature & humidity sensor work with python and Google docs spreadsheets. You will likely need to use an older version of Google speadsheets; the lateest iteration of spreadsheet does not seem to function with gspread, the python library for writing to google docs spreadsheets.

Look in the forum for more information re. the older google docs.

Once you have that working, you will have most the crucial components, including knowledge of the sensor and how it is integrated into python.

What you Need
=============

1) MySQL and a database. There are lots of good tutorials for acquiring, installing, and configuring MySQL for the Pi, so I won't waste time here with an example.
