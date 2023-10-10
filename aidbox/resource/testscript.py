from typing import Optional
from ..base import *

class TestScript_Variable(BackboneElement):
	defaultValue: Optional[str] = None
	description: Optional[str] = None
	expression: Optional[str] = None
	headerField: Optional[str] = None
	hint: Optional[str] = None
	name: str
	path: Optional[str] = None
	sourceId: Optional[str] = None

class TestScript_Setup_Action_Assert(BackboneElement):
	response: Optional[str] = None
	description: Optional[str] = None
	path: Optional[str] = None
	headerField: Optional[str] = None
	compareToSourceId: Optional[str] = None
	expression: Optional[str] = None
	value: Optional[str] = None
	warningOnly: bool
	compareToSourceExpression: Optional[str] = None
	label: Optional[str] = None
	resource: Optional[str] = None
	responseCode: Optional[str] = None
	minimumId: Optional[str] = None
	operator: Optional[str] = None
	contentType: Optional[str] = None
	compareToSourcePath: Optional[str] = None
	validateProfileId: Optional[str] = None
	sourceId: Optional[str] = None
	requestMethod: Optional[str] = None
	requestURL: Optional[str] = None
	direction: Optional[str] = None
	navigationLinks: Optional[bool] = None

class TestScript_Setup_Action_Operation_RequestHeader(BackboneElement):
	field: str
	value: str

class TestScript_Setup_Action_Operation(BackboneElement):
	description: Optional[str] = None
	method: Optional[str] = None
	targetId: Optional[str] = None
	requestHeader: list[TestScript_Setup_Action_Operation_RequestHeader] = []
	params: Optional[str] = None
	type: Optional[Coding] = None
	requestId: Optional[str] = None
	encodeRequestUrl: bool
	label: Optional[str] = None
	resource: Optional[str] = None
	url: Optional[str] = None
	origin: Optional[int] = None
	contentType: Optional[str] = None
	sourceId: Optional[str] = None
	responseId: Optional[str] = None
	destination: Optional[int] = None
	accept: Optional[str] = None

class TestScript_Setup_Action(BackboneElement):
	assert_: Optional[TestScript_Setup_Action_Assert] = None
	operation: Optional[TestScript_Setup_Action_Operation] = None

class TestScript_Setup(BackboneElement):
	action: list[TestScript_Setup_Action]

class TestScript_Origin(BackboneElement):
	index: int
	profile: Coding

class TestScript_Fixture(BackboneElement):
	autocreate: bool
	autodelete: bool
	resource: Optional[Reference] = None

class TestScript_Teardown_Action(BackboneElement):
	operation: str

class TestScript_Teardown(BackboneElement):
	action: list[TestScript_Teardown_Action]

class TestScript_Metadata_Capability(BackboneElement):
	capabilities: str
	description: Optional[str] = None
	destination: Optional[int] = None
	link: list[str] = []
	origin: list[int] = []
	required: bool
	validated: bool

class TestScript_Metadata_Link(BackboneElement):
	description: Optional[str] = None
	url: str

class TestScript_Metadata(BackboneElement):
	capability: list[TestScript_Metadata_Capability]
	link: list[TestScript_Metadata_Link] = []

class TestScript_Destination(BackboneElement):
	index: int
	profile: Coding

class TestScript_Test_Action(BackboneElement):
	assert_: Optional[str] = None
	operation: Optional[str] = None

class TestScript_Test(BackboneElement):
	action: list[TestScript_Test_Action]
	description: Optional[str] = None
	name: Optional[str] = None

class TestScript(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	variable: list[TestScript_Variable] = []
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	setup: Optional[TestScript_Setup] = None
	status: str
	url: str
	identifier: Optional[Identifier] = None
	origin: list[TestScript_Origin] = []
	fixture: list[TestScript_Fixture] = []
	version: Optional[str] = None
	teardown: Optional[TestScript_Teardown] = None
	contact: list[ContactDetail] = []
	metadata: Optional[TestScript_Metadata] = None
	destination: list[TestScript_Destination] = []
	test: list[TestScript_Test] = []
	profile: list[Reference] = []

