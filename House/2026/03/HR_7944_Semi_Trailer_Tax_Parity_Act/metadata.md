# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7944?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7944
- Title: Semi-Trailer Tax Parity Act
- Congress: 119
- Bill type: HR
- Bill number: 7944
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-04-21T01:23:20Z
- Update date including text: 2026-04-21T01:23:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7944",
    "number": "7944",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Semi-Trailer Tax Parity Act",
    "type": "HR",
    "updateDate": "2026-04-21T01:23:20Z",
    "updateDateIncludingText": "2026-04-21T01:23:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7944ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7944\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. Moore of Utah (for himself and Mrs. Torres of California ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to apply the floor plan financing interest rules to semi-trailers.\n#### 1. Short title\nThis Act may be cited as the Semi-Trailer Tax Parity Act .\n#### 2. Application of floor plan financing interest rules to semitrailers\n##### (a) In general\nSection 163(j)(9)(C) of the Internal Revenue Code of 1986 is amended by adding at the end the following: Such term shall further include any truck trailer or semi-trailer chassis or truck trailer or semi-trailer bodies (within the meaning of subparagraphs (C) and (D) of section 4051(a)(1), but without regard to whether the acquisition is the first retail sale of such property) which are not described in section 4051(a)(3). .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2026-03-16",
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
        "name": "Taxation",
        "updateDate": "2026-04-21T01:23:19Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7944ih.xml"
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
      "title": "Semi-Trailer Tax Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Semi-Trailer Tax Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to apply the floor plan financing interest rules to semi-trailers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T05:18:52Z"
    }
  ]
}
```
