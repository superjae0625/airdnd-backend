from django.db import models
from common.models import CommonModel


class Room(CommonModel):
    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="US")
    city = models.CharField(max_length=80, default="Salt Lake City")
    price = models.PositiveIntegerField()
    rooms = models.PositiveBigIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    # can you room instead of self
    def __str__(self) -> str:
        return self.name

    def total_amenities(room):
        return room.amenities.count()

    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return "No Reivews"
        else:
            total_rating = 0
            # print(room.reviews.all().values("rating"))
            # print(room.reviews.all())
            for review in room.reviews.all().values("rating"):
                total_rating += review["rating"]
                # changed to dictionary format
            return round(total_rating / count, 2)


class Amenity(CommonModel):
    """Amenity Definition"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    # can you amenity instead of self
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
