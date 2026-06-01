# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3710?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3710
- Title: Loved Ones Interment Act
- Congress: 119
- Bill type: HR
- Bill number: 3710
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2025-12-12T09:07:23Z
- Update date including text: 2025-12-12T09:07:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-04 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-04 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3710",
    "number": "3710",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Loved Ones Interment Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:23Z",
    "updateDateIncludingText": "2025-12-12T09:07:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-04T15:38:19Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3710ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3710\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Ms. Brownley introduced the following bill; which was referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to furnish headstones and markers for certain veterans for whom urns were previously furnished when such veterans are interred with other eligible individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Loved Ones Interment Act .\n#### 2. Department of Veterans Affairs headstones and markers for certain cremated veterans interred with other eligible individuals\nSection 2306(h)(2) of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively;\n**(2)**\nby striking If the Secretary and inserting (A) Except as provided in subparagraph (B), if the Secretary ; and\n**(3)**\nby adding at the end the following new subparagraph (B):\n(B) In the case of a deceased individual referred to in subsection (a) who is cremated and for whom an urn or commemorative plaque is furnished under paragraph (1), the Secretary may also furnish a headstone or marker for the individual if\u2014 (i) the individual is interred at the same burial site as another individual referred to in section 2402(a) of this title; (ii) the headstone or marker furnished includes information about both such individuals; and (iii) the inclusion of such information does not increase the cost of the headstone or marker beyond the maximum amount permitted under law. .",
      "versionDate": "2025-06-04",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-01T16:19:12Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3710ih.xml"
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
      "title": "Loved Ones Interment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T06:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Loved Ones Interment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to furnish headstones and markers for certain veterans for whom urns were previously furnished when such veterans are interred with other eligible individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T06:18:41Z"
    }
  ]
}
```
