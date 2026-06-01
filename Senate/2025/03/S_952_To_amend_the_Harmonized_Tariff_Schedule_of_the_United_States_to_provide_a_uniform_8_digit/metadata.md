# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/952?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/952
- Title: A bill to amend the Harmonized Tariff Schedule of the United States to provide a uniform 8-digit subheading number for all whiskies.
- Congress: 119
- Bill type: S
- Bill number: 952
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-04-15T10:56:31Z
- Update date including text: 2026-04-15T10:56:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/952",
    "number": "952",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A bill to amend the Harmonized Tariff Schedule of the United States to provide a uniform 8-digit subheading number for all whiskies.",
    "type": "S",
    "updateDate": "2026-04-15T10:56:31Z",
    "updateDateIncludingText": "2026-04-15T10:56:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
            "date": "2025-03-11T20:29:02Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-11T20:29:02Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MI"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "KY"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "WV"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "AR"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "SC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "TN"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s952is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 952\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Cassidy (for himself, Mr. Peters , and Mr. McConnell ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Harmonized Tariff Schedule of the United States to provide a uniform 8-digit subheading number for all whiskies.\n#### 1. Uniform duty treatment of whiskies\n##### (a) In general\nChapter 22 of the Harmonized Tariff Schedule of the United States is amended by striking subheadings 2208.30, 2208.30.30, and 2208.30.60 and inserting the following, with the article description for subheading 2208.30.00 having the same degree of indentation as the article description for subheading 2208.50.00:\n2208.30.00 Whiskies Free $2.04/pf liter .\n##### (b) Instruction to United States International Trade Commission\nThe United States International Trade Commission shall add statistical suffixes to subheading 2208.30.00 of the Harmonized Tariff Schedule of the United States, as amended by subsection (a), as follows:\n2208.30.0010 Irish or Scotch in containers each holding not over 4 liters 2208.30.0015 Irish or Scotch in containers each holding over 4 liters 2208.30.0020 Bourbon in containers each holding not over 4 liters 2208.30.0025 Bourbon in containers each holding over 4 liters 2208.30.0030 Rye in containers each holding not over 4 liters 2208.30.0035 Rye in containers each holding over 4 liters 2208.30.0040 Other in containers each holding not over 4 liters 2208.30.0045 Other in containers each holding over 4 liters. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to articles entered, or withdrawn from warehouse for consumption, on or after the date that is 15 days after the date of the enactment of this Act.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-04-24",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3028",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Duty Drawback Clarification Act",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-12T18:03:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s952",
          "measure-number": "952",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2025-06-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s952v00",
            "update-date": "2025-06-25"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill revises Chapter 22 of the Harmonized Tariff Schedule of the United States to provide a uniform rate of duty for all whiskies.</p>"
        },
        "title": "A bill to amend the Harmonized Tariff Schedule of the United States to provide a uniform 8-digit subheading number for all whiskies."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s952.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill revises Chapter 22 of the Harmonized Tariff Schedule of the United States to provide a uniform rate of duty for all whiskies.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119s952"
    },
    "title": "A bill to amend the Harmonized Tariff Schedule of the United States to provide a uniform 8-digit subheading number for all whiskies."
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill revises Chapter 22 of the Harmonized Tariff Schedule of the United States to provide a uniform rate of duty for all whiskies.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119s952"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s952is.xml"
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
      "title": "A bill to amend the Harmonized Tariff Schedule of the United States to provide a uniform 8-digit subheading number for all whiskies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:11Z"
    },
    {
      "title": "A bill to amend the Harmonized Tariff Schedule of the United States to provide a uniform 8-digit subheading number for all whiskies.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T10:56:22Z"
    }
  ]
}
```
