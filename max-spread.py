def max_spread():
   '''
      Create a function that reads data from the weather.dat file and calculates the maximum spread (Mxt-MnT) 
     then prints it on the terminal 
    ''' 
   with open('weather.dat') as data:

    #Skip the first two lines (header and empty array) 
     next(data)
     next(data)
     
     #initialize the max spread variable to 0
     max_spread = 0
     
     for line in data:

      #split the rows into lists
       row = line.split()

      #strip the *  from the min and max values and remain with numeric characters 
       maxTemp = float(row[1].strip('*'))
       minTemp = float(row[2].strip('*')) 

      #strip the *  from the min and max values and remain with numeric characters 
       spread = (maxTemp - minTemp)
       
       #compare the maxspread and the difference between MxT and MnT
       if spread > max_spread:
         max_spread = spread
         day = row[0] 

         
   print (day, max_spread)

   
if __name__ == "__main__":
  max_spread() 
