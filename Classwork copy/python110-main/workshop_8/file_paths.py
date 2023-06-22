from pathlib import Path
# absolute path
# relative path

BASE_DIR: Path = Path(__file__).parent
print(f'{__file__ = }')
USERS_FILE = BASE_DIR / 'users.dat'
print(f'{BASE_DIR = }')
print(f'{USERS_FILE = }')

with USERS_FILE.open() as f:
    content = f.read()
    users = content.split('\n')

print(users)
