bill_amt=int(input("Enter bill amount: "))
mem_type=input("Enter membership type: ")

def calc_final_price(bill_amt,mem_type):

    def get_discount(mem_type):
        discount=0
        if mem_type=="platinum":
            discount=0.25
        elif mem_type=="gold":
            discount=0.20
        elif mem_type=="silver":
            discount=0.10
        return discount
    discount=get_discount(mem_type)
    final_amt=bill_amt-(bill_amt*discount)
    return final_amt
final_bill_amt=calc_final_price(bill_amt,mem_type)
print(final_bill_amt)

        