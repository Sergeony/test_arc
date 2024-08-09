import schemas
from .common import CommonRepo
from .helpers import write_query
from .schemas import LocationCreate, LocationRead


__all__ = [
    "LocationRepo",
]


class LocationRepo(CommonRepo):
    def create(self, args: schemas.LocationBase) -> schemas.LocationEcom:
        # convert data for request to Shopify native schema
        variables = LocationCreate(
            name=args.name,
        )

        # process the query
        response = write_query(
            credentials=self.credentials,
            model="location",
            variables=variables,
        )

        # validate response with Shopify native schema
        data = LocationRead(json=response.get("data"))

        # return response converted back to our Location schema
        return schemas.LocationEcom(
            external_id=data.location_id,
            name=data.name,
        )
