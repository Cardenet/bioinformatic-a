from pathlib import Path

# 1. Read csv file
# -----------------------------------------------------------------------------
def read_csv(csv_file_path: str) -> str:
   '''Input:  The path to a .csv file.
      Output: The contents of the .csv file as a single string.'''

   raw_text:      str = Path(csv_file_path).read_text()
   stripped_text: str = raw_text.strip()

   return stripped_text


# 2. Separate by rows
# -----------------------------------------------------------------------------
def separate_by_rows(contents: str) -> list[str]:
   '''Input:  The file contents as a single string.
      Output: A list of strings where each string is a row of the csv file.'''
   
   rows: list[str] = contents.split("\n")

   return rows


# 3. Separate by columns
# -----------------------------------------------------------------------------
def separate_by_columns(rows: list[str]) -> list[list[str]]:
   '''Input:  A list of strings. Each string is a row of a csv file. Row fields are separated by ";".
      Output: A table where each row has been splitted into a list of fields.'''
   
   table: list[list[str]] = []
   row:   str

   for row in rows:
      splitted_row: list[str] = row.split(";")
      table.append(splitted_row)

   return table
#4. Average vaccinated people in barcelona
#------------------------------------------------------------------------------
def average_vaccinated_barcelona(table: list[list[str]]) -> tuple[int,int]:
    '''Input: a list of two columns: VACUNATS_DOSI_1	VACUNATS_DOSI_2
       Output:the data of the average of people with the 2 dosis'''
    row: list[str]
    Barcelona: str= table.index("BARCELONA")
    
    dosi1_list: list[str]=[]
    dosi2_list: list[str]=[]





# Main
# -----------------------------------------------------------------------------
contents: str                   = read_csv("2022-01-20-covid-dades-aga.csv")
rows:     list[str]             = separate_by_rows(contents)
table:    list[list[str]]       = separate_by_columns(rows)