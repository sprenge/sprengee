# -*- coding: utf-8 -*-

from unittest import TestCase
from monolithe.lib import SDKUtils


class GetPythonNameTest(TestCase):
    """ Test for get_python_name function

    """
    def assertPythonNameEquals(self, rest_name, python_name):
        """ Check that the remote name is well converted to
            the python name

        """
        self.assertEqual(SDKUtils.get_idiomatic_name_in_language(rest_name, 'python'), python_name)

    def test_get_python_name(self):
        """ Convert REST names to Python

        """
        self.assertPythonNameEquals('enterpriseID', 'enterprise_id')
        self.assertPythonNameEquals('permittedEntityType', 'permitted_entity_type')
        self.assertPythonNameEquals('L2Domain', 'l2_domain')
        self.assertPythonNameEquals('L2DomainTemplate', 'l2_domain_template')
        self.assertPythonNameEquals('UUID', 'uuid')
        self.assertPythonNameEquals('VM', 'vm')
        self.assertPythonNameEquals('VMs', 'vms')
        self.assertPythonNameEquals('VPort', 'vport')
        self.assertPythonNameEquals('VPortTag', 'vport_tag')
        self.assertPythonNameEquals('PATEnabled', 'pat_enabled')
        self.assertPythonNameEquals('DHCPServerAddress', 'dhcp_server_address')
        self.assertPythonNameEquals('VMsInterfaces', 'vms_interfaces')
        self.assertPythonNameEquals('zoneIds', 'zone_ids')
        self.assertPythonNameEquals('domainIDs', 'domain_ids')
        self.assertPythonNameEquals('VPortsTag', 'vports_tag')
        self.assertPythonNameEquals('VPortsTagOptionL2Domain', 'vports_tag_option_l2_domain')
        self.assertPythonNameEquals('IDsTORemove', 'ids_to_remove')
        self.assertPythonNameEquals('MultiNICVPortsFetcher', 'multi_nic_vports_fetcher')
        self.assertPythonNameEquals('FloatingIPID', 'floating_ip_id')
        self.assertPythonNameEquals('VCenter', 'vcenter')
        self.assertPythonNameEquals('VCenterHypervisor', 'vcenter_hypervisor')
        self.assertPythonNameEquals('VCenterEAMConfig', 'vcenter_eam_config')
        self.assertPythonNameEquals('vCenterIP', 'vcenter_ip')
        self.assertPythonNameEquals('associatedIPv6', 'associated_ipv6')
        self.assertPythonNameEquals('IPv6Address', 'ipv6_address')
        self.assertPythonNameEquals('IPv4Address', 'ipv4_address')
