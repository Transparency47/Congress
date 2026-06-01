# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/149?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/149
- Title: Public Safety First Act
- Congress: 119
- Bill type: S
- Bill number: 149
- Origin chamber: Senate
- Introduced date: 2025-01-17
- Update date: 2025-08-25T22:01:25Z
- Update date including text: 2025-08-25T22:01:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-17: Introduced in Senate
- 2025-01-17 - IntroReferral: Introduced in Senate
- 2025-01-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-17: Introduced in Senate

## Actions

- 2025-01-17 - IntroReferral: Introduced in Senate
- 2025-01-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-17",
    "latestAction": {
      "actionDate": "2025-01-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/149",
    "number": "149",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Public Safety First Act",
    "type": "S",
    "updateDate": "2025-08-25T22:01:25Z",
    "updateDateIncludingText": "2025-08-25T22:01:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-17",
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
      "actionDate": "2025-01-17",
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
          "date": "2025-01-17T16:05:56Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s149is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 149\nIN THE SENATE OF THE UNITED STATES\nJanuary 17, 2025 Mr. Cornyn introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Secretary of Homeland Security to take into custody aliens who have been charged in the United States with theft, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Safety First Act .\n#### 2. Detention of certain aliens who commit theft\nSection 236(c) of the Immigration and Nationality Act ( 8 U.S.C. 1226(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (C), by striking or ;\n**(B)**\nin subparagraph (D), by striking the comma at the end and inserting , or ; and\n**(C)**\nby inserting after subparagraph (D) the following:\n(E) (i) is inadmissible under paragraph (6)(A), (6)(C), or (7) of section 212(a); and (ii) is charged with, is arrested for, is convicted of, admits having committed, or admits committing acts which constitute the essential elements of any burglary, theft, larceny, shoplifting, or assault of a law enforcement officer offense, or any crime that results in death or serious bodily injury to another person, ;\n**(2)**\nby redesignating paragraph (2) as paragraph (4); and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) Definition For purposes of paragraph (1)(E), the terms burglary , theft , larceny , shoplifting , assault of a law enforcement officer , and serious bodily injury have the meanings given such terms in the jurisdiction in which the acts occurred. (3) Detainer The Secretary of Homeland Security shall issue a detainer for an alien described in paragraph (1)(E) and, if the alien is not otherwise detained by Federal, State, or local officials, shall effectively and expeditiously take custody of the alien. .",
      "versionDate": "2025-01-17",
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
        "actionDate": "2025-01-29",
        "text": "Became Public Law No: 119-1."
      },
      "number": "5",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Laken Riley Act",
      "type": "S"
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
        "updateDate": "2025-02-20T19:11:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-17",
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
          "measure-id": "id119s149",
          "measure-number": "149",
          "measure-type": "s",
          "orig-publish-date": "2025-01-17",
          "originChamber": "SENATE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s149v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-01-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Public Safety First Act</strong></p><p>This bill requires the Department of Homeland Security (DHS) to detain certain non-U.S. nationals (<em>aliens</em> under federal law) who have been arrested for burglary, theft, larceny, or shoplifting. Specifically, DHS must detain an individual who (1) is unlawfully present in the United States or did not possess the necessary documents when applying for admission; and (2) has been charged with, arrested for, convicted of, or admits to having committed acts that constitute the essential elements of burglary, theft, larceny, or shoplifting.</p><ul></ul>"
        },
        "title": "Public Safety First Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s149.xml",
    "summary": {
      "actionDate": "2025-01-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Public Safety First Act</strong></p><p>This bill requires the Department of Homeland Security (DHS) to detain certain non-U.S. nationals (<em>aliens</em> under federal law) who have been arrested for burglary, theft, larceny, or shoplifting. Specifically, DHS must detain an individual who (1) is unlawfully present in the United States or did not possess the necessary documents when applying for admission; and (2) has been charged with, arrested for, convicted of, or admits to having committed acts that constitute the essential elements of burglary, theft, larceny, or shoplifting.</p><ul></ul>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s149"
    },
    "title": "Public Safety First Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Public Safety First Act</strong></p><p>This bill requires the Department of Homeland Security (DHS) to detain certain non-U.S. nationals (<em>aliens</em> under federal law) who have been arrested for burglary, theft, larceny, or shoplifting. Specifically, DHS must detain an individual who (1) is unlawfully present in the United States or did not possess the necessary documents when applying for admission; and (2) has been charged with, arrested for, convicted of, or admits to having committed acts that constitute the essential elements of burglary, theft, larceny, or shoplifting.</p><ul></ul>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s149"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s149is.xml"
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
      "title": "Public Safety First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T02:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public Safety First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Homeland Security to take into custody aliens who have been charged in the United States with theft, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:26Z"
    }
  ]
}
```
