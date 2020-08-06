#from __future__ import annotations
import numpy as np
from pandas._typing import DType, Label, TT, UU
from pandas.core.arrays import ExtensionArray
from pandas.core.base import IndexOpsMixin, PandasObject
from pandas.core.strings import StringMethods
from typing import Any, Dict, Generic, Hashable, Iterable, Iterator, List, Optional, Sequence, Tuple, Type, Union, overload

class InvalidIndexError(Exception): ...

class Index(IndexOpsMixin[TT], PandasObject, Generic[TT]):
    @property
    def str(self) -> StringMethods: ...
    def __new__(cls: Any, data: Any=..., dtype: Any=..., copy: Any=..., name: Any=..., tupleize_cols: Any=..., **kwargs: Any) -> Index: ...
    def __init__(
        self, data: Iterable[TT], dtype: Any = ..., copy: bool = ..., name: Any = ..., tupleize_cols: bool = ...,
    ): ...
    @property
    def asi8(self) -> None: ...
    def is_(self, other: Any) -> bool: ...
    def __len__(self) -> int: ...
    def __array__(self, dtype: Any=...) -> np.ndarray: ...
    def __array_wrap__(self, result: Any, context: Optional[Any] = ...): ...
    def dtype(self): ...
    def ravel(self, order: str = ...): ...
    def view(self, cls: Optional[Any] = ...): ...
    @overload
    def astype(self, dtype: Type[UU]) -> Index[UU]: ...
    @overload
    def astype(self, dtype: str) -> Index: ...
    def take(self, indices: Any, axis: int = ..., allow_fill: bool = ..., fill_value: Optional[Any] = ..., **kwargs: Any): ...
    def repeat(self, repeats: Any, axis: Optional[Any] = ...): ...
    def copy(self, name: Optional[Any] = ..., deep: bool = ..., dtype: Optional[Any] = ..., **kwargs: Any): ...
    def __copy__(self, **kwargs: Any): ...
    def __deepcopy__(self, memo: Optional[Any] = ...): ...
    def format(self, name: bool = ..., formatter: Optional[Any] = ..., **kwargs: Any): ...
    def to_native_types(self, slicer: Optional[Any] = ..., **kwargs: Any): ...
    def to_flat_index(self): ...
    def to_series(self, index: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def to_frame(self, index: bool = ..., name: Any = ...) -> DataFrame: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, value: Any) -> None: ...
    @property
    def names(self) -> List[str]: ...
    def set_names(self, names: Any, level: Optional[Any] = ..., inplace: bool = ...): ...
    def rename(self, name: Any, inplace: bool = ...): ...
    @property
    def nlevels(self) -> int: ...
    def sortlevel(self, level: Optional[Any] = ..., ascending: bool = ..., sort_remaining: Optional[Any] = ...): ...
    def get_level_values(self, level: str) -> Index: ...
    def droplevel(self, level: int = ...): ...
    @property
    def is_monotonic(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def is_unique(self) -> bool: ...
    @property
    def has_duplicates(self) -> bool: ...
    def is_boolean(self) -> bool: ...
    def is_integer(self) -> bool: ...
    def is_floating(self) -> bool: ...
    def is_numeric(self) -> bool: ...
    def is_object(self) -> bool: ...
    def is_categorical(self) -> bool: ...
    def is_interval(self) -> bool: ...
    def is_mixed(self) -> bool: ...
    def holds_integer(self): ...
    def inferred_type(self): ...
    def is_all_dates(self) -> bool: ...
    def __reduce__(self): ...
    def hasnans(self) -> bool: ...
    def isna(self): ...
    isnull: Any = ...
    def notna(self): ...
    notnull: Any = ...
    def fillna(self, value: Optional[Any] = ..., downcast: Optional[Any] = ...): ...
    def dropna(self, how: str = ...): ...
    def unique(self, level: Optional[Any] = ...): ...
    def drop_duplicates(self, keep: str = ...): ...
    def duplicated(self, keep: str = ...): ...
    def __add__(self, other: Any) -> Index[TT]: ...
    def __radd__(self, other: Any) -> Index[TT]: ...
    def __iadd__(self, other: Any) -> Index[TT]: ...
    def __sub__(self, other: Any) -> Index[TT]: ...
    def __rsub__(self, other: Any) -> Index[TT]: ...
    def __and__(self, other: Any) -> Index[TT]: ...
    def __or__(self, other: Any) -> Index[TT]: ...
    def __xor__(self, other: Any) -> Index[TT]: ...
    def __nonzero__(self) -> None: ...
    __bool__: Any = ...
    def union(self, other: Union[List[TT], Index[TT]], sort: Optional[Any] = ...) -> Index[TT]: ...
    def intersection(self, other: Union[List[TT], Index[TT]], sort: bool = ...) -> Index[TT]: ...
    def difference(self, other: Union[List[TT], Index[TT]]) -> Index[TT]: ...
    def symmetric_difference(self, other: Union[List[TT], Index[TT]], result_name: Optional[Any] = ..., sort: Optional[Any] = ...) -> Index[TT]: ...
    def get_loc(self, key: Any, method: Optional[Any] = ..., tolerance: Optional[Any] = ...): ...
    def get_indexer(self, target: Any, method: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...): ...
    def reindex(self, target: Any, method: Optional[Any] = ..., level: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...): ...
    def join(self, other: Any, how: str = ..., level: Optional[Any] = ..., return_indexers: bool = ..., sort: bool = ...): ...
    @property
    def values(self) -> np.ndarray: ...
    def array(self) -> ExtensionArray: ...
    def memory_usage(self, deep: bool = ...): ...
    def where(self, cond: Any, other: Optional[Any] = ...): ...
    def is_type_compatible(self, kind: Any) -> bool: ...
    def __contains__(self, key: Any) -> bool: ...
    def __hash__(self) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    @overload
    def __getitem__(self, idx: Union[int, Series[bool], slice, np.ndarray]) -> TT: ...
    @overload
    def __getitem__(self, idx: Index[TT]) -> Index[TT]: ...
    @overload
    def __getitem__(self, idx: Tuple[np.ndarray, ...]) -> TT: ...
    def append(self, other: Any): ...
    def putmask(self, mask: Any, value: Any): ...
    def equals(self, other: Any) -> bool: ...
    def identical(self, other: Any) -> bool: ...
    def asof(self, label: Any): ...
    def asof_locs(self, where: Any, mask: Any): ...
    def sort_values(self, return_indexer: bool = ..., ascending: bool = ...): ...
    def sort(self, *args: Any, **kwargs: Any) -> None: ...
    def shift(self, periods: int = ..., freq: Optional[Any] = ...) -> None: ...
    def argsort(self, *args: Any, **kwargs: Any): ...
    def get_value(self, series: Any, key: Any): ...
    def set_value(self, arr: Any, key: Any, value: Any) -> None: ...
    def get_indexer_non_unique(self, target: Any): ...
    def get_indexer_for(self, target: Any, **kwargs: Any): ...
    def groupby(self, values: Any) -> Dict[Hashable, np.ndarray]: ...
    def map(self, mapper: Any, na_action: Optional[Any] = ...) -> Index: ...
    def isin(self, values: Any, level: Optional[Any] = ...): ...
    def slice_indexer(self, start: Optional[Any] = ..., end: Optional[Any] = ..., step: Optional[Any] = ..., kind: Optional[Any] = ...): ...
    def get_slice_bound(self, label: Any, side: Any, kind: Any): ...
    def slice_locs(self, start: Optional[Any] = ..., end: Optional[Any] = ..., step: Optional[Any] = ..., kind: Optional[Any] = ...): ...
    def delete(self, loc: Any): ...
    def insert(self, loc: Any, item: Any): ...
    def drop(self, labels: Any, errors: str = ...): ...
    @property
    def shape(self) -> Tuple[int, ...]: ...

    # Extra methods from old stubs    

    def __eq__(self, other: object) -> Series: ...  # type: ignore
    @overload
    def __iter__(self) -> Iterator: ...
    def __ne__(self, other: str) -> Index[TT]: ...  # type: ignore


def ensure_index_from_sequences(sequences: Sequence[Sequence[DType]], names: Sequence[str]=...) -> Index: ...
def ensure_index(index_like: Union[Sequence, Index], copy: bool=...) -> Index: ...
def maybe_extract_name(name, obj, cls) -> Label: ...

from pandas.core.series import Series
from pandas.core.frame import DataFrame