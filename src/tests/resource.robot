*** Settings ***
Library     ../RobotLibrary.py


*** Keywords ***
Input reference
    [Arguments]    ${id}    ${name}    ${type}    ${value}
    Input    add
    Input    ${id}
    Input    ${name}
    Input    ${type}
    Input    ${value}

Input type
    [Arguments]    ${type}    ${value}
    Input    ${type}
    Input    ${value}
