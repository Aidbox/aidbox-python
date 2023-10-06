from typing import Optional

from base import Reference
from base import BackboneElement
from base import ContactDetail
from base import CodeableConcept
from base import BackboneElement
from base import UsageContext
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Annotation
from base import ContactDetail
from base import CodeableConcept
from base import Reference
from base import Identifier
from base import ContactDetail
from base import BackboneElement
from base import ContactDetail
from base import Reference
from base import BackboneElement
from base import RelatedArtifact
from base import ContactDetail
from base import Period
from base import DomainResource


class EffectEvidenceSynthesis(DomainResource):
	description: Optional[str] = None
	exposureAlternative: Reference
	date: Optional[str] = None
	effectEstimate: list[BackboneElement] = []
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	sampleSize: Optional[BackboneElement] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	studyType: Optional[CodeableConcept] = None
	outcome: Reference
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	note: list[Annotation] = []
	author: list[ContactDetail] = []
	synthesisType: Optional[CodeableConcept] = None
	status: str
	population: Reference
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	certainty: list[BackboneElement] = []
	reviewer: list[ContactDetail] = []
	exposure: Reference
	resultsByExposure: list[BackboneElement] = []
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	effectivePeriod: Optional[Period] = None

