# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1348?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1348
- Title: Venezuelan Adjustment Act
- Congress: 119
- Bill type: HR
- Bill number: 1348
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-05-12T08:06:25Z
- Update date including text: 2026-05-12T08:06:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1348",
    "number": "1348",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001200",
        "district": "9",
        "firstName": "Darren",
        "fullName": "Rep. Soto, Darren [D-FL-9]",
        "lastName": "Soto",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Venezuelan Adjustment Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:06:25Z",
    "updateDateIncludingText": "2026-05-12T08:06:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-13T14:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "NE"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "FL"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NY"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "PA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "FL"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-11-13",
      "state": "NY"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "FL"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "TX"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "IL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "FL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NC"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "PR"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1348ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1348\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Soto (for himself, Ms. Salazar , Ms. Wasserman Schultz , and Ms. Wilson of Florida ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the Secretary of Homeland Security to adjust the status of certain aliens who are nationals of Venezuela to that of aliens lawfully admitted for permanent residence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Venezuelan Adjustment Act .\n#### 2. Venezuelan refugee immigration fairness\n##### (a) Definitions\nIn this section:\n**(1) In general**\nExcept as otherwise specifically provided, any term used in this Act that is used in the immigration laws shall have the meaning given the term in the immigration laws.\n**(2) Immigration laws**\nThe term immigration laws has the meaning given the term in section 101(a)(17) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(17) ).\n**(3) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n##### (b) Adjustment of status\n**(1) In general**\nExcept as provided in paragraph (3), the Secretary shall adjust the status of an alien described in subsection (c) to that of an alien lawfully admitted for permanent residence if the alien\u2014\n**(A)**\napplies for adjustment not later than 3 years after the date of the enactment of this Act;\n**(B)**\nis otherwise eligible to receive an immigrant visa; and\n**(C)**\nsubject to paragraph (2), is admissible to the United States for permanent residence.\n**(2) Applicability of grounds of inadmissibility**\nIn determining the admissibility of an alien under paragraph (1)(C), the grounds of inadmissibility specified in paragraphs (4), (5), (6)(A), and (7)(A) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) shall not apply.\n**(3) Exceptions**\nAn alien shall not be eligible for adjustment of status under this subsection if the Secretary determines that the alien\u2014\n**(A)**\nhas been convicted of any aggravated felony;\n**(B)**\nhas been convicted of two or more crimes involving moral turpitude (other than a purely political offense); or\n**(C)**\nhas ordered, incited, assisted, or otherwise participated in the persecution of any person on account of race, religion, nationality, membership in a particular social group, or political opinion.\n**(4) Relationship of application to certain orders**\n**(A) In general**\nAn alien present in the United States who has been subject to an order of exclusion, deportation, removal, or voluntary departure under any provision of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) may, notwithstanding such order, submit an application for adjustment of status under this subsection if the alien is otherwise eligible for adjustment of status under paragraph (1).\n**(B) Separate motion not required**\nAn alien described in subparagraph (A) shall not be required, as a condition of submitting or granting an application under this subsection, to file a separate motion to reopen, reconsider, or vacate an order described in subparagraph (A).\n**(C) Effect of decision by secretary**\n**(i) Grant**\nIf the Secretary adjusts the status of an alien pursuant to an application under this subsection, the Secretary shall cancel any order described in subparagraph (A) to which the alien has been subject.\n**(ii) Denial**\nIf the Secretary makes a final decision to deny such application, any such order shall be effective and enforceable to the same extent that such order would be effective and enforceable if the application had not been made.\n##### (c) Aliens eligible for adjustment of status\n**(1) In general**\nThe benefits provided under subsection (b) shall apply to any alien who\u2014\n**(A)**\n**(i)**\nis a national of Venezuela;\n**(ii)**\nentered the United States before or on December 31, 2021; and\n**(iii)**\nhas been continuously physically present in the United States for not less than 1 year as of the date on which the alien submits an application under such subsection (b); or\n**(B)**\nis the spouse, child, or unmarried son or daughter of an alien described in subparagraph (A).\n**(2) Determination of continuous physical presence**\nFor purposes of establishing the period of continuous physical presence referred to in paragraph (1)(A)(ii), an alien shall not be considered to have failed to maintain continuous physical presence based on one or more absences from the United States for one or more periods amounting, in the aggregate, to not more than 180 days.\n##### (d) Stay of removal\n**(1) In general**\nThe Secretary shall promulgate regulations establishing procedures by which an alien who is subject to a final order of deportation, removal, or exclusion, may seek a stay of such order based on the filing of an application under subsection (b).\n**(2) During certain proceedings**\n**(A) In general**\nExcept as provided in subparagraph (B), notwithstanding any provision of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ), the Secretary may not order an alien to be removed from the United States if the alien\u2014\n**(i)**\nis in exclusion, deportation, or removal proceedings under any provision of such Act; and\n**(ii)**\nhas submitted an application for adjustment of status under subsection (b).\n**(B) Exception**\nThe Secretary may order an alien described in subparagraph (A) to be removed from the United States if the Secretary has made a final determination to deny the application for adjustment of status under subsection (b) of the alien.\n**(3) Work authorization**\n**(A) In general**\nThe Secretary may\u2014\n**(i)**\nauthorize an alien who has applied for adjustment of status under subsection (b) to engage in employment in the United States during the period in which a determination on such application is pending; and\n**(ii)**\nprovide such alien with an employment authorized endorsement or other appropriate document signifying authorization of employment.\n**(B) Pending applications**\nIf an application for adjustment of status under subsection (b) is pending for a period exceeding 180 days and has not been denied, the Secretary shall authorize employment for the applicable alien.\n##### (e) Record of permanent residence\nOn the approval of an application for adjustment of status under subsection (b) of an alien, the Secretary shall establish a record of admission for permanent residence for the alien as of the date of the arrival of the alien in the United States.\n##### (f) Availability of administrative review\nThe Secretary shall provide applicants for adjustment of status under subsection (b) with the same right to, and procedures for, administrative review as are provided to\u2014\n**(1)**\napplicants for adjustment of status under section 245 of the Immigration and Nationality Act ( 8 U.S.C. 1255 ); and\n**(2)**\naliens subject to removal proceedings under section 240 of such Act ( 8 U.S.C. 1229a ).\n##### (g) Limitation on judicial review\n**(1) In general**\nA determination by the Secretary with respect to the adjustment of status of any alien under this section is final and shall not be subject to review by any court.\n**(2) Rule of construction**\nNothing in paragraph (1) shall be construed to preclude the review of a constitutional claim or a question of law under section 704 of title 5, United States Code, with respect to a denial of adjustment of status under this section.\n##### (h) No offset in number of visas available\nThe Secretary of State shall not be required to reduce the number of immigrant visas authorized to be issued under any provision of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) to offset the adjustment of status of an alien who has been lawfully admitted for permanent residence pursuant to this section.\n##### (i) Application of immigration and nationality act provisions\n**(1) Savings provision**\nNothing in this Act may be construed to repeal, amend, alter, modify, effect, or restrict the powers, duties, function, or authority of the Secretary in the administration and enforcement of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) or any other law relating to immigration, nationality, or naturalization.\n**(2) Effect of eligibility for adjustment of status**\nThe eligibility of an alien to be lawfully admitted for permanent residence under this section shall not preclude the alien from seeking any status under any other provision of law for which the alien may otherwise be eligible.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-03-17T17:38:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1348",
          "measure-number": "1348",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-01-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1348v00",
            "update-date": "2026-01-05"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Venezuelan Adjustment Act</strong></p> <p>This bill requires the Department of Homeland Security (DHS) to grant lawful permanent resident status to qualifying nationals of Venezuela.</p> <p>A national of Venezuela shall be eligible if that individual (1) applies for lawful permanent resident status no later than three years after this bill's enactment, (2) entered the United States on or before December 31, 2021, (3) has been continuously physically present in the United States for at least one year when filing their application, (4) is otherwise eligible to receive an immigrant visa, and (5) is not inadmissible under various grounds such as a conviction for an aggravated felony. Certain grounds for inadmissibility, such as the public charge ground, shall not apply.</p> <p>The spouse, child, or unmarried son or daughter of an eligible individual shall also be eligible. </p> <p>If an individual has applied for lawful permanent resident status under this bill and is subject to exclusion, deportation, or removal proceedings, DHS may not order that individual's removal unless DHS has made a final determination to deny the application. </p> <p>DHS must provide work authorization to an individual whose application has been pending for more than 180 days, and may also provide authorization before that.</p>"
        },
        "title": "Venezuelan Adjustment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1348.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Venezuelan Adjustment Act</strong></p> <p>This bill requires the Department of Homeland Security (DHS) to grant lawful permanent resident status to qualifying nationals of Venezuela.</p> <p>A national of Venezuela shall be eligible if that individual (1) applies for lawful permanent resident status no later than three years after this bill's enactment, (2) entered the United States on or before December 31, 2021, (3) has been continuously physically present in the United States for at least one year when filing their application, (4) is otherwise eligible to receive an immigrant visa, and (5) is not inadmissible under various grounds such as a conviction for an aggravated felony. Certain grounds for inadmissibility, such as the public charge ground, shall not apply.</p> <p>The spouse, child, or unmarried son or daughter of an eligible individual shall also be eligible. </p> <p>If an individual has applied for lawful permanent resident status under this bill and is subject to exclusion, deportation, or removal proceedings, DHS may not order that individual's removal unless DHS has made a final determination to deny the application. </p> <p>DHS must provide work authorization to an individual whose application has been pending for more than 180 days, and may also provide authorization before that.</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119hr1348"
    },
    "title": "Venezuelan Adjustment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Venezuelan Adjustment Act</strong></p> <p>This bill requires the Department of Homeland Security (DHS) to grant lawful permanent resident status to qualifying nationals of Venezuela.</p> <p>A national of Venezuela shall be eligible if that individual (1) applies for lawful permanent resident status no later than three years after this bill's enactment, (2) entered the United States on or before December 31, 2021, (3) has been continuously physically present in the United States for at least one year when filing their application, (4) is otherwise eligible to receive an immigrant visa, and (5) is not inadmissible under various grounds such as a conviction for an aggravated felony. Certain grounds for inadmissibility, such as the public charge ground, shall not apply.</p> <p>The spouse, child, or unmarried son or daughter of an eligible individual shall also be eligible. </p> <p>If an individual has applied for lawful permanent resident status under this bill and is subject to exclusion, deportation, or removal proceedings, DHS may not order that individual's removal unless DHS has made a final determination to deny the application. </p> <p>DHS must provide work authorization to an individual whose application has been pending for more than 180 days, and may also provide authorization before that.</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119hr1348"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1348ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Venezuelan Adjustment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Venezuelan Adjustment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Homeland Security to adjust the status of certain aliens who are nationals of Venezuela to that of aliens lawfully admitted for permanent residence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:29Z"
    }
  ]
}
```
