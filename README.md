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

1) MySQL Server. There are lots of good tutorials for installing MySQL for the Pi, so go forth and Google. Or, if you already have a MySQL Server, skip to instruction 2.

2) A database in the MySQL Server with a database and user that you can connect to and execute INSERT statements against. You will need a table with the four following columns, which have self-explanatory names:
          
              capturetime, temperature, humidity, sensornum
              
   I decided to include a sensornum column in the event you are capturing data from more than one sensor (i.e. one indoors    and one outdoors).
   
   A stand-alone table would have a create script like this:
   
              CREATE TABLE `wd_temp_humidity` (
                           `id` int(11) NOT NULL AUTO_INCREMENT,
                           `capturetime` datetime DEFAULT NULL,
                           `temperature` decimal(5,1) DEFAULT NULL,
                           `humidity` decimal(5,1) DEFAULT NULL,
                           `sensornumber` int(11) NOT NULL,
                           PRIMARY KEY (`id`)
                          )

3) Python Library MySQLdb for connecting your python script to your database. I installed the library on my Pi using apt-get:

              sudo apt-get install python-mysqldb
             
             
