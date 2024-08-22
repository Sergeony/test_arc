__all__ = [
    "Location",
]


class Location:
    id: int

    def create(self, *args, **kwargs):
        self.id = kwargs.get('id')
