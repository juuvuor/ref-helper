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
