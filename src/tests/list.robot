*** Settings ***
Resource    resource.robot


*** Test Cases ***
Test Input List
    Populate Data
    Input    list
    Input    exit
    Run Application
    # stub_bibtex_manager.py : create_data VPL11
    Output Should Contain    VPL11

# Käytännössä interpreterille tarkoitettu testi
#Test Input Should Not Exist
#    Input    testi
#    Run Application
#   Output Should Contain    Tunnistamaton komento. help auttaa

# Testien testi
#Test Instance Should Contain
#    [Documentation]    This is a dummy test
#    Instance Should Contain    testi
