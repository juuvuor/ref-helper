*** Settings ***
Library     ../RobotLibrary.py


*** Keywords ***
Input reference
    [Arguments]    ${id}    ${name}    ${type}    ${value}
    Input    Add
    Input    ${id}
    Input    ${name}
    Input    ${type}
    Input    ${value}
    Run Application

Input type
    [Arguments]    ${type}    ${value}
    Input    ${type}
    Input    ${value}
