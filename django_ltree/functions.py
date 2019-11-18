from django.db.models import Transform
from django.db.models import fields
from .fields import PathField

__all__ = ("NLevel",)


@PathField.register_lookup
class NLevel(Transform):
    lookup_name = "depth"
    function = "nlevel"
    output_field = fields.IntegerField()
