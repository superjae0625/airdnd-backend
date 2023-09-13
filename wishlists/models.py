from django.db import models
from common.models import CommonModel


class Wishlists(CommonModel):
    """Wishlist Model Definition"""

    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField(
        "rooms.Room",
        related_name="wishlists",
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    class Meta:
        verbose_name_plural = "Wishlists"

    def __str__(self) -> str:
        return self.name
