from typing import Optional

from base import BackboneElement
from base import DomainResource


class OperationOutcome(DomainResource):
	issue: list[BackboneElement]

