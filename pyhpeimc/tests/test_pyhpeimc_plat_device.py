from unittest import TestCase
from nose.plugins.skip import Skip, SkipTest
from pyhpeimc.tests.test_machine import *
from pyhpeimc.plat.device import *


class TestGet_all_devs(TestCase):
    def test_get_all_devs_type(self):
        dev_list = get_all_devs(auth.creds, auth.url)
        self.assertIs(type(dev_list), list)


    def test_get_all_devs_network_address_filter_type(self):
        dev_list = get_all_devs(auth.creds, auth.url, network_address='10.11.')
        self.assertIs(type(dev_list), list)

    def test_get_all_devs_content(self):
        dev_list = get_all_devs(auth.creds, auth.url, network_address='10.11.')
        self.assertIs(len(dev_list[0]), 23)
        self.assertIn('typeName', dev_list[0])
        self.assertIn('sysOid', dev_list[0])
        self.assertIn('mask', dev_list[0])
        self.assertIn('symbolId', dev_list[0])
        self.assertIn('symbolName', dev_list[0])
        self.assertIn('ip', dev_list[0])
        self.assertIn('symbolLevel', dev_list[0])
        self.assertIn('symbolType', dev_list[0])
        self.assertIn('link', dev_list[0])
        self.assertIn('symbolDesc', dev_list[0])
        self.assertIn('contact', dev_list[0])
        self.assertIn('parentId', dev_list[0])
        self.assertIn('status', dev_list[0])
        self.assertIn('devCategoryImgSrc', dev_list[0])
        self.assertIn('label', dev_list[0])
        self.assertIn('categoryId', dev_list[0])
        self.assertIn('sysName', dev_list[0])
        self.assertIn('sysDescription', dev_list[0])
        self.assertIn('location', dev_list[0])
        self.assertIn('topoIconName', dev_list[0])
        self.assertIn('statusDesc', dev_list[0])
        self.assertIn('id', dev_list[0])
        self.assertIn('mac', dev_list[0])

#####Test Get_Dev_Details for Multiple Vendor Devices

###Switches

#CW3 Switch
class TestGet_dev_details_CW3_Switch(TestCase):
    def test_get_dev_details_type(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW3_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW3_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


#CW5 Switch
class TestGet_dev_details_CW5_Switch(TestCase):
    def test_get_dev_details_type(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)

#CW7 Switch
class TestGet_dev_details_CW7_Switch(TestCase):
    def test_get_dev_details_type(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW7_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW7_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)

#Cisco Switch
class TestGet_dev_details_Cisco_Switch(TestCase):
    def test_get_dev_details_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Cisco_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Cisco_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)

#Arista Switch
class TestGet_dev_details_Arista_Switch(TestCase):
    def test_get_dev_details_type(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Arista_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Arista_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)

#Juniper Switch
class TestGet_dev_details_Juniper_Switch(TestCase):
    def test_get_dev_details_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Juniper_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Juniper_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)

