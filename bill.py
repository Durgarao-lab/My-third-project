import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date

# ---------- AUTO INVOICE NUMBER ----------
def get_invoice_no():
    try:
        with open("invoice_no.txt", "r") as f:
            no = int(f.read())
    except:
        no = 0
    no += 1
    with open("invoice_no.txt", "w") as f:
        f.write(str(no))
    return no


# ---------- PDF INVOICE ----------
def generate_pdf(invoice_no, cust_id, name, phone, address,
                 item_details, total_cost, discount, final_price):

    pdf_name = f"Invoice_{invoice_no}.pdf"
    c = canvas.Canvas(pdf_name, pagesize=A4)
    width, height = A4
    today = date.today().strftime("%d-%m-%Y")

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height-50, "RANGE MEN'S WEAR")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, height-70, "Complete Men's Wear")
    c.drawCentredString(width/2, height-85, "Jaggampeta, Andhra Pradesh")
    c.drawCentredString(width/2, height-100, "Contact: 9848863447 | Email:rangemens@gmail.com")

    # Invoice info
    c.setFont("Helvetica", 10)
    c.drawString( 50, height-120, f"Invoice No : {invoice_no}")
    c.drawRightString(width-50, height-120, f"Date : {today}")

    # Customer details
    c.drawString(50, height-150, f"Customer ID : {cust_id}")
    c.drawString(50, height-170, f"Customer Name : {name}")
    c.drawString(50, height-190, f"Customer Phone NO : {phone}")
    c.drawString(50, height-210, f"Customer Address : {address}")

    # Table header
    y = height - 260
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Item")
    c.drawString(220, y, "Qty")
    c.drawString(270, y, "Rate")
    c.drawString(350, y, "Amount")
    c.line(50, y-5, width-50, y-5)

    # Table rows
    c.setFont("Helvetica", 11)
    y -= 25
    for item, qty, rate, amt in item_details:
        c.drawString(50, y, item)
        c.drawString(220, y, str(qty))
        c.drawString(270, y, str(rate))
        c.drawString(350, y, str(amt))
        y -= 18

    # Totals
    y -= 10
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, f"Total Cost : ₹ {total_cost}")

    if discount > 0:
        c.drawString(50, y-20, f"Discount : {discount}%")
        c.drawString(50, y-40, f"Final Amount : ₹ {int(final_price)}") 
        

   # Footer
    c.setFont("Helvetica-Oblique", 11)
    c.drawCentredString(
        width / 2,
        y - 120,
        "Thank you for shopping with us! Visit Again."
    )

    c.drawRightString(
        width - 50,
        y - 150,
        "Authorised Signatory"
    )
   
    c.save()
    print(f"📄 PDF Invoice Created → {pdf_name}")
    
# MAIN PROGRAM
print("1. Generate Invoice")
print("2. Scan Invoice")
main_choice = int(input("Enter choice (1/2): "))

