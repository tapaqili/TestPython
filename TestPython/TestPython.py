import time

h = -1
r = -1
gross_pay = 0.0
attempts = 0

def stop():
    print "Too many failed attempts...exiting"
    time.sleep(5)
    quit()

def overtime_pay(h,r):
	return 40*r + (h-40)*1.5*r
	
def normal_pay(h, r):   
	return 40*r       

while h < 0 | r < 0:
   
    for i in range(0,3):
        attempts = attempts + 1
        try:
            hrs = raw_input("Enter Hours:")
            h = float(hrs)
            if (h < 0):     
               if (attempts > 2):stop()
               else:
                   print "Please enter a number 0 or greater"
                   break 	 

            rate = raw_input("Enter Rate:")
            r = float(rate)    
            if (r < 0):
               if (attempts > 2):stop()
               else:
                   print "Please enter a number 0 or greater"
                   break

        except: 	
              h = -1
              r = -1
              if (attempts > 2):stop()
              else:
                  print "Please enter a numerical value" 
   
if (h > 40):
    gross_pay = overtime_pay(h,r)
    print gross_pay   
else:
    gross_pay = normal_pay(h,r)
    print gross_pay 