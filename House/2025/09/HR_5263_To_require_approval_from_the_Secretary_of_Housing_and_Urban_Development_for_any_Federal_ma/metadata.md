# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5263?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5263
- Title: To require approval from the Secretary of Housing and Urban Development for any Federal manufactured home and safety standards, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5263
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-03-19T08:07:14Z
- Update date including text: 2026-03-19T08:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5263",
    "number": "5263",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "To require approval from the Secretary of Housing and Urban Development for any Federal manufactured home and safety standards, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:14Z",
    "updateDateIncludingText": "2026-03-19T08:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:02:30Z",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MO"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "VA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5263ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5263\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Flood (for himself and Mr. Cleaver ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require approval from the Secretary of Housing and Urban Development for any Federal manufactured home and safety standards, and for other purposes.\n#### 1. Primary authority to establish manufactured home construction and safety standards\nThe Housing and Community Development Act of 1974 ( 42 U.S.C. 5401 et seq. ) is amended\u2014\n**(1)**\nin section 603(7), by inserting energy efficiency, after design, ; and\n**(2)**\nin section 604, by adding at the end the following new subsection:\n(i) Primary authority To establish standards (1) In general The Secretary shall have the primary authority to establish Federal manufactured home construction and safety standards. (2) Approval from Secretary (A) In general The head of any Federal agency that seeks to establish a Federal manufactured home construction and safety standard on or after the date of the enactment of this subsection\u2014 (i) shall submit to the Secretary a proposal describing such standard; and (ii) may not establish such standard without approval from the Secretary. (B) Rejection of standards The Secretary shall reject the standards described in subparagraph (A)\u2014 (i) if the standards would significantly increase the cost of producing manufactured homes, as determined by the Secretary; (ii) if the standards conflict with existing manufactured home construction and safety standards established by the Secretary; or (iii) for any other reason as determined appropriate by the Secretary. (C) Rule of construction Nothing in this subsection shall be construed to require the Secretary to establish new or revised Federal manufactured home construction and safety standards. .",
      "versionDate": "2025-09-10",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-23T18:52:56Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5263ih.xml"
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
      "title": "To require approval from the Secretary of Housing and Urban Development for any Federal manufactured home and safety standards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:33Z"
    },
    {
      "title": "To require approval from the Secretary of Housing and Urban Development for any Federal manufactured home and safety standards, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T08:06:37Z"
    }
  ]
}
```
