# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/741?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/741
- Title: Protecting Mushroom Farmers Act
- Congress: 119
- Bill type: S
- Bill number: 741
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2025-05-02T19:11:25Z
- Update date including text: 2025-05-02T19:11:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/741",
    "number": "741",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
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
    "title": "Protecting Mushroom Farmers Act",
    "type": "S",
    "updateDate": "2025-05-02T19:11:25Z",
    "updateDateIncludingText": "2025-05-02T19:11:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T16:53:41Z",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s741is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 741\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Fetterman (for himself and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Crop Insurance Act to require research and development regarding a policy to insure the production of mushrooms.\n#### 1. Short title\nThis Act may be cited as the Protecting Mushroom Farmers Act .\n#### 2. Research and development authority\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended by adding at the end the following:\n(20) Mushrooms (A) In general The Corporation shall carry out research and development, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out research and development, regarding a policy to insure the production of mushrooms or revenue derived from the production of mushrooms. (B) Report Not later than 1 year after the date of enactment of this paragraph, the Corporation shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report that describes\u2014 (i) the results of the research and development carried out under subparagraph (A); and (ii) any recommendations with respect to those results. .",
      "versionDate": "2025-02-26",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-02T16:24:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119s741",
          "measure-number": "741",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s741v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Protecting Mushroom Farmers Act</b></p> <p>This bill requires the federal crop insurance program to provide for the research and development of a policy to insure the production of mushrooms or revenue derived from the production of mushrooms. (The term <i>policy</i> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.) </p>"
        },
        "title": "Protecting Mushroom Farmers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s741.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Protecting Mushroom Farmers Act</b></p> <p>This bill requires the federal crop insurance program to provide for the research and development of a policy to insure the production of mushrooms or revenue derived from the production of mushrooms. (The term <i>policy</i> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.) </p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s741"
    },
    "title": "Protecting Mushroom Farmers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Protecting Mushroom Farmers Act</b></p> <p>This bill requires the federal crop insurance program to provide for the research and development of a policy to insure the production of mushrooms or revenue derived from the production of mushrooms. (The term <i>policy</i> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.) </p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s741"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s741is.xml"
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
      "title": "Protecting Mushroom Farmers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Mushroom Farmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Crop Insurance Act to require research and development regarding a policy to insure the production of mushrooms.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:26Z"
    }
  ]
}
```
