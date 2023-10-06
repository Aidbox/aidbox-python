from typing import Optional

from base import DataRequirement
from base import ContactDetail
from base import CodeableConcept
from base import Attachment
from base import CodeableConcept
from base import UsageContext
from base import CodeableConcept
from base import CodeableConcept
from base import ContactDetail
from base import Identifier
from base import ContactDetail
from base import ContactDetail
from base import RelatedArtifact
from base import ContactDetail
from base import Reference
from base import ParameterDefinition
from base import Period
from base import DomainResource


class Library(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	dataRequirement: list[DataRequirement] = []
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	content: list[Attachment] = []
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	type: CodeableConcept
	experimental: Optional[bool] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	author: list[ContactDetail] = []
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	reviewer: list[ContactDetail] = []
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	subjectReference: Optional[Reference] = None
	parameter: list[ParameterDefinition] = []
	effectivePeriod: Optional[Period] = None

