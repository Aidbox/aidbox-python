from typing import Optional

from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import Attachment
from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import DomainResource


class Consent(DomainResource):
	patient: Optional[Reference] = None
	category: list[CodeableConcept]
	provision: Optional[BackboneElement] = None
	sourceAttachment: Optional[Attachment] = None
	organization: list[Reference] = []
	verification: list[BackboneElement] = []
	scope: CodeableConcept
	policy: list[BackboneElement] = []
	sourceReference: Optional[Reference] = None
	dateTime: Optional[str] = None
	status: str
	policyRule: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	performer: list[Reference] = []

