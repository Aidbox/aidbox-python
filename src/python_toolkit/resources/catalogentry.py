from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Period
from base import Identifier
from base import Identifier
from base import BackboneElement
from base import DomainResource


class CatalogEntry(DomainResource):
	additionalCharacteristic: list[CodeableConcept] = []
	additionalClassification: list[CodeableConcept] = []
	referencedItem: Reference
	type: Optional[CodeableConcept] = None
	classification: list[CodeableConcept] = []
	validityPeriod: Optional[Period] = None
	orderable: bool
	status: Optional[str] = None
	validTo: Optional[str] = None
	identifier: list[Identifier] = []
	additionalIdentifier: list[Identifier] = []
	lastUpdated: Optional[str] = None
	relatedEntry: list[BackboneElement] = []

