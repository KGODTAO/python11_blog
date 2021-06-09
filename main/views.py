from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CreatePostForm, UpdatePostForm
from .models import Category, Post


# TODO: Переписать при помощи классов

class IndexPageView(View):
    def get(self, request):
        categories = Category.object.all()
        return render(request, 'main/index.html', {'categories': categories})

class IndexPageView(ListView):
    queryset = Category.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'categories'

#posts/category_id/
#posts/?category=id


class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category')
        return queryset.filter(category_id=category_id)


class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_details.html'
    context_object_name = 'post'


class CreateNewPostView(CreateView):
    queryset = Post.objects.all()
    template_name = 'main/create_post.html'
    form_class = CreatePostForm

class EditPostView(UpdateView):
    queryset = Post.objects.all()
    template_name = 'main/edit_post.html'
    form_class = UpdatePostForm

class DeletePostView(DeleteView):
    queryset = Post.objects.all()
    template_name = 'main/delete_post.html'


# TODO: Регистрация,активация,логин,логаут
# TODO: HTML - письмо
# TODO: Фильтрация поиск сортировка
# TODO: Пагинация
# TODO: Переиспользование шаблонов
# TODO: Проверка прав
# TODO: Избранное
# TODO: Дизайн
