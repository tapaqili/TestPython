import time

h = -1
r = -1
gross_pay = 0.0
attempts = 0

def stop():
    print "Too many failed attempts...exiting"
    time.sleep(5)
    #quit()
    exit()

def computepay(h,r):
    gross_pay = 0.0
    if (h > 40):
        gross_pay = 40*r + (h-40)*1.5*r
    else:
        gross_pay = 40*r
        
    return gross_pay  

#Can't quite figure out how to fix this while loop
#while (h < 0) or (r < 0):
   
for attempts in range(1,4):
        #attempts = attempts + 1
        try:
            hrs = raw_input("\n\nEnter Hours:")
            h = float(hrs)
            if (h < 0):     
               if (attempts > 2):
                   stop()
                   #print "why are we here"
               else:
                   print "Please enter a number 0 or greater"
                   continue
                   #break 	 

            rate = raw_input("\n\nEnter Rate:")
            r = float(rate)    
            if (r < 0):
               if (attempts > 2):stop()
               else:
                   print "Please enter a number 0 or greater"
                   continue
            else:
                break  #we have satisfied all our conditions we do not need to go through the loop again

        except: 	
              h = -1
              r = -1
              if (attempts > 2):stop()
              else:
                  print "Please enter a numerical value" 
   
pay = computepay(h,r)
print pay
