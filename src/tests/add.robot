*** Settings ***
Resource    resource.robot
Library    ../stub_http_util.py

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

Test Fetch Bibtex Reference with Valid URL
    ${result}=    Http Get Url    http://dx.doi.org/10.1145/2380552.2380613    application/x-bibtex
    ${mime_type}    ${bibtex}=    Set Variable    ${result}
    Should Contain    ${bibtex}    @inproceedings{Luukkainen_2012

Test Fetch Bibtex Reference with Invalid URL
    Run Keyword And Expect Error    No mapping found for URL    Http Get Url    http://invalid.url/10.1145/2380552.2380613    application/x-bibtex