#ArubaOS Switch ( Previously Provision)
class TestGet_dev_details_ArubaOS_Switch(TestCase):
    def test_get_dev_details_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(ArubaOS_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(ArubaOS_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


###Routers

#Cisco Router
class TestGet_dev_details_Cisco_Router(TestCase):
    def test_get_dev_details_type(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(Cisco_Router, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(Cisco_Router, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)

#CW5 Router
class TestGet_dev_details_CW5_Router(TestCase):
    def test_get_dev_details_type(self):
        if CW5_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Router, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if CW5_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Router, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)

#Juniper Router ( SRX )
class TestGet_dev_details_Juniper_Router(TestCase):
    def test_get_dev_details_type(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Router, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(Juniper_Router, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


#Servers

#Windows Server
class TestGet_dev_details_Windows_Server(TestCase):
    def test_get_dev_details_type(self):
        if Windows_Server is None:
            raise SkipTest
        dev_1 = get_dev_details(Windows_Server, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Windows_Server is None:
            raise SkipTest
        dev_1 = get_dev_details(Windows_Server, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)

#Linux Server
class TestGet_dev_details_Linux_Server(TestCase):
    def test_get_dev_details_type(self):
        if Linux_Server is None:
            raise SkipTest
        dev_1 = get_dev_details(Linux_Server, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Linux_Server is None:
            raise SkipTest
        dev_1 = get_dev_details(Linux_Server, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


#Hypervisors

#VMWare ESX Hypervisor
class TestGet_dev_details_ESX(TestCase):
    def test_get_dev_details_type(self):
        if ESX is None:
            raise SkipTest
        dev_1 = get_dev_details(ESX, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if ESX is None:
            raise SkipTest
        dev_1 = get_dev_details(ESX, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


#Microsoft HyperV Hypervisor
class TestGet_dev_details_HyperV(TestCase):
    def test_get_dev_details_type(self):
        if HyperV is None:
            raise SkipTest
        dev_1 = get_dev_details(HyperV, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if HyperV is None:
            raise SkipTest
        dev_1 = get_dev_details(HyperV, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


"""============================================================================================="""

######Test TestGet_dev_interface for Multiple Vendor Devices

### Switches


#CW3 Switch
class TestGet_dev_interface_CW3_Switch(TestCase):
    def test_get_dev_interface_type(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip = CW3_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


#CW5 Switch
class TestGet_dev_interface_CW5_Switch(TestCase):
    def test_get_dev_interface_type(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


#CW7 Switch
class TestGet_dev_interface_CW7_Switch(TestCase):
    def test_get_dev_interface_type(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


#Cisco Switch
class TestGet_dev_interface_Cisco_Switch(TestCase):
    def test_get_dev_interface_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


#Juniper Switch
class TestGet_dev_interface_Juniper_Switch(TestCase):
    def test_get_dev_interface_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


#Arista Switch
class TestGet_dev_interface_Arista_Switch(TestCase):
    def test_get_dev_interface_type(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


#ArubaOS Switch ( Formerly Provision )
class TestGet_dev_interface_ArubaOS_Switch(TestCase):
    def test_get_dev_interface_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


### Routers


#Cisco Router
class TestGet_dev_interface_Cisco_Router(TestCase):
    def test_get_dev_interface_type(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


#CW5 Router
class TestGet_dev_interface_CW5_Router(TestCase):
    def test_get_dev_interface_type(self):
        if CW5_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if CW5_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


#Juniper Router ( SRX )
class TestGet_dev_interface_Juniper_Router(TestCase):
    def test_get_dev_interface_type(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


### Servers

# Windows_Server
class TestGet_dev_interface_Windows_Server(TestCase):
    def test_get_dev_interface_type(self):
        if Windows_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Windows_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# Linux_Server
class TestGet_dev_interface_Linux_Server(TestCase):
    def test_get_dev_interface_type(self):
        if Linux_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Linux_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


### Hypervisors


#VMWare ESX Hypervisor
class TestGet_dev_interface_ESX_Server(TestCase):
    def test_get_dev_interface_type(self):
        if ESX is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if ESX is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# HyperV
class TestGet_dev_interface_HyperV_Server(TestCase):
    def test_get_dev_interface_type(self):
        if HyperV is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if HyperV is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


"""============================================================================================="""

#####Test TestGet_dev_run_config for Multiple Vendor Devices

###Switches

#CW3 Switch
class TestGet_dev_run_configCW3_Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if CW3_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(run_config), str)


#CW5_Switch
class TestGet_dev_run_configCW5_Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if CW5_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(run_config), str)


#CW7_Switch
class TestGet_dev_run_configCW7_Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if CW7_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(run_config), str)


#Cisco_Switch
class TestGet_dev_run_configCisco_Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if Cisco_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(run_config), str)


#Juniper_Switch
class TestGet_dev_run_configJuniper_Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if Juniper_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(run_config), str)


#Arista_Switch
class TestGet_dev_run_configArista_Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if Arista_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(run_config), str)

    def test_get_dev_run_config_unsupported(self):
        if Arista_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Arista_Switch)
        self.assertEqual(run_config,"This features is no supported on this device")


#ArubaOS_Switch (Formerly Provision)
class TestGet_dev_run_configArubaOS_Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(run_config), str)


###Routers

#Cisco_Router
class TestGet_dev_run_configCisco_Router(TestCase):
    def test_get_dev_run_config_supported(self):
        if Cisco_Router is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(run_config), str)


#CW5_Router
class TestGet_dev_run_configCW5_Router(TestCase):
    def test_get_dev_run_config_supported(self):
        if CW5_Router is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(run_config), str)


#Juniper_Router (SRV)
class TestGet_dev_run_configJuniper_Router(TestCase):
    def test_get_dev_run_config_supported(self):
        if Juniper_Router is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(run_config), str)


####Servers


#Windows_Server
class TestGet_dev_run_configWindows_Server(TestCase):
    def test_get_dev_run_config_unsupported(self):
        if Windows_Server is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Windows_Server)
        self.assertEqual(run_config,"This features is no supported on this device")

#Linux_Server
class TestGet_dev_run_configLinux_Server(TestCase):
    def test_get_dev_run_config_unsupported(self):
        if Linux_Server is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Linux_Server)
        self.assertEqual(run_config,"This features is no supported on this device")

###Hypervisors


#VMWare ESX
class TestGet_dev_run_configVMWare(TestCase):
    def test_get_dev_run_config_unsupported(self):
        if ESX is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=ESX)
        self.assertEqual(run_config,"This features is no supported on this device")


#HyperV
class TestGet_dev_run_configHyperV(TestCase):
    def test_get_dev_run_config_unsupported(self):
        if HyperV is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=HyperV)
        self.assertEqual(run_config,"This features is no supported on this device")



#Test TestGet_dev_start_config for Multiple Vendor Devices

"""============================================================================================="""

#####Test TEST_NAME_HERE for Multiple Vendor Devices

###Switches

#CW3_Switch
class TestGet_dev_start_configCW3_Switch(TestCase):
    def test_get_dev_run_start_supported(self):
        if CW3_Switch is None:
            raise SkipTest
            start_config = get_dev_start_config(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(start_config), str)


#CW5_Switch
class TestGet_dev_start_configCW5_Switch(TestCase):
    def test_get_dev__start_supported(self):
        if CW5_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(start_config), str)


#CW7_Switch
class TestGet_dev_start_configCW7_Switch(TestCase):
    def test_get_dev_start_supported(self):
        if CW7_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(start_config), str)


#Cisco_Switch
class TestGet_dev_start_configCisco_Switch(TestCase):
    def test_get_dev_start_supported(self):
        if Cisco_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(start_config), str)


