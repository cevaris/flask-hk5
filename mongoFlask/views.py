from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from mongoFlask.models import Article

articles = Blueprint('articles', __name__, template_folder='templates')

class Index(MethodView):
  def get(self):
    articles = Article.objects.all()
    return render_template('articles/index.html', articles=articles)

articles.add_url_rule('/', view_func=Index.as_view('show'))