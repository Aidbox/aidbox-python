from typing import Optional
from ..base import *

class ExampleScenario_Instance_ContainedInstance(BackboneElement):
	resourceId: str
	versionId: Optional[str] = None

class ExampleScenario_Instance_Version(BackboneElement):
	description: str
	versionId: str

class ExampleScenario_Instance(BackboneElement):
	containedInstance: list[ExampleScenario_Instance_ContainedInstance] = []
	description: Optional[str] = None
	name: Optional[str] = None
	resourceId: str
	resourceType: str
	version: list[ExampleScenario_Instance_Version] = []

class ExampleScenario_Process_Step_Alternative(BackboneElement):
	description: Optional[str] = None
	step: list[str] = []
	title: str

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

class ExampleScenario_Process_Step(BackboneElement):
	alternative: list[ExampleScenario_Process_Step_Alternative] = []
	operation: Optional[ExampleScenario_Process_Step_Operation] = None
	pause: Optional[bool] = None
	process: list[str] = []

class ExampleScenario_Process(BackboneElement):
	description: Optional[str] = None
	postConditions: Optional[str] = None
	preConditions: Optional[str] = None
	step: list[ExampleScenario_Process_Step] = []
	title: str

class ExampleScenario_Actor(BackboneElement):
	actorId: str
	description: Optional[str] = None
	name: Optional[str] = None
	type: str

class ExampleScenario(DomainResource):
	date: Optional[str] = None
	publisher: Optional[str] = None
	instance: list[ExampleScenario_Instance] = []
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	process: list[ExampleScenario_Process] = []
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	workflow: list[str] = []
	status: str
	url: Optional[str] = None
	identifier: list[Identifier] = []
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	actor: list[ExampleScenario_Actor] = []

