from django.shortcuts import render, redirect

from .models import Bug

from .forms import CommentForm

# Create your views here.
def frontpage(request):
    bugs = Bug.objects.all()
    return render(request, 'tracker/frontpage.html', {'bugs': bugs})


def bug_detail(request, slug):
    bug = Bug.objects.get(slug = slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.bug = bug
            comment.save()

            return redirect('bug_detail', slug=bug.slug)
    else:
        form = CommentForm()

    return render(request, 'tracker/bug_detail.html', {'bug': bug, 'form': form})