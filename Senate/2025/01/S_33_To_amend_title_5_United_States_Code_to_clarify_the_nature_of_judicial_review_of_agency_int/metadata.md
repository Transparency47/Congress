# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/33?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/33
- Title: SOPRA
- Congress: 119
- Bill type: S
- Bill number: 33
- Origin chamber: Senate
- Introduced date: 2025-01-08
- Update date: 2025-05-07T12:45:28Z
- Update date including text: 2025-05-07T12:45:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-08: Introduced in Senate
- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-08: Introduced in Senate

## Actions

- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-08",
    "latestAction": {
      "actionDate": "2025-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/33",
    "number": "33",
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
    "title": "SOPRA",
    "type": "S",
    "updateDate": "2025-05-07T12:45:28Z",
    "updateDateIncludingText": "2025-05-07T12:45:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-08",
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
      "actionDate": "2025-01-08",
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
          "date": "2025-01-08T18:36:16Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "ND"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "KY"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "IA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "TN"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "AL"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s33is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 33\nIN THE SENATE OF THE UNITED STATES\nJanuary 8, 2025 Mr. Schmitt (for himself, Mr. Cruz , Mr. Cramer , Mr. Paul , Ms. Ernst , Mr. Budd , Mrs. Blackburn , Mrs. Britt , and Mr. Hagerty ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to clarify the nature of judicial review of agency interpretations of statutory and regulatory provisions.\n#### 1. Short title\nThis Act may be cited as the Separation of Powers Restoration Act of 2025 or SOPRA .\n#### 2. Judicial review of statutory and regulatory interpretations\nSection 706 of title 5, United States Code, is amended\u2014\n**(1)**\nby striking To the extent necessary and inserting (a) To the extent necessary ;\n**(2)**\nin subsection (a), as so designated\u2014\n**(A)**\nby striking decide all relevant questions of law, interpret constitutional and statutory provisions, and ;\n**(B)**\nby inserting after of the terms of an agency action the following and decide de novo all relevant questions of law, including the interpretation of constitutional and statutory provisions, rules made by agencies, and interpretative rules, general statements of policy, and all other agency guidance documents. Notwithstanding any other provision of law, this subsection shall apply in any action for judicial review of agency action authorized under any provision of law. No law may exempt any such civil action from the application of this section except by specific reference to this section ; and\n**(3)**\nby striking The reviewing court shall\u2014 and inserting the following:\n(b) The reviewing court shall\u2014 ; and\n**(4)**\nby striking In making the foregoing determinations and inserting the following:\n(c) In making the foregoing determinations .",
      "versionDate": "2025-01-08",
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
        "actionDate": "2025-02-26",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1605",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Separation of Powers Restoration Act of 2025",
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
        "name": "Law",
        "updateDate": "2025-05-01T20:32:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-08",
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
          "measure-id": "id119s33",
          "measure-number": "33",
          "measure-type": "s",
          "orig-publish-date": "2025-01-08",
          "originChamber": "SENATE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s33v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-01-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Separation of Powers Restoration Act</strong> <strong>of 2025 or SOPRA</strong></p><p>This bill modifies the scope of judicial review of agency actions to authorize courts reviewing agency actions to decide de novo (i.e., without giving deference to the agency's interpretation) all relevant questions of law, including the interpretation of (1) constitutional and statutory provisions, (2) rules made by agencies, (3) interpretative rules, (4) general statements of policy, and (5) all other agency guidance documents.</p><p>No law may exempt a civil action from the standard of review required by this bill except by specific reference to such provision.</p>"
        },
        "title": "SOPRA"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s33.xml",
    "summary": {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Separation of Powers Restoration Act</strong> <strong>of 2025 or SOPRA</strong></p><p>This bill modifies the scope of judicial review of agency actions to authorize courts reviewing agency actions to decide de novo (i.e., without giving deference to the agency's interpretation) all relevant questions of law, including the interpretation of (1) constitutional and statutory provisions, (2) rules made by agencies, (3) interpretative rules, (4) general statements of policy, and (5) all other agency guidance documents.</p><p>No law may exempt a civil action from the standard of review required by this bill except by specific reference to such provision.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s33"
    },
    "title": "SOPRA"
  },
  "summaries": [
    {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Separation of Powers Restoration Act</strong> <strong>of 2025 or SOPRA</strong></p><p>This bill modifies the scope of judicial review of agency actions to authorize courts reviewing agency actions to decide de novo (i.e., without giving deference to the agency's interpretation) all relevant questions of law, including the interpretation of (1) constitutional and statutory provisions, (2) rules made by agencies, (3) interpretative rules, (4) general statements of policy, and (5) all other agency guidance documents.</p><p>No law may exempt a civil action from the standard of review required by this bill except by specific reference to such provision.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s33"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s33is.xml"
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
      "title": "SOPRA",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T12:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SOPRA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Separation of Powers Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to clarify the nature of judicial review of agency interpretations of statutory and regulatory provisions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:28Z"
    }
  ]
}
```
