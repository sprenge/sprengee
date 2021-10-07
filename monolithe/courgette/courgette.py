# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from builtins import object

from monolithe.courgette.lib import CourgetteTestsRunner
from .result import CourgetteResult


class Courgette(object):
    """ Validates API by launching specification-generated tests

    """
    def __init__(self, url, username, password, enterprise, apiversion, sdk_identifier, monolithe_config):
        """ Initializes Courgette

            Args:
                url (string): the url of the server with its port
                username (string): the username to launch tests
                password (string): the password to connect to the server
                enterprise (string): the name of the enterprise to connect to the server
                apiversion (float): the version of the API to connect
                sdk (string): the full name of the SDK to use
        """
        self.url = url
        self.username = username
        self.password = password
        self.enterprise = enterprise
        self.apiversion = apiversion
        self.monolithe_config = monolithe_config
        self.sdk_identifier = sdk_identifier

    def run(self, configurations):
        """ Run all tests

            Returns:
                A dictionnary containing tests results.

        """
        result = CourgetteResult()

        for configuration in configurations:

            runner = CourgetteTestsRunner(url=self.url,
                                          username=self.username,
                                          password=self.password,
                                          enterprise=self.enterprise,
                                          version=self.apiversion,
                                          specification=configuration.specification,
                                          sdk_identifier=self.sdk_identifier,
                                          monolithe_config=self.monolithe_config,
                                          parent_resource=configuration.parent_resource_name,
                                          parent_id=configuration.parent_id,
                                          default_values=configuration.default_values)

            result.add_report(configuration.specification.rest_name + ".spec", runner.run())

        return result
