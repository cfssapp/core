from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
def fake_data_01(request):
	api_urls = {
    "salesData": [
        {
            "x": "Jan",
            "y": 1
        },
    ],
}

	return JsonResponse(api_urls, safe=False)


# def show_topic(request, topic_id, full=True):
#     """
#     * Display a topic
#     * save a reply
#     * save a poll vote

#     TODO: Add reply in lofi mode
#     """
#     post_request = request.method == "POST"
#     user_is_authenticated = request.user.is_authenticated()
#     if post_request and not user_is_authenticated:
#         # Info: only user that are logged in should get forms in the page.
#         raise PermissionDenied

#     topic = get_object_or_404(Topic.objects.select_related(), pk=topic_id)
#     if not topic.forum.category.has_access(request.user):
#         raise PermissionDenied
#     Topic.objects.filter(pk=topic.id).update(views=F('views') + 1)

#     last_post = topic.last_post

#     if request.user.is_authenticated():
#         topic.update_read(request.user)
#     posts = topic.posts.all().select_related()

#     moderator = request.user.is_superuser or request.user in topic.forum.moderators.all()
#     if user_is_authenticated and request.user in topic.subscribers.all():
#         subscribed = True
#     else:
#         subscribed = False

#     # reply form
#     reply_form = None
#     form_url = None
#     back_url = None
#     if user_is_authenticated and not topic.closed:
#         form_url = request.path + "#reply" # if form validation failed: browser should scroll down to reply form ;)
#         back_url = request.path
#         ip = request.META.get('REMOTE_ADDR', None)
#         post_form_kwargs = {"topic":topic, "user":request.user, "ip":ip}
#         if post_request and AddPostForm.FORM_NAME in request.POST:
#             reply_form = AddPostForm(request.POST, request.FILES, **post_form_kwargs)
#             if reply_form.is_valid():
#                 post = reply_form.save()
#                 messages.success(request, _("Your reply saved."))
#                 return HttpResponseRedirect(post.get_absolute_url())
#         else:
#             reply_form = AddPostForm(
#                 initial={
#                     'markup': request.user.forum_profile.markup,
#                     'subscribe': request.user.forum_profile.auto_subscribe,
#                 },
#                 **post_form_kwargs
#             )

#     # handle poll, if exists
#     poll_form = None
#     polls = topic.poll_set.all()
#     if not polls:
#         poll = None
#     else:
#         poll = polls[0]
#         if user_is_authenticated: # Only logged in users can vote
#             poll.deactivate_if_expired()
#             has_voted = request.user in poll.users.all()
#             if not post_request or not VotePollForm.FORM_NAME in request.POST:
#                 # It's not a POST request or: The reply form was send and not a poll vote
#                 if poll.active and not has_voted:
#                     poll_form = VotePollForm(poll)
#             else:
#                 if not poll.active:
#                     messages.error(request, _("This poll is not active!"))
#                     return HttpResponseRedirect(topic.get_absolute_url())
#                 elif has_voted:
#                     messages.error(request, _("You have already vote to this poll in the past!"))
#                     return HttpResponseRedirect(topic.get_absolute_url())

#                 poll_form = VotePollForm(poll, request.POST)
#                 if poll_form.is_valid():
#                     ids = poll_form.cleaned_data["choice"]
#                     queryset = poll.choices.filter(id__in=ids)
#                     queryset.update(votes=F('votes') + 1)
#                     poll.users.add(request.user) # save that this user has vote
#                     messages.success(request, _("Your votes are saved."))
#                     return HttpResponseRedirect(topic.get_absolute_url())

#     highlight_word = request.GET.get('hl', '')
#     view_data = {
#         'categories': Category.objects.all(),
#         'topic': topic,
#         'posts_page': get_page(posts, request, forum_settings.TOPIC_PAGE_SIZE),
#         'poll': poll,
#         'poll_form': poll_form,
#     }
#     if full:
#         view_data.update({
#             'last_post': last_post,
#             'form_url': form_url,
#             'reply_form': reply_form,
#             'back_url': back_url,
#             'moderator': moderator,
#             'subscribed': subscribed,
#             'highlight_word': highlight_word,
#         })
#         return render(request, 'djangobb_forum/topic.html', view_data)
#     else:
#         return render(request, 'djangobb_forum/lofi/topic.html', view_data)
