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

class CreateArticle(MethodView):

  def get(self):
    return render_template('articles/create.html')

  def post(self):

    if request.method == 'POST':
      body = request.form['body']
      author = request.form['body']
      title = request.form['body']
      slug = slugify(title)
      article = Article(body=body, author=author, title=title, slug=slug)
      article.save()

      return render_template('articles/show.html', article=article)
    return render_template('articles/create.html')

class ShowArticle(MethodView):

  def get(self, slug):
    article = Article.objects.get_or_404(slug=slug)
    return render_template('articles/show.html', article=article)



articles.add_url_rule('/', view_func=Index.as_view('index'))
articles.add_url_rule('/create', view_func=CreateArticle.as_view('create'))
articles.add_url_rule('/view/<slug>/', view_func=ShowArticle.as_view('show'))
articles.add_url_rule('/search', view_func=Search.as_view('search'))

