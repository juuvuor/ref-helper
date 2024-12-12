*** Settings ***
Resource        resource.robot

Test Setup      Populate Data


*** Test Cases ***
Test Input edit
    Input    edit edittausta
    Input field_1    book
    Input field    sivu    30
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Päivitetty lähde edittausta, book, {'sivu': '30'}.

Test Editing needs actual ID to edit
    Input    edit 23
    Input field_1    book
    Input field    sivu    30
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Lähdeavainta "23" ei löydetty!

Test Edit With Invalid Field
    Input    edit edittaust
    Input field_1    book
    Input field    sivu    30
    Input field    ${EMPTY}    ${EMPTY}
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Lähdeavainta "edittaust" ei löydetty!

Test Edit With Empty ID
    Input    edit
    Input field_1    book
    Input field    sivu    30
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    error: the following arguments are required: key_to_edit
