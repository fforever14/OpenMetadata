#  Copyright 2021 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""
Oracle query parsing module
"""
from abc import ABC
from typing import Optional

from metadata.generated.schema.entity.services.connections.database.oracleConnection import (
    OracleConnection,
)
from metadata.generated.schema.metadataIngestion.workflow import (
    Source as WorkflowSource,
)
from metadata.ingestion.api.steps import InvalidSourceException
from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.ingestion.source.database.query_parser_source import QueryParserSource
from metadata.utils.logger import ingestion_logger

logger = ingestion_logger()


class OracleQueryParserSource(QueryParserSource, ABC):
    """
    Oracle base for usage and lineage
    """

    filters: str

    @classmethod
    def create(
        cls, config_dict, metadata: OpenMetadata, pipeline_name: Optional[str] = None
    ):
        config: WorkflowSource = WorkflowSource.parse_obj(config_dict)
        connection: OracleConnection = config.serviceConnection.__root__.config
        if not isinstance(connection, OracleConnection):
            raise InvalidSourceException(
                f"Expected OracleConnection, but got {connection}"
            )
        return cls(config, metadata)
