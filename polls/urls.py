urlpatterns += [
    path('add-author/', add_author, name='add_author'),
    path('add-quote/', add_quote, name='add_quote'),
]

path('reset-password/', include('django.contrib.auth.urls')),
