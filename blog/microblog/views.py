from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import BlogPost

# Create your views here.
class Index(ListView):
    model = BlogPost
    queryset = BlogPost.objects.all().order_by('-date')
    template_name = 'microblog/index.html'
    paginate_by = 1


class DetailPostView(DetailView):
    model = BlogPost
    template_name = 'microblog/post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailPostView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        micropost = BlogPost.objects.get(id=self.kwargs.get('pk'))
        if micropost.likes.filter(pk=self.request.user.id).exists():
            return True
        else:
            return context
        
class LikePost(View):
    def post(self, request, pk):
        micropost = Post.objects.get(id=pk)
        if micropost.likes.filter(pk=self.request.user.id).exists():
            micropost.likes.remove(request.user.id)
        else:
            micropost.likes.add(request.user.id)

        micropost.save()
        return redirect('detail_post',pk)
