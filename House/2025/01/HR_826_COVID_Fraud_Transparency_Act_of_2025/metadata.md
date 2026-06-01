# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/826?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/826
- Title: COVID Fraud Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 826
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-05-21T08:08:52Z
- Update date including text: 2026-05-21T08:08:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 23 - 0.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 23 - 0.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/826",
    "number": "826",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "W000816",
        "district": "25",
        "firstName": "Roger",
        "fullName": "Rep. Williams, Roger [R-TX-25]",
        "lastName": "Williams",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "COVID Fraud Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:52Z",
    "updateDateIncludingText": "2026-05-21T08:08:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 23 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
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
        "item": [
          {
            "date": "2026-05-20T21:44:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-28T16:11:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr826ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 826\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Williams of Texas (for himself, Mr. Latimer , Mr. Bean of Florida , and Mr. Mfume ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo require the Inspector General of the Small Business Administration to submit a quarterly report on fraud relating to certain COVID\u201319 loans.\n#### 1. Short title\nThis Act may be cited as the COVID Fraud Transparency Act of 2025 .\n#### 2. Report on fraud relating to certain COVID\u201319 loans\n##### (a) In general\nNot later than 60 days after the date of the enactment of this Act, and every 3 months thereafter, the Inspector General of the Small Business Administration shall submit to the Committee on Small Business of the House of Representatives and the Committee on Small Business and Entrepreneurship of the Senate a report on the number of borrowers engaged in fraud with respect to a covered loan.\n##### (b) Elements\nThe report required under subsection (a) shall include, with respect to the period covered by such report\u2014\n**(1)**\nthe number and total dollar amount of all covered loans made;\n**(2)**\nthe number of new cases of fraud and suspected fraud;\n**(3)**\nthe number of fraud cases resolved; and\n**(4)**\nthe types of fraud cases described in paragraphs (2) and (3).\n##### (c) Covered loan defined\nIn this section, the term covered loan means\u2014\n**(1)**\na loan made under paragraph (36) or (37) of section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ); or\n**(2)**\na loan made under section 7(b) of such Act ( 15 U.S.C. 636(b) ) in response to COVID\u201319 during the covered period (as defined in section 1110(a) of the CARES Act ( 15 U.S.C. 9009 )).\n##### (d) Termination\nThis Act and the requirements of this Act shall terminate on the date that is two years after the date of the enactment of this Act.\n#### 3. Compliance with CUTGO\nNo additional amounts are authorized to be appropriated to carry out this Act.",
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
        "updateDate": "2025-03-01T17:12:16Z"
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
          "measure-id": "id119hr826",
          "measure-number": "826",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr826v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>COVID Fraud Transparency Act of 2025</strong></p><p>This bill requires the Small Business Administration's Office of Inspector General to report quarterly about fraud cases involving certain COVID-19 loans (e.g., Paycheck Protection Program loans).</p>"
        },
        "title": "COVID Fraud Transparency Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr826.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>COVID Fraud Transparency Act of 2025</strong></p><p>This bill requires the Small Business Administration's Office of Inspector General to report quarterly about fraud cases involving certain COVID-19 loans (e.g., Paycheck Protection Program loans).</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr826"
    },
    "title": "COVID Fraud Transparency Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>COVID Fraud Transparency Act of 2025</strong></p><p>This bill requires the Small Business Administration's Office of Inspector General to report quarterly about fraud cases involving certain COVID-19 loans (e.g., Paycheck Protection Program loans).</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr826"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr826ih.xml"
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
      "title": "COVID Fraud Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COVID Fraud Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Inspector General of the Small Business Administration to submit a quarterly report on fraud relating to certain COVID-19 loans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:44Z"
    }
  ]
}
```
