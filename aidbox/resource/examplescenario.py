from pydantic import *
from typing import Optional, List
from ..base import *

class ExampleScenario_Instance_Version(BackboneElement):
	versionId: str
	description: str

class ExampleScenario_Instance_ContainedInstance(BackboneElement):
	resourceId: str
	versionId: Optional[str] = None

class ExampleScenario_Instance(BackboneElement):
	resourceId: str
	resourceType: str
	name: Optional[str] = None
	description: Optional[str] = None
	version: Optional[List[ExampleScenario_Instance_Version]] = None
	containedInstance: Optional[List[ExampleScenario_Instance_ContainedInstance]] = None

class ExampleScenario_Process_Step_Operation(BackboneElement):
	response: Optional[str] = None
	description: Optional[str] = None
	request: Optional[str] = None
	number: str
	name: Optional[str] = None
	initiator: Optional[str] = None
	type: Optional[str] = None
	receiverActive: Optional[bool] = None
	initiatorActive: Optional[bool] = None
	receiver: Optional[str] = None

class ExampleScenario_Process_Step_Alternative(BackboneElement):
	title: str
	description: Optional[str] = None
	step: Optional[List[str]] = None

class ExampleScenario_Process_Step(BackboneElement):
	process: Optional[List[str]] = None
	pause: Optional[bool] = None
	operation: Optional[ExampleScenario_Process_Step_Operation] = None
	alternative: Optional[List[ExampleScenario_Process_Step_Alternative]] = None

class ExampleScenario_Process(BackboneElement):
	title: str
	description: Optional[str] = None
	preConditions: Optional[str] = None
	postConditions: Optional[str] = None
	step: Optional[List[ExampleScenario_Process_Step]] = None

class ExampleScenario_Actor(BackboneElement):
	actorId: str
	type: str
	name: Optional[str] = None
	description: Optional[str] = None

class ExampleScenario(DomainResource):
	date: Optional[str] = None
	publisher: Optional[str] = None
	instance: Optional[List[ExampleScenario_Instance]] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	name: Optional[str] = None
	process: Optional[List[ExampleScenario_Process]] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	workflow: Optional[List[str]] = None
	status: str
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None
	actor: Optional[List[ExampleScenario_Actor]] = None