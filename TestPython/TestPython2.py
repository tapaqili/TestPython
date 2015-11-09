
# Program to determine maximum and minimum values

list_ = [];
flag = 0
count = 0
largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : 
        break
    else:    
        try:
           n = float(num)
           #print num
        except:
           print "Invalid input" 
           continue

        #list_[count] = n
        list_.append(n); 
        count = count + 1    
 
if count > 0:

   largest = list_[0]
   smallest = list_[0]

   for i in range(0,count): 
       if list_[i] >= largest:
           largest = list_[i]
       if list_[i] <= smallest:
           smallest = list_[i] 
             
   print "Maximum", largest
   print "Minimum", smallest
else:
    print "no number was input"