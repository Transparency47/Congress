# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/399?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/399
- Title: Protecting Our Supreme Court Justices Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 399
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2025-12-05T22:52:23Z
- Update date including text: 2025-12-05T22:52:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/399",
    "number": "399",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Protecting Our Supreme Court Justices Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:52:23Z",
    "updateDateIncludingText": "2025-12-05T22:52:23Z"
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
          "date": "2025-02-04T22:47:08Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "UT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AR"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s399is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 399\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mrs. Blackburn (for herself, Mr. Cruz , Mr. Lee , Mrs. Hyde-Smith , and Mr. Cotton ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 1507 of title 18, United States Code, to establish appropriate penalties for obstruction of justice by picketing or parading in or near court buildings or residences of judges, jurors, witnesses, or other court officers.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Supreme Court Justices Act of 2025 .\n#### 2. Obstruction of justice by picketing or parading\nSection 1507 of title 18, United States Code, is amended, in the first undesignated paragraph, by striking one year and inserting 5 years .",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-04-08",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2724",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Our Supreme Court Justices Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-04-14T17:44:03Z"
          },
          {
            "name": "First Amendment rights",
            "updateDate": "2025-04-14T17:43:50Z"
          },
          {
            "name": "Judges",
            "updateDate": "2025-04-14T17:43:40Z"
          },
          {
            "name": "Protest and dissent",
            "updateDate": "2025-04-14T17:43:55Z"
          },
          {
            "name": "Supreme Court",
            "updateDate": "2025-04-14T17:43:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-03-10T11:47:17Z"
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
          "measure-id": "id119s399",
          "measure-number": "399",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-06-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s399v00",
            "update-date": "2025-06-04"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Our Supreme Court Justices Act of 2025 </strong></p><p>This bill increases the statutory maximum prison term\u2014from one year to five years\u2014for picketing or parading in or near a building or residence used by a judge, juror, witness, or court officer with the intent of interfering with, obstructing, or impeding the administration of justice, or with the intent of influencing a judge, juror, witness, or court officer, in the discharge of his or her duty.\u00a0</p>"
        },
        "title": "Protecting Our Supreme Court Justices Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s399.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Our Supreme Court Justices Act of 2025 </strong></p><p>This bill increases the statutory maximum prison term\u2014from one year to five years\u2014for picketing or parading in or near a building or residence used by a judge, juror, witness, or court officer with the intent of interfering with, obstructing, or impeding the administration of justice, or with the intent of influencing a judge, juror, witness, or court officer, in the discharge of his or her duty.\u00a0</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119s399"
    },
    "title": "Protecting Our Supreme Court Justices Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Our Supreme Court Justices Act of 2025 </strong></p><p>This bill increases the statutory maximum prison term\u2014from one year to five years\u2014for picketing or parading in or near a building or residence used by a judge, juror, witness, or court officer with the intent of interfering with, obstructing, or impeding the administration of justice, or with the intent of influencing a judge, juror, witness, or court officer, in the discharge of his or her duty.\u00a0</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119s399"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s399is.xml"
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
      "title": "Protecting Our Supreme Court Justices Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T02:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Our Supreme Court Justices Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 1507 of title 18, United States Code, to establish appropriate penalties for obstruction of justice by picketing or parading in or near court buildings or residences of judges, jurors, witnesses, or other court officers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T02:48:19Z"
    }
  ]
}
```
