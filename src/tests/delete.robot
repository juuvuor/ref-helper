*** Settings ***
Resource    resource.robot

*** Test Cases ***
Test Delete Method
    Populate Data
    Input    delete VPL11
    Input field_1    k
    Input    exit
    Run Application
    Output Should Contain   Poistettu lähde VPL11. 

Test Delete need valid id
    Populate Data
    Input    delete korok
    Input field_1    e
    Input    exit
    Run Application
    Output Should Contain   Poistoa ei suoritettu. 
