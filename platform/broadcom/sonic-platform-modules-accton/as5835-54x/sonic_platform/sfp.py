#!/usr/bin/env python

try:
    import natsort
    from sonic_platform_pddf_base.pddf_sfp import PddfSfp
    from sonic_platform_base.sonic_sfp.sfputilhelper import SfpUtilHelper
    from sonic_py_common import device_info
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")


class Sfp(PddfSfp):
    """
    PDDF Platform-Specific Sfp class
    """

    def __init__(self, index, pddf_data=None, pddf_plugin_data=None):
        PddfSfp.__init__(self, index, pddf_data, pddf_plugin_data)
        self.index = index + 1

    # Provide the functions/variables below for which implementation is to be overwritten
    def __get_path_to_port_config_file(self):
        platform, hwsku = device_info.get_platform_and_hwsku()
        hwsku_path = "/".join(["/usr/share/sonic/platform",hwsku])
        return "/".join([hwsku_path, "port_config.ini"])

    def get_name(self):
        """
        Retrieves the name of the device
            Returns:
            string: The name of the device
        """                
        sfputil_helper = SfpUtilHelper()
        sfputil_helper.read_porttab_mappings(
            self.__get_path_to_port_config_file())

        logical_port_list = sfputil_helper.logical
        logical_port_list = natsort.natsorted(logical_port_list)
        name = logical_port_list[self.port_index-1] or "Unknown"

        return name

    def get_position_in_parent(self):
        """Retrieves 1-based relative physical position in parent device."""
        return self.port_index

    def get_error_description(self):
        """
        Retrives the error descriptions of the SFP module

        Returns:
            String that represents the current error descriptions of vendor specific errors
            In case there are multiple errors, they should be joined by '|',
            like: "Bad EEPROM|Unsupported cable"
        """
        raise NotImplementedError

