from flask import Flask, request, render_template, jsonify, url_for, redirect
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)
app.config["SECRET_KEY"]='thisismysecretkey'

movies = {}

class CreateForm(FlaskForm):
    movie_id = StringField(validators=[
                           InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Movie_ID"})

    moviename = StringField(validators=[
                             InputRequired(), Length(min=1, max=20)], render_kw={"placeholder": "Moviename"})

    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    movie_id = StringField(validators=[
                           InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Movie_ID"})

    moviename = StringField(validators=[
                             InputRequired(), Length(min=1, max=20)], render_kw={"placeholder": "Moviename"})

    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    movie_id = StringField(validators=[
                           InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Movie_ID"})

    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("Intermediate_flask-4_home.html")

@app.route('/create_movie', methods=['GET','POST'])
def create_movie():
    form=CreateForm()
    if form.validate_on_submit():
        movie_id=request.form.get('movie_id')
        data = request.form.get('moviename')
        movies[movie_id]=data
        return "Movies data created."
    return render_template("Intermediate_flask-4_create.html",form=form)

@app.route('/get_movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

@app.route('/update_movie', methods=['GET','POST'])
def update_movie():
    form=UpdateForm()
    data = request.form.get('moviename')
    movie_id = request.form.get('movie_id')
    if movie_id in movies:
        movies[movie_id]=data
        return "Movies updated successfully."  
    return render_template("Intermediate_flask-4_update.html",form=form)
    

@app.route('/delete_movie', methods=['GET','POST'])
def delete_movie():
    form=DeleteForm()
    movie_id = request.form.get('movie_id') 
    if movie_id in movies:
        del movies[movie_id]
        return "Your movie successfully removed."
    return render_template("Intermediate_flask-4_delete.html",form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)
