# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/822?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/822
- Title: POST IT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 822
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-07-28T14:13:07Z
- Update date including text: 2025-07-28T14:13:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/822",
    "number": "822",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "POST IT Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-28T14:13:07Z",
    "updateDateIncludingText": "2025-07-28T14:13:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr822ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 822\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Van Drew (for himself and Ms. Scholten ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to require the Small Business and Agriculture Regulatory Enforcement Ombudsman to publish guidance documents for certain rules, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Opportunities to Show Transparency via Information Technology Act of 2025 or the POST IT Act of 2025 .\n#### 2. Inclusion of guidance on Ombudsman website\n##### (a) Website requirement\nSection 30 of the Small Business Act ( 15 U.S.C. 657 ) is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1), by striking and at the end;\n**(B)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following new paragraph:\n(3) to the extent practicable, hyperlinks for any guidance that is designed to set forth policy on a statutory, regulatory, or technical issue, or an interpretation of such issue, for any rule for which an agency produces a small entity compliance guide. ; and\n**(2)**\nby adding at the end the following new subsection:\n(g) Protection of confidential information Subsection (e) does not require the public availability of information that is exempt from public disclosure under section 552(b) of title 5, United States Code (commonly known as the Freedom of Information Act ). .\n##### (b) Applicability\nParagraph (3) of section 30(e) of the Small Business Act ( 15 U.S.C. 657 ), as added by this section, shall apply with respect to guidance on, or interpretation of, a rule for which an agency produces a small entity compliance guide described under section 212(a)(1) of the Small Business Regulatory Enforcement Fairness Act of 1996 ( 5 U.S.C. 601 note) on or after the date of the enactment of this Act.\n#### 3. Compliance with CUTGO\nNo additional amounts are authorized to be appropriated to carry out this Act or the amendments made by this Act.",
      "versionDate": "2025-01-28",
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
        "name": "Commerce",
        "updateDate": "2025-05-01T21:16:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr822",
          "measure-number": "822",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-07-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr822v00",
            "update-date": "2025-07-28"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Providing Opportunities to Show Transparency via Information Technology Act of 2025 or the POST IT Act of 2025</strong></p><p>This bill requires the Small Business Administration's Office of the National Ombudsman to include hyperlinks on its website to any guidance that sets forth policy related to a rule covered by a small entity compliance guide.</p><p>Generally, agencies must prepare a small entity compliance guide for rules that are expected to have a significant economic impact on a substantial number of small entities.</p>"
        },
        "title": "POST IT Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr822.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Providing Opportunities to Show Transparency via Information Technology Act of 2025 or the POST IT Act of 2025</strong></p><p>This bill requires the Small Business Administration's Office of the National Ombudsman to include hyperlinks on its website to any guidance that sets forth policy related to a rule covered by a small entity compliance guide.</p><p>Generally, agencies must prepare a small entity compliance guide for rules that are expected to have a significant economic impact on a substantial number of small entities.</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr822"
    },
    "title": "POST IT Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Providing Opportunities to Show Transparency via Information Technology Act of 2025 or the POST IT Act of 2025</strong></p><p>This bill requires the Small Business Administration's Office of the National Ombudsman to include hyperlinks on its website to any guidance that sets forth policy related to a rule covered by a small entity compliance guide.</p><p>Generally, agencies must prepare a small entity compliance guide for rules that are expected to have a significant economic impact on a substantial number of small entities.</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr822"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr822ih.xml"
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
      "title": "POST IT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POST IT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Opportunities to Show Transparency via Information Technology Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to require the Small Business and Agriculture Regulatory Enforcement Ombudsman to publish guidance documents for certain rules, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:45Z"
    }
  ]
}
```
