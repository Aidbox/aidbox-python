from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Bundle_Link(BackboneElement):
	relation: str
	url: str

class Bundle_Entry_Search(BackboneElement):
	mode: Optional[str] = None
	score: Optional[str] = None

class Bundle_Entry_Request(BackboneElement):
	method: str
	url: str
	ifNoneMatch: Optional[str] = None
	ifModifiedSince: Optional[str] = None
	ifMatch: Optional[str] = None
	ifNoneExist: Optional[str] = None

class Bundle_Entry_Response(BackboneElement):
	status: str
	location: Optional[str] = None
	etag: Optional[str] = None
	lastModified: Optional[str] = None
	outcome: Optional[Resource] = None

class Bundle_Entry(BackboneElement):
	link: Optional[List[str]] = None
	fullUrl: Optional[str] = None
	resource: Optional[Resource] = None
	search: Optional[Bundle_Entry_Search] = None
	request: Optional[Bundle_Entry_Request] = None
	response: Optional[Bundle_Entry_Response] = None

class McodePatientBundle(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-patient-bundle"])
	identifier: Optional[Identifier] = None
	type: Literal["collection"] = "collection"
	timestamp: Optional[str] = None
	total: Optional[str] = None
	link: Optional[List[Bundle_Link]] = None
	entry: List[Bundle_Entry]
	signature: Optional[Signature] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None