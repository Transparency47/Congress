# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1453?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1453
- Title: Clean Energy Demonstration Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1453
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-05-19 15:33:07 - Floor: Mr. Babin moved to suspend the rules and pass the bill.
- 2025-05-19 15:33:22 - Floor: Considered under suspension of the rules. (consideration: CR H2115-2116)
- 2025-05-19 15:33:23 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1453.
- 2025-05-19 15:42:06 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H2115)
- 2025-05-19 15:42:06 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H2115)
- 2025-05-19 15:42:08 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-05-20 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-05-19 15:33:07 - Floor: Mr. Babin moved to suspend the rules and pass the bill.
- 2025-05-19 15:33:22 - Floor: Considered under suspension of the rules. (consideration: CR H2115-2116)
- 2025-05-19 15:33:23 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1453.
- 2025-05-19 15:42:06 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H2115)
- 2025-05-19 15:42:06 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H2115)
- 2025-05-19 15:42:08 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-05-20 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1453",
    "number": "1453",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Clean Energy Demonstration Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-05-19",
      "actionTime": "15:42:08",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-05-19",
      "actionTime": "15:42:06",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H2115)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-05-19",
      "actionTime": "15:42:06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H2115)",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-05-19",
      "actionTime": "15:33:23",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 1453.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-05-19",
      "actionTime": "15:33:22",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H2115-2116)",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-05-19",
      "actionTime": "15:33:07",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mr. Babin moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-05-20T19:40:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-21T20:33:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1453ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1453\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Carey (for himself and Mr. Riley of New York ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to require reporting regarding clean energy demonstration projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Energy Demonstration Transparency Act of 2025 .\n#### 2. Project management and oversight reporting requirements\nSubsection (h) of section 41201 of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18861 ) is amended by adding at the end following new paragraph:\n(3) Further reports (A) In general Not later than six months after the date of the enactment of this paragraph and at least semiannually thereafter, the Secretary shall submit to the Committee on Science, Space, and Technology and the Committee on Appropriations of the House of Representatives and the Committee on Energy and Natural Resources and the Committee on Appropriations of the Senate a report, and make publicly available in digital online format, that contains, for the period covered by each such report, for each covered project or other demonstration project administered or supported by the program, the following: (i) A copy of any initial contracts or financial assistance agreements executed between the Department and an award recipient, including any related documentation, as the Secretary determines appropriate. (ii) A list of any material, technical, or financial milestones that have or have not been met. (iii) Any material modifications to the scope, schedule, funding profile (including cost-share requirements), project partners or participating entities, or budget of the project. (B) Streamlining To the extent practicable, the Secretary may synchronize the reports required under subparagraph (A) with other required reports, such as those required under\u2014 (i) paragraph (1); and (ii) section 9005(e) of the Energy Act of 2020 ( 42 U.S.C. 7256c(e) ; enacted as division Z of the Consolidated Appropriations Act, 2021). .",
      "versionDate": "2025-02-21",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1453rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 1453\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2025 Received; read twice and referred to the Committee on Energy and Natural Resources\nAN ACT\nTo amend the Infrastructure Investment and Jobs Act to require reporting regarding clean energy demonstration projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Energy Demonstration Transparency Act of 2025 .\n#### 2. Project management and oversight reporting requirements\nSubsection (h) of section 41201 of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18861 ) is amended by adding at the end following new paragraph:\n(3) Further reports (A) In general Not later than six months after the date of the enactment of this paragraph and at least semiannually thereafter, the Secretary shall submit to the Committee on Science, Space, and Technology and the Committee on Appropriations of the House of Representatives and the Committee on Energy and Natural Resources and the Committee on Appropriations of the Senate a report, and make publicly available in digital online format, that contains, for the period covered by each such report, for each covered project or other demonstration project administered or supported by the program, the following: (i) A copy of any initial contracts or financial assistance agreements executed between the Department and an award recipient, including any related documentation, as the Secretary determines appropriate. (ii) A list of any material, technical, or financial milestones that have or have not been met. (iii) Any material modifications to the scope, schedule, funding profile (including cost-share requirements), project partners or participating entities, or budget of the project. (B) Streamlining To the extent practicable, the Secretary may synchronize the reports required under subparagraph (A) with other required reports, such as those required under\u2014 (i) paragraph (1); and (ii) section 9005(e) of the Energy Act of 2020 ( 42 U.S.C. 7256c(e) ; enacted as division Z of the Consolidated Appropriations Act, 2021). .",
      "versionDate": "",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1453eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1453\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo amend the Infrastructure Investment and Jobs Act to require reporting regarding clean energy demonstration projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Energy Demonstration Transparency Act of 2025 .\n#### 2. Project management and oversight reporting requirements\nSubsection (h) of section 41201 of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18861 ) is amended by adding at the end following new paragraph:\n(3) Further reports (A) In general Not later than six months after the date of the enactment of this paragraph and at least semiannually thereafter, the Secretary shall submit to the Committee on Science, Space, and Technology and the Committee on Appropriations of the House of Representatives and the Committee on Energy and Natural Resources and the Committee on Appropriations of the Senate a report, and make publicly available in digital online format, that contains, for the period covered by each such report, for each covered project or other demonstration project administered or supported by the program, the following: (i) A copy of any initial contracts or financial assistance agreements executed between the Department and an award recipient, including any related documentation, as the Secretary determines appropriate. (ii) A list of any material, technical, or financial milestones that have or have not been met. (iii) Any material modifications to the scope, schedule, funding profile (including cost-share requirements), project partners or participating entities, or budget of the project. (B) Streamlining To the extent practicable, the Secretary may synchronize the reports required under subparagraph (A) with other required reports, such as those required under\u2014 (i) paragraph (1); and (ii) section 9005(e) of the Energy Act of 2020 ( 42 U.S.C. 7256c(e) ; enacted as division Z of the Consolidated Appropriations Act, 2021). .",
      "versionDate": "",
      "versionType": "Engrossed in House"
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
            "name": "Alternative and renewable resources",
            "updateDate": "2025-05-20T15:31:06Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2025-05-20T15:31:21Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-20T15:30:56Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-20T15:30:49Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-05-20T15:30:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-18T14:34:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1453",
          "measure-number": "1453",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1453v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Clean Energy Demonstration Transparency Act of 2025</strong></p><p>This bill directs the Department of Energy (DOE) to submit and publish online semiannual reports on the status of certain clean energy demonstration projects that are managed or supported by DOE's Office of Clean Energy Demonstrations.</p>"
        },
        "title": "Clean Energy Demonstration Transparency Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1453.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Clean Energy Demonstration Transparency Act of 2025</strong></p><p>This bill directs the Department of Energy (DOE) to submit and publish online semiannual reports on the status of certain clean energy demonstration projects that are managed or supported by DOE's Office of Clean Energy Demonstrations.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr1453"
    },
    "title": "Clean Energy Demonstration Transparency Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Clean Energy Demonstration Transparency Act of 2025</strong></p><p>This bill directs the Department of Energy (DOE) to submit and publish online semiannual reports on the status of certain clean energy demonstration projects that are managed or supported by DOE's Office of Clean Energy Demonstrations.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr1453"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1453ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1453rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1453eh.xml"
        }
      ],
      "type": "Engrossed in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Clean Energy Demonstration Transparency Act of 2025",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Clean Energy Demonstration Transparency Act of 2025",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "title": "Clean Energy Demonstration Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clean Energy Demonstration Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Infrastructure Investment and Jobs Act to require reporting regarding clean energy demonstration projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:37Z"
    }
  ]
}
```
