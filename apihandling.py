"""
API Key handling
"""
from pathlib import Path

def configPath():
    home = Path.home()
    return home / 'openaiclient' / '.config'
	
def config():
    path = configPath()
    
    if path.exists():
        file = open(path, 'rw')
    else:
        file = open(path, 'rx')
    
    return file