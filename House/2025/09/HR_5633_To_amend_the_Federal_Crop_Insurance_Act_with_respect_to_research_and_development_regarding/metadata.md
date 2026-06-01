# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5633
- Title: Agriculture Infrastructure Stability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5633
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-11-25T16:17:22Z
- Update date including text: 2025-11-25T16:17:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5633",
    "number": "5633",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Agriculture Infrastructure Stability Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-25T16:17:22Z",
    "updateDateIncludingText": "2025-11-25T16:17:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "TX"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5633ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5633\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Jackson of Texas (for himself and Mr. Arrington ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Crop Insurance Act with respect to research and development regarding harvest incentive policies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Agriculture Infrastructure Stability Act of 2025 .\n#### 2. Harvest incentive policies\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended by adding at the end the following:\n(20) Harvest incentive policies (A) In general The Corporation shall carry out research and development, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out research and development, regarding a harvest incentive for a policy that provides coverage for loss of revenue. (B) Availability of policy Notwithstanding the last sentence of section 508(a)(1), and section 508(a)(2), not later than 2 years after the date of enactment of this paragraph, the Corporation shall make a policy described in subparagraph (A) available if the requirements of section 508(h) are met. (C) Report Not later than 1 year after the date of enactment of this paragraph, the Corporation shall submit to the Committees on Appropriations and on Agriculture of the House of Representatives and the Committees on Appropriations and on Agriculture, Nutrition, and Forestry of the Senate a report that includes\u2014 (i) the results of the research and development carried out under subparagraph (A); and (ii) a description of any policy made available under subparagraph (B). .",
      "versionDate": "2025-09-30",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-25T16:17:22Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5633ih.xml"
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
      "title": "Agriculture Infrastructure Stability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Agriculture Infrastructure Stability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Crop Insurance Act with respect to research and development regarding harvest incentive policies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:13Z"
    }
  ]
}
```
