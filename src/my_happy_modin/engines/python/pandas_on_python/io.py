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

from my_happy_modin.engines.base.io import BaseIO
from my_happy_modin.backends.pandas.query_compiler import PandasQueryCompiler
from my_happy_modin.engines.python.pandas_on_python.frame.data import PandasOnPythonFrame


class PandasOnPythonIO(BaseIO):

    frame_cls = PandasOnPythonFrame
    query_compiler_cls = PandasQueryCompiler
