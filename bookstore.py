header = '''\t\tBookstore Receipt
\t\t   Trivandrum
\t----------------------------------------\n\n'''

book1_title = "Python Basics"
book1_price = 450

book2_title="Data Science Intro" 
book2_price = 600

print(header)
book_info = "\t{}-----₹{}"
book1_format=book_info.format(book1_title,book1_price)
book2_format=book_info.format(book2_title,book2_price)

total_cost = 450 + 600
cost_format = "\tTotal Amount:-----₹{}"
final_cost=cost_format.format(total_cost)

thankYou = "\tThank You for shopping with us!!!\n"

full_receipt = (
    header + 
    book1_format + "\n" + 
    book2_format + "\n\n" + 
    "\t----------------------------------------\n" + 
    final_cost + "\n" + 
    "\t----------------------------------------\n\n" +
    thankYou
)

print(full_receipt.upper())





