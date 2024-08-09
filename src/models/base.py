from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


__all__ = [
    "Base",
]


class Base(DeclarativeBase):
    """ This is an abstract Base model for all the SQLAlchemy models.

    The main purpose for it is:
        define that all our SQLAlchemy models will have IDs.
        By default, IDs are integers, but they can easily be overriden for need.
    """
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
