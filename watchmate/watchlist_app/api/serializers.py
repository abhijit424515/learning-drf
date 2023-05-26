from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(
        many=True, read_only=True
    )  # reviews is the related_name we chose in the model

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(
        many=True, read_only=True
    )  # watchlist is the related_name we chose in the model

    # watchlist = serializers.StringRelatedField(
    #     many=True,
    #     read_only=True
    # )  # the one we defined in __str__

    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="watch-list-nth"
    # )  # the actual api link to the related object

    class Meta:
        model = StreamPlatform
        fields = "__all__"
