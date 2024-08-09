from sqlalchemy import make_session, Session, Engine, update, select

from models import Base
from ..base_repos import CommonBaseRepo
from .helpers import engine


__all__ = [
    "CommonRepo",
]


class CommonRepo(CommonBaseRepo):
    """ An SQLAlchemy implementation of common DB Repo.

    This one actually implements data access management to DB with SQLAlchemy ORM.

    It implements all common DB Repo methods, which could be used by all DB Model Repos for this ORM.
    """
    def __init__(
            self,
            _model: type[Base],
            session: Session = None,
            _engine: Engine = engine,
    ):
        self._model = _model

        if session is not None:
            self.session = session
        else:
            self.session = make_session(bind=_engine)

    def delete(self, args):
        self.session.query(self._model).filter_by(id=args).delete()
        self.session.commit()

    def update(self, args):
        update_data = args.model_dump()

        if 'id' in update_data:
            update_data.pop('id')

        stmt = (
            update(self._model)
            .filter_by(id=args.id)
            .values(**update_data)
        )

        result = self.session.execute(stmt)

        if result.rowcount == 0:
            raise ValueError(f"{self._model} with ID: {args.id} not found")

        self.session.commit()

        stmt = (
            select(self._model)
            .filter_by(id=args.id)
        )
        updated_model = self.session.execute(stmt).first()

        return updated_model

    def create(self, args):
        create_data = args.model_dump()
        create_model = self._model(**create_data)
        self.session.add(create_model)
        self.session.commit()
        return create_model

    def get_by_id(self, args):
        stmt = (
            select(self._model)
            .filter_by(id=args)
        )
        return self.session.execute(stmt).first()

    def get_all(self, skip=None, limit=None):
        return list(
            self.session.execute(
                select(self._model)
                .offset(skip)
                .limit(limit))
        )
