# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/79?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/79
- Title: ACCESS Act
- Congress: 119
- Bill type: S
- Bill number: 79
- Origin chamber: Senate
- Introduced date: 2025-01-13
- Update date: 2025-12-05T22:01:32Z
- Update date including text: 2025-12-05T22:01:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in Senate
- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-13: Introduced in Senate

## Actions

- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/79",
    "number": "79",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "ACCESS Act",
    "type": "S",
    "updateDate": "2025-12-05T22:01:32Z",
    "updateDateIncludingText": "2025-12-05T22:01:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T23:28:16Z",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s79is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 79\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Lankford (for himself and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 41, United States Code, to prohibit minimum educational requirements for proposed contractor personnel in certain contract solicitations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Allowing Contractors to Choose Employees for Select Skills Act or the ACCESS Act .\n#### 2. Use of requirements regarding education of contractor personnel\n##### (a) Flexibility in contractor education requirements\nChapter 33 of title 41, United States Code, is amended by adding at the end the following new section:\n3313. Flexibility in contractor education requirements (a) Prohibition A solicitation may not set forth any minimum education requirement for proposed contractor personnel in order for a bidder to be eligible for award of a contract unless the contracting officer includes in the solicitation a written justification that explains why the needs of the executive agency cannot be met without any such requirement and clarifies how the requirement ensures the needs are met. (b) Executive agency defined In this section, the term executive agency has the meaning given that term in section 133 of this title. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 33 of title 41, United States Code, is amended by adding at the end the following new item:\n3313. Flexibility in contractor education requirements. .\n##### (c) OMB guidance\nNot later than 180 days after the date of the enactment of this Act, the Director of the Office of Management and Budget shall issue guidance to the heads of executive agencies for implementing the amendment made by subsection (a) that includes the following:\n**(1)**\nInstructions for contracting officers for the justifications under section 3313(a) of title 41, United States Code, as added by subsection (a), including a requirement that each use of an education requirement be determined, justified, and reviewed.\n**(2)**\nInstructions for contracting officers that encourages the use of alternatives to education requirements.\n##### (d) Applicability\nThe amendments made by this section shall apply with respect to solicitations issued on or after the date that is 15 months after the date of the enactment of this Act.\n##### (e) Repeal\nSection 813 of the Floyd D. Spence National Defense Authorization Act for Fiscal Year 2001 ( Public Law 106\u2013398 ; 114 Stat. 1654A\u2013214), as implemented in subpart 39.104 of the Federal Acquisition Regulation, as in effect on January 3, 2025, is repealed as of the date that the guidance required by subsection (c) becomes effective.\n##### (f) GAO report\nNot later than 3 years after the date of the enactment of this Act, the Comptroller General shall submit to Congress an evaluation of executive agency compliance with section 3313 of title 41, United States Code, as added by subsection (a).\n##### (g) Definitions\nIn this section:\n**(1) Education**\nThe term education means an associate, baccalaureate, graduate, or professional degree, specified coursework, or other form of educational attainment awarded by a junior or community college, college, or university that is accredited as a collegiate institution by a recognized accrediting agency or approved by the appropriate State education authority under State law to grant associate or higher degrees.\n**(2) Education requirement**\nThe term education requirement includes a requirement that can be met either through\u2014\n**(A)**\neducation alone;\n**(B)**\neducation or experience; or\n**(C)**\na combination of education and experience.\n**(3) Executive agency**\nThe term executive agency has the meaning given that term in section 133 of title 41, United States Code.",
      "versionDate": "2025-01-13",
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
        "actionDate": "2025-12-02",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0."
      },
      "number": "5235",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Skills-Based Federal Contracting Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-02-24T19:40:53Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-24T19:40:53Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-02-24T19:40:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-20T15:08:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119s79",
          "measure-number": "79",
          "measure-type": "s",
          "orig-publish-date": "2025-01-13",
          "originChamber": "SENATE",
          "update-date": "2025-07-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s79v00",
            "update-date": "2025-07-02"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Allowing Contractors to Choose Employees for Select Skills Act or the ACCESS Act</strong></p><p>This bill prohibits federal contract bid solicitations for contractor personnel from including minimum educational requirements unless the contracting officer justifies the requirements.\u00a0The prohibition applies to educational requirements that may be met through education alone, education or experience, or a combination of education and experience.</p><p>The bill also requires the Office of Management and Budget to issue implementing guidance to federal agencies, including instructions for contracting officers that encourage using alternatives to education requirements.</p>"
        },
        "title": "ACCESS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s79.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Allowing Contractors to Choose Employees for Select Skills Act or the ACCESS Act</strong></p><p>This bill prohibits federal contract bid solicitations for contractor personnel from including minimum educational requirements unless the contracting officer justifies the requirements.\u00a0The prohibition applies to educational requirements that may be met through education alone, education or experience, or a combination of education and experience.</p><p>The bill also requires the Office of Management and Budget to issue implementing guidance to federal agencies, including instructions for contracting officers that encourage using alternatives to education requirements.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119s79"
    },
    "title": "ACCESS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Allowing Contractors to Choose Employees for Select Skills Act or the ACCESS Act</strong></p><p>This bill prohibits federal contract bid solicitations for contractor personnel from including minimum educational requirements unless the contracting officer justifies the requirements.\u00a0The prohibition applies to educational requirements that may be met through education alone, education or experience, or a combination of education and experience.</p><p>The bill also requires the Office of Management and Budget to issue implementing guidance to federal agencies, including instructions for contracting officers that encourage using alternatives to education requirements.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119s79"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s79is.xml"
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
      "title": "ACCESS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ACCESS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Allowing Contractors to Choose Employees for Select Skills Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 41, United States Code, to prohibit minimum educational requirements for proposed contractor personnel in certain contract solicitations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:36Z"
    }
  ]
}
```
