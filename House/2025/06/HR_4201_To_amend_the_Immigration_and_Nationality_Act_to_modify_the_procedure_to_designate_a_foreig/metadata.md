# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4201?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4201
- Title: TPS Reform Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4201
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-05-08T08:06:47Z
- Update date including text: 2026-05-08T08:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4201",
    "number": "4201",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "TPS Reform Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:47Z",
    "updateDateIncludingText": "2026-05-08T08:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:03:00Z",
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
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "WI"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AZ"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TX"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "PA"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "MD"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4201ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4201\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Roy (for himself, Mr. Tiffany , Mr. Gill of Texas , Mr. Crane , Mr. Cloud , Mr. Babin , and Mr. Perry ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to modify the procedure to designate a foreign state, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the TPS Reform Act of 2025 .\n#### 2. Temporary Protected Status\n##### (a) Power To designate a foreign state\nSection 244(b) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(b) ) is amended\u2014\n**(1)**\nby striking paragraphs (1), (2), and (3) and inserting the following:\n(1) Initial designation For purposes of this section, a foreign state shall be designated upon the enactment of an Act that satisfies the following requirements: (A) The Act shall contain a finding\u2014 (i) that there is an ongoing armed conflict within the state and, due to such conflict, requiring the return of aliens who are nationals of that state (or to the part of the state) would pose a serious threat to their personal safety; (ii) that\u2014 (I) there has been an earthquake, flood, drought, epidemic, or other immediately life-threatening environmental disaster in the state resulting in a substantial, but temporary, disruption of living conditions in the area affected; (II) the foreign state is unable, temporarily, to handle adequately the return to the state of aliens who are nationals of the state; and (III) the foreign state officially has requested designation under this subparagraph; or (iii) that there exist extraordinary and temporary conditions in the foreign state that prevent aliens who are nationals of the state from returning to the state in safety and that permitting the aliens to remain temporarily in the United States is not contrary to the national interest of the United States. (B) The Act shall include\u2014 (i) an estimate of the number of nationals of the foreign state who are (or within the effective period of the designation are likely to become) eligible for temporary protected status under this section; (ii) such nationals\u2019 immigration status in the United States; and (iii) a time period for the effectiveness of the designation that is not greater than 18 months. (2) Termination (A) Timely termination If an initial designation of a foreign state is not extended under paragraph (3), the initial designation shall terminate at the end of the time period described in paragraph (1)(B)(iii). (B) Early termination For purposes of this section, the designation of a foreign state shall be terminated upon the enactment of an Act that contains a finding that the foreign state (or part of such foreign state) no longer meets the conditions for designation under paragraph (1)(A). (3) Extension For purposes of this section, the time period for the effectiveness of the designation of a foreign state shall be extended upon the enactment of an Act that includes\u2014 (A) a finding that the conditions for designation under paragraph (1)(A) continue to be met; and (B) a time period for the effectiveness of the extension that is not greater than 12 months. ; and\n**(2)**\nin paragraph (5)(A), by striking of the Attorney General and inserting made in any Act .\n##### (b) Aliens lacking lawful immigration status\nSection 244(c)(2)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(c)(2)(B) ) is amended\u2014\n**(1)**\nin clause (i), by striking , or at the end and inserting a semicolon;\n**(2)**\nin clause (ii), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(iii) the alien lacks a lawful immigration status. .\n##### (c) Conforming amendments\nSection 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a et seq. ) is amended\u2014\n**(1)**\nin subsection (d)(3), by striking If the Attorney General terminates the designation of a foreign state (or part of such foreign state) under subsection (b)(3)(B) and inserting If the designation of a foreign state (or part of such foreign state) is terminated under section 244(b)(2) ; and\n**(2)**\nin subsection (i)(1)\u2014\n**(A)**\nin subparagraph (A), by striking the comma at the end and adding ; and ;\n**(B)**\nin subparagraph (B), by striking , and at the end and inserting a period; and\n**(C)**\nby striking subparagraph (C).\n##### (d) Technical corrections\nSection 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ), as amended by subsections (a) and (b) of this Act, is further amended by striking Attorney General each place it appears and inserting Secretary of Homeland Security .",
      "versionDate": "2025-06-26",
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
        "actionDate": "2025-01-23",
        "text": "Referred to the Subcommittee on Border Security and Enforcement."
      },
      "number": "696",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "End Unaccountable Amnesty Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-23",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "225",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "End Unaccountable Amnesty Act",
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
        "updateDate": "2025-07-28T12:39:20Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4201ih.xml"
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
      "title": "TPS Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T07:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TPS Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to modify the procedure to designate a foreign state, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T07:18:30Z"
    }
  ]
}
```
