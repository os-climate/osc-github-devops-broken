# From: origin	https://gerrit.o-ran-sc.org/r/aiml-fw/athp/sdk/feature-store (fetch)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2024 The Linux Foundation <https://linuxfoundation.org>

# ==================================================================================
#
#       Copyright (c) 2022 Samsung Electronics Co., Ltd. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ==================================================================================

from setuptools import setup

setup(
    name="featurestoresdk",
    version="0.1",
    description="feature store SDK for Training Host",
    url="https://gerrit.o-ran-sc.org/r/admin/repos/aiml-fw/athp/sdk/feature-store,general",
    author="Joseph Thaliath",
    author_email="jo.thaliath@samsung.com",
    license="Apache 2.0",
    packages=["featurestoresdk"],
    zip_safe=False,
)
