# Licensed to my_happy_modin Development Team under one or more contributor license agreements.
# See the NOTICE file distributed with this work for additional information regarding
# copyright ownership.  The my_happy_modin Development Team licenses this file to you under the
# Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.
import my_happy_pandas


from my_happy_pandas import (
    eval,
    cut,
    factorize,
    test,
    qcut,
    date_range,
    period_range,
    Index,
    MultiIndex,
    CategoricalIndex,
    bdate_range,
    DatetimeIndex,
    Timedelta,
    Timestamp,
    to_timedelta,
    set_eng_float_format,
    options,
    set_option,
    NaT,
    PeriodIndex,
    Categorical,
    Interval,
    UInt8Dtype,
    UInt16Dtype,
    UInt32Dtype,
    UInt64Dtype,
    SparseDtype,
    Int8Dtype,
    Int16Dtype,
    Int32Dtype,
    Int64Dtype,
    StringDtype,
    BooleanDtype,
    CategoricalDtype,
    DatetimeTZDtype,
    IntervalDtype,
    PeriodDtype,
    RangeIndex,
    Int64Index,
    UInt64Index,
    Float64Index,
    TimedeltaIndex,
    IntervalIndex,
    IndexSlice,
    Grouper,
    array,
    Period,
    show_versions,
    DateOffset,
    timedelta_range,
    infer_freq,
    interval_range,
    ExcelWriter,
    datetime,
    NamedAgg,
    NA,
)
import threading
import os
import multiprocessing

from my_happy_modin.config import Engine, Parameter

# Set this so that Pandas doesn't try to multithread by itself
os.environ["OMP_NUM_THREADS"] = "1"
DEFAULT_NPARTITIONS = 4
num_cpus = 1


_is_first_update = {}
dask_client = None
_NOINIT_ENGINES = {
    "Python",
}  # engines that don't require initialization, useful for unit tests


def _update_engine(publisher: Parameter):
    global DEFAULT_NPARTITIONS, dask_client, num_cpus
    from my_happy_modin.config import Backend, CpuCount

    if publisher.get() == "Ray":
        import ray
        from my_happy_modin.engines.ray.utils import initialize_ray

        # With OmniSci backend there is only a single worker per node
        # and we allow it to work on all cores.
        if _is_first_update.get("Ray", True):
            # initialize_ray()
            if ray.is_initialized() == False:
                ray.init(address='auto')

        num_cpus = ray.cluster_resources()["CPU"]


    elif publisher.get() not in _NOINIT_ENGINES:
        raise ImportError("Unrecognized execution engine: {}.".format(publisher.get()))

    _is_first_update[publisher.get()] = False
    DEFAULT_NPARTITIONS = max(4, int(num_cpus))


Engine.subscribe(_update_engine)

from .. import __version__
from .dataframe import DataFrame
from .io import (
    read_csv,
    read_parquet,
    read_json,
    read_html,
    read_clipboard,
    read_excel,
    read_hdf,
    read_feather,
    read_stata,
    read_sas,
    read_pickle,
    read_sql,
    read_gbq,
    read_table,
    read_fwf,
    read_sql_table,
    read_sql_query,
    read_spss,
    ExcelFile,
    to_pickle,
    HDFStore,
    json_normalize,
    read_orc,
)
from .series import Series
from .general import (
    concat,
    isna,
    isnull,
    merge,
    merge_asof,
    merge_ordered,
    pivot_table,
    notnull,
    notna,
    pivot,
    to_numeric,
    to_datetime,
    unique,
    value_counts,
    get_dummies,
    melt,
    crosstab,
    lreshape,
    wide_to_long,
)
from .plotting import Plotting as plotting

__all__ = [
    "DataFrame",
    "Series",
    "read_csv",
    "read_parquet",
    "read_json",
    "read_html",
    "read_clipboard",
    "read_excel",
    "read_hdf",
    "read_feather",
    "read_stata",
    "read_sas",
    "read_pickle",
    "read_sql",
    "read_gbq",
    "read_table",
    "read_spss",
    "read_orc",
    "json_normalize",
    "concat",
    "eval",
    "cut",
    "factorize",
    "test",
    "qcut",
    "to_datetime",
    "get_dummies",
    "isna",
    "isnull",
    "merge",
    "pivot_table",
    "date_range",
    "Index",
    "MultiIndex",
    "Series",
    "bdate_range",
    "period_range",
    "DatetimeIndex",
    "to_timedelta",
    "set_eng_float_format",
    "options",
    "set_option",
    "CategoricalIndex",
    "Timedelta",
    "Timestamp",
    "NaT",
    "PeriodIndex",
    "Categorical",
    "__version__",
    "melt",
    "crosstab",
    "plotting",
    "Interval",
    "UInt8Dtype",
    "UInt16Dtype",
    "UInt32Dtype",
    "UInt64Dtype",
    "SparseDtype",
    "Int8Dtype",
    "Int16Dtype",
    "Int32Dtype",
    "Int64Dtype",
    "CategoricalDtype",
    "DatetimeTZDtype",
    "IntervalDtype",
    "PeriodDtype",
    "BooleanDtype",
    "StringDtype",
    "NA",
    "RangeIndex",
    "Int64Index",
    "UInt64Index",
    "Float64Index",
    "TimedeltaIndex",
    "IntervalIndex",
    "IndexSlice",
    "Grouper",
    "array",
    "Period",
    "show_versions",
    "DateOffset",
    "timedelta_range",
    "infer_freq",
    "interval_range",
    "ExcelWriter",
    "read_fwf",
    "read_sql_table",
    "read_sql_query",
    "ExcelFile",
    "to_pickle",
    "HDFStore",
    "lreshape",
    "wide_to_long",
    "merge_asof",
    "merge_ordered",
    "notnull",
    "notna",
    "pivot",
    "to_numeric",
    "unique",
    "value_counts",
    "datetime",
    "NamedAgg",
    "DEFAULT_NPARTITIONS",
]

del my_happy_pandas, Engine, Parameter
