bill_amt=int(input("enter bill amount:"))
mem_type=input("enter member ship type:")

def cal_final_price(bill_amt,mem_type):
    def get_discount(mem_type):
        if(mem_type=="platinam"):
            discount=0.25
        elif(mem_type=="gold"):
            discount=0.20
        elif(mem_type=="silver"):
            discount=0.10
        else:
            discount=0
        return discount
    
    discount=get_discount(mem_type)
    final_amt=bill_amt-(bill_amt*discount)
    return final_amt

final_bill_amt=cal_final_price(bill_amt,mem_type)
print("final bill amount is:",final_bill_amt)