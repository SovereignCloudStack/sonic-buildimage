#!/usr/bin/env python


try:
    from sonic_platform_pddf_base.pddf_thermal import PddfThermal
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")



class Thermal(PddfThermal):
    """PDDF Platform-Specific Thermal class"""

    def __init__(self, index, pddf_data=None, pddf_plugin_data=None, is_psu_thermal=False, psu_index=0):
        PddfThermal.__init__(self, index, pddf_data, pddf_plugin_data, is_psu_thermal, psu_index)
        
        self.pddf_obj = pddf_data
        self.thermal_obj_name = "TEMP{}".format(self.thermal_index)
        self.thermal_obj = self.pddf_obj.data[self.thermal_obj_name]

    # Provide the functions/variables below for which implementation is to be overwritten
    def get_name(self):
        if self.is_psu_thermal:
            return "PSU-{0} temp sensor 1".format(self.thermals_psu_index)
        else:
            if 'dev_attr' in self.thermal_obj.keys():
                if 'display_name' in self.thermal_obj['dev_attr']:
                    return str(self.thermal_obj['dev_attr']['display_name'])

            # In case of errors
            return "Temp sensor {0}".format(self.thermal_index)

    def get_status(self):
        get_temp=self.get_temperature()

        if get_temp is not None:
            return True if get_temp else False
