# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3843?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3843
- Title: TEMP Act
- Congress: 119
- Bill type: S
- Bill number: 3843
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-05-05T12:27:20Z
- Update date including text: 2026-05-05T12:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-02-11: Introduced in Senate

## Actions

- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3843",
    "number": "3843",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "TEMP Act",
    "type": "S",
    "updateDate": "2026-05-05T12:27:20Z",
    "updateDateIncludingText": "2026-05-05T12:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T20:27:08Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3843is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3843\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Mrs. Moody introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Crop Insurance Act to direct the Federal Crop Insurance Corporation to conduct research and development on frost or cold weather insurance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Temperature Event Mitigation Policy Act or the TEMP Act .\n#### 2. Research and development on frost or cold weather insurance\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended by adding at the end the following:\n(20) Frost or cold weather insurance (A) In general The Corporation shall carry out research and development, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out research and development, regarding an index-based policy to insure crops (including tomatoes, peppers, sugarcane, strawberries, melons, citrus, peaches, blueberries, and any other crop) on a nationally available basis against losses due to a frost or cold weather event. (B) Research and development Research and development under subparagraph (A) shall\u2014 (i) evaluate the effectiveness of risk management tools, such as the use of an index, with respect to low frequency and catastrophic loss weather events; and (ii) result in a policy that provides protection for at least 1 of the following: (I) Production loss. (II) Revenue loss. (C) Report Not later than 1 year after the date of enactment of this paragraph, the Corporation shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report that describes\u2014 (i) the results of the research and development carried out under this paragraph; and (ii) any recommendations with respect to those results. .",
      "versionDate": "2026-02-11",
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
        "actionDate": "2026-05-01",
        "text": "Placed on the Union Calendar, Calendar No. 548."
      },
      "number": "8646",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2027",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-10",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7464",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TEMP Act",
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
        "updateDate": "2026-03-03T19:56:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-11",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s3843",
          "measure-number": "3843",
          "measure-type": "s",
          "orig-publish-date": "2026-02-11",
          "originChamber": "SENATE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3843v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Temperature Event Mitigation Policy Act or the</strong> <strong>TEMP Act </strong></p><p>This bill directs the federal crop insurance program to provide for research and development regarding a temperature-based index policy to insure crops (including\u00a0tomatoes, peppers, sugarcane, strawberries, melons, citrus, peaches, and blueberries) on a nationally-available basis against losses due to a frost or cold weather event.</p><p>The research and development must (1) evaluate the effectiveness of risk management tools with respect to low frequency and catastrophic loss weather events, and (2) result in a policy that provides protection for production loss or revenue loss.\u00a0</p><p>The term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.\u00a0Under an index policy, claim payments are generally triggered based on a predetermined index that is entirely independent of the individual farm operation (e.g., temperature level). Under such a policy, the payments are automatically triggered when the index reaches a certain level rather than when an insured farmer files a claim.\u00a0</p>"
        },
        "title": "TEMP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3843.xml",
    "summary": {
      "actionDate": "2026-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Temperature Event Mitigation Policy Act or the</strong> <strong>TEMP Act </strong></p><p>This bill directs the federal crop insurance program to provide for research and development regarding a temperature-based index policy to insure crops (including\u00a0tomatoes, peppers, sugarcane, strawberries, melons, citrus, peaches, and blueberries) on a nationally-available basis against losses due to a frost or cold weather event.</p><p>The research and development must (1) evaluate the effectiveness of risk management tools with respect to low frequency and catastrophic loss weather events, and (2) result in a policy that provides protection for production loss or revenue loss.\u00a0</p><p>The term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.\u00a0Under an index policy, claim payments are generally triggered based on a predetermined index that is entirely independent of the individual farm operation (e.g., temperature level). Under such a policy, the payments are automatically triggered when the index reaches a certain level rather than when an insured farmer files a claim.\u00a0</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s3843"
    },
    "title": "TEMP Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Temperature Event Mitigation Policy Act or the</strong> <strong>TEMP Act </strong></p><p>This bill directs the federal crop insurance program to provide for research and development regarding a temperature-based index policy to insure crops (including\u00a0tomatoes, peppers, sugarcane, strawberries, melons, citrus, peaches, and blueberries) on a nationally-available basis against losses due to a frost or cold weather event.</p><p>The research and development must (1) evaluate the effectiveness of risk management tools with respect to low frequency and catastrophic loss weather events, and (2) result in a policy that provides protection for production loss or revenue loss.\u00a0</p><p>The term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.\u00a0Under an index policy, claim payments are generally triggered based on a predetermined index that is entirely independent of the individual farm operation (e.g., temperature level). Under such a policy, the payments are automatically triggered when the index reaches a certain level rather than when an insured farmer files a claim.\u00a0</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s3843"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3843is.xml"
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
      "title": "TEMP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TEMP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T05:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Temperature Event Mitigation Policy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T05:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Crop Insurance Act to direct the Federal Crop Insurance Corporation to conduct research and development on frost or cold weather insurance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T04:33:30Z"
    }
  ]
}
```
