
from pathlib import Path
import engine
from jinja2             import Environment, BaseLoader, FileSystemLoader, select_autoescape
from jinja2.environment import Template

#Luis Cardenete Mayoral
#Ejercicio 3
"""
Exercici 3:

- Fes un programa per visualitzar imatges d'un directori local.
- El programa només rep un paràmetre: un directori 'dir'.
- El programa ha de buscar totes les imatges a 'dir' i generar una pàgina html
  que les mostri.
- El programa ha de rebre el directori 'dir' des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**

"""

#Aqui se consigue la lista de imagenes
def get_images_list(dir: str, type :str)-> list[str]:
  
  images_Path: list[Path] = list(Path(dir).rglob(type))
  images_list: list[str] =  [str(Path) for Path in images_Path]
  return images_list

#Aqui se juntaria con el template
def make_html(template_filename: str, images_list: list[str]):
  
  template_str: str  = Path(template_filename).read_text()
  vars_dict:  dict = {'images_list': images_list}
  html_file:  str  = engine.fill_template_str(template_str, vars_dict) 
  return html_file

#Aqui se crearia un archivo   
def write_html(html_file):
  
  filename: str  = "Result.html"
  filepath: Path = Path(filename)
  filepath.write_text(html_file)


def final_result(dir: str, type: str, template_filename: str):
  pictures: list[str]=  get_images_list(dir, type)
  archive = make_html(template_filename, pictures)
  final = write_html(archive)
  return final





final_result(".", "*.jpg", "template.html")
