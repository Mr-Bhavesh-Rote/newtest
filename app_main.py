
from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"
import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    app.run()
