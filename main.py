# The main.py file is the main file in our project
from website import create_app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True) 