*** Settings ***
Library     ../RobotLibrary.py


*** Test Cases ***
Test Input List
    Input    list
    Run Application
    Output Should Contain Atleast    List of references:

Test Input l
    Input    l
    Run Application
    Output Should Contain Atleast    List of references:

Test Input Should Not Exist
    Input    testi
    Run Application
    Output Should Contain    Tunnistamaton komento. help auttaa

Test Instance Should Contain
    [Documentation]    This is a dummy test
    Instance Should Contain    testi
