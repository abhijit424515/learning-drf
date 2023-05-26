from django.urls import path, include
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,
    ReviewCreate,
)

urlpatterns = [
    path("watch/", WatchListAV.as_view(), name="watch-list"),
    path("watch/<int:pk>", WatchDetailAV.as_view(), name="watch-list-nth"),
    path(
        "stream/",
        StreamPlatformListAV.as_view(),
        name="stream",
    ),
    path(
        "stream/<int:pk>",
        StreamPlatformDetailAV.as_view(),
        name="stream-platform-list-nth",
    ),
    path("watch/<int:pk>/review/", ReviewList.as_view(), name="review-list"),
    path("watch/<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path("watch/review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
]
