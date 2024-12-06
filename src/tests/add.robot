*** Settings ***
Library     ../RobotLibrary.py
Resource    resource.robot


*** Test Cases ***
Test Input Add One
    Input reference    testi    testi    testi    testi
    Input  ${EMPTY}
    Input  exit
    Run Application
    Output Should Contain    Lisätty lähde testi, testi, {'testi': 'testi'}

Test Input Add Many Fields
    Input    Add
    Input    id
    Input    name
    Input type    kentan koko    suuri
    Input type    kentta    Jalkapallokentta
    Run Application
    Output Should Contain    Lisätty lähde id, name, kentan koko, suuri, kentta, Jalkapallokentta
