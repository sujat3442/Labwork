#checking which will be faster
#taking 1 miles = 1609.344m
distance1=4*1609.344
speed1=(25*1609.344)/(60*60)
time1=distance1/speed1
totaltime1=time1+(2*10)

#checking the time taken by running
#the first condition on speed 7mph
dis1=1609.344
pace1=(7*1609.344)
duration1=dis1/pace1
#second condition on 15 mph
dis2=2*1609.344
pace2=(15*1609.344)/(60*60)
duration2=dis2/pace2
#third condition on 7mph
dis3=1609.344
pace3=(7*1609.344)
duration3=dis3/pace3
#total time taken by running is
totaltime2=duration1+duration2+duration3

#checking taking bus is faster or by bus
if totaltime1<totaltime2:
    print("by bus is faster")
else:
    print("by running is faster")