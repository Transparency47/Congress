# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7320?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7320
- Title: Minnesota Voter Integrity Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7320
- Origin chamber: House
- Introduced date: 2026-02-02
- Update date: 2026-02-20T15:38:39Z
- Update date including text: 2026-02-20T15:38:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-02-02: Introduced in House

## Actions

- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7320",
    "number": "7320",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Minnesota Voter Integrity Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-20T15:38:39Z",
    "updateDateIncludingText": "2026-02-20T15:38:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "MN"
    },
    {
      "bioguideId": "E000294",
      "district": "6",
      "firstName": "Tom",
      "fullName": "Rep. Emmer, Tom [R-MN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Emmer",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "MN"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7320ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7320\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Mr. Stauber (for himself, Mr. Finstad , Mr. Emmer , and Mrs. Fischbach ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo prohibit the provision of funding to the State of Minnesota until certain reporting requirements pertaining to voting are satisfied.\n#### 1. Short title\nThis Act may be cited as the Minnesota Voter Integrity Act of 2026 .\n#### 2. Limitation on funding\nNone of the funds authorized to be made available under the Help America Vote Act of 2002 may be made available to the State of Minnesota until the Minnesota Secretary of State submits to the Attorney General the following information:\n**(1)**\nAll records supporting or documenting same-day voter registrations, as authorized under Minn. Stat. 201.061, Subd. 3.\n**(2)**\nAll records for the votes cast by voters registered under Minn. Stat. 201.061, Subd. 3.\n**(3)**\nAll records kept under Minn. Stat. 201.01, Subds. 7 and 8.\n**(4)**\nAny other records the Attorney General determines to be relevant to compliance with requirements under the Help America Vote Act of 2002.",
      "versionDate": "2026-02-02",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-20T15:38:39Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7320ih.xml"
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
      "title": "Minnesota Voter Integrity Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Minnesota Voter Integrity Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T07:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the provision of funding to the State of Minnesota until certain reporting requirements pertaining to voting are satisfied.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T07:48:29Z"
    }
  ]
}
```
