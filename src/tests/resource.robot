*** Settings ***
Library  ../RobotLibrary.py

#*** Keywords ***
# Esimerkkejä
#Input Login Command
#    Input  login

#Input Credentials
#    [Arguments]  ${username}  ${password}
#    Input  ${username}
#    Input  ${password}
#    Run Application

*** Test Cases ***
Test Ci Pipeline
    Instance Should Contain  testi
