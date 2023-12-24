#checks for after gregorian calender. i.e., after 1582

year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
   if year%4==0:
       print("Leap year")
   elif year%4!=0:
       print("Common year")
	
