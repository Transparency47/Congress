# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/418?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/418
- Title: Ensuring Accountability in Agency Rulemaking Act
- Congress: 119
- Bill type: HR
- Bill number: 418
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-06-24T08:05:39Z
- Update date including text: 2025-06-24T08:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/418",
    "number": "418",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Ensuring Accountability in Agency Rulemaking Act",
    "type": "HR",
    "updateDate": "2025-06-24T08:05:39Z",
    "updateDateIncludingText": "2025-06-24T08:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "ME"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WY"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "OK"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WI"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TN"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "FL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr418ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 418\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Cline (for himself, Mr. Golden of Maine , Ms. Hageman , Mr. Ellzey , Mr. Crenshaw , Mr. Brecheen , Mr. Fitzgerald , and Mr. Green of Tennessee ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the head of an agency to issue and sign any rule issued by that agency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Accountability in Agency Rulemaking Act .\n#### 2. Rulemaking requirements\n##### (a) Approval required\n**(1) Rules promulgated by Senate confirmed appointee**\nExcept as provided in paragraph (3), any rule promulgated under section 553 of title 5, United States Code, shall be issued and signed by an individual appointed by the President, by and with the advice and consent of the Senate.\n**(2) Initiation of Rulemaking and regulatory agenda**\nExcept as provided in paragraph (3), any rule initiated under section 553 of title 5, United States Code, shall be initiated by a senior appointee.\n**(3) Exception**\nParagraph (1) or (2) does not apply if the head of an agency\u2014\n**(A)**\ndetermines, on a nondelegable basis, that compliance with the relevant paragraph would impede public safety or security;\n**(B)**\nsubmits to the Administrator a notification disclosing the reasons for the exemption; and\n**(C)**\npublishes such notification, consistent with public safety, security, and privacy interests, in the Federal Register.\n##### (b) Oversight\n**(1) Agency compliance**\nThe head of each agency shall ensure that the issuance of any agency rule promulgated under section 553 of title 5, United States Code, adheres to the requirements of this section.\n**(2) OIRA guidance and compliance**\nThe Administrator shall provide guidance on the implementation of and shall monitor agency compliance with this section.\n##### (c) Rules of construction\nThis section may not be construed to impair or otherwise affect the functions of the Director of the Office of Management and Budget relating to budgetary, administrative, or legislative proposals.\n##### (d) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Office of Information and Regulatory Affairs (OIRA) in the Office of Management and Budget (OMB).\n**(2) Agency**\nThe term agency has the meaning given that term under section 551 of title 5, United States Code.\n**(3) Rule**\nThe term rule has the meaning given that term in section 551 of title 5, United States Code, and does not include any rule of agency organization, procedure, or practice that does not substantially affect the rights or obligations of non-agency parties.\n**(4) Senior appointee**\nThe term senior appointee means an individual appointed by the President, or performing the functions and duties of an office that requires appointment by the President, or a non-career member of the Senior Executive Service (or equivalent agency system).",
      "versionDate": "2025-01-15",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-06T16:49:41Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-03-06T16:49:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-28T19:43:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr418",
          "measure-number": "418",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-05-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr418v00",
            "update-date": "2025-05-01"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ensuring Accountability in Agency Rulemaking Act</strong></p><p>This bill requires, subject to a limited exception, that any agency rule promulgated under notice and comment procedures must be (1) initiated by a senior appointee (e.g., an individual who was appointed by the President or is a non-career member of the Senior Executive Service), and\u00a0(2) issued and signed by an individual who was appointed by the President and confirmed by the Senate.</p><p>The Office of Information and Regulatory Affairs must issue guidance for agencies to implement this requirement.</p>"
        },
        "title": "Ensuring Accountability in Agency Rulemaking Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr418.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring Accountability in Agency Rulemaking Act</strong></p><p>This bill requires, subject to a limited exception, that any agency rule promulgated under notice and comment procedures must be (1) initiated by a senior appointee (e.g., an individual who was appointed by the President or is a non-career member of the Senior Executive Service), and\u00a0(2) issued and signed by an individual who was appointed by the President and confirmed by the Senate.</p><p>The Office of Information and Regulatory Affairs must issue guidance for agencies to implement this requirement.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119hr418"
    },
    "title": "Ensuring Accountability in Agency Rulemaking Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring Accountability in Agency Rulemaking Act</strong></p><p>This bill requires, subject to a limited exception, that any agency rule promulgated under notice and comment procedures must be (1) initiated by a senior appointee (e.g., an individual who was appointed by the President or is a non-career member of the Senior Executive Service), and\u00a0(2) issued and signed by an individual who was appointed by the President and confirmed by the Senate.</p><p>The Office of Information and Regulatory Affairs must issue guidance for agencies to implement this requirement.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119hr418"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr418ih.xml"
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
      "title": "Ensuring Accountability in Agency Rulemaking Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Accountability in Agency Rulemaking Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the head of an agency to issue and sign any rule issued by that agency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T03:03:19Z"
    }
  ]
}
```
