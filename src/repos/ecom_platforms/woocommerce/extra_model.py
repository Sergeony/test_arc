import schemas
from .common import CommonRepo
from .helpers import request
from .schemas import ExtraModelRead


__all__ = [
    "ExtraModelRepo",
]


class ExtraModelRepo(CommonRepo):
    async def get_by_id(self, id_schema: schemas.IdSchema) -> schemas.IdSchema:
        # convert data for request to WooCommerce native schema
        body = ExtraModelRead(
            some_field=id_schema.id,
        ).model_dump()

        # process the query
        response = await request(
            credentials=self.credentials,
            endpoint=f"/warehouses",
            body=body,
        )

        # validate response with Woocommerce native schema
        data = ExtraModelRead(json=response.get("data"))

        # return response converted back to our Location schema
        return schemas.IdSchema(
            id=data.some_field
        )
