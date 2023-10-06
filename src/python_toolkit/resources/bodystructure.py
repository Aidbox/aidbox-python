from typing import Optional

from base import Identifier
from base import Attachment
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import DomainResource


class BodyStructure(DomainResource):
	active: Optional[bool] = None
	description: Optional[str] = None
	identifier: list[Identifier] = []
	image: list[Attachment] = []
	location: Optional[CodeableConcept] = None
	locationQualifier: list[CodeableConcept] = []
	morphology: Optional[CodeableConcept] = None
	patient: Reference

