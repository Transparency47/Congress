# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/42?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/42
- Title: Build the Wall Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 42
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-12-05T22:50:02Z
- Update date including text: 2025-12-05T22:50:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/42",
    "number": "42",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Build the Wall Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:50:02Z",
    "updateDateIncludingText": "2025-12-05T22:50:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T19:36:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "OK"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WY"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "KS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ID"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s42is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 42\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Barrasso (for himself, Mr. Lankford , Ms. Lummis , Mr. Marshall , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo establish the Southern Border Wall Construction Fund and to transfer unobligated amounts from the Coronavirus State and local fiscal recovery funds to such Fund to construct and maintain physical barriers along the southern border.\n#### 1. Short title\nThis Act may be cited as the Build the Wall Act of 2025 .\n#### 2. Southern Border Wall Construction Fund\n##### (a) Establishment\nThere is established in the general fund of the Treasury a separate account, which shall be known as the Southern Border Wall Construction Fund (referred to in this section as the Fund ).\n##### (b) Deposits\nNotwithstanding any other provision of law, there shall be immediately deposited into the Fund all of the unobligated amounts in the Coronavirus State and local fiscal recovery funds established under sections 602 and 603 of the Social Security Act (42 U.S.C. 802 and 803).\n##### (c) Use of funds\nAmounts in the Fund shall be used by the Secretary of Homeland Security to construct and maintain physical barriers along the southern international border of the United States.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the Subcommittee on Border Security and Enforcement."
      },
      "number": "816",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Build the Wall Act of 2025",
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
        "name": "Immigration",
        "updateDate": "2025-02-10T17:15:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119s42",
          "measure-number": "42",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s42v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Build the Wall Act of 2025</strong></p><p>This bill establishes the Southern Border Wall Construction Fund to be used by the Department of Homeland Security to construct and maintain physical barriers along the U.S.-Mexico border. All unobligated amounts in the Coronavirus State and Local Fiscal Recovery Funds must be immediately deposited in the Southern Border Wall Construction Fund.</p>"
        },
        "title": "Build the Wall Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s42.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Build the Wall Act of 2025</strong></p><p>This bill establishes the Southern Border Wall Construction Fund to be used by the Department of Homeland Security to construct and maintain physical barriers along the U.S.-Mexico border. All unobligated amounts in the Coronavirus State and Local Fiscal Recovery Funds must be immediately deposited in the Southern Border Wall Construction Fund.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119s42"
    },
    "title": "Build the Wall Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Build the Wall Act of 2025</strong></p><p>This bill establishes the Southern Border Wall Construction Fund to be used by the Department of Homeland Security to construct and maintain physical barriers along the U.S.-Mexico border. All unobligated amounts in the Coronavirus State and Local Fiscal Recovery Funds must be immediately deposited in the Southern Border Wall Construction Fund.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119s42"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s42is.xml"
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
      "title": "Build the Wall Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Build the Wall Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Southern Border Wall Construction Fund and to transfer unobligated amounts from the Coronavirus State and local fiscal recovery funds to such Fund to construct and maintain physical barriers along the southern border.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:36Z"
    }
  ]
}
```
