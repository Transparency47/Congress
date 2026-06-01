# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3594?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3594
- Title: Nutrition Administration Assistance Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3594
- Origin chamber: Senate
- Introduced date: 2026-01-07
- Update date: 2026-02-05T17:40:03Z
- Update date including text: 2026-02-05T17:40:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in Senate
- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-01-07: Introduced in Senate

## Actions

- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3594",
    "number": "3594",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Nutrition Administration Assistance Act of 2026",
    "type": "S",
    "updateDate": "2026-02-05T17:40:03Z",
    "updateDateIncludingText": "2026-02-05T17:40:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-07",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T22:32:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3594is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3594\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2026 Mr. Luj\u00e1n introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo provide additional funds to States for administration of certain nutrition programs.\n#### 1. Short title\nThis Act may be cited as the Nutrition Administration Assistance Act of 2026 .\n#### 2. Additional funds for administration costs\n##### (a) Commodity supplemental food program\nIn addition to funds otherwise made available to State agencies to pay administration costs incurred by State agencies to carry out section 5 of the Agriculture and Consumer Protection Act of 1973 ( 7 U.S.C. 612c note), 70 percent of the funds appropriated under section 3 shall be provided to States for such administration costs.\n##### (b) Emergency Food Assistance Act of 1983\nIn addition to funds otherwise made available to States to pay administration costs incurred by States to carry out State plans under section 203A of the Emergency Food Assistance Act of 1983 ( 7 U.S.C. 7504 ), 20 percent of the funds appropriated under section 3 shall be provided to States for such administration costs.\n##### (c) Seniors farmers\u2019 market nutrition program\nIn addition to funds otherwise made available to the Secretary of Agriculture for administration costs to carry out section 4402 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 3007 ), 10 percent of the funds appropriated under section 3 shall be provided to States for such administration costs.\n#### 3. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $1,000,000 for each of the fiscal years 2026 through 2030.",
      "versionDate": "2026-01-07",
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
        "actionDate": "2026-01-07",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "6966",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Nutrition Administration Assistance Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-02-04T23:35:44Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3594is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide additional funds to States for administration of certain nutrition programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:36Z"
    },
    {
      "title": "Nutrition Administration Assistance Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nutrition Administration Assistance Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```
