# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4321?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4321
- Title: SMART for TBI Act
- Congress: 119
- Bill type: HR
- Bill number: 4321
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2025-09-19T17:07:39Z
- Update date including text: 2025-09-19T17:07:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4321",
    "number": "4321",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "SMART for TBI Act",
    "type": "HR",
    "updateDate": "2025-09-19T17:07:39Z",
    "updateDateIncludingText": "2025-09-19T17:07:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4321ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4321\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Crow (for himself and Mr. Crank ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to develop a strategy for treating traumatic brain injuries through digital health technologies.\n#### 1. Short title\nThis Act may be cited as the Supporting Modern Approaches in Recovery Technology for Traumatic Brain Injury Act or the SMART for TBI Act .\n#### 2. Strategy for treating traumatic brain injuries through digital health technologies\nSection 735 of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( Public Law 117\u2013263 ; 10 U.S.C. 1071 note) is amended\u2014\n**(1)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively; and\n**(2)**\nby inserting after subsection (d) the following new subsection:\n(e) Digital health technologies (1) Working group As part of the Initiative, the Secretary shall establish a working group to develop a strategy for treating traumatic brain injuries through digital health technologies. (2) Membership The working group shall be composed of members of the Armed Forces, civilian employees of the Department of Defense, and individuals not employed by the Federal Government, who have expertise in traumatic brain injury clinical care, biomedical informatics, engineering, or implementation science. (3) Elements The strategy developed under paragraph (1) shall include the following: (A) Identification of capability gaps in the treatment of traumatic brain injuries that could be addressed through artificial intelligence and digital health technologies. (B) An analysis of existing research, development, and acquisition efforts leveraging artificial intelligence-based capabilities and digital health technologies, including any applicable commercial off-the-shelf solutions being used by the Secretary to support the treatment of traumatic brain injuries. (C) Recommendations with respect to advances required to\u2014 (i) address gaps identified under subparagraph (A); and (ii) significantly improve the treatment of traumatic brain injuries using artificial intelligence and digital health technologies. (D) A recommended investment plan to advance technology and knowledge readiness levels to field digital health technologies to treat traumatic brain injuries. (4) Briefing Not later than September 30, 2026, the Secretary shall provide to the congressional defense committees a briefing on the strategy developed under paragraph (1). .",
      "versionDate": "2025-07-10",
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
        "updateDate": "2025-09-19T17:07:39Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4321ih.xml"
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
      "title": "SMART for TBI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SMART for TBI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Modern Approaches in Recovery Technology for Traumatic Brain Injury Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to develop a strategy for treating traumatic brain injuries through digital health technologies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T02:03:48Z"
    }
  ]
}
```
