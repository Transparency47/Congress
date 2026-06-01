# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/257?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/257
- Title: SEC Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 257
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-02-28T18:44:20Z
- Update date including text: 2025-02-28T18:44:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Financial Services.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/257",
    "number": "257",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "SEC Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-28T18:44:20Z",
    "updateDateIncludingText": "2025-02-28T18:44:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-09T14:40:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr257ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 257\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mrs. Bice introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Exchange Act of 1934 to prohibit the Securities and Exchange Commission from requiring an issuer to make climate-related disclosures that are not material to investors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Environmental Calculations Act of 2025 or the SEC Act of 2025 .\n#### 2. Prohibition on requiring an issuer to make climate-related disclosures that are not material to investors\nSection 23 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78w ) is amended by adding at the end the following:\n(e) Prohibition on requiring an issuer To make climate-Related disclosures that are not material to investors The Commission may not require an issuer to make climate-related disclosures that are not material to investors. .",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in House"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-02-06T20:22:25Z"
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
    "originChamber": "House",
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
          "measure-id": "id119hr257",
          "measure-number": "257",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr257v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Environmental Calculations Act of 2025 or the SEC Act of 2025 </strong></p><p>This bill prohibits the Securities and Exchange Commission from requiring issuers of securities to make climate-related disclosures that are not material to investors.</p>"
        },
        "title": "SEC Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr257.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Environmental Calculations Act of 2025 or the SEC Act of 2025 </strong></p><p>This bill prohibits the Securities and Exchange Commission from requiring issuers of securities to make climate-related disclosures that are not material to investors.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr257"
    },
    "title": "SEC Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Environmental Calculations Act of 2025 or the SEC Act of 2025 </strong></p><p>This bill prohibits the Securities and Exchange Commission from requiring issuers of securities to make climate-related disclosures that are not material to investors.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr257"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr257ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SEC Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEC Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Environmental Calculations Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Exchange Act of 1934 to prohibit the Securities and Exchange Commission from requiring an issuer to make climate-related disclosures that are not material to investors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:23Z"
    }
  ]
}
```
