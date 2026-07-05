from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32

iris = Entity(
    name="iris_id",
    join_keys=["iris_id"],
)

iris_source = FileSource(
    name="iris_source",
    path="data/iris_data_adapted_for_feast.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

iris_features = FeatureView(
    name="iris_features",
    entities=[iris],
    ttl=timedelta(days=365),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
    ],
    source=iris_source,
)