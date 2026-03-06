import csv
from statistics import mean
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import styles
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

# Read Data from CSV
file_name = "data.csv"
students = []
marks = []

with open(file_name, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append([row['Name'], int(row['Marks'])])
        marks.append(int(row['Marks']))

# Analyze Data
average_marks = mean(marks)
highest = max(marks)
lowest = min(marks)

# Create PDF
pdf = SimpleDocTemplate("Student_Report.pdf", pagesize=A4)
elements = []
 
styles = styles.getSampleStyleSheet()
title_style = styles["Heading1"]

# Title
elements.append(Paragraph("Student Performance Report", title_style))
elements.append(Spacer(1, 0.3 * inch))

# Table Data
table_data = [["Name", "Marks"]] + students
table = Table(table_data)

table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('ALIGN', (1, 1), (-1, -1), 'CENTER')
]))

elements.append(table)
elements.append(Spacer(1, 0.5 * inch))

# Summary Section
elements.append(Paragraph(f"Average Marks: {average_marks}", styles["Normal"]))
elements.append(Paragraph(f"Highest Marks: {highest}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Marks: {lowest}", styles["Normal"]))

pdf.build(elements)

print("PDF Report Generated Successfully!")