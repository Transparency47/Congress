# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4581?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4581
- Title: CCP Sanctions Shot Clock Act
- Congress: 119
- Bill type: S
- Bill number: 4581
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-29T07:08:32Z
- Update date including text: 2026-05-29T07:08:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4581",
    "number": "4581",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "CCP Sanctions Shot Clock Act",
    "type": "S",
    "updateDate": "2026-05-29T07:08:32Z",
    "updateDateIncludingText": "2026-05-29T07:08:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T15:39:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4581is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4581\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the National Defense Authorization Act for Fiscal Year 2026 to require inclusion of certain foreign persons in the Non-SDN Chinese Military-Industrial Complex Companies List.\n#### 1. Short title\nThis Act may be cited as the Chinese Communist Party Sanctions Shot Clock Act or the CCP Sanctions Shot Clock Act .\n#### 2. Requirement of inclusion of certain foreign persons in Non-SDN Chinese Military-Industrial Complex Companies List\nSection 8531 of the National Defense Authorization Act for Fiscal Year 2026 is amended\u2014\n**(1)**\nby redesignating subsection (b) as subsection (c); and\n**(2)**\nby inserting after subsection (a) the following new subsection (b):\n(b) Update and publication of list Not later than one year after the President submits a report under subsection (a), the Secretary of the Treasury shall\u2014 (1) add to the Non-SDN Chinese Military-Industrial Complex Companies List any foreign person that\u2014 (A) is indicated in that report as qualifying for inclusion in that list; and (B) has not already been added to that list; and (2) if any foreign person is added under paragraph (1), publish in the Federal Register a newly revised Non-SDN Chinese Military-Industrial Complex Companies List. .",
      "versionDate": "2026-05-20",
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
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4581is.xml"
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
      "title": "CCP Sanctions Shot Clock Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:08:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CCP Sanctions Shot Clock Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:08:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chinese Communist Party Sanctions Shot Clock Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:08:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Defense Authorization Act for Fiscal Year 2026 to require inclusion of certain foreign persons in the Non-SDN Chinese Military-Industrial Complex Companies List.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:03:38Z"
    }
  ]
}
```
