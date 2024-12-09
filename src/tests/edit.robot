*** Settings ***
Resource    resource.robot

*** Test Cases ***
Test Input edit
    Populate Data
    Input    edit edittausta    
    Input field_1    book
    Input field    sivu    30
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Päivitetty lähde edittausta, book, {'sivu': '30'}.

Editing needs actual ID to edit
    Populate Data
    Input    edit 23
    Input field_1    book
    Input field    sivu    30
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Lähdeavainta "23" ei löydetty!