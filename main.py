from classes.user import User

def init():
	user = User('andisetiawan@example.com', 'admin123')
	if user.id is None:
		print("User not found")
	else:
		print("User found")
		print(user.id)

if __name__ == "__main__":
    init()