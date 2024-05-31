from pydantic import *
from typing import Optional, List
from ..base import *

class TestReport_Participant(BackboneElement):
	type: str
	uri: str
	display: Optional[str] = None

class TestReport_Setup_Action_Operation(BackboneElement):
	result: str
	message: Optional[str] = None
	detail: Optional[str] = None

class TestReport_Setup_Action_Assert(BackboneElement):
	result: str
	message: Optional[str] = None
	detail: Optional[str] = None

class TestReport_Setup_Action(BackboneElement):
	operation: Optional[TestReport_Setup_Action_Operation] = None
	assert_: Optional[TestReport_Setup_Action_Assert] = None

class TestReport_Setup(BackboneElement):
	action: List[TestReport_Setup_Action]

class TestReport_Teardown_Action(BackboneElement):
	operation: str

class TestReport_Teardown(BackboneElement):
	action: List[TestReport_Teardown_Action]

class TestReport_Test_Action(BackboneElement):
	operation: Optional[str] = None
	assert_: Optional[str] = None

class TestReport_Test(BackboneElement):
	name: Optional[str] = None
	description: Optional[str] = None
	action: List[TestReport_Test_Action]

class TestReport(DomainResource):
	tester: Optional[str] = None
	name: Optional[str] = None
	testScript: Reference
	participant: Optional[List[TestReport_Participant]] = None
	setup: Optional[TestReport_Setup] = None
	status: str
	result: str
	score: Optional[float] = None
	identifier: Optional[Identifier] = None
	issued: Optional[str] = None
	teardown: Optional[TestReport_Teardown] = None
	test: Optional[List[TestReport_Test]] = None