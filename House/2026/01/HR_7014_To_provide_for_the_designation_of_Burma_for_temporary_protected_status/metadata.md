# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7014?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7014
- Title: To provide for the designation of Burma for temporary protected status.
- Congress: 119
- Bill type: HR
- Bill number: 7014
- Origin chamber: House
- Introduced date: 2026-01-12
- Update date: 2026-05-13T08:06:52Z
- Update date including text: 2026-05-13T08:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-12: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-12: Introduced in House

## Actions

- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7014",
    "number": "7014",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "To provide for the designation of Burma for temporary protected status.",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:52Z",
    "updateDateIncludingText": "2026-05-13T08:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-12",
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
      "actionDate": "2026-01-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-12",
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
          "date": "2026-01-12T17:02:50Z",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "MN"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NC"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "DC"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7014ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7014\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 12, 2026 Mr. Huizenga (for himself, Mr. Bera , Ms. Kamlager-Dove , Mr. Meeks , Ms. McCollum , and Mr. Kennedy of New York ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for the designation of Burma for temporary protected status.\n#### 1. Designation for purposes of granting temporary protected status\n##### (a) Designation\n**(1) In general**\nFor purposes of section 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ), Burma shall be treated as if it had been designated under subsection (b)(1)(C) of that section, subject to the provisions of this section.\n**(2) Period of designation**\nThe initial period of the designation referred to in paragraph (1) shall be for the 18-month period beginning on November 25, 2025.\n##### (b) Aliens eligible\nAs a result of the designation made under subsection (a), an alien who is a national of Burma is deemed to satisfy the requirements under paragraph (1) of section 244(c) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(c) ), subject to paragraph (3) of such section, if the alien\u2014\n**(1)**\nhas been continuously physically present in the United States since the date of the enactment of this Act;\n**(2)**\nis admissible as an immigrant, except as otherwise provided in paragraph (2)(A) of such section, and is not ineligible for temporary protected status under paragraph (2)(B) of such section; and\n**(3)**\nregisters for temporary protected status in a manner established by the Secretary of Homeland Security.\n##### (c) Consent To travel abroad\n**(1) In general**\nThe Secretary of Homeland Security shall give prior consent to travel abroad, in accordance with section 244(f)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(f)(3) ), to an alien who is granted temporary protected status pursuant to the designation made under subsection (a) if the alien establishes to the satisfaction of the Secretary of Homeland Security that emergency and extenuating circumstances beyond the control of the alien require the alien to depart for a brief, temporary trip abroad.\n**(2) Treatment upon return**\nAn alien returning to the United States in accordance with an authorization described in paragraph (1) shall be treated as any other returning alien provided temporary protected status under section 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ).",
      "versionDate": "2026-01-12",
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
        "updateDate": "2026-02-04T18:32:30Z"
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
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7014ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the designation of Burma for temporary protected status.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T06:48:23Z"
    },
    {
      "title": "To provide for the designation of Burma for temporary protected status.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T09:05:23Z"
    }
  ]
}
```
