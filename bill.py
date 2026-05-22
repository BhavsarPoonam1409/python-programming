units = int (input("Enter number of units:"))
slab1=0
slab2=0
slab3=0
slab4=0
total=0
final_bill_amount=0

if (units<=50):
    slab1=units * 0.50
elif (units>=51 and units<=150):
    slab2=(50*0.50) + ((units - 50)*0.75)
elif (units>=151 and units<=250):
    slab3=(50*0.50) + (100*0.75) + ( units-150 *1.20)
else:
    slab4=(50*0.50) + (100*0.75) + (100*1.20) + ( (units-250)*1.50)
total = slab1 + slab2 + slab3 + slab4   
surcharge=(total*0.20)
final_bill_amount = total + surcharge
print("final bill amount:" ,final_bill_amount , surcharge)