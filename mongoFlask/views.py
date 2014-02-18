from slugify import slugify
from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form
from mongoFlask.models import Article

articles = Blueprint('articles', __name__, template_folder='templates')

class Search(MethodView):

  form = model_form(Article, exclude=['created_at', 'slug'])

  def get_context(self, slug):
    article = Article.objects.get_or_404(slug=slug)
    form = self.form(request.form)

    context = {
      "article": article,
      "form": form
    }
    return context

  def get(self, slug):
    context = self.get_context(slug)
    return render_template('article/show.html', **context)

  def post(self, slug):
      context = self.get_context(slug)
      form = context.get('form')

      if form.validate():
        comment = Comment()
        form.populate_obj(comment)

        article = context.get('article')
        article.slug = slugify(article.title)
        article.save()

        return redirect(url_for('articles.show', slug=slug))
      return render_template('articles/show.html', **context)

class Index(MethodView):  

  def get(self):
    articles = Article.objects.all()
    return render_template('articles/index.html', articles=articles)

class ShowArticle(MethodView):

  def get(self, slug):
    article = Article.objects.get_or_404(slug=slug)
    return render_template('articles/show.html', article=article)




articles.add_url_rule('/', view_func=Index.as_view('index'))
articles.add_url_rule('/search/', view_func=Index.as_view('search'))
articles.add_url_rule('/articles/<slug>/', view_func=ShowArticle.as_view('show'))