#Juniper_Switch
class TestGet_dev_start_configJuniper_Switch(TestCase):
    def test_get_dev_start_supported(self):
        if Juniper_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(start_config), str)


#Arista_Switch
class TestGet_dev_start_configArista_Switch(TestCase):
    def test_get_dev_start_supported(self):
        if Arista_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(start_config), str)


#ArubaOS_Switch (Formerly Provision)
class TestGet_dev_start_configArubaOS_Switch(TestCase):
    def test_get_dev_start_supported(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(start_config), str)


###Routers

#Cisco_Router
class TestGet_dev_start_configCisco_Router(TestCase):
    def test_get_dev_start_supported(self):
        if Cisco_Router is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(start_config), str)

#CW5_Router
class TestGet_dev_start_configCW5_Router(TestCase):
    def test_get_dev_start_supported(self):
        if CW5_Router is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(start_config), str)

#Juniper_Router (SRV)
class TestGet_dev_start_configJuniper_Router(TestCase):
    def test_get_dev_start_supported(self):
        if Juniper_Router is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(start_config), str)

####Servers


#Windows_Server
class TestGet_dev_start_configWindows_Server(TestCase):
    def test_get_dev_run_start_unsupported(self):
        if Windows_Server is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Windows_Server)
        self.assertEqual(run_config,"This features is no supported on this device")


#Linux_Server
class TestGet_dev_start_configLinux_Server(TestCase):
    def test_get_dev_run_start_unsupported(self):
        if Linux_Server is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Linux_Server)
        self.assertEqual(run_config,"This features is no supported on this device")


###Hypervisors


#VMWare ESX
class TestGet_dev_start_configVMWare(TestCase):
    def test_get_dev_run_start_unsupported(self):
        if ESX is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=VMWare)
        self.assertEqual(run_config,"This features is no supported on this device")

#HyperV
class TestGet_dev_start_configHyperV(TestCase):
    def test_get_dev_run_start_unsupported(self):
        if HyperV is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=HyperV)
        self.assertEqual(run_config,"This features is no supported on this device")


