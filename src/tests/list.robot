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

Test Input Should Not Exist
    Input    testi
    Input    exit
    Run Application
    Output Should Contain    Unrecognized command.

Test Instance Should Contain
    [Documentation]    This is a dummy test
    Instance Should Contain    testi
