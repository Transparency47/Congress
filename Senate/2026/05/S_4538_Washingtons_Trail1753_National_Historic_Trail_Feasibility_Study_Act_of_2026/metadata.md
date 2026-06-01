# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4538?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4538
- Title: Washington’s Trail—1753 National Historic Trail Feasibility Study Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4538
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-30T04:53:26Z
- Update date including text: 2026-05-30T04:53:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4538",
    "number": "4538",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Washington\u2019s Trail\u20141753 National Historic Trail Feasibility Study Act of 2026",
    "type": "S",
    "updateDate": "2026-05-30T04:53:26Z",
    "updateDateIncludingText": "2026-05-30T04:53:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-05-14T17:12:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "VA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "VA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "WV"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4538is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4538\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Mr. Fetterman (for himself, Mr. McCormick , Mr. Kaine , Mr. Warner , Mr. Justice , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the National Trails System Act to direct the Secretary of the Interior to conduct a study on the feasibility of designating Washington\u2019s Trail\u20141753 as a national historic trail, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Washington\u2019s Trail\u20141753 National Historic Trail Feasibility Study Act of 2026 .\n#### 2. Washington\u2019s Trail\u20141753 National Historic Trail Feasibility Study\nSection 5(c) of the National Trails System Act ( 16 U.S.C. 1244(c) ) is amended by adding at the end the following:\n(50) Washington\u2019s Trail\u20141753 Washington\u2019s Trail\u20141753, extending approximately 500 miles from Williamsburg, Virginia, to Fort LeBoeuf (now Waterford), Pennsylvania, following the route taken by George Washington and his party on his diplomatic mission to the French on behalf of Virginia Governor Robert Dinwiddie from October 31, 1753, to January 16, 1754, just prior to the start of the French and Indian War (1754\u20131763). .",
      "versionDate": "2026-05-14",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4538is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Washington\u2019s Trail\u20141753 National Historic Trail Feasibility Study Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T04:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Washington\u2019s Trail\u20141753 National Historic Trail Feasibility Study Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Trails System Act to direct the Secretary of the Interior to conduct a study on the feasibility of designating Washington's Trail-1753 as a national historic trail, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T04:48:24Z"
    }
  ]
}
```