#Test TestGet_dev_mac_learn for Multiple Vendor Devices


"""============================================================================================="""

#####Test TestGet_dev_mac_learn for Multiple Vendor Devices

###Switches

#CW3_Switch
class TestGet_dev_mac_learnCW3_Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

#CW5_Switch
class TestGet_dev_mac_learnCW5_Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


#CW7_Switch
class TestGet_dev_mac_learnCW7_Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

#Cisco_Switch
class TestGet_dev_mac_learnCisco_Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(dev_mac_learn), 10)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

#Juniper_Switch
class TestGet_dev_mac_learnJuniper_Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

#Arista_Switch
class TestGet_dev_mac_learnArista_Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

#ArubaOS_Switch (Formerly Provision)
class TestGet_dev_mac_learnArubaOS_Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])
###Routers

#Cisco_Router
class TestGet_dev_mac_learnCisco_Router(TestCase):
    def test_get_dev_mac_learnType(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

#CW5_Router
class TestGet_dev_mac_learnCW5_Router(TestCase):
    def test_get_dev_mac_learnType(self):
        if CW5_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if CW5_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

#Juniper_Router (SRV)
class TestGet_dev_mac_learnJuniper_Router(TestCase):
    def test_get_dev_mac_learnType(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

####Servers


#Windows_Server
class TestGet_dev_mac_learnWindows_Server(TestCase):
    def test_get_dev_mac_learnType(self):
        if Windows_Server is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Windows_Server is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

#Linux_Server
class TestGet_dev_mac_learnLinux_Server(TestCase):
    def test_get_dev_mac_learnType(self):
        if Linux_Server is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Linux_Server is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


###Hypervisors


#VMWare ESX
class TestGet_dev_mac_learnESX(TestCase):
    def test_get_dev_mac_learnType(self):
        if ESX is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if ESX is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])

#HyperV

class TestGet_dev_mac_learnHyperV(TestCase):
    def test_get_dev_mac_learnType(self):
        if HyperV is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if HyperV is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])




"""============================================================================================="""

#####Test TestRun_dev_cmd for Multiple Vendor Devices

###Switches

# CW3_Switch
class TestRun_dev_cmd_CW3_Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if CW3_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if CW3_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)

# CW5_Switch
class TestRun_dev_cmd_CW5_Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if CW5_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if CW5_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)

# CW7_Switch
class TestRun_dev_cmd_CW7_Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if CW7_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if CW7_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# Cisco_Switch
class TestRun_dev_cmd_Cisco_Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)

# Juniper_Switch
class TestRun_dev_cmd_Juniper_Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)

# Arista_Switch
class TestRun_dev_cmd_Arista_Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if Arista_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Arista_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)

# ArubaOS_Switch (Formerly Provision)
class TestRun_dev_cmd_ArubaOS_Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
###Routers

# Cisco_Router
class TestRun_dev_cmd_Cisco_Router(TestCase):
    def test_run_dev_cmd_type(self):
        if Cisco_Router is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Cisco_Router is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# CW5_Router
class TestRun_dev_cmd_CW5_Router(TestCase):
    def test_run_dev_cmd_type(self):
        if CW5_Router is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if CW5_Router is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# Juniper_Router (SRX)
class TestRun_dev_cmd_Juniper_Router(TestCase):
    def test_run_dev_cmd_type(self):
        if Juniper_Router is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Juniper_Router is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
####Servers


