# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7684?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7684
- Title: SCOPE Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7684
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-24T20:11:45Z
- Update date including text: 2026-04-24T20:11:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7684",
    "number": "7684",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "SCOPE Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-24T20:11:45Z",
    "updateDateIncludingText": "2026-04-24T20:11:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:00:10Z",
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
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7684ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7684\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Beyer (for himself, Mr. Mullin , and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Administrator of the Environmental Protection Agency to conduct a study, and publish guidance on, calculating and reporting scope 3 emissions.\n#### 1. Short title\nThis Act may be cited as the Standardized Calculation of Operational Polluting Emissions Act of 2026 or the SCOPE Act of 2026 .\n#### 2. Study and guidance on scope 3 emissions\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Direct emitter**\nThe term direct emitter means\u2014\n**(A)**\na facility\u2014\n**(i)**\nthat is in 1 of the source categories described in any of subparts C through JJ of part 98 of title 40, Code of Federal Regulations (or successor regulations); and\n**(ii)**\nwith respect to which the greenhouse gas reporting requirements and related monitoring, recordkeeping, and reporting requirements of that part apply; and\n**(B)**\nany other facility the Administrator determines appropriate.\n**(3) Greenhouse gas**\nThe term greenhouse gas means the air pollutants (as defined in section 302 of the Clean Air Act ( 42 U.S.C. 7602 )) carbon dioxide, hydrofluorocarbons, methane, nitrous oxide, perfluorocarbons, and sulfur hexafluoride.\n**(4) Scope 3 emissions**\nThe term scope 3 emissions means indirect greenhouse gas emissions resulting from upstream and downstream value chain activities, as determined by the Administrator.\n##### (b) Study; guidance\nNot later than 1 year after the date of enactment of this Act, the Administrator shall conduct a study on, and publish guidance with respect to, calculating and reporting, for direct emitters, scope 3 emissions above thresholds the Administrator determines appropriate.\n##### (c) Inclusions\nThe guidance published under subsection (b) shall include\u2014\n**(1)**\nthresholds of scope 3 emissions above which reporting to the Environmental Protection Agency is recommended;\n**(2)**\ncalculation methodologies for scope 3 emissions based on source categories;\n**(3)**\nrecommendations on frequency of monitoring scope 3 emissions;\n**(4)**\nquality assurance and control guidance for scope 3 emissions data;\n**(5)**\nmethodologies for estimating missing scope 3 emissions data; and\n**(6)**\nguidance for recordkeeping for scope 3 emissions data and reporting of those data.\n##### (d) Savings provision\nNothing in this section affects the authority of the President, any Federal agency, or any State under existing law.",
      "versionDate": "2026-02-25",
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
        "actionDate": "2026-02-26",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "3928",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SCOPE Act of 2026",
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
        "name": "Environmental Protection",
        "updateDate": "2026-04-24T20:11:45Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7684ih.xml"
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
      "title": "SCOPE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T06:53:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SCOPE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T06:53:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Standardized Calculation of Operational Polluting Emissions Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T06:53:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Environmental Protection Agency to conduct a study, and publish guidance on, calculating and reporting scope 3 emissions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T06:47:22Z"
    }
  ]
}
```
