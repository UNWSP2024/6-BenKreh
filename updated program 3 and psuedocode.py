#pseudocode
#Get the total sales from the user
#share this number with others
#take the number * 0.05
#print that the above number is state tax
#take the number * 0.025
#print that the above number is country tax
#take the number again times it by 0.5 and 0.025 then add them together
#print that the above number is the total tax and





#Ben Krehbiel
#2/24/2025
#taxes :skull:

def get_sales():
    total_sales = float(input("Please input the total sales this month :$"))
    return total_sales


def state_tax(total_sales):
    s_tax = total_sales * 0.05
    print("state tax will be:$", s_tax)

def country_tax(total_sales):
    c_tax = total_sales * 0.025
    print("country tax will be:$", c_tax)

def total_tax(total_sales):
    t_tax = round(total_sales * (0.025 + 0.05), 2)
    print("Total taxes: $", t_tax)

#mainline

sales = get_sales()
state_tax(sales)
country_tax(sales)
total_tax(sales)
