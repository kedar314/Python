# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = (r"C:\Users\Kedar\Downloads\WFH.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
sheet.cell_value(0, 0) 
  
print("The information is here - " + str(sheet.row_values(1))) 


