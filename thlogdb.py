#!/usr/bin/python
#
# ===========================================================================
# AM2302 Temperature and Humidity
# -------------------------------
#
# Capture data and store it in a MySQL database
#
# By Pete Tomlinson, 16/05/2014
#
# Adapted from Adafruit script
#
# ==========================================================================

import subprocess
import re
import sys
import time
import datetime
import MySQLdb

# ===========================================================================
# Variables
# ===========================================================================

# pin AM2302 is connected to on your pi
pin = 17

# time (in seconds) to wait between read/insert
wt = 300

# ===========================================================================
# Functions
# ===========================================================================

def WrtLogFile( message ):
        "This function opens the log file, writes to it the message passed \
         to it, then closes the file."

        logfile = open("am2302.txt","ab")
        logfile.write("At " + str(datetime.datetime.now()) + ": " + message + "\n")
        logfile.close
        return



# ===========================================================================
# MySQL Database Details
# ===========================================================================

server  = 'mypi.ca'
user    = 'mypi_wdadmin'
pw      = '#N0m2m0#'
dbname  = 'mypi_wdN0M2M0'

db = MySQLdb.connect(server, user, pw, dbname)
cursor = db.cursor()

# Continuously append data
while(True):
  # Run the DHT program to get the humidity and temperature readings!

  output = subprocess.check_output(["./Adafruit_DHT", "2302", str(pin)]);
  matches = re.search("Temp =\s+([0-9.]+)", output)
  if (not matches):
        time.sleep(3)
        continue
  temp = float(matches.group(1))

  # search for humidity printout
  matches = re.search("Hum =\s+([0-9.]+)", output)
  if (not matches):
        time.sleep(3)
        continue
  humidity = float(matches.group(1))

  # Write data to database
  sql = "INSERT INTO wd_temp_humidity (capturetime, temperature, \
         humidity, sensornumber) VALUES \
         ('%s', '%s', '%s', '%s') " % \
         (datetime.datetime.now(), temp, humidity, 1)

 # Open the data base for writing
  db = MySQLdb.connect(server, user, pw, dbname)
  cursor = db.cursor()

  try:
    cursor.execute(sql)
    db.commit()
    db.close()
    WrtLogFile( sql + " <--SUCCEEDED" )
  except:
    db.rollback()
    db.close()
    WrtLogFile( sql + " <--FAILED" )

  # Wait for wt seconds
  time.sleep(wt)
else:
  db.close()
