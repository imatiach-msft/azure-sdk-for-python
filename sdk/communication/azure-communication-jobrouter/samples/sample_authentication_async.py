# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_authentication_async.py
DESCRIPTION:
    These samples demonstrates how to create a Router client.
    You need a valid connection string to an Azure Communication Service to execute the sample

USAGE:
    python sample_authentication_async.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_COMMUNICATION_SERVICE_ENDPOINT - Communication Service endpoint url
"""

import os
import asyncio


class RouterClientAuthenticationSamplesAsync(object):
    endpoint = os.environ["AZURE_COMMUNICATION_SERVICE_ENDPOINT"]

    async def create_router_client(self):
        connection_string = self.endpoint

        # [START auth_from_connection_string_async]
        from azure.communication.jobrouter.aio import JobRouterClient

        # set `connection_string` to an existing ACS endpoint
        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)
        print("JobRouterClient created successfully!")

        # [END auth_from_connection_string_async]

    async def create_router_admin_client(self):
        connection_string = self.endpoint

        # [START admin_auth_from_connection_string_async]
        from azure.communication.jobrouter.aio import JobRouterAdministrationClient

        # set `connection_string` to an existing ACS endpoint
        router_client = JobRouterAdministrationClient.from_connection_string(conn_str=connection_string)
        print("JobRouterAdministrationClient created successfully!")

        # [END admin_auth_from_connection_string_async]


async def main():
    sample = RouterClientAuthenticationSamplesAsync()
    await sample.create_router_client()
    await sample.create_router_admin_client()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
