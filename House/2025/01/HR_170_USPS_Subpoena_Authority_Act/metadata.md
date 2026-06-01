# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/170?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/170
- Title: USPS Subpoena Authority Act
- Congress: 119
- Bill type: HR
- Bill number: 170
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-05-16T08:06:06Z
- Update date including text: 2025-05-16T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/170",
    "number": "170",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "USPS Subpoena Authority Act",
    "type": "HR",
    "updateDate": "2025-05-16T08:06:06Z",
    "updateDateIncludingText": "2025-05-16T08:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:26:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "NY"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NJ"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr170ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 170\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Ms. Malliotakis (for herself, Ms. Meng , and Mr. Smith of New Jersey ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 39, United States Code, to enhance the administrative subpoena authority of the United States Postal Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the USPS Subpoena Authority Act .\n#### 2. United States Postal Service administrative subpoena authority\nSection 3016(a)(1) of title 39, United States Code, is amended\u2014\n**(1)**\nby redesignating subparagraph (B) as subparagraph (D);\n**(2)**\nby striking subparagraph (A) and inserting the following:\n(A) In general In any investigation relating to a covered offense, the Postmaster General may issue in writing and cause to be served a subpoena requiring the production and testimony described in subparagraph (B). In this subparagraph, the term covered offense means a violation of\u2014 (i) any section in this chapter; (ii) any section of chapter 83 of title 18 insofar as such violation involves the use of the mails; (iii) any other provision of law enumerated in section 3001(a); or (iv) the Controlled Substances Act ( 21 U.S.C. 801 et seq. ), insofar as such violation involves the use of the mails. (B) Production and testimony Except as provided in subparagraph (C), a subpoena issued under subparagraph (A) may require\u2014 (i) the production of any records (including books, papers, documents, and other tangible things that constitute or contain evidence) that the Postmaster General considers relevant or material to such investigation; and (ii) testimony by the custodian of the things required to be produced concerning the production and authenticity of those things. (C) Application A subpoena issued in connection with an investigation under section 3005(a) shall not require testimony as set forth in subparagraph (B)(ii). ; and\n**(3)**\nin subparagraph (D), as redesignated by paragraph (1) of this section, by amending clause (iii) to read as follows:\n(iii) delegation of subpoena approval authority be limited to the Postal Service\u2019s General Counsel, a Deputy General Counsel, or the Chief Postal Inspector. .",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-02-24T16:54:12Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2025-02-24T16:54:07Z"
          },
          {
            "name": "U.S. Postal Service",
            "updateDate": "2025-02-24T16:54:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-19T15:49:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr170",
          "measure-number": "170",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-04-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr170v00",
            "update-date": "2025-04-23"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>USPS Subpoena Authority Act</strong></p><p>This bill expands the administrative subpoena authority of the U.S. Postal Service (USPS).</p><p>Specifically, the bill authorizes subpoenas to investigate additional violations of law that involve the mail, including violations related to controlled substances and hazardous materials.</p><p>The bill also expands the senior USPS officials to whom subpoena approval authority may be delegated to include the Chief Postal Inspector.</p>"
        },
        "title": "USPS Subpoena Authority Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr170.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>USPS Subpoena Authority Act</strong></p><p>This bill expands the administrative subpoena authority of the U.S. Postal Service (USPS).</p><p>Specifically, the bill authorizes subpoenas to investigate additional violations of law that involve the mail, including violations related to controlled substances and hazardous materials.</p><p>The bill also expands the senior USPS officials to whom subpoena approval authority may be delegated to include the Chief Postal Inspector.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119hr170"
    },
    "title": "USPS Subpoena Authority Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>USPS Subpoena Authority Act</strong></p><p>This bill expands the administrative subpoena authority of the U.S. Postal Service (USPS).</p><p>Specifically, the bill authorizes subpoenas to investigate additional violations of law that involve the mail, including violations related to controlled substances and hazardous materials.</p><p>The bill also expands the senior USPS officials to whom subpoena approval authority may be delegated to include the Chief Postal Inspector.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119hr170"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr170ih.xml"
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
      "title": "USPS Subpoena Authority Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USPS Subpoena Authority Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 39, United States Code, to enhance the administrative subpoena authority of the United States Postal Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:18:17Z"
    }
  ]
}
```
