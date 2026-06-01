# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8527
- Title: Rural Animal Shelter Investment Act
- Congress: 119
- Bill type: HR
- Bill number: 8527
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-05-08T20:29:35Z
- Update date including text: 2026-05-08T20:29:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8527",
    "number": "8527",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001229",
        "district": "6",
        "firstName": "Jefferson",
        "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
        "lastName": "Shreve",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Rural Animal Shelter Investment Act",
    "type": "HR",
    "updateDate": "2026-05-08T20:29:35Z",
    "updateDateIncludingText": "2026-05-08T20:29:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
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
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:05:35Z",
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
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8527ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8527\nIN THE HOUSE OF REPRESENTATIVES\nApril 27, 2026 Mr. Shreve (for himself and Mr. Figures ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to designate animal shelters as essential community facilities eligible for direct loans and grants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Animal Shelter Investment Act .\n#### 2. Eligibility of animal shelters under the Community Facility Direct Loan and Grant Program\nSection 306(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a) ) is amended by adding at the end the following:\n(27) Animal shelter considered an essential community facility For the purpose of the essential community facilities loan and grant programs under this subsection, an animal shelter shall be considered an essential community facility. .\n#### 3. Effective date\nThe amendment made by this Act shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2026-04-27",
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
        "updateDate": "2026-05-08T20:29:34Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8527ih.xml"
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
      "title": "Rural Animal Shelter Investment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T08:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Animal Shelter Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T08:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Farm and Rural Development Act to designate animal shelters as essential community facilities eligible for direct loans and grants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T08:03:34Z"
    }
  ]
}
```
