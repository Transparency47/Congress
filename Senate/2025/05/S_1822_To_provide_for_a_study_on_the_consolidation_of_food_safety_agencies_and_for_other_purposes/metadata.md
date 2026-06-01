# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1822?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1822
- Title: SAFE FOOD Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1822
- Origin chamber: Senate
- Introduced date: 2025-05-20
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-20: Introduced in Senate
- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-20: Introduced in Senate

## Actions

- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1822",
    "number": "1822",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "SAFE FOOD Act of 2025",
    "type": "S",
    "updateDate": "2026-05-12T11:03:31Z",
    "updateDateIncludingText": "2026-05-12T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
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
      "actionDate": "2025-05-20",
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
        "item": [
          {
            "date": "2025-05-20T21:53:09Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-20T21:53:09Z",
            "name": "Referred To"
          }
        ]
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
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1822is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1822\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo provide for a study on the consolidation of food safety agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Study And Framework for Efficiency in Food Oversight and Organizational Design Act of 2025 or the SAFE FOOD Act of 2025 .\n#### 2. Study on consolidation of food safety agencies\n##### (a) Study\nNot later than 60 days after the date of enactment of this Act, the Secretary of Agriculture shall conduct a study on the consolidation of Federal agencies with a primary role in ensuring food safety in the United States (including the Food Safety and Inspection Service, the Food and Drug Administration, and Centers for Disease Control and Prevention) into a single agency.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary of Agriculture shall submit to the appropriate committees of Congress a report containing\u2014\n**(1)**\nthe results of the study; and\n**(2)**\nany recommendations of the Secretary of Agriculture with respect to the consolidation.",
      "versionDate": "2025-05-20",
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
        "updateDate": "2025-06-10T23:22:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-20",
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
          "measure-id": "id119s1822",
          "measure-number": "1822",
          "measure-type": "s",
          "orig-publish-date": "2025-05-20",
          "originChamber": "SENATE",
          "update-date": "2026-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1822v00",
            "update-date": "2026-04-24"
          },
          "action-date": "2025-05-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Study And Framework for Efficiency in Food Oversight and Organizational Design Act of 2025 or the SAFE FOOD Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to conduct a study and submit a report to Congress on the consolidation of federal food safety agencies into a single agency.</p><p>Federal agencies that currently have a role in food safety include the Food Safety and Inspection Service, which is part of the USDA, and the Food and Drug Administration and the Centers for Disease Control and Prevention, which are part of the Department of Health and Human Services.</p>"
        },
        "title": "SAFE FOOD Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1822.xml",
    "summary": {
      "actionDate": "2025-05-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Study And Framework for Efficiency in Food Oversight and Organizational Design Act of 2025 or the SAFE FOOD Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to conduct a study and submit a report to Congress on the consolidation of federal food safety agencies into a single agency.</p><p>Federal agencies that currently have a role in food safety include the Food Safety and Inspection Service, which is part of the USDA, and the Food and Drug Administration and the Centers for Disease Control and Prevention, which are part of the Department of Health and Human Services.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119s1822"
    },
    "title": "SAFE FOOD Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Study And Framework for Efficiency in Food Oversight and Organizational Design Act of 2025 or the SAFE FOOD Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to conduct a study and submit a report to Congress on the consolidation of federal food safety agencies into a single agency.</p><p>Federal agencies that currently have a role in food safety include the Food Safety and Inspection Service, which is part of the USDA, and the Food and Drug Administration and the Centers for Disease Control and Prevention, which are part of the Department of Health and Human Services.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119s1822"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1822is.xml"
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
      "title": "SAFE FOOD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE FOOD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Study And Framework for Efficiency in Food Oversight and Organizational Design Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for a study on the consolidation of food safety agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T01:03:35Z"
    }
  ]
}
```
