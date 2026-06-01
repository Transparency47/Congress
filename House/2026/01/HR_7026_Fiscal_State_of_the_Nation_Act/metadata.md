# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7026?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7026
- Title: Fiscal State of the Nation Act
- Congress: 119
- Bill type: HR
- Bill number: 7026
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-05-14T08:08:33Z
- Update date including text: 2026-05-14T08:08:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Rules.
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Rules.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7026",
    "number": "7026",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Fiscal State of the Nation Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:33Z",
    "updateDateIncludingText": "2026-05-14T08:08:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NC"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NV"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "TN"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NE"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "OK"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "GU"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7026ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7026\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Barr (for himself and Mr. Peters ) introduced the following bill; which was referred to the Committee on Rules\nA BILL\nProviding for a joint hearing of the Committees on the Budget of the House of Representatives and the Senate to receive a presentation from the Comptroller General of the United States regarding the audited financial statement of the executive branch.\n#### 1. Short title\nThis Act may be cited as the Fiscal State of the Nation Act .\n#### 2. Annual joint hearing of Budget Committees to receive a presentation by the Comptroller General\n##### (a) In general\nNot later than 45 days (excluding Saturdays, Sundays, and holidays) after the date on which the Secretary of the Treasury submits to Congress the audited financial statement required under paragraph (1) of section 331(e) of title 31, United States Code, on a date agreed upon by the chairs of the Committees on the Budget of the House of Representatives and the Senate (hereafter referred to as the Budget Committees ) and the Comptroller General of the United States, the chairs shall conduct a joint hearing to receive a presentation from the Comptroller General reviewing the findings of the audit required under paragraph (2) of such section and providing, with respect to the information included by the Secretary in the report accompanying such audited financial statement, an analysis of the financial position and condition of the Federal Government, including financial measures (such as the net operating cost, income, budget deficits, or budget surpluses) and sustainability measures (such as the long-term fiscal projection or social insurance projection) described in such report.\n##### (b) Presentation of statement in accordance with GAO Strategies and Means\nThe Comptroller General of the United States shall ensure that the presentation at the joint hearing conducted under subsection (a) is made in accordance with the Strategies and Means of the Government Accountability Office, so that the presentation will provide professional, objective, fact-based, nonpartisan, nonideological, fair, and balanced information to the members attending the hearing.\n##### (c) Rules applicable to hearing\n**(1) In general**\nThe joint hearing conducted by the chairs of Budget Committees under subsection (a) shall be conducted in accordance with the Rules of the House of Representatives and the applicable Standing Rules of the Senate which apply to such a hearing, including the provisions requiring hearings conducted by committees to be open to the public, including to radio, television, and still photography coverage.\n**(2) Permitting participation by Senators and Members not serving on Budget Committees**\nNotwithstanding any provision of the Rules of the House of Representatives or the Standing Rules of the Senate, any Senator and any Member of the House of Representatives (including a Delegate or Resident Commissioner to the Congress) may participate in the joint hearing in the same manner and to the same extent as a Senator or Member of the House of Representatives who is a member of either of the Budget Committees.\n##### (d) Effective date\nThe requirement under subsection (a) shall apply with respect to any audited financial statement submitted on or after the date of the enactment of this Act.",
      "versionDate": "2026-01-13",
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
        "name": "Economics and Public Finance",
        "updateDate": "2026-01-26T17:22:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-13",
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
          "measure-id": "id119hr7026",
          "measure-number": "7026",
          "measure-type": "hr",
          "orig-publish-date": "2026-01-13",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7026v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2026-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fiscal State of the Nation Act</strong></p><p>This bill requires the congressional budget committees to conduct an annual joint hearing to receive a presentation from the Comptroller General regarding (1) the Government Accountability Office's audit of the financial statement of the executive branch, and (2) the financial position and condition of the federal government.</p>"
        },
        "title": "Fiscal State of the Nation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7026.xml",
    "summary": {
      "actionDate": "2026-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fiscal State of the Nation Act</strong></p><p>This bill requires the congressional budget committees to conduct an annual joint hearing to receive a presentation from the Comptroller General regarding (1) the Government Accountability Office's audit of the financial statement of the executive branch, and (2) the financial position and condition of the federal government.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr7026"
    },
    "title": "Fiscal State of the Nation Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fiscal State of the Nation Act</strong></p><p>This bill requires the congressional budget committees to conduct an annual joint hearing to receive a presentation from the Comptroller General regarding (1) the Government Accountability Office's audit of the financial statement of the executive branch, and (2) the financial position and condition of the federal government.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr7026"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7026ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for a joint hearing of the Committees on the Budget of the House of Representatives and the Senate to receive a presentation from the Comptroller General of the United States regarding the audited financial statement of the executive branch.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T14:18:24Z"
    },
    {
      "title": "Fiscal State of the Nation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T14:14:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fiscal State of the Nation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T14:14:37Z"
    }
  ]
}
```
