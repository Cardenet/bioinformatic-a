from pathlib import Path
import engine
from jinja2             import Environment, FileSystemLoader
from jinja2.environment import Template


current_dir = Path('.')
template_filename: str = 'invitation.txt'

friends_txt:  str       = Path('friends.txt').read_text().strip()
friends_list: list[str] = friends_txt.split(',')

for friend in friends_list:

    vars_dict:  dict = {'friend_name': friend}
    invitation: str  = engine.fill_template(current_dir, template_filename, vars_dict) 

    filename: str  = f"{friend}.txt"
    filepath: Path = Path(filename)
    filepath.write_text(invitation)

