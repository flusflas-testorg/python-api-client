# generated by datamodel-codegen:
#   filename:  anythingdb.yaml
#   timestamp: 2023-01-16T13:59:45+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import Field, conint, constr

from swx.models.basemodel import IterBaseModel


class AnyValue(IterBaseModel):
    __root__: Any = Field(
        ..., description="Can be any value - string, number, boolean, array or object."
    )


class Type(Enum):
    boolean = "boolean"
    integer = "integer"
    number = "number"
    string = "string"
    object = "object"
    array = "array"
    null = "null"


class DataSchema(IterBaseModel):

    field_type: Optional[Union[str, List[str]]] = Field(None, alias="@type")
    description: Optional[str] = None
    title: Optional[str] = None
    readOnly: Optional[bool] = None
    oneOf: Optional[List[DataSchema]] = None
    unit: Optional[str] = None
    enum: Optional[List] = Field(None, min_items=1, unique_items=True)
    const: Optional[Any] = None
    type: Optional[Type] = None
    items: Optional[Union[DataSchema, List[DataSchema]]] = None
    maxItems: Optional[conint(ge=0)] = None
    minItems: Optional[conint(ge=0)] = None
    minimum: Optional[float] = None
    maximum: Optional[float] = None
    properties: Optional[Any] = None
    required: Optional[List[str]] = None


class InteractionAffordance(IterBaseModel):
    field_type: Optional[Union[str, List[str]]] = Field(None, alias="@type")
    title: Optional[str] = None
    description: Optional[str] = None


class PropertyAffordance(InteractionAffordance):
    observable: Optional[bool] = None


class ActionAffordance(InteractionAffordance):
    input: Optional[DataSchema] = None
    output: Optional[DataSchema] = None
    safe: Optional[bool] = None
    idempotent: Optional[bool] = None


class EventAffordance(InteractionAffordance):
    subscription: Optional[DataSchema] = None
    data: Optional[DataSchema] = None
    cancellation: Optional[DataSchema] = None


class Link(IterBaseModel):
    href_pattern: Optional[str] = Field(
        None, example="/spaces/myspace/categories/cpus/things/+"
    )
    rel_pattern: Optional[str] = Field(None, example="*")
    multiple: Optional[bool] = Field(None, example=False)
    optional: Optional[bool] = Field(None, example=False)


class Validators(IterBaseModel):
    links: Optional[List[Link]] = None


class Paging(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example="")
    previous_cursor: Optional[str] = Field(None, example="")


class ModelDescription(IterBaseModel):
    name: Optional[str] = Field(
        None, description="Model name.", example="RaspberryPiModel"
    )
    version: Optional[int] = Field(None, description="Version number.", example=1)


class ModelDescriptionCategory(IterBaseModel):
    name: str = Field(..., description="Model name.", example="RaspberryPiModel")
    version: Optional[int] = Field(None, description="Version number.", example=1)


class ThingBase(IterBaseModel):
    title: Optional[str] = Field(None, example="SmartWorks Device")
    description: Optional[str] = Field(None, example="My connected SmartWorks device")
    field_type: Optional[Union[str, List[str]]] = Field(
        None, alias="@type", example=["Light", "OnOffSwitch"]
    )
    model: Optional[ModelDescription] = None
    properties: Optional[Dict[str, PropertyAffordance]] = Field(
        None,
        example={
            "cpu": {
                "title": "CPU %",
                "description": "Device CPU usage in percent",
                "type": "number",
                "unit": "percent",
                "readOnly": False,
            },
            "disk": {
                "title": "Disk %",
                "description": "Device Disk usage in percent",
                "type": "number",
                "unit": "percent",
                "readOnly": False,
            },
            "memory": {
                "title": "Memory %",
                "description": "Device Memory usage in percent",
                "type": "number",
                "unit": "percent",
                "readOnly": False,
            },
        },
    )
    actions: Optional[Dict[str, ActionAffordance]] = Field(
        None,
        example={
            "delay": {
                "title": "Delay",
                "description": "Change sending frequency",
                "input": {
                    "properties": {
                        "input": {"maximum": 100, "minimum": 3, "type": "number"}
                    }
                },
            },
            "reboot": {"title": "Reboot", "description": "Reboot device"},
        },
    )
    events: Optional[Dict[str, EventAffordance]] = Field(
        None,
        example={
            "highCPU": {
                "title": "High CPU",
                "description": "The CPU usage is over 50%",
                "data": {"type": "number", "unit": "percent"},
            }
        },
    )