# Windows_Server
class TestRun_dev_cmd_Windows_Server(TestCase):
    def test_run_dev_cmd_type(self):
        if Windows_Server is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Windows_Server is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(cmd_output), 5)
        self.assertIn('success', cmd_output)
        self.assertIn('errorCode', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
        self.assertIn('errorMsg', cmd_output)

# Linux_Server
class TestRun_dev_cmd_Linux_Server(TestCase):
    def test_run_dev_cmd_type(self):
        if Linux_Server is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Linux_Server is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(cmd_output), 5)
        self.assertIn('success', cmd_output)
        self.assertIn('errorCode', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
        self.assertIn('errorMsg', cmd_output)

###Hypervisors


# VMWare ESX
class TestRun_dev_cmd_ESX(TestCase):
    def test_run_dev_cmd_type(self):
        if ESX is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=ESX)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if ESX is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=ESX)
        self.assertIs(len(cmd_output), 5)
        self.assertIn('success', cmd_output)
        self.assertIn('errorCode', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
        self.assertIn('errorMsg', cmd_output)


# HyperV
class TestRun_dev_cmd_VMWare(TestCase):
    def test_run_dev_cmd_type(self):
        if HyperV is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if HyperV is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(cmd_output), 5)
        self.assertIn('success', cmd_output)
        self.assertIn('errorCode', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
        self.assertIn('errorMsg', cmd_output)




"""============================================================================================="""

######Test TestGet_all_interface_details for Multiple Vendor Devices

###Switches

#CW3_Switch
class TestGet_all_interface_details_CW3_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if CW3_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if CW3_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])

#CW5_Switch
class TestGet_all_interface_details_CW5_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if CW5_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if CW5_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])

#CW7_Switch
class TestGet_all_interface_details_CW7_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if CW7_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if CW7_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


#Cisco_Switch
class TestGet_all_interface_details_Cisco_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


#Juniper_Switch
class TestGet_all_interface_details_Juniper_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


#Arista_Switch
class TestGet_all_interface_details_Arista_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if Arista_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Arista_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


#ArubaOS_Switch (Formerly Provision)
class TestGet_all_interface_details_ArubaOS_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


###Routers

#Cisco_Router
class TestGet_all_interface_details_Cisco_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if Cisco_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


#CW5_Router
class TestGet_all_interface_details_CW5_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if CW5_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if CW5_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


#Juniper_Router (SRV)
class TestGet_all_interface_details_Juniper_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if Juniper_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Juniper_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


####Servers


#Windows_Server
class TestGet_all_interface_details_Windows_Server(TestCase):
    def test_get_all_interface_details_type(self):
        if Windows_Server is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


#Linux_Server
class TestGet_all_interface_details_Linux_Server(TestCase):
    def test_get_all_interface_details_type(self):
        if Linux_Server is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Linux_Server is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])

###Hypervisors


#VMWare ESX
class TestGet_all_interface_details_VMWare(TestCase):
    def test_get_all_interface_details_type(self):
        if ESX is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if ESX is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


#HyperV
class TestGet_all_interface_details_HyperV(TestCase):
    def test_get_all_interface_details_type(self):
        if HyperV is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if HyperV is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


#TODO
"""============================================================================================="""

######Test TestGet_interface_details for Multiple Vendor Devices


###Switches

#CW3_Switch
class TestGet_interface_details_CW3_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if CW3_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if CW3_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)






#CW5_Switch
class TestGet_interface_details_CW5_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if CW5_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if CW5_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)



#CW7_Switch
class TestGet_interface_details_CW7_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if CW7_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if CW7_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)



#Cisco_Switch
class TestGet_interface_details_Cisco_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)



#Juniper_Switch
class TestGet_interface_details_Juniper_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)



#Arista_Switch
class TestGet_interface_details_Arista_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if Arista_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Arista_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)



#ArubaOS_Switch (Formerly Provision)
class TestGet_interface_details_ArubaOS_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)




###Routers

#Cisco_Router
class TestGet_interface_details_Cisco_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if Cisco_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Cisco_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)



#CW5_Router
class TestGet_interface_details_CW5_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if CW5_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if CW5_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)



#Juniper_Router (SRV)
class TestGet_interface_details_Juniper_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if Juniper_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Juniper_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


####Servers


#Windows_Server
class TestGet_interface_details_Windows_Server(TestCase):
    def test_get_all_interface_details_type(self):
        if Windows_Server is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Windows_Server is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)



#Linux_Server
class TestGet_interface_details_Linux_Server(TestCase):
    def test_get_all_interface_details_type(self):
        if Linux_Server is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Linux_Server is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


###Hypervisors


#ESX
class TestGet_interface_details_ESX(TestCase):
    def test_get_all_interface_details_type(self):
        if ESX is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=ESX)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if ESX is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=ESX)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


#HyperV
class TestGet_interface_details_HyperV(TestCase):
    def test_get_all_interface_details_type(self):
        if HyperV is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if HyperV is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


"""============================================================================================="""

