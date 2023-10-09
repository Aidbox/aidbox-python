from typing import Optional
from base import *

class CapabilityStatement_Document(BackboneElement):
	documentation: Optional[str] = None
	mode: str
	profile: str

class CapabilityStatement_Messaging_Endpoint(BackboneElement):
	address: str
	protocol: Coding

class CapabilityStatement_Messaging_SupportedMessage(BackboneElement):
	definition: str
	mode: str

class CapabilityStatement_Messaging(BackboneElement):
	documentation: Optional[str] = None
	endpoint: list[CapabilityStatement_Messaging_Endpoint] = []
	reliableCache: Optional[str] = None
	supportedMessage: list[CapabilityStatement_Messaging_SupportedMessage] = []

class CapabilityStatement_Software(BackboneElement):
	name: str
	releaseDate: Optional[str] = None
	version: Optional[str] = None

class CapabilityStatement_Implementation(BackboneElement):
	custodian: Optional[Reference] = None
	description: str
	url: Optional[str] = None

class CapabilityStatement_Rest_Interaction(BackboneElement):
	code: str
	documentation: Optional[str] = None

class CapabilityStatement_Rest_Resource_SearchParam(BackboneElement):
	definition: Optional[str] = None
	documentation: Optional[str] = None
	name: str
	type: str

class CapabilityStatement_Rest_Resource_Operation(BackboneElement):
	definition: str
	documentation: Optional[str] = None
	name: str

class CapabilityStatement_Rest_Resource_Interaction(BackboneElement):
	code: str
	documentation: Optional[str] = None

class CapabilityStatement_Rest_Resource(BackboneElement):
	searchRevInclude: list[str] = []
	searchParam: list[CapabilityStatement_Rest_Resource_SearchParam] = []
	conditionalUpdate: Optional[bool] = None
	conditionalRead: Optional[str] = None
	operation: list[CapabilityStatement_Rest_Resource_Operation] = []
	referencePolicy: list[str] = []
	readHistory: Optional[bool] = None
	type: str
	interaction: list[CapabilityStatement_Rest_Resource_Interaction] = []
	documentation: Optional[str] = None
	updateCreate: Optional[bool] = None
	conditionalCreate: Optional[bool] = None
	supportedProfile: list[str] = []
	searchInclude: list[str] = []
	versioning: Optional[str] = None
	profile: Optional[str] = None
	conditionalDelete: Optional[str] = None

class CapabilityStatement_Rest_Security(BackboneElement):
	cors: Optional[bool] = None
	description: Optional[str] = None
	service: list[CodeableConcept] = []

class CapabilityStatement_Rest(BackboneElement):
	compartment: list[str] = []
	documentation: Optional[str] = None
	interaction: list[CapabilityStatement_Rest_Interaction] = []
	mode: str
	operation: list[str] = []
	resource: list[CapabilityStatement_Rest_Resource] = []
	searchParam: list[str] = []
	security: Optional[CapabilityStatement_Rest_Security] = None

class CapabilityStatement(DomainResource):
	description: Optional[str] = None
	format: list[str]
	date: str
	publisher: Optional[str] = None
	patchFormat: list[str] = []
	fhirVersion: str
	jurisdiction: list[CodeableConcept] = []
	instantiates: list[str] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	imports: list[str] = []
	title: Optional[str] = None
	document: list[CapabilityStatement_Document] = []
	status: str
	messaging: list[CapabilityStatement_Messaging] = []
	kind: str
	implementationGuide: list[str] = []
	url: Optional[str] = None
	software: Optional[CapabilityStatement_Software] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	implementation: Optional[CapabilityStatement_Implementation] = None
	rest: list[CapabilityStatement_Rest] = []