class Thing(ThingBase):
    uid: Optional[str] = Field(None, example="01FPSXTMN4CEGX09HF5RQ4RMY6")
    id: Optional[str] = Field(
        None,
        example="https://api.swx.altairone.com/beta/spaces/space01/things/01FPSXTMN4CEGX09HF5RQ4RMY6",
    )
    categories: Optional[List[str]] = Field(None, example=["category1", "category2"])
    created: Optional[datetime] = Field(None, example="2021-12-13T09:38:11Z")
    modified: Optional[datetime] = Field(None, example="2021-12-13T09:38:11Z")


class Paging3(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example="")
    previous_cursor: Optional[str] = Field(None, example="")


class ThingList(IterBaseModel):
    data: Optional[List[Thing]] = None
    paging: Optional[Paging3] = None


class ActionValue(IterBaseModel):
    input: Optional[AnyValue] = None
    status: Optional[str] = None
    timeRequested: Optional[datetime] = None
    timeCompleted: Optional[datetime] = None
    href: Optional[str] = None


class ActionCreateRequest1(IterBaseModel):
    input: Optional[AnyValue] = None


class ActionCreateRequest(IterBaseModel):
    __root__: Optional[Dict[str, ActionCreateRequest1]] = None


class ActionResponse(IterBaseModel):
    __root__: Optional[Dict[str, ActionValue]] = None


class Paging5(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example="")
    previous_cursor: Optional[str] = Field(None, example="")


class ActionListResponse(IterBaseModel):
    data: Optional[List[ActionResponse]] = Field(
        None,
        example=[
            {
                "delay": {
                    "input": {"delay": 5},
                    "status": "pending",
                    "timeRequested": "2022-06-02 15:37:46+0000",
                    "href": "/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCAQE78A7CP6REXV5J8BAKR",
                }
            },
            {
                "delay": {
                    "input": {"delay": 7},
                    "status": "pending",
                    "timeRequested": "2022-06-02 15:39:54+0000",
                    "href": "/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCB9FMD0Q3QR0YV4TWY4S3E",
                }
            },
            {
                "reboot": {
                    "status": "pending",
                    "timeRequested": "2022-06-02 15:56:12+0000",
                    "href": "/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCCZYATJW1Z3D4T4BA4S2QH",
                }
            },
        ],
    )
    paging: Optional[Paging5] = None


class ActionUpdateRequest1(IterBaseModel):
    output: Optional[AnyValue] = None
    status: Optional[str] = None


class ActionUpdateRequest(IterBaseModel):
    __root__: Optional[Dict[str, ActionUpdateRequest1]] = None


class EventValue(IterBaseModel):
    data: Optional[AnyValue] = None
    href: Optional[str] = None
    timestamp: Optional[datetime] = None


class EventCreateRequest1(IterBaseModel):
    data: Optional[AnyValue] = None


class EventCreateRequest(IterBaseModel):
    __root__: Optional[Dict[str, EventCreateRequest1]] = None


class EventResponse(IterBaseModel):
    __root__: Optional[Dict[str, EventValue]] = None


class Paging6(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example="")
    previous_cursor: Optional[str] = Field(None, example="")


class EventListResponse(IterBaseModel):
    data: Optional[List[EventResponse]] = Field(
        None,
        example=[
            {
                "highCPU": {
                    "data": 61,
                    "timestamp": "2020-04-02 15:22:37+0000",
                    "href": "/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/events/highCPU/01EDCEZDTJX50SQTCJST5EW5NX",
                }
            },
            {
                "highCPU": {
                    "data": 85,
                    "timestamp": "2020-04-02 15:26:42+0000",
                    "href": "/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/events/highCPU/01EDCGYKV4YQ1CY3QHHSX8J843",
                }
            },
            {
                "lowDiskSpace": {
                    "data": 95,
                    "timestamp": "2020-04-03 07:12:55+0000",
                    "href": "/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/events/lowDiskSpace/01GPX7BR5X3YT5Y65ZMT24YT1N",
                }
            },
        ],
    )
    paging: Optional[Paging6] = None


class Properties(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class Property(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class CategoryBase(IterBaseModel):
    name: Optional[constr(regex=r"^[a-zA-Z0-9_:-]{1,26}$")] = Field(
        None,
        description="Name of the Category that will be used as a unique identifier.",
        example="ElectronicBoards",
    )
    description: Optional[str] = Field(None, example="My category")
    model: Optional[ModelDescriptionCategory] = None
    validators: Optional[Validators] = None


class Category(CategoryBase):
    created: Optional[datetime] = Field(None, example="2021-11-17T03:15:40Z")
    modified: Optional[datetime] = Field(None, example="2021-11-17T03:15:40Z")


class CategoryList(IterBaseModel):
    data: Optional[List[Category]] = None
    paging: Optional[Paging] = None


DataSchema.update_forward_refs()
