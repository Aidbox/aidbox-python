from typing import Optional

from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import Identifier
from base import BackboneElement
from base import BackboneElement
from base import DomainResource


class TestReport(DomainResource):
	tester: Optional[str] = None
	name: Optional[str] = None
	testScript: Reference
	participant: list[BackboneElement] = []
	setup: Optional[BackboneElement] = None
	status: str
	result: str
	score: Optional[str] = None
	identifier: Optional[Identifier] = None
	issued: Optional[str] = None
	teardown: Optional[BackboneElement] = None
	test: list[BackboneElement] = []

