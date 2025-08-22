import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

NAME_OF_PROJECT = 'DataScienceProject'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{NAME_OF_PROJECT}/__init__.py',
    f'src/{NAME_OF_PROJECT}/components/__init__.py',
    f'src/{NAME_OF_PROJECT}/utils/__init__.py',
    f'src/{NAME_OF_PROJECT}/utils/common.py',
    f'src/{NAME_OF_PROJECT}/config/__init__.py',
    f'src/{NAME_OF_PROJECT}/config/configuration.py',
    f'src/{NAME_OF_PROJECT}/pipeline/__init__.py',
    f'src/{NAME_OF_PROJECT}/entity/__init__.py',
    f'src/{NAME_OF_PROJECT}/entity/config_entity',
    f'src/{NAME_OF_PROJECT}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'Dockerfile',
    'setup.py', ## Package your project into PYPI Package
    'research/research.ipynb',
    'templates/index.html',
    '.env'

]

for file_path in list_of_files:
   file_path = Path(file_path)

   file_dir, file_name = os.path.split(file_path)

   if file_dir != '':
    logging.info(f'Creating directory {file_dir} for the file {file_name}')
    os.makedirs(file_dir,exist_ok=True)

   if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,'w') as f:
            pass
        logging.info(f'Creating an empty file: {file_path}')
   else:
        logging.info(f'File already exists: {file_path}')