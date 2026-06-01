# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8782?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8782
- Title: PLOW Storms Act
- Congress: 119
- Bill type: HR
- Bill number: 8782
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-27T08:23:30Z
- Update date including text: 2026-05-27T08:23:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-13: Introduced in House

## Actions

- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8782",
    "number": "8782",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "PLOW Storms Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:23:30Z",
    "updateDateIncludingText": "2026-05-27T08:23:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "WI"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8782ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8782\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2026 Mr. Bergman (for himself, Mr. Wied , and Mr. Stauber ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Clean Air Act to include dedicated-use municipal snow removal vehicles and machinery as examples of an emergency vehicle in the definition of covered fleet, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Lifesaving Operations during Winter Storms Act or the PLOW Storms Act .\n#### 2. Inclusion of certain snow removal vehicles and machinery as emergency vehicles in the definition of covered fleet\nSection 241(5) of the Clean Air Act ( 42 U.S.C. 7581(5) ) is amended by striking emergency vehicles, and inserting emergency vehicles (including dedicated-use vehicles and machinery owned or operated by a unit of State, local, or tribal government and used primarily for the clearance of snow or ice from, or the application of anti-icing or de-icing material to, public roads, public rights-of-way, or other public property), .",
      "versionDate": "2026-05-13",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8782ih.xml"
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
      "title": "PLOW Storms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PLOW Storms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-27T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Lifesaving Operations during Winter Storms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-27T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Clean Air Act to include dedicated-use municipal snow removal vehicles and machinery as examples of an emergency vehicle in the definition of covered fleet, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:18:41Z"
    }
  ]
}
```
