from typing import Optional
from ..base import *

class TestReport_Participant(BackboneElement):
	display: Optional[str] = None
	type: str
	uri: str

class TestReport_Setup_Action_Assert(BackboneElement):
	detail: Optional[str] = None
	message: Optional[str] = None
	result: str

class TestReport_Setup_Action_Operation(BackboneElement):
	detail: Optional[str] = None
	message: Optional[str] = None
	result: str

class TestReport_Setup_Action(BackboneElement):
	assert_: Optional[TestReport_Setup_Action_Assert] = None
	operation: Optional[TestReport_Setup_Action_Operation] = None

class TestReport_Setup(BackboneElement):
	action: list[TestReport_Setup_Action]

class TestReport_Teardown_Action(BackboneElement):
	operation: str

class TestReport_Teardown(BackboneElement):
	action: list[TestReport_Teardown_Action]

class TestReport_Test_Action(BackboneElement):
	assert_: Optional[str] = None
	operation: Optional[str] = None

class TestReport_Test(BackboneElement):
	action: list[TestReport_Test_Action]
	description: Optional[str] = None
	name: Optional[str] = None

class TestReport(DomainResource):
	tester: Optional[str] = None
	name: Optional[str] = None
	testScript: Reference
	participant: list[TestReport_Participant] = []
	setup: Optional[TestReport_Setup] = None
	status: str
	result: str
	score: Optional[str] = None
	identifier: Optional[Identifier] = None
	issued: Optional[str] = None
	teardown: Optional[TestReport_Teardown] = None
	test: list[TestReport_Test] = []

