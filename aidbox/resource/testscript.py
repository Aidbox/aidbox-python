from pydantic import *
from typing import Optional, List
from ..base import *

class TestScript_Variable(BackboneElement):
	name: str
	defaultValue: Optional[str] = None
	description: Optional[str] = None
	expression: Optional[str] = None
	headerField: Optional[str] = None
	hint: Optional[str] = None
	path: Optional[str] = None
	sourceId: Optional[str] = None

class TestScript_Setup_Action_Operation_RequestHeader(BackboneElement):
	field: str
	value: str

class TestScript_Setup_Action_Operation(BackboneElement):
	description: Optional[str] = None
	method: Optional[str] = None
	targetId: Optional[str] = None
	requestHeader: Optional[List[TestScript_Setup_Action_Operation_RequestHeader]] = None
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

class TestScript_Setup_Action(BackboneElement):
	operation: Optional[TestScript_Setup_Action_Operation] = None
	assert_: Optional[TestScript_Setup_Action_Assert] = None

class TestScript_Setup(BackboneElement):
	action: List[TestScript_Setup_Action]

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
	action: List[TestScript_Teardown_Action]

class TestScript_Metadata_Link(BackboneElement):
	url: str
	description: Optional[str] = None

class TestScript_Metadata_Capability(BackboneElement):
	required: bool
	validated: bool
	description: Optional[str] = None
	origin: Optional[List[int]] = None
	destination: Optional[int] = None
	link: Optional[List[str]] = None
	capabilities: str

class TestScript_Metadata(BackboneElement):
	link: Optional[List[TestScript_Metadata_Link]] = None
	capability: List[TestScript_Metadata_Capability]

class TestScript_Destination(BackboneElement):
	index: int
	profile: Coding

class TestScript_Test_Action(BackboneElement):
	operation: Optional[str] = None
	assert_: Optional[str] = None

class TestScript_Test(BackboneElement):
	name: Optional[str] = None
	description: Optional[str] = None
	action: List[TestScript_Test_Action]

class TestScript(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	variable: Optional[List[TestScript_Variable]] = None
	publisher: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	setup: Optional[TestScript_Setup] = None
	status: str
	url: str
	identifier: Optional[Identifier] = None
	origin: Optional[List[TestScript_Origin]] = None
	fixture: Optional[List[TestScript_Fixture]] = None
	version: Optional[str] = None
	teardown: Optional[TestScript_Teardown] = None
	contact: Optional[List[ContactDetail]] = None
	metadata: Optional[TestScript_Metadata] = None
	destination: Optional[List[TestScript_Destination]] = None
	test: Optional[List[TestScript_Test]] = None
	profile: Optional[List[Reference]] = None