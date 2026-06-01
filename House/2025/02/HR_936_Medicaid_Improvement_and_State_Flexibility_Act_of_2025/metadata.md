# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/936?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/936
- Title: Medicaid Improvement and State Flexibility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 936
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-03-10T19:14:58Z
- Update date including text: 2025-03-10T19:14:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/936",
    "number": "936",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000590",
        "district": "7",
        "firstName": "Mark",
        "fullName": "Rep. Green, Mark E. [R-TN-7]",
        "lastName": "Green",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Medicaid Improvement and State Flexibility Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-10T19:14:58Z",
    "updateDateIncludingText": "2025-03-10T19:14:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr936ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 936\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Green of Tennessee (for himself and Mr. Brecheen ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XI of the Social Security Act to provide for State approval and implementation of specified waivers under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Medicaid Improvement and State Flexibility Act of 2025 .\n#### 2. Providing for State approval and implementation of specified waivers under the Medicaid program\nSection 1115 of the Social Security Act ( 42 U.S.C. 1315 ) is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by striking An application and inserting Subject to paragraph (4), an application ; and\n**(B)**\nby adding at the end the following new paragraph:\n(4) (A) An experimental, pilot, or demonstration project undertaken under subsection (a) may be approved or renewed by a State if such project is described in subparagraph (B). (B) An experimental, pilot, or demonstration project is described in this subparagraph if such project provides for a waiver of requirements with respect to a State plan (or a waiver of such plan) under title XIX such that\u2014 (i) individuals enrolled under such plan (or such waiver) may elect to participate in such project with respect to a year; (ii) such individuals who elect to so participate\u2014 (I) are furnished with an electronic benefits transfer card in an amount determined appropriate by the State for purposes of purchasing primary care services and medications during such year; (II) are furnished a cash payment by the State equal to the amount of funds remaining on the individual\u2019s electronic benefits transfer card at the end of such year; and (III) are enrolled in a catastrophic insurance program determined appropriate by the State for purposes of covering services not described in subclause (I) and covering services that are described in such subclause if such individual exceeds the amount of funds provided to such individual on such card for such year; and (iii) Federal expenditures under such title for the period during which such project is in effect are equal to or lesser than what such expenditures would have been during such period if such project were not in effect. (C) (i) In no case may a project described in subparagraph (B) result in an expenditure to pay for any abortion or to assist in the purchase, in whole or in part, of health benefit coverage that includes coverage of abortion. (ii) Clause (i) shall not apply to an abortion only if necessary to save the life of the mother or if the pregnancy is the result of an act of rape or incest. (D) For purposes of a State\u2019s approval or renewal of an experimental, pilot, or demonstration project under subparagraph (A), each reference to the Secretary in subsection (a) shall be deemed to be a reference to the State . ; and\n**(2)**\nin subsection (e), by inserting (other than such a project that is described in paragraph (4)(B)) before the period at the end.",
      "versionDate": "2025-02-04",
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
        "name": "Health",
        "updateDate": "2025-03-07T15:50:02Z"
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
          "measure-id": "id119hr936",
          "measure-number": "936",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr936v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Medicaid Improvement and State Flexibility Act of 2025</strong><strong></strong></p><p>This bill authorizes states to approve their own experimental, pilot, or demonstration project under Medicaid if the project provides certain benefits involving electronic benefits transfer (EBT) cards. (Currently, the Centers for Medicare & Medicaid Services approves Medicaid demonstration projects; such projects are also known as <em>Section 1115 Demonstrations</em>.)</p><p>Specifically, the project must provide enrollees who elect to participate with an EBT card to purchase primary care services; enrollees must receive any remaining balance at the end of the year in the form of a cash payment and must also obtain catastrophic health insurance.</p>"
        },
        "title": "Medicaid Improvement and State Flexibility Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr936.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid Improvement and State Flexibility Act of 2025</strong><strong></strong></p><p>This bill authorizes states to approve their own experimental, pilot, or demonstration project under Medicaid if the project provides certain benefits involving electronic benefits transfer (EBT) cards. (Currently, the Centers for Medicare & Medicaid Services approves Medicaid demonstration projects; such projects are also known as <em>Section 1115 Demonstrations</em>.)</p><p>Specifically, the project must provide enrollees who elect to participate with an EBT card to purchase primary care services; enrollees must receive any remaining balance at the end of the year in the form of a cash payment and must also obtain catastrophic health insurance.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr936"
    },
    "title": "Medicaid Improvement and State Flexibility Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid Improvement and State Flexibility Act of 2025</strong><strong></strong></p><p>This bill authorizes states to approve their own experimental, pilot, or demonstration project under Medicaid if the project provides certain benefits involving electronic benefits transfer (EBT) cards. (Currently, the Centers for Medicare & Medicaid Services approves Medicaid demonstration projects; such projects are also known as <em>Section 1115 Demonstrations</em>.)</p><p>Specifically, the project must provide enrollees who elect to participate with an EBT card to purchase primary care services; enrollees must receive any remaining balance at the end of the year in the form of a cash payment and must also obtain catastrophic health insurance.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr936"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr936ih.xml"
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
      "title": "Medicaid Improvement and State Flexibility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicaid Improvement and State Flexibility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XI of the Social Security Act to provide for State approval and implementation of specified waivers under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:58Z"
    }
  ]
}
```
