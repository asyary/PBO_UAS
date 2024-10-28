from utils.gui import GUI
from classes.user import User

def init():
	user = User('aandisetiawan@example.com', 'admin1234', '1234123412341234', 'Aandi Setiawan')
	print(user.status)

if __name__ == "__main__":
    init()