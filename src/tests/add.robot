*** Settings ***
Resource    resource.robot


*** Test Cases ***
Test Input Add One
    Input    add
    Input reference    testi    testi
    Input field    testi    testi
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Lisätty lähde testi, testi, {'testi': 'testi'}.

Test Input Add Existing
    Input    add
    Input reference    testi    testi
    Input field    testi    testi
    Input    ${EMPTY}
    Input    add
    Input reference    testi    testi
    Input field    testi    testi
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Lähdeavain "testi" on jo olemassa!

Test Input Add Many Fields
    Input    add
    Input reference    id    type
    Input field    kentan koko    suuri
    Input field    kentta    Jalkapallokentta
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Lisätty lähde id, type, {'kentan koko': 'suuri', 'kentta': 'Jalkapallokentta'}.

Test Input Add Many Fields With Empty
    Input    add
    Input reference    id    type
    Input field    kentan koko    suuri
    Input field    kentta    Jalkapallokentta
    Input    ${EMPTY}
    Input    add
    Input reference    id    type
    Input field    kentan koko    suuri
    Input field    kentta    Jalkapallokentta
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Lähdeavain "id" on jo olemassa!

Test Input Add Empty Reference
    Input    add
    Input reference    ${EMPTY}    ${EMPTY}
    Input field    testi    testi
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Lähteelle täytyy lisätä lähdeviitteen id!

Test Input Add Empty Field
    Input    add
    Input reference    id    type
    Input field    ${EMPTY}    ${EMPTY}
    Input    ${EMPTY}
    Input    exit
    Run Application
    Output Should Contain    Lisätty lähde id, type, {}.
