import schemas
from .common import CommonRepo
from .helpers import request
from .schemas import WarehouseCreate, WarehouseRead
from .extra_model import ExtraModelRepo

__all__ = [
    "LocationRepo",
]


class LocationRepo(CommonRepo):
    async def create(self, args: schemas.LocationBase) -> schemas.LocationEcom:
        # convert data for request to WooCommerce native schema
        body = WarehouseCreate(
            warehouse_id=args.id,
        ).model_dump()

        # process the query
        response = await request(
            credentials=self.credentials,
            endpoint=f"/warehouses",
            body=body,
        )

        # do some extra stuff that is not in universal repo methods
        _ = self._some_extra_request_needed_to_create_warehouse()

        # do some extra stuff that is related to some other repo
        extra_repo = ExtraModelRepo(
            shop_url=self.credentials.get("shop_url"),
            api_key=self.credentials.get("api_key"),
        )
        one_more_extra_stuff = extra_repo.get_by_id(
            id_schema=schemas.IdSchema(id=args.id),
        )

        # validate response with Woocommerce native schema
        data = WarehouseRead(json={response.get("data"), one_more_extra_stuff})

        # return response converted back to our Location schema
        return schemas.LocationEcom(
            external_id=data.warehouse_id,
            name=data.name,
        )

    async def _some_extra_request_needed_to_create_warehouse(self):
        """ IF some of the basic Repo methods need some more queries
            or just too large to be easily tested and read,
            we create such additional functions to split it.
        """
        ...
