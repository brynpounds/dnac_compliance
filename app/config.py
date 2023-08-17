####################################################################################
# project: DNAC-ComplianceMon
# module: config.py
# author: kebaldwi@cisco.com
# use case: Simple Check of XML audit files against configuration
# developers:
#            Gabi Zapodeanu, TME, Enterprise Networks, Cisco Systems
#            Keith Baldwin, TSA, EN Architectures, Cisco Systems
####################################################################################

# This file contains the:
# DNAC username and password, server info and file locations

# Update this section with the DNA Center server info and user information
DNAC_URL = 'https://10.18.180.6'
DNAC_USER = 'admin'
DNAC_PASS = 'C1sc012345'

# File location to be used for configurations
CONFIG_PATH = f"."
CONFIG_STORE = f"DNAC-CompMon-Data"
COMPLIANCE_STORE = f"PrimeComplianceChecks"