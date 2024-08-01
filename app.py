# import
from flask import Flask

# instancia
app = Flask(__name__)

# routes
## root
@app.route('/')
def hello_word():
    return 'Hello Word'

if __name__ == "__main__":
    app.run(debug=True)