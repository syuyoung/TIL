from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm


def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    count = review.comment_set.count()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
        'count': count,
    }
    return render(request, 'reviews/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST, request.FILES)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.save()
        return redirect('reviews:detail', review.pk)
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)


def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)