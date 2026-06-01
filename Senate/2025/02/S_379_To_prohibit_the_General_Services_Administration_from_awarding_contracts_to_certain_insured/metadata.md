# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/379
- Title: No Red and Blue Banks Act
- Congress: 119
- Bill type: S
- Bill number: 379
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2025-07-25T18:38:25Z
- Update date including text: 2025-07-25T18:38:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/379",
    "number": "379",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "No Red and Blue Banks Act",
    "type": "S",
    "updateDate": "2025-07-25T18:38:25Z",
    "updateDateIncludingText": "2025-07-25T18:38:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:48:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s379is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 379\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Kennedy (for himself and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit the General Services Administration from awarding contracts to certain insured depository institutions that avoid doing business with certain companies that are engaged in lawful commerce based solely on social policy considerations.\n#### 1. Short title\nThis Act may be cited as the No Red and Blue Banks Act .\n#### 2. Insured depository institutions\n##### (a) In general\nThe General Services Administration may not award a contract to an insured depository institution, as defined in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ), or an affiliate of a depository institution if the insured depository institution or affiliate avoids doing business with certain companies that the insured depository institution or affiliate believes are engaged in lawful commerce based solely on social policy considerations.\n##### (b) Applicability\nThis Act shall not apply to any contract awarded before the date of enactment of this Act.",
      "versionDate": "2025-02-04",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-07T14:41:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119s379",
          "measure-number": "379",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s379v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>No Red and Blue Banks Act</strong></p><p>This bill prohibits the General Services Administration from awarding a contract to a depository institution insured by the Federal Deposit Insurance Corporation if the institution avoids doing business with companies based solely on social policy considerations.</p>"
        },
        "title": "No Red and Blue Banks Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s379.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Red and Blue Banks Act</strong></p><p>This bill prohibits the General Services Administration from awarding a contract to a depository institution insured by the Federal Deposit Insurance Corporation if the institution avoids doing business with companies based solely on social policy considerations.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s379"
    },
    "title": "No Red and Blue Banks Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Red and Blue Banks Act</strong></p><p>This bill prohibits the General Services Administration from awarding a contract to a depository institution insured by the Federal Deposit Insurance Corporation if the institution avoids doing business with companies based solely on social policy considerations.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s379"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s379is.xml"
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
      "title": "No Red and Blue Banks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Red and Blue Banks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the General Services Administration from awarding contracts to certain insured depository institutions that avoid doing business with certain companies that are engaged in lawful commerce based solely on social policy considerations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:33Z"
    }
  ]
}
```
