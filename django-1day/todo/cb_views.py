from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from todo.models import Todo


class TodoListView(LoginRequiredMixin, ListView):
    template_name = 'todo/todo_list.html'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        qs = Todo.objects.all()
        if not self.request.user.is_superuser:
            qs = qs.filter(user=self.request.user)

        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return qs


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo/todo_info.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("조회 권한이 없습니다.")
        return obj


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'start_date', 'end_date']
    template_name = 'todo/todo_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('cbv_todo_detail', kwargs={'pk': self.object.id})


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'start_date', 'end_date', 'is_completed']
    template_name = 'todo/todo_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("수정 권한이 없습니다.")
        return obj

    def get_success_url(self):
        return reverse_lazy('cbv_todo_detail', kwargs={'pk': self.object.id})


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("삭제 권한이 없습니다.")
        return obj

    def get_success_url(self):
        return reverse_lazy('cbv_todo_list')
