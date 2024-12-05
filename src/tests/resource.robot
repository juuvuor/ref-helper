*** Settings ***
Library     ../RobotLibrary.py


*** Keywords ***
Input reference
    [Arguments]    ${id}    ${name}    ${type}    ${value}
    Input    ${id}
    Input    ${name}
    Input    ${type}
    Input    ${value}
    Run Application
