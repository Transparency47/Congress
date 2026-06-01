# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7527
- Title: Pay Less at the Pump Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7527
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-03-05T00:30:16Z
- Update date including text: 2026-03-05T00:30:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7527",
    "number": "7527",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Pay Less at the Pump Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-05T00:30:16Z",
    "updateDateIncludingText": "2026-03-05T00:30:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:01:50Z",
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
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "OK"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "WI"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7527ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7527\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Carey (for himself, Mr. Hern of Oklahoma , Mrs. Miller of West Virginia , Ms. Malliotakis , and Mr. Wied ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to terminate the Hazardous Substance Superfund financing rate.\n#### 1. Short title\nThis Act may be cited as the Pay Less at the Pump Act of 2026 .\n#### 2. Termination of Hazardous Substance Superfund financing rate\n##### (a) In general\nSection 4611 of the Internal Revenue Code of 1986 is amended by inserting after subsection (d) the following new subsection:\n(e) Application of Hazardous Substance Superfund financing rate The Hazardous Substance Superfund financing rate under this section shall not apply after December 31, 2025. .\n##### (b) Termination of authority for advances\nSection 9507(d)(3)(B) of such Code is amended\u2014\n**(1)**\nby striking December 31, 2032 and inserting the date of the enactment of the Pay Less at the Pump Act of 2026 , and\n**(2)**\nby striking on or before such date and inserting on a quarterly basis from unobligated amounts available in such Fund until repaid in full .\n##### (c) Effective date\n**(1) In general**\nThe amendment made by subsection (a) shall take effect on January 1, 2026.\n**(2) Termination of authority for advances**\nThe amendments made by subsection (b) shall take effect on the date of the enactment of this Act.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on Finance. (text: CR S611)"
      },
      "number": "3863",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Pay Less at the Pump Act of 2026",
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
        "name": "Taxation",
        "updateDate": "2026-02-27T21:41:33Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7527ih.xml"
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
      "title": "Pay Less at the Pump Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T09:38:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pay Less at the Pump Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T09:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to terminate the Hazardous Substance Superfund financing rate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T09:33:39Z"
    }
  ]
}
```
