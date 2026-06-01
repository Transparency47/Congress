# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/417?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/417
- Title: End U.N. Censorship Act
- Congress: 119
- Bill type: HR
- Bill number: 417
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-02-28T17:45:11Z
- Update date including text: 2025-02-28T17:45:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/417",
    "number": "417",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "End U.N. Censorship Act",
    "type": "HR",
    "updateDate": "2025-02-28T17:45:11Z",
    "updateDateIncludingText": "2025-02-28T17:45:11Z"
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
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
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
          "date": "2025-01-15T15:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TN"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr417ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 417\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Cline (for himself, Mr. Cloud , and Mr. Ogles ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit the use of United States contributions to the United Nations to support the iVerify tool developed by the United Nations Development Programme, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End U.N. Censorship Act .\n#### 2. Prohibition\n##### (a) In general\nNo Federal funds made available to the Department of State or any other department or agency may be used\u2014\n**(1)**\nto develop, implement, or otherwise support the iVerify tool developed by the United Nations Development Programme;\n**(2)**\nfor any other effort that seeks to label speech or expression as mal-, mis-, or dis-information;\n**(3)**\nto make any voluntary contributions to the United Nations or any entity of the United Nations that\u2014\n**(A)**\nfund, implement, develop, or otherwise support the iVerify platform or any similar platform; or\n**(B)**\notherwise support initiatives that seek to label speech or expression as mal-, mis-, or disinformation; or\n**(4)**\nto make any contribution to any other international organization for the purposes of funding, implementing, developing, or otherwise supporting the iVerify platform or any similar effort that seeks to label speech or expression as mal-, mis-, or disinformation.\n##### (b) Rescission\nAny amounts withheld pursuant to this section\u2014\n**(1)**\nshall be permanently rescinded as of the date on which the Secretary makes the determination described in subsection (a)(1);\n**(2)**\nshall be deposited in the general fund of the Treasury; and\n**(3)**\nshall not be considered arrears to be repaid to the United Nations or any entity of the United Nations.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-02-20T14:12:34Z"
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
          "measure-id": "id119hr417",
          "measure-number": "417",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr417v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>End U.N. Censorship Act</strong></p><p>This bill specifies that no federal funds may be made available to support the iVerify tool (a fact-checking tool developed by the United Nations Development Programme) or any other effort that seeks to label speech or expression as mal-, mis-, or dis-information.</p>"
        },
        "title": "End U.N. Censorship Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr417.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End U.N. Censorship Act</strong></p><p>This bill specifies that no federal funds may be made available to support the iVerify tool (a fact-checking tool developed by the United Nations Development Programme) or any other effort that seeks to label speech or expression as mal-, mis-, or dis-information.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr417"
    },
    "title": "End U.N. Censorship Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End U.N. Censorship Act</strong></p><p>This bill specifies that no federal funds may be made available to support the iVerify tool (a fact-checking tool developed by the United Nations Development Programme) or any other effort that seeks to label speech or expression as mal-, mis-, or dis-information.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr417"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr417ih.xml"
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
      "title": "End U.N. Censorship Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T11:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End U.N. Censorship Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of United States contributions to the United Nations to support the iVerify tool developed by the United Nations Development Programme, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T11:03:28Z"
    }
  ]
}
```
