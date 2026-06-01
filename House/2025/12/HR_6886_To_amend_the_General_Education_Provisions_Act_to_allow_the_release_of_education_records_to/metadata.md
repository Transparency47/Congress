# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6886
- Title: Reverse Transfer Efficiency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6886
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-05T16:05:20Z
- Update date including text: 2026-01-05T16:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6886",
    "number": "6886",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Reverse Transfer Efficiency Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-05T16:05:20Z",
    "updateDateIncludingText": "2026-01-05T16:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:07:00Z",
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
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6886ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6886\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Neguse (for himself and Mr. Kennedy of Utah ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the General Education Provisions Act to allow the release of education records to facilitate the award of a recognized postsecondary credential.\n#### 1. Short title\nThis Act may be cited as the Reverse Transfer Efficiency Act of 2025 .\n#### 2. Release of education records to facilitate the award of a recognized postsecondary credential\nSection 444(b)(1) of the General Education Provisions Act ( 20 U.S.C. 1232g(b)(1) ) is amended\u2014\n**(1)**\nin subparagraph (K)(ii), by striking ; and and inserting a semicolon;\n**(2)**\nin subparagraph (L), by striking the period at the end and inserting ; and ; and\n**(3)**\nby inserting after subparagraph (L) the following:\n(M) an institution of postsecondary education in which the student was previously enrolled, to which records of postsecondary coursework and credits are sent for the purpose of applying such coursework and credits toward completion of a recognized postsecondary credential (as that term is defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 )), upon condition that the student provides written consent prior to receiving such credential. .",
      "versionDate": "2025-12-18",
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
        "name": "Education",
        "updateDate": "2026-01-05T16:05:20Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6886ih.xml"
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
      "title": "To amend the General Education Provisions Act to allow the release of education records to facilitate the award of a recognized postsecondary credential.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T12:39:56Z"
    },
    {
      "title": "Reverse Transfer Efficiency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reverse Transfer Efficiency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T12:23:18Z"
    }
  ]
}
```
