# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3928?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3928
- Title: SCOPE Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3928
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-04-24T20:11:29Z
- Update date including text: 2026-04-24T20:11:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3928",
    "number": "3928",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SCOPE Act of 2026",
    "type": "S",
    "updateDate": "2026-04-24T20:11:29Z",
    "updateDateIncludingText": "2026-04-24T20:11:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T16:21:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3928is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3928\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Mr. Schiff introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo direct the Administrator of the Environmental Protection Agency to conduct a study, and publish guidance on, calculating and reporting scope 3 emissions.\n#### 1. Short title\nThis Act may be cited as the Standardized Calculation of Operational Polluting Emissions Act of 2026 or the SCOPE Act of 2026 .\n#### 2. Study and guidance on scope 3 emissions\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Direct emitter**\nThe term direct emitter means\u2014\n**(A)**\na facility\u2014\n**(i)**\nthat is in 1 of the source categories described in any of subparts C through JJ of part 98 of title 40, Code of Federal Regulations (or successor regulations); and\n**(ii)**\nwith respect to which the greenhouse gas reporting requirements and related monitoring, recordkeeping, and reporting requirements of that part apply; and\n**(B)**\nany other facility the Administrator determines appropriate.\n**(3) Greenhouse gas**\nThe term greenhouse gas means the air pollutants (as defined in section 302 of the Clean Air Act ( 42 U.S.C. 7602 )) carbon dioxide, hydrofluorocarbons, methane, nitrous oxide, perfluorocarbons, and sulfur hexafluoride.\n**(4) Scope 3 emissions**\nThe term scope 3 emissions means indirect greenhouse gas emissions resulting from upstream and downstream value chain activities, as determined by the Administrator.\n##### (b) Study; guidance\nNot later than 1 year after the date of enactment of this Act, the Administrator shall conduct a study on, and publish guidance with respect to, calculating and reporting, for direct emitters, scope 3 emissions above thresholds the Administrator determines appropriate.\n##### (c) Inclusions\nThe guidance published under subsection (b) shall include\u2014\n**(1)**\nthresholds of scope 3 emissions above which reporting to the Environmental Protection Agency is recommended;\n**(2)**\ncalculation methodologies for scope 3 emissions based on source categories;\n**(3)**\nrecommendations on frequency of monitoring scope 3 emissions;\n**(4)**\nquality assurance and control guidance for scope 3 emissions data;\n**(5)**\nmethodologies for estimating missing scope 3 emissions data; and\n**(6)**\nguidance for recordkeeping for scope 3 emissions data and reporting of those data.\n##### (d) Savings provision\nNothing in this section affects the authority of the President, any Federal agency, or any State under existing law.",
      "versionDate": "2026-02-26",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-02-25",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "7684",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SCOPE Act of 2026",
      "type": "HR"
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
        "updateDate": "2026-03-19T14:46:26Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3928is.xml"
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
      "title": "SCOPE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T04:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SCOPE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Standardized Calculation of Operational Polluting Emissions Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Administrator of the Environmental Protection Agency to conduct a study, and publish guidance on, calculating and reporting scope 3 emissions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-17T04:18:26Z"
    }
  ]
}
```
