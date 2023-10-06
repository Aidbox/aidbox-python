from typing import Optional

from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Identifier
from base import BackboneElement
from base import DomainResource


class DeviceMetric(DomainResource):
	category: str
	measurementPeriod: Optional[str] = None
	color: Optional[str] = None
	parent: Optional[Reference] = None
	unit: Optional[CodeableConcept] = None
	type: CodeableConcept
	source: Optional[Reference] = None
	identifier: list[Identifier] = []
	calibration: list[BackboneElement] = []
	operationalStatus: Optional[str] = None

