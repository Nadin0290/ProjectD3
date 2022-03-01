# from news.models import *
# User1 = User.objects.create(username='Ivan', first_name ='Ivanov')
# Author.objects.create(authorUser=User1)
# User2 = User.objects.create(username='Petr', first_name ='Petrov')
# Author.objects.create(authorUser=User2)
#
# Category.objects.create(name='C1')
# Category.objects.create(name='C2')
# Category.objects.create(name='C3')
# Category.objects.create(name='C4')
#
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Ivan')), categoryType='NW', title='Новость номер 1', text='Здесь находится текст первой новости!')
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Petr')), categoryType='NW', title='Новость номер 2', text='Здесь находится текст второй новости!')
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Petr')), categoryType='AR', title='Первая статья', text='Здесь находится текст первой статьи!')
#
# post1 = Post.objects.get(pk=1)
# post2 = Post.objects.get(pk=2)
# post3 = Post.objects.get(pk=3)
# cat1 = Category.objects.get(name='C1')
# cat2 = Category.objects.get(name='C2')
# cat3 = Category.objects.get(name='C3')
# cat4 = Category.objects.get(name='C4')
# post1.postCategory.add(cat1)
# post1.postCategory.add(cat2)
# post2.postCategory.add(cat2)
# post3.postCategory.add(cat1, cat3)
#
# Comment.objects.create(commentUser=User.objects.get(username='Ivan'), commentPost=Post.objects.get(pk=1), text='Здесь текст первого комментария.')
# Comment.objects.create(commentUser=User.objects.get(username='Petr'), commentPost=Post.objects.get(pk=1), text='Здесь текст второго комментария.')
# Comment.objects.create(commentUser=User.objects.get(username='Ivan'), commentPost=Post.objects.get(pk=2), text='Комментарий Ивана.')
# Post.objects.get(pk=1).like()
# Post.objects.get(pk=1).like()
# Post.objects.get(pk=2).dislike()
# Comment.objects.get(pk=1).dislike()
# Comment.objects.get(pk=2).like()
# Comment.objects.get(pk=3).like()
#
# Author.objects.get(authorUser=User.objects.get(username='Ivan')). update_rating()
# Author.objects.get(authorUser=User.objects.get(username='Petr')). update_rating()
# a = Author.objects.get(authorUser=User.objects.get(username='Ivan'))
# a.ratingAuthor
# Author.objects.get(authorUser=User.objects.get(username='Petr')).ratingAuthor
#
# best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
# print(best)
# d = User.objects.all().values('username', 'date_joined')
# print(d)
#
# best_post = Post.objects.all().order_by('-rating').values('id','dateCreation', 'rating', 'author_id')[0]
# prev = Post.objects.get(id=best_post['id']).preview()
# post_user = User.objects.get(id=best_post['author_id'])
# print(f"Лучшая статья\n Автор: {post_user},\n Дата добавления: {best_post['dateCreation']},\n Рейтинг статьи: {best_post['rating']},\n {prev}")
# comment_post = Comment.objects.get(id=best_post['id']).post_com()
# print(comment_post)
#