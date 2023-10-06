from typing import Optional

from base import ContactDetail
from base import CodeableConcept
from base import UsageContext
from base import CodeableConcept
from base import Annotation
from base import ContactDetail
from base import BackboneElement
from base import Identifier
from base import ContactDetail
from base import ContactDetail
from base import RelatedArtifact
from base import ContactDetail
from base import Period
from base import DomainResource


class EvidenceVariable(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	type: Optional[str] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	note: list[Annotation] = []
	author: list[ContactDetail] = []
	characteristic: list[BackboneElement]
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	reviewer: list[ContactDetail] = []
	shortTitle: Optional[str] = None
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	effectivePeriod: Optional[Period] = None

