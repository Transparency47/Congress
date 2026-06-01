# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/67?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/67
- Title: Censorship Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 67
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/67",
    "number": "67",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Censorship Accountability Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
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
          "date": "2025-01-09T21:47:44Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s67is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 67\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Schmitt introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide for a right of action against Federal employees for violations of rights secured by the First Amendment to the Constitution of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Censorship Accountability Act .\n#### 2. Right of action against Federal employees for violations of rights secured by the First Amendment to the Constitution of the United States\n##### (a) Definition\nIn this section, the term Federal employee means an individual, other than the President or the Vice President, who occupies a position in any agency or instrumentality in the executive branch of the Federal Government, including in any independent agency in that branch.\n##### (b) Liability\n**(1) In general**\nA Federal employee who, under color of any statute, ordinance, regulation, custom, or usage, of the United States, subjects, or causes to be subjected, any citizen of the United States or any person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the First Amendment to the Constitution of the United States, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.\n**(2) Exception**\nUnder paragraph (1), a Federal employee may not bring suit against the agency or instrumentality employing the Federal employee, or against the Federal Government, for conduct that is within the scope of the employment relationship.\n##### (c) Attorney\u2019s fees\nIn any action or proceeding to enforce this section, the court, in the discretion of the court, may allow the prevailing party, other than the United States, a reasonable attorney\u2019s fee as part of the costs.\n##### (d) Severability\nIf any provision of this section, or the application of a provision of this section to any person or circumstance, is held to be unconstitutional, the remainder of this section, and the application of the provisions of this section to any person or circumstance, shall not be affected by that holding.",
      "versionDate": "2025-01-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-02-24T20:28:39Z"
          },
          {
            "name": "First Amendment rights",
            "updateDate": "2025-02-24T20:28:39Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-02-24T20:28:39Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-02-24T20:28:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-02-08T14:51:47Z"
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
          "measure-id": "id119s67",
          "measure-number": "67",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s67v00",
            "update-date": "2025-05-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Censorship Accountability Act</strong></p><p>This bill creates a new federal cause of action for the deprivation of any rights, privileges, or immunities secured by the First Amendment by a federal employee acting under color of any statute, ordinance, custom, or usage of the United States.</p><p>The term <em>federal employee</em> means an individual, other than the President or Vice President, who occupies a position in the Executive Branch.</p>"
        },
        "title": "Censorship Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s67.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Censorship Accountability Act</strong></p><p>This bill creates a new federal cause of action for the deprivation of any rights, privileges, or immunities secured by the First Amendment by a federal employee acting under color of any statute, ordinance, custom, or usage of the United States.</p><p>The term <em>federal employee</em> means an individual, other than the President or Vice President, who occupies a position in the Executive Branch.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119s67"
    },
    "title": "Censorship Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Censorship Accountability Act</strong></p><p>This bill creates a new federal cause of action for the deprivation of any rights, privileges, or immunities secured by the First Amendment by a federal employee acting under color of any statute, ordinance, custom, or usage of the United States.</p><p>The term <em>federal employee</em> means an individual, other than the President or Vice President, who occupies a position in the Executive Branch.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119s67"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s67is.xml"
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
      "title": "Censorship Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Censorship Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill for a right of action against Federal employees for violations of rights secured by the First Amendment to the Constitution of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:37Z"
    }
  ]
}
```
