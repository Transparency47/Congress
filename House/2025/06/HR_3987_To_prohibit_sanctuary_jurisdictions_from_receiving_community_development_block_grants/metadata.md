# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3987?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3987
- Title: No Community Development Block Grants for Sanctuary Cities Act
- Congress: 119
- Bill type: HR
- Bill number: 3987
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-12-05T21:31:22Z
- Update date including text: 2025-12-05T21:31:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3987",
    "number": "3987",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "N000190",
        "district": "5",
        "firstName": "Ralph",
        "fullName": "Rep. Norman, Ralph [R-SC-5]",
        "lastName": "Norman",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "No Community Development Block Grants for Sanctuary Cities Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:31:22Z",
    "updateDateIncludingText": "2025-12-05T21:31:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:08:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "SC"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "FL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "SC"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "MI"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3987ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3987\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Norman (for himself, Ms. Mace , Mr. Buchanan , and Mrs. Biggs of South Carolina ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prohibit sanctuary jurisdictions from receiving community development block grants.\n#### 1. Short title\nThis Act may be cited as the No Community Development Block Grants for Sanctuary Cities Act .\n#### 2. Ineligibility of sanctuary jurisdictions for community development block grants\nTitle I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 102(a) ( 42 U.S.C. 5302(a) ), by adding at the end the following:\n(25) (A) Except as provided in subparagraph (B), the term sanctuary jurisdiction means any State or political subdivision of a State that has in effect a statute, ordinance, policy, or practice that prohibits or restricts any government entity or official from\u2014 (i) sending, receiving, maintaining, or exchanging with any Federal, State, or local government entity information regarding the citizenship or immigration status (lawful or unlawful) of any individual; or (ii) complying with a request lawfully made by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act ( 8 U.S.C. 1226 , 1357) to comply with a detainer for, or notify about the release of, an individual. (B) A State or political subdivision of a State shall not be deemed a sanctuary jurisdiction based solely on its having a policy whereby its officials will not share information regarding, or comply with a request made by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act ( 8 U.S.C. 1226 , 1357) to comply with a detainer regarding, an individual who comes forward as a victim or a witness to a criminal offense. ; and\n**(2)**\nin section 104(b) ( 42 U.S.C. 5304(b) )\u2014\n**(A)**\nin paragraph (5), by striking and at the end;\n**(B)**\nby redesignating paragraph (6) as paragraph (7); and\n**(C)**\nby inserting after paragraph (5) the following:\n(6) the grantee is not a sanctuary jurisdiction and will not become a sanctuary jurisdiction during the period for which the grantee receives a grant under this title; and .",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-12",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2060",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Community Development Block Grants for Sanctuary Cities Act",
      "type": "S"
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
        "updateDate": "2025-07-03T13:47:58Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3987ih.xml"
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
      "title": "No Community Development Block Grants for Sanctuary Cities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Community Development Block Grants for Sanctuary Cities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit sanctuary jurisdictions from receiving community development block grants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:37Z"
    }
  ]
}
```
