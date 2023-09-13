from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            # first element shows in url
            # second element is the text that user clicks
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    # It returns filtered reviews
    def queryset(self, request, reviews):
        # print(dir(request))
        # print(request.GET)
        # print(self.value())
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