######Test TestSet_inteface_up for Multiple Vendor Devices


###Switches

#CW3_Switch
class TestSet_inteface_up_CW3_Switch(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if CW3_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=CW3_Switch)
        int_up_response = set_inteface_up('1', auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)

#CW5_Switch
class TestSet_inteface_up_CW5_Switch(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if CW5_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=CW5_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


#CW7_Switch
class TestSet_inteface_up_CW7_Switch(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if CW7_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=CW7_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


#Cisco_Switch
class TestSet_inteface_up_Cisco_Switch(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if Cisco_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Cisco_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


#Juniper_Switch
class TestSet_inteface_up_Juniper_Switch(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if Juniper_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Juniper_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


#Arista_Switch
class TestSet_inteface_up_Arista_Switch(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if Arista_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Arista_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


#ArubaOS_Switch (Formerly Provision)
class TestSet_inteface_up_ArubaOS_Switch(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if ArubaOS_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)

###Routers

#Cisco_Router

# Ensure that the ifIndex for this test is the far interface of the router away from IMC or you will kill access to the machine
#which will force manual intervention
class TestSet_inteface_up_Cisco_Router(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if Cisco_Router is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Cisco_Router)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


#CW5_Router
# Ensure that the ifIndex for this test is the far interface of the router away from IMC or you will kill access to the machine
#which will force manual intervention
class TestSet_inteface_up_CW5_Router(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if CW5_Router is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=CW5_Router)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)

#Juniper_Router (SRV)
# Ensure that the ifIndex for this test is the far interface of the router away from IMC or you will kill access to the machine
#which will force manual intervention
class TestSet_inteface_up_Juniper_Router(TestCase):
    def test_set_inteface_up(self):
        if set_interface_up is False:
            raise SkipTest
        if Juniper_Router is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Juniper_Router)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)
####Servers


#Windows_Server
#Deemed inappropriate to test

#Linux_Server
#Deemed inappropriate to test

###Hypervisors


#ESX
#Deemed inappropriate to test

#HyperV
#Deemed inappropriate to test


"""============================================================================================="""

######Test TestSet_inteface_down for Multiple Vendor Devices

###Switches

#CW3_Switch
class TestSet_inteface_down_CW3_Switch(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if CW3_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=CW3_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=CW3_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)

#CW5_Switch
class TestSet_inteface_down_CW5_Switch(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if CW5_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=CW5_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=CW5_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


#CW7_Switch
class TestSet_inteface_down_CW7_Switch(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if CW7_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=CW7_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=CW7_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


#Cisco_Switch
class TestSet_inteface_down_Cisco_Switch(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if Cisco_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Cisco_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)

#Juniper_Switch
class TestSet_inteface_down_Juniper_Switch(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if Juniper_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Juniper_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)

#Arista_Switch
class TestSet_inteface_down_Arista_Switch(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if Arista_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Arista_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Arista_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


#ArubaOS_Switch (Formerly Provision)
class TestSet_inteface_down_ArubaOS_Switch(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if ArubaOS_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)




###Routers

#Cisco_Router
# Ensure that the ifIndex for this test is the far interface of the router away from IMC or you will kill access to the machine
#which will force manual intervention
class TestSet_inteface_down_Cisco_Router(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if Cisco_Router is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Router)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Cisco_Router)
        set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)

#CW5_Router
# Ensure that the ifIndex for this test is the far interface of the router away from IMC or you will kill access to the machine
#which will force manual intervention
class TestSet_inteface_down_CW5_Router(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if CW5_Router is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=CW5_Router)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=CW5_Router)
        set_inteface_up('9', auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)

#Juniper_Router (SRV)
# Ensure that the ifIndex for this test is the far interface of the router away from IMC or you will kill access to the machine
#which will force manual intervention
class TestSet_inteface_down_Juniper_Router(TestCase):
    def test_set_inteface_down(self):
        if set_interface_down is False:
            raise SkipTest
        if Juniper_Router is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Router)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Juniper_Router)
        set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)

####Servers


#Windows_Server
#Deemed inappropriate to test

#Linux_Server
#Deemed inappropriate to test
###Hypervisors


#ESX
#Deemed inappropriate to test

#HyperV
#Deemed inappropriate to test