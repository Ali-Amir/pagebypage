from flask import Flask
app = Flask(__name__)

import main_page

@app.route("/")
def main():
    return main_page.main()

if __name__ == "__main__":
    app.run()