# GENERATE INVOICE
if main_choice == 1:

    invoice_no = get_invoice_no()
    cust_id = input("Customer ID: ")
    name = input("Customer Name: ")
    phone = int(input("Customer Phone: "))
    address = input("Customer Address: ")

    print("\nItems available:")
    print("1. Only Shirt")
    print("2. Only Pant")
    print("3. Only Inner Wear")
    print("4. Shirt + Pant")
    print("5. Shirt + Pant + Inner Wear")
    print("6. 2 Shirts + 2 Pants")
    print("7. T-Shirt + Tracks")
    print("8. Only T-Shirt")
    print("9. 2 T-Shirts")
    print("10. Only Track Pant")
    print("11. 2 Tracks")
    print("12. T-Shirt + Shorts")
    print("13. 2 T-Shirts + 2 Shorts")
    print("14. Only Shorts")
    print("15. 2 Shorts")
    print("16. 2 T-Shirts")

    #MULTIPLE CHOICE INPUT ikada comma separated values ivvandi, example: 1 or 1,4,8
    choices = input("Enter your choice(s) (ex: 1 or 1,4,8): ")
    choice_list = [int(c.strip()) for c in choices.split(",")]

    item_details = []
    total_cost = 0

    for choice in choice_list:

        # 1
        if choice == 1:
            company1 = input("Shirt Company: ")
            r = int(input("Rate: "))
            q = int(input("Quantity: "))
            a = r * q
            item_details.append((f"{company1}Shirt", q, r, a))
            total_cost += a
            company = company1

        # 2
        elif choice == 2:
            company1 = input("Pant Company: ")
            r = int(input("Rate: "))
            q = int(input("Quantity: "))
            a = r * q
            item_details.append((f"{company1}Pant", q, r, a))
            total_cost += a
            company = company1

        # 3
        elif choice == 3:
            company1 = input("Inner Wear Company: ")
            r = int(input("Rate: "))
            q = int(input("Quantity: "))
            a = r * q
            item_details.append((f"{company1}Inner Wear", q, r, a))
            total_cost += a
            company = company1

        # 4
        elif choice == 4:
            company1 = input("Shirt Company: ")
            r1 = int(input("Shirt Rate: "))
            company2 = input("Pant Company: ")
            r2 = int(input("Pant Rate: "))
            item_details += [
                (f"{company1} (Shirt)", 1, r1, r1),
                (f"{company2} (Pant)", 1, r2, r2)
            ]
            total_cost += r1 + r2
            company = f"{company1}Shirt + {company2}Pant"

        # 5
        elif choice == 5:
            company1 = input("Shirt Company: ")
            r1 = int(input("Shirt Rate: "))
            company2 = input("Pant Company: ")
            r2 = int(input("Pant Rate: "))
            company3 = input("Inner Wear Company: ")
            r3 = int(input("Inner Wear Rate: "))
            item_details += [
                (f"{company1} (Shirt)", 1, r1, r1),
                (f"{company2} (Pant)", 1, r2, r2),
                (f"{company3} (Inner Wear)", 1, r3, r3)
            ]
            total_cost += r1 + r2 + r3
            company = f"{company1}Shirt + {company2}Pant + {company3}Inner Wear"

        # 6
        elif choice == 6:
            for label in ["Shirt", "Shirt", "Pant", "Pant"]:
                company1 = input(f"{label} Company: ")
                r = int(input("Rate: "))
                item_details.append((f"{company1} {label}", 1, r, r))
                total_cost += r
                company = company1

        # 7
        elif choice == 7:
            company1 = input("T-Shirt Company: ")
            r1 = int(input("T-Shirt Rate: "))
            company2 = input("Tracks Company: ")
            r2 = int(input("Tracks Rate: "))
            item_details += [
                (f"{company1} T-Shirt", 1, r1, r1),
                (f"{company2} Tracks", 1, r2, r2)
            ]
            total_cost += r1 + r2
            company = f"{company1} T-Shirt + {company2} Tracks"

        # 8
        elif choice == 8:
            company1 = input("T-Shirt Company: ")
            r = int(input("Rate: "))
            q = int(input("Quantity: "))
            a = r * q
            item_details.append((f"{company1} T-Shirt", q, r, a))
            total_cost += a
            company = company1

        # 9
        elif choice == 9:
            for i in range(2):
                company1 = input(f"T-Shirt {i+1} Company: ")
                r = int(input("Rate: "))
                item_details.append((f"{company1} T-Shirt", 1, r, r))
                total_cost += r
                company = company1

        # 10
        elif choice == 10:
            company1 = input("Tracks Company: ")
            r = int(input("Rate: "))
            q = int(input("Quantity: "))
            a = r * q
            item_details.append((f"{company1} Tracks", q, r, a))
            total_cost += a
            company = company1

        # 11
        elif choice == 11:
            for i in range(2):
                company1 = input(f"Tracks {i+1} Company: ")
                r = int(input("Rate: "))
                item_details.append((f"{company1} Tracks", 1, r, r))
                total_cost += r
                company = company1

        # 12
        elif choice == 12:
            company1 = input("T-Shirt Company: ")
            r1 = int(input("Rate: "))
            company2 = input("Shorts Company: ")
            r2 = int(input("Rate: "))
            item_details += [
                (f"{company1} T-Shirt", 1, r1, r1),
                (f"{company2} Shorts", 1, r2, r2)
            ]
            total_cost += r1 + r2
            company = f"{company1} T-Shirt + {company2} Shorts"

        # 13
        elif choice == 13:
            for label in ["T-Shirt", "T-Shirt", "Shorts", "Shorts"]:
                company1 = input(f"{label} Company: ")
                r = int(input("Rate: "))
                item_details.append((f"{company1} {label}", 1, r, r))
                total_cost += r
                company = company1

        # 14
        elif choice == 14:
            company1 = input("Shorts Company: ")
            r = int(input("Rate: "))
            q = int(input("Quantity: "))
            a = r * q
            item_details.append((f"{company1} Shorts", q, r, a))
            total_cost += a
            company = company1

        # 15
        elif choice == 15:
            for i in range(2):
                company1 = input(f"Shorts {i+1} Company: ")
                r = int(input("Rate: "))
                item_details.append((f"{company1} Shorts", 1, r, r))
                total_cost += r
                company = company1

        # 16
        elif choice == 16:
            for i in range(2):
                company1 = input(f"T-Shirt {i+1} Company: ")
                r = int(input("Rate: "))
                item_details.append((f"{company1} T-Shirt", 1, r, r))
                total_cost += r
                company = company1

    discount = 0
    if input("Apply discount (y/n): ").lower() == "y":
        discount = int(input("Choose Discount U Want To Apply%: "))

    final_price = total_cost - (total_cost * discount / 100)

    generate_pdf(invoice_no, cust_id, name, phone, address,
                 item_details, total_cost, discount, final_price)
    
# Save invoice record to text file
    with open("invoices.txt", "a") as file:
        file.write("\n---INVOICE START---\n")
        file.write(f"Invoice No : {invoice_no}\n")
        file.write(f"Total Cost : {total_cost}\n")
        file.write(f"Customer ID : {cust_id}\n")
        file.write(f"Name : {name}\n")
        file.write(f"Phone : {phone}\n")
        file.write(f"Address : {address}\n")
        file.write(f"Company : {company}\n")
        file.write(f"Discount : {discount}%\n")
        file.write(f"Final Price : {int(final_price)}\n")
        file.write("---INVOICE END---\n")

# ================= SCAN =================
elif main_choice == 2:
    if not os.path.exists("invoices.txt"):
        print("❌ No invoice records found.")
    else:
        search_no = input("Enter Invoice Number: ")
        printing = False
        with open("invoices.txt") as f:
            for line in f:
                if f"Invoice No : {search_no}" in line:
                    printing = True
                    print("\n📄 INVOICE FOUND\n")
                if printing:
                    print(line, end="")
                if printing and "---INVOICE END---" in line:
                    break