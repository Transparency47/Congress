# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8002?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8002
- Title: Fair Wages for Incarcerated Workers Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8002
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-05-22T10:23:36Z
- Update date including text: 2026-05-22T10:23:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8002",
    "number": "8002",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001061",
        "district": "5",
        "firstName": "Emanuel",
        "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
        "lastName": "Cleaver",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Fair Wages for Incarcerated Workers Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T10:23:36Z",
    "updateDateIncludingText": "2026-05-22T10:23:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "GA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "IL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "IL"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "IL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NM"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "WI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "DC"
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
      "sponsorshipDate": "2026-04-20",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8002ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8002\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Cleaver (for himself, Ms. Kamlager-Dove , Mr. Johnson of Georgia , Mrs. Ramirez , Mr. Garc\u00eda of Illinois , Mr. Davis of Illinois , Ms. Stansbury , Mr. Pocan , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require coverage of incarcerated workers under the Fair Labor Standards Act of 1938, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Wages for Incarcerated Workers Act of 2026 .\n#### 2. Coverage of incarcerated workers under the Fair Labor Standards Act of 1938\nSection 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ) is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (B), by striking ; and and inserting a semicolon;\n**(ii)**\nin subparagraph (C)(ii)(V), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(D) any individual employed as an incarcerated worker by a public agency that operates the correctional facility in which such individual is incarcerated or detained. ; and\n**(B)**\nby adding at the end the following:\n(6) The term employee includes (in addition to an individual described in paragraph (2)(D)) any individual employed as an incarcerated worker by a private entity that operates, through a contract with a public agency, the correctional facility in which such individual is incarcerated or detained. ;\n**(2)**\nin subsection (m)(1), by striking any employee. and inserting any employee: Provided further , That, in the case of an employee who is an incarcerated worker, the cost of board, lodging, or other facilities and any amount taken from amounts paid by such incarcerated worker for payment of a court-imposed fee shall not be included in the wage paid to such employee. ; and\n**(3)**\nby adding at the end the following:\n(z) (1) Incarcerated worker means an individual, incarcerated or detained in a correctional facility operated by a public agency or by a private entity through a contract with a public agency, who performs work offered or required by or through the correctional facility, including work associated with prison work programs, work release programs, the UNICOR program, State prison industries, public works programs, restitution centers, correctional facility operations and maintenance, and private entities. (2) An incarcerated worker shall be considered employed by\u2014 (A) the public agency operating the correctional facility in which the individual is incarcerated or detained; or (B) in the case of a correctional facility operated by a private entity through a contract with a public agency, such private entity. (aa) Correctional facility has the meaning given such term in section 901 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251 ). (bb) (1) Court-imposed fee means any fee imposed by a court as a result of a criminal conviction, including any surcharge imposed for a felony or misdemeanor conviction, a criminal justice administrative fee, a court-appointed attorney fee, a court clerk fee, a filing clerk fee, a DNA database fee, a jury fee, a crime lab analysis fee, a late fee, an installment fee, or any other court cost. (2) The term court-imposed fee does not include any amount required by a court to be paid for child support, to a crime victim compensation fund, for a civil judgment, or for a criminal fine. .",
      "versionDate": "2026-03-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8002ih.xml"
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
      "title": "Fair Wages for Incarcerated Workers Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Wages for Incarcerated Workers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require coverage of incarcerated workers under the Fair Labor Standards Act of 1938, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:29Z"
    }
  ]
}
```
