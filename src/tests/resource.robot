*** Settings ***
Library     ../RobotLibrary.py


*** Keywords ***
Input reference
    [Arguments]    ${id}    ${type}
    Input    ${id}
    Input    ${type}

Input field
    [Arguments]    ${field}    ${value}
    Input    ${field}
    Input    ${value}

Input field_1
    [Arguments]    ${value}
    Input    ${value}
