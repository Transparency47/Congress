# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/713?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/713
- Title: Broadband Buildout Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 713
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-12-05T22:01:42Z
- Update date including text: 2025-12-05T22:01:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/713",
    "number": "713",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
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
    "title": "Broadband Buildout Accountability Act",
    "type": "S",
    "updateDate": "2025-12-05T22:01:42Z",
    "updateDateIncludingText": "2025-12-05T22:01:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T17:53:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "WY"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "UT"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "AK"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MS"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "IN"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s713is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 713\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Scott of Florida (for himself, Mr. Barrasso , Mrs. Blackburn , Mr. Curtis , Mr. Sullivan , Mr. Wicker , and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo apply the Freedom of Information Act to actions and decisions of the Assistant Secretary of Commerce for Communications and Information in carrying out the Broadband Equity, Access, and Deployment Program.\n#### 1. Short title\nThis Act may be cited as the Broadband Buildout Accountability Act .\n#### 2. Applicability of FOIA to the Broadband Equity, Access, and Deployment Program\nSection 60102(o)(2) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(o)(2) ) is amended by inserting after Act\u2019) the following: , except for section 552 of that title (commonly referred to as the Freedom of Information Act ) .",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-02-25",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1579",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Broadband Buildout Accountability Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-07T13:22:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119s713",
          "measure-number": "713",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-07-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s713v00",
            "update-date": "2025-07-03"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Broadband Buildout Accountability Act</strong></p> <p>This bill makes actions or decisions of the National Telecommunications and Information Administration concerning the Broadband Equity, Access, and Deployment Program subject to the Freedom of Information Act, which governs the release of federal documents.</p>"
        },
        "title": "Broadband Buildout Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s713.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Broadband Buildout Accountability Act</strong></p> <p>This bill makes actions or decisions of the National Telecommunications and Information Administration concerning the Broadband Equity, Access, and Deployment Program subject to the Freedom of Information Act, which governs the release of federal documents.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119s713"
    },
    "title": "Broadband Buildout Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Broadband Buildout Accountability Act</strong></p> <p>This bill makes actions or decisions of the National Telecommunications and Information Administration concerning the Broadband Equity, Access, and Deployment Program subject to the Freedom of Information Act, which governs the release of federal documents.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119s713"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s713is.xml"
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
      "title": "Broadband Buildout Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Broadband Buildout Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to apply the Freedom of Information Act to actions and decisions of the Assistant Secretary of Commerce for Communications and Information in carrying out the Broadband Equity, Access, and Deployment Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:20Z"
    }
  ]
}
```
