*** Settings ***
Resource    resource.robot


*** Test Cases ***
Test Input List
    Populate Data
    Input    list
    Input    exit
    Run Application
    # stub_bibtex_manager.py : create_data VPL11
    Output Should Contain    VPL11

Test Input Should Not Exist
    Input    testi
    Input    exit
    Run Application
    Output Should Contain    Unrecognized command.

Test Instance Should Contain
    [Documentation]    This is a dummy test
    Instance Should Contain    testi
Test List filter With Specific type
    [Documentation]    Testaa list-komennon toiminnallisuus tietyn tyypin perusteella.
    Populate Data    # Lisää tarvittavat argumentit
    Input field_1   list -t book
    Input    exit
    Run Application
    Output Should Contain    book

Test List filter With Specific Year
    [Documentation]    Testaa list-komennon toiminnallisuus tietyn vuoden perusteella.
    Populate Data    # Lisää tarvittavat argumentit
    Input    l -f year 2011
    Input    exit
    Run Application
    Output Should Contain  2011

 Test List filter With Multiple Filters
    [Documentation]    Testaa list-komennon toiminnallisuus useiden suodattimien perusteella.
    Populate Data    # Lisää tarvittavat argumentit
    Input    list -t book -f year 2008
    Input    exit
    Run Application
    Output Should Contain    book
    Output Should Contain    2008   