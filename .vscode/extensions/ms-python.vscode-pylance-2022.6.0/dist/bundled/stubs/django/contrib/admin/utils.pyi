import datetime
import sys
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Set, Tuple, Type, Union, overload
from uuid import UUID

from django.contrib.admin.options import BaseModelAdmin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.db.models.base import Model
from django.db.models.deletion import Collector
from django.db.models.fields import Field, reverse_related
from django.db.models.options import Options
from django.db.models.query import QuerySet
from django.forms.forms import BaseForm
from django.forms.formsets import BaseFormSet
from django.http.request import HttpRequest
from django.utils.datastructures import _IndexableCollection

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

class FieldIsAForeignKeyColumnName(Exception): ...

def lookup_needs_distinct(opts: Options, lookup_path: str) -> bool: ...
def prepare_lookup_value(key: str, value: Union[datetime.datetime, str]) -> Union[bool, datetime.datetime, str]: ...
def quote(s: Union[int, str, UUID]) -> str: ...
def unquote(s: str) -> str: ...
def flatten(fields: Any) -> List[Union[Callable, str]]: ...
def flatten_fieldsets(fieldsets: Any) -> List[Union[Callable, str]]: ...
def get_deleted_objects(
    objs: Union[Sequence[Optional[Model]], QuerySet[Model]], request: HttpRequest, admin_site: AdminSite
) -> Tuple[List[Model], Dict[str, int], Set[str], List[str]]: ...

class NestedObjects(Collector):
    data: Dict[str, Any]
    dependencies: Dict[Any, Any]
    fast_deletes: List[Any]
    field_updates: Dict[Any, Any]
    using: str
    edges: Any = ...
    protected: Any = ...
    model_objs: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def add_edge(self, source: Optional[Model], target: Model) -> None: ...
    def related_objects(
        self, related_model: Type[Model], related_fields: Iterable[Field], objs: _IndexableCollection[Model]
    ) -> QuerySet[Model]: ...
    def nested(self, format_callback: Callable = ...) -> List[Any]: ...
    def can_fast_delete(self, *args: Any, **kwargs: Any) -> bool: ...

def model_format_dict(obj: Union[Model, Type[Model], QuerySet, Options[Model]]): ...
def model_ngettext(obj: Union[Options, QuerySet], n: Optional[int] = ...) -> str: ...
def lookup_field(
    name: Union[Callable, str], obj: Model, model_admin: Optional[BaseModelAdmin] = ...
) -> Tuple[Optional[Field], Optional[str], Any]: ...
@overload
def label_for_field(  # type: ignore
    name: Union[Callable, str],
    model: Type[Model],
    model_admin: Optional[BaseModelAdmin] = ...,
    return_attr: Literal[True] = ...,
    form: Optional[BaseForm] = ...,
) -> Tuple[str, Union[Callable, str, None]]: ...
@overload
def label_for_field(
    name: Union[Callable, str],
    model: Type[Model],
    model_admin: Optional[BaseModelAdmin] = ...,
    return_attr: Literal[False] = ...,
    form: Optional[BaseForm] = ...,
) -> str: ...
def help_text_for_field(name: str, model: Type[Model]) -> str: ...
def display_for_field(value: Any, field: Field, empty_value_display: str) -> str: ...
def display_for_value(value: Any, empty_value_display: str, boolean: bool = ...) -> str: ...

class NotRelationField(Exception): ...

def get_model_from_relation(field: Union[Field, reverse_related.ForeignObjectRel]) -> Type[Model]: ...
def reverse_field_path(model: Type[Model], path: str) -> Tuple[Type[Model], str]: ...
def get_fields_from_path(model: Type[Model], path: str) -> List[Field]: ...
def construct_change_message(
    form: AdminPasswordChangeForm, formsets: Iterable[BaseFormSet], add: bool
) -> List[Dict[str, Dict[str, List[str]]]]: ...
