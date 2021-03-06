# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from .vqe.vqe import VQE
from .qaoa.qaoa import QAOA
from .qsvm.qsvm_variational import QSVMVariational
from .vqalgorithm import VQAlgorithm

__all__ = ['VQE',
           'QAOA',
           'QSVMVariational',
           'VQAlgorithm']
