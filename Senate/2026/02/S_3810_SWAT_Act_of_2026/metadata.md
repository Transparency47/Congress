# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3810?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3810
- Title: SWAT Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3810
- Origin chamber: Senate
- Introduced date: 2026-02-09
- Update date: 2026-05-20T11:03:29Z
- Update date including text: 2026-05-20T11:03:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-09: Introduced in Senate
- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-02-09: Introduced in Senate

## Actions

- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3810",
    "number": "3810",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "SWAT Act of 2026",
    "type": "S",
    "updateDate": "2026-05-20T11:03:29Z",
    "updateDateIncludingText": "2026-05-20T11:03:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T23:14:18Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "ME"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "GA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "OR"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3810is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3810\nIN THE SENATE OF THE UNITED STATES\nFebruary 9, 2026 Mr. Peters (for himself, Ms. Collins , Mr. Ossoff , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Plant Protection Act to establish a fund for spotted wing drosophila research and mitigation.\n#### 1. Short title\nThis Act may be cited as the Spotted Wing Abatement Trust Act of 2026 or the SWAT Act of 2026 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe spotted wing drosophila, an invasive species from East Asia, has caused significant damage to many valuable fruit crops in the United States, including raspberries, blackberries, blueberries, strawberries, peaches, plums, and cherries; and\n**(2)**\nthe Department of Agriculture estimates that spotted wing drosophila account for a combined 20 percent revenue loss across strawberry, blueberry, raspberry, blackberry, and cherry crops, based on reported yield losses due to that species.\n#### 3. Spotted wing drosophila research and mitigation\nSubtitle A of the Plant Protection Act ( 7 U.S.C. 7711 et seq. ) is amended by adding at the end the following:\n420A. Spotted wing drosophila research and mitigation (a) In general The Administrator of the Animal and Plant Health Inspection Service (referred to in this section as the Administrator ) shall establish a fund within the Department of Agriculture to fund research relating to, and activities to mitigate the negative effects of, spotted wing drosophila. (b) Administration of fund The Administrator shall\u2014 (1) determine eligible recipients to enter into cooperative agreements with, or award grants to, using amounts in the fund established under subsection (a); and (2) oversee the activities carried out using amounts in that fund. (c) Authorization of appropriations There is authorized to be appropriated for the fund established under subsection (a) $6,500,000 for the fiscal year in which the Spotted Wing Abatement Trust Act of 2026 is enacted and each of the 4 fiscal years thereafter. .",
      "versionDate": "2026-02-09",
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
        "updateDate": "2026-02-27T16:29:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-09",
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
          "measure-id": "id119s3810",
          "measure-number": "3810",
          "measure-type": "s",
          "orig-publish-date": "2026-02-09",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3810v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2026-02-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Spotted Wing Abatement Trust Act of 2026 or the SWAT Act of 2026</strong></p><p>This bill directs the Animal and Plant Health Inspection Service to establish a fund for research relating to, and activities to mitigate the negative effects of, spotted wing drosophila. Spotted wing drosophila is an invasive species of insect from East Asia that has caused significant damage to unripe berry and stone fruit crops in the United States, including raspberries, blackberries, blueberries, strawberries, peaches, plums, and cherries.</p>"
        },
        "title": "SWAT Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3810.xml",
    "summary": {
      "actionDate": "2026-02-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Spotted Wing Abatement Trust Act of 2026 or the SWAT Act of 2026</strong></p><p>This bill directs the Animal and Plant Health Inspection Service to establish a fund for research relating to, and activities to mitigate the negative effects of, spotted wing drosophila. Spotted wing drosophila is an invasive species of insect from East Asia that has caused significant damage to unripe berry and stone fruit crops in the United States, including raspberries, blackberries, blueberries, strawberries, peaches, plums, and cherries.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s3810"
    },
    "title": "SWAT Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-02-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Spotted Wing Abatement Trust Act of 2026 or the SWAT Act of 2026</strong></p><p>This bill directs the Animal and Plant Health Inspection Service to establish a fund for research relating to, and activities to mitigate the negative effects of, spotted wing drosophila. Spotted wing drosophila is an invasive species of insect from East Asia that has caused significant damage to unripe berry and stone fruit crops in the United States, including raspberries, blackberries, blueberries, strawberries, peaches, plums, and cherries.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s3810"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3810is.xml"
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
      "title": "SWAT Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SWAT Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Spotted Wing Abatement Trust Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Plant Protection Act to establish a fund for spotted wing drosophila research and mitigation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T03:48:23Z"
    }
  ]
}
```
