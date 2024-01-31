from flask import *

app = Flask(__name__)           ## Name of the module


posts =[
    {
        'author':'Corey',
        'title':'Blog post 1',
        'content':'First blog post',
        'date_posted':'January, 31 2024',
    },
    {
        'author':'Jane',
        'title':'Blog post 2',
        'content':'Second blog post',
        'date_posted':'January, 3 2024',
    }
]



@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts = posts, title= "Blog Page")


@app.route("/about")
def about():
    return render_template('about.html',title = "About Page")


if __name__ == '__main__':
    app.run(debug=True)