## Bill Generator

A simple **Python-based Invoice Generator** that creates professional **PDF invoices** for a clothing store using the **ReportLab library**.
The system allows users to generate invoices, apply discounts, store invoice records, and search previously generated invoices.

---

#  Project Description

This project simulates a **billing system for a men's clothing store (Range Men's Wear)**.
It collects customer information, allows selection of clothing items, calculates total cost, applies discounts, and automatically generates a **PDF invoice**.

The system also stores invoice details in a text file and provides an option to **scan/search invoices by invoice number**.

---

#  Features

*  Automatic Invoice Number Generation
* Customer Information Input
* Multiple Item Selection
* Discount Calculation
* Professional PDF Invoice Generation
* Invoice Records Saved in Text File
* Invoice Search (Scan Invoice Feature)

---

# Technologies Used

* Python
* ReportLab (for PDF generation)
* File Handling
* OS Module
* Datetime Module

---

# Project Structure

```
invoice-generator/
│
├── invoice_generator.py
├── invoice_no.txt
├── invoices.txt
├── Invoice_1.pdf
├── Invoice_2.pdf
└── README.md
```

#  How to Run
python bill.py
```
You will see the menu:
```
1. Generate Invoice
2. Scan Invoice
```

#  Generate Invoice

* Enter customer details
* Choose product options
* Enter quantity and price
* Apply discount (optional)
* A PDF invoice will be generated automatically

#  Scan Invoice

Enter the **invoice number** to retrieve previously saved invoice details.

---

#  Sample Output

The system generates a PDF invoice containing:

* Store Details
* Invoice Number
* Date
* Customer Information
* Item List (Qty, Rate, Amount)
* Total Cost
* Discount
* Final Price

---

#  Example Use Case

A clothing shop owner can quickly generate bills for customers purchasing items like:

* Shirts
* Pants
* T-Shirts
* Tracks
* Shorts
* Inner Wear

The system calculates totals and produces a professional invoice.

---

#  Future Improvements

* Add GST calculation
* Add shop logo in invoice
* Create GUI version using Tkinter
* Add database storage
* Generate daily sales reports

---

#  Author

Yalamarthi Durgarao



---
