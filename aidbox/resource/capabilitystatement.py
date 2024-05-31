from pydantic import *
from typing import Optional, List
from ..base import *

class CapabilityStatement_Document(BackboneElement):
	mode: str
	documentation: Optional[str] = None
	profile: str

class CapabilityStatement_Messaging_Endpoint(BackboneElement):
	protocol: Coding
	address: str

class CapabilityStatement_Messaging_SupportedMessage(BackboneElement):
	mode: str
	definition: str

class CapabilityStatement_Messaging(BackboneElement):
	endpoint: Optional[List[CapabilityStatement_Messaging_Endpoint]] = None
	reliableCache: Optional[NonNegativeInt] = None
	documentation: Optional[str] = None
	supportedMessage: Optional[List[CapabilityStatement_Messaging_SupportedMessage]] = None

class CapabilityStatement_Software(BackboneElement):
	name: str
	version: Optional[str] = None
	releaseDate: Optional[str] = None

class CapabilityStatement_Implementation(BackboneElement):
	description: str
	url: Optional[str] = None
	custodian: Optional[Reference] = None

class CapabilityStatement_Rest_Security(BackboneElement):
	cors: Optional[bool] = None
	service: Optional[List[CodeableConcept]] = None
	description: Optional[str] = None

class CapabilityStatement_Rest_Resource_SearchParam(BackboneElement):
	name: str
	definition: Optional[str] = None
	type: str
	documentation: Optional[str] = None

class CapabilityStatement_Rest_Resource_Operation(BackboneElement):
	name: str
	definition: str
	documentation: Optional[str] = None

class CapabilityStatement_Rest_Resource_Interaction(BackboneElement):
	code: str
	documentation: Optional[str] = None

class CapabilityStatement_Rest_Resource(BackboneElement):
	searchRevInclude: Optional[List[str]] = None
	searchParam: Optional[List[CapabilityStatement_Rest_Resource_SearchParam]] = None
	conditionalUpdate: Optional[bool] = None
	conditionalRead: Optional[str] = None
	operation: Optional[List[CapabilityStatement_Rest_Resource_Operation]] = None
	referencePolicy: Optional[List[str]] = None
	readHistory: Optional[bool] = None
	type: str
	interaction: Optional[List[CapabilityStatement_Rest_Resource_Interaction]] = None
	documentation: Optional[str] = None
	updateCreate: Optional[bool] = None
	conditionalCreate: Optional[bool] = None
	supportedProfile: Optional[List[str]] = None
	searchInclude: Optional[List[str]] = None
	versioning: Optional[str] = None
	profile: Optional[str] = None
	conditionalDelete: Optional[str] = None

class CapabilityStatement_Rest_Interaction(BackboneElement):
	code: str
	documentation: Optional[str] = None

class CapabilityStatement_Rest(BackboneElement):
	mode: str
	documentation: Optional[str] = None
	security: Optional[CapabilityStatement_Rest_Security] = None
	resource: Optional[List[CapabilityStatement_Rest_Resource]] = None
	interaction: Optional[List[CapabilityStatement_Rest_Interaction]] = None
	searchParam: Optional[List[str]] = None
	operation: Optional[List[str]] = None
	compartment: Optional[List[str]] = None

class CapabilityStatement(DomainResource):
	description: Optional[str] = None
	format: List[str]
	date: str
	publisher: Optional[str] = None
	patchFormat: Optional[List[str]] = None
	fhirVersion: str
	jurisdiction: Optional[List[CodeableConcept]] = None
	instantiates: Optional[List[str]] = None
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	imports: Optional[List[str]] = None
	title: Optional[str] = None
	document: Optional[List[CapabilityStatement_Document]] = None
	status: str
	messaging: Optional[List[CapabilityStatement_Messaging]] = None
	kind: str
	implementationGuide: Optional[List[str]] = None
	url: Optional[str] = None
	software: Optional[CapabilityStatement_Software] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None
	implementation: Optional[CapabilityStatement_Implementation] = None
	rest: Optional[List[CapabilityStatement_Rest]] = None