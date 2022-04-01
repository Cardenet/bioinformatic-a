from pathlib import Path
"""
Luis Cardenete Mayoral
e4.py
Exercici 4:

- Fes un programa que llegeixi les dades covid del fitxer adjunt i calculi el següent:
- Ranking d'àrees (NOM) per número de morts (EXITUS).
- Primer mostrar les àrees amb més morts i al final les de menys morts.
- El programa només rep un paràmetre: el nom del fitxer .csv amb les dades covid.
- El programa ha de rebre el nom del fitxer des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**

Pasos recomanats:
1. Filtrar per nom d'àrea
2. Sumar els morts d'una àrea
3. Llistar les àrees úniques
4. Per cada àrea calcular la suma total de morts
5. Ordenar àrees pel total de morts
6. Llegir csv per la línea d'ordres
"""


def read_csv(csv_file_path: str) -> str:
    
    raw_text:      str = Path(csv_file_path).read_text()
    stripped_text: str = raw_text.strip()
    return stripped_text

def separate_by_rows(contents: str) -> list[str]:
    
    rows: list[str] = contents.split("\n")
    return rows

def separate_by_columns(rows: list[str]) -> list[list[str]]:
    
    table: list[list[str]] = [row.split(";") for row in rows]
    return table

def read_table(csv_file_path: str) -> list[list[str]]:
    
    csv_str: str             = read_csv(csv_file_path)
    rows:    list[str]       = separate_by_rows(csv_str)
    table:   list[list[str]] = separate_by_columns(rows)
    return table

def filter_rows(table: list[list[str]], column_name: str, search_str:str) -> list[list[str]]:
    header: list[str]       = table[0]
    data:   list[list[str]] = table[1:]
    column_index: int = header.index(column_name)
    filtered_data: list[list[str]] = [row for row in data if (search_str in row[column_index])]

    result: list[list[str]] = [header] + filtered_data

    return result

def sum_data (table: list[list[str]], column_name: str) -> int:

    header: list[str]       = table[0]
    data:   list[list[str]] = table[1:]
    column_index: int = header.index(column_name)
    filter_data_str: list[str] = [row[column_index] for row in data]
    filter_data_int: list[int] = [int(elem) for elem in filter_data_str]
    result:int = sum(filter_data_int)
    return result

def get_list_area(table: list[list[str]]):
    
    list_set = set(table)
    
    unique_list = (list(list_set))
    for x in unique_list:
        print (x)

#def total(table: list[list[str]], column_name: str):
#    for area in list_area



if __name__ == "__main__":
    table:     list[list[str]] = read_table("2022-03-09-covid-dades-example.csv")
    filter_table: list[list[str]] = filter_rows(table, 'NOM', 'ALT EMPORDÀ')
    #: list[list[str]] = unique()
#    exitus_list: int = sum_data(filter_table, 'EXITUS')
#    print(exitus_list)