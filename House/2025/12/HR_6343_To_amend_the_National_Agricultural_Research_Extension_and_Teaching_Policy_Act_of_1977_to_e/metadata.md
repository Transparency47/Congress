# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6343?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6343
- Title: Parity for Alaska Native and Native Hawaiian Students in Agriculture Act
- Congress: 119
- Bill type: HR
- Bill number: 6343
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2026-05-16T08:07:55Z
- Update date including text: 2026-05-16T08:07:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-12-01: Introduced in House

## Actions

- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6343",
    "number": "6343",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Parity for Alaska Native and Native Hawaiian Students in Agriculture Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:55Z",
    "updateDateIncludingText": "2026-05-16T08:07:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T17:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:01:42Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "AK"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6343ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6343\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Ms. Tokuda (for herself, Mr. Begich , and Mr. Case ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to extend education grant programs for Alaska Native serving institutions and Native Hawaiian serving institutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Parity for Alaska Native and Native Hawaiian Students in Agriculture Act .\n#### 2. Education grants to Alaska Native serving institutions and Native Hawaiian serving institutions\nSection 1419B of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3156 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraph (3) as paragraph (4);\n**(B)**\nby inserting after paragraph (2) the following:\n(3) Grant period A grant made under this subsection shall be for a period of not more than 3 years. ; and\n**(C)**\nin paragraph (4) (as so redesignated), by striking $10,000,000 in fiscal years 2001 through 2023 and inserting $10,000,000 for fiscal year 2026 and $15,000,000 for each of fiscal years 2027 through 2031 ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraph (3) as paragraph (4);\n**(B)**\nby inserting after paragraph (2) the following:\n(3) Grant period A grant made under this subsection shall be for a period of not more than 3 years. ; and\n**(C)**\nin paragraph (4) (as so redesignated), by striking $10,000,000 for each of fiscal years 2001 through 2023 and inserting $10,000,000 for fiscal year 2026 and $15,000,000 for each of fiscal years 2027 through 2031 .",
      "versionDate": "2025-12-01",
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
        "name": "Native Americans",
        "updateDate": "2025-12-11T15:16:30Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6343ih.xml"
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
      "title": "Parity for Alaska Native and Native Hawaiian Students in Agriculture Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T07:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parity for Alaska Native and Native Hawaiian Students in Agriculture Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T07:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to extend education grant programs for Alaska Native serving institutions and Native Hawaiian serving institutions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T07:03:28Z"
    }
  ]
}
```
