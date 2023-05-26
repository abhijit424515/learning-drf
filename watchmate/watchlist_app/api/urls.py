from django.urls import path, include
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,
)

urlpatterns = [
    path("watch-list/", WatchListAV.as_view(), name="watch-list"),
    path("watch-list/<int:pk>", WatchDetailAV.as_view(), name="watch-list-nth"),
    path(
        "stream-platform-list/",
        StreamPlatformListAV.as_view(),
        name="stream-platform-list",
    ),
    path(
        "stream-platform-list/<int:pk>",
        StreamPlatformDetailAV.as_view(),
        name="stream-platform-list-nth",
    ),
    path("review/", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
]
