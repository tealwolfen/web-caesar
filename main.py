from flask import Flask 

app = Flask(__name__)
app.config['DEBUG'] = True

add_form = """
<!DOCtYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px san-serif;
                border-readius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method ='POST'>
            <label>Key
                <input name="rot" type="text' value='{0}' />
            </label>

            <label>Message
                <textarea name="text"></ textarea>
            </label>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return "Hello World"

app.run()    