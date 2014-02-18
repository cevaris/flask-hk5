from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from mongoFlask.models import Article

articles = Blueprint('articles', __name__, template_folder='templates')


class Index(MethodView):

  def get(self):
    articles = Article.objects.all()
    return "Hello World"

class ShowArticle(MethodView):

  def get(self, slug):
    article = Article.objects.get_or_404(slug=slug)
    return render_template('articles/show.html', article=article)


# articles.add_url_rule('/', view_func=Index.as_view())
articles.add_url_rule('/articles/<slug>/', view_func=ShowArticle.as_view('show'))