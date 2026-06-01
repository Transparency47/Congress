# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3276?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3276
- Title: UNtaxed Act
- Congress: 119
- Bill type: S
- Bill number: 3276
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-01-20T14:07:36Z
- Update date including text: 2026-01-20T14:07:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3276",
    "number": "3276",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "UNtaxed Act",
    "type": "S",
    "updateDate": "2026-01-20T14:07:36Z",
    "updateDateIncludingText": "2026-01-20T14:07:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T20:39:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3276is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3276\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo provide for limitations on the implementation and enforcement of a global carbon tax with respect to the United States.\n#### 1. Short title\nThis Act may be cited as the UNtaxed Act .\n#### 2. Limitation on United Nations taxes, tariffs, fees, or other such penalties\nNo tax, tariff, fee, or other such penalty may be levied upon United States citizens or United States entities by the United Nations or any organ, specialized agency, commission, or other formally affiliated body of the United Nations, unless such tax, tariff, fee, or other such penalty is imposed under a treaty with respect to which the Senate has provided its advice and consent under clause 2 of section 2 of article II of the Constitution of the United States.\n#### 3. Limitation on funds relating to global carbon taxes\nNo funds are authorized to be appropriated or otherwise made available for\u2014\n**(1)**\nassessed or voluntary contributions of the United States to the United Nations or any United Nations-affiliated body that would be used to impose a global carbon tax; or\n**(2)**\nimplementation or enforcement of such a global carbon tax.\n#### 4. Definitions\nIn this Act:\n**(1) Global carbon tax**\nThe term global carbon tax means a tax imposed under a global fuel regime that\u2014\n**(A)**\nrequires the owner or operator of a vessel to reduce the level of greenhouse gases emitted by the vessel; and\n**(B)**\nimposes such a tax at set costs with respect to such level of emission of greenhouse gases.\n**(2) United States entity**\nThe term United States entity means an entity organized under the laws of the United States or any jurisdiction within the United States.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-10-31",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5888",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "UNtaxed Act",
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
        "name": "International Affairs",
        "updateDate": "2025-12-19T18:04:16Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3276is.xml"
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
      "title": "UNtaxed Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "UNtaxed Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for limitations on the implementation and enforcement of a global carbon tax with respect to the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:54Z"
    }
  ]
}
```
