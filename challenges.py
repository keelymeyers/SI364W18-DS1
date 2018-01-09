from flask import Flask, request
import requests 
import json

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# Task 2
# Write a return statement such that it displays 'Welcome to <course_name>'
# when you navigate to localhost:5000/course/<course_name>
# Remember to get rid of the pass statement
@app.route('/course/<course>')
def course(course):
   return "<h1>Welcome to {}</h1>".format(course)

# Task 3.1
# Edit the HTML form such that form data is sent to localhost:5000/result using POST method
@app.route('/form')
def enterData():
    s = """<!DOCTYPE html>
<html>
<body>
<form action="/display" method="POST">
  INGREDIENT:<br>
  <input type="text" name="ingredient" value="Enter value">
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
# Note that by default eggs would be entered in the input field
    return s


## Task 3.2
## Modify the function code and return statement
## to display recipes for the ingredient entered
@app.route('/display',methods = ['POST', 'GET'])
def displayData():
    if request.method == 'POST':
        data = request.form['ingredient']
        base_url = "http://www.recipepuppy.com/api/?"
        search_term = "i={}".format(data)
        recipe_data = requests.get(base_url+search_term)
        recipe_data = json.loads(recipe_data.text)
        recipes = '<p>'
        for x in recipe_data["results"]:
          recipes += x["title"]+'<br/>'
        recipes += '</p>'
        return recipes
        #return data

## Task 4
## Note : Since this is a dyanmic URL, recipes function should recieve a paramter called `ingrdient` 
@app.route('/recipe/<ingredient>')
def recipes():
    pass

if __name__ == '__main__':
    app.run()
