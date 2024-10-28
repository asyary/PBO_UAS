from utils.gui import GUI
from classes.user import User

def init():
	user = User('aandisetiawan@example.com', 'admin123')
	print(user.status)

if __name__ == "__main__":
    init()