from typing import Optional

from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Annotation
from base import CodeableConcept
from base import CodeableConcept
from base import Identifier
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import Period
from base import Reference
from base import RelatedArtifact
from base import CodeableConcept
from base import ContactDetail
from base import Reference
from base import DomainResource


class ResearchStudy(DomainResource):
	description: Optional[str] = None
	category: list[CodeableConcept] = []
	enrollment: list[Reference] = []
	arm: list[BackboneElement] = []
	site: list[Reference] = []
	protocol: list[Reference] = []
	principalInvestigator: Optional[Reference] = None
	phase: Optional[CodeableConcept] = None
	reasonStopped: Optional[CodeableConcept] = None
	title: Optional[str] = None
	note: list[Annotation] = []
	keyword: list[CodeableConcept] = []
	status: str
	condition: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	primaryPurposeType: Optional[CodeableConcept] = None
	focus: list[CodeableConcept] = []
	objective: list[BackboneElement] = []
	period: Optional[Period] = None
	partOf: list[Reference] = []
	relatedArtifact: list[RelatedArtifact] = []
	location: list[CodeableConcept] = []
	contact: list[ContactDetail] = []
	sponsor: Optional[Reference] = None

