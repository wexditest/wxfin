# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import get_object_or_404, redirect
# from django.views import generic
# from .models import Post, PostComment
# from django.views.generic.base import TemplateView
# from django.contrib import messages

# class PostList(generic.ListView):
#     queryset = Post.objects.all()
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['recent_posts'] = Post.objects.filter(status=1).order_by('-created_on')[:3]
#         return context

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

#     def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             context['recent_posts'] = Post.objects.filter(status=1).order_by('-created_on')[:3]
#             return context

# class ContactView(TemplateView):
#     template_name = 'contact.html'

# class AboutView(TemplateView):
#     template_name = 'about.html'

# class AddComment(generic.DetailView):
#     def post(self, request, *args, **kwargs):
#         comment = request.POST.get('comment')
#         user = request.user
#         post_id = request.POST.get('post_id')
#         post = get_object_or_404(Post, id=post_id)

#         comment_instance = PostComment(comment=comment, user=user, post=post)
#         comment_instance.save()
#         messages.success(request, "Comment Added Successfully!!")

#         return redirect('blog:blog-details', slug=post.slug)

#     def get(self, request, *args, **kwargs):
#         messages.error(request, "An error occurred while adding a comment!")
#         return redirect('blog:home')
