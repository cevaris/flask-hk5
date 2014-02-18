from slugify import slugify
from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form
from mongoFlask.models import Article

articles = Blueprint('articles', __name__, template_folder='templates')

class Search(MethodView):

  def get(self):
    query = request.args.get('q', '')
    count = int(request.args.get('n', 0))
    print query
    print count

    try:
      articles = Article.objects(body__contains=query)
    except Article.DoesNotExist:
      articles = []

    if count > 0:
      return render_template('articles/index.html', articles=articles[:count])
    else:
      return render_template('articles/index.html', articles=articles)
      

class Index(MethodView):  

  def get(self):
    articles = Article.objects.all()
    return render_template('articles/index.html', articles=articles)

class ShowArticle(MethodView):

  def get(self, slug):
    article = Article.objects.get_or_404(slug=slug)
    return render_template('articles/show.html', article=article)




articles.add_url_rule('/articles', view_func=Index.as_view('index'))
articles.add_url_rule('/articles/search/', view_func=Search.as_view('search'))
articles.add_url_rule('/articles/<slug>/', view_func=ShowArticle.as_view('show'))
