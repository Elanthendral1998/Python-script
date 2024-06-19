from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_string = request.form['input_string']
        if input_string == "hello":
            result = "The string is 'hello'."
        else:
            result = "The string is not 'hello'."
        return f'''
            <h1>Check a String</h1>
            <form method="post">
                <label for="input_string">Enter a string:</label>
                <input type="text" id="input_string" name="input_string">
                <input type="submit" value="Check">
            </form>
            <p>Result: {result}</p>
        '''
    return '''
        <h1>Check a String</h1>
        <form method="post">
            <label for="input_string">Enter a string:</label>
            <input type="text" id="input_string" name="input_string">
            <input type="submit" value="Check">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
