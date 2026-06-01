# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1771?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1771
- Title: Improper Payments Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 1771
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2025-10-04T08:05:28Z
- Update date including text: 2025-10-04T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1771",
    "number": "1771",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "Y000067",
        "district": "2",
        "firstName": "Rudy",
        "fullName": "Rep. Yakym, Rudy [R-IN-2]",
        "lastName": "Yakym",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Improper Payments Transparency Act",
    "type": "HR",
    "updateDate": "2025-10-04T08:05:28Z",
    "updateDateIncludingText": "2025-10-04T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:08:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "MI"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1771ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1771\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Yakym (for himself, Mr. Panetta , Mr. Bergman , and Mr. Peters ) introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo amend title 31, United States Code, to include information on improper payments under Federal programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improper Payments Transparency Act .\n#### 2. Including improper payment information in Presidents budget submission\nSection 1105(a) of title 31, United States Code, is amended by adding at the end the following:\n(40) information with respect to improper payment (as such term is defined in section 3351) amounts and rates for programs and activities at each executive agency required to submit improper payment reports under subchapter IV of chapter 33, including\u2014 (A) a narrative description, including a detailed explanation with respect to why any improper payment amounts and rates occurred and trends of\u2014 (i) each program and activity whose improper payment amount and rates have increased or decreased on average over the previous three years; and (ii) each program and activity whose improper payment amount and rates did not change over such years; and (B) what corrective actions, including any such action in any corrective action plan under section 3352(d), with respect to such programs and activities are incomplete, and steps the executive agency will take to address improper payment amount and rate issues. .",
      "versionDate": "2025-03-03",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "747",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improper Payments Transparency Act",
      "type": "S"
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
        "updateDate": "2025-05-06T15:54:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119hr1771",
          "measure-number": "1771",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2025-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1771v00",
            "update-date": "2025-05-06"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Improper Payments Transparency Act</strong></p><p>This bill requires the President's annual budget to include specified information regarding improper payment amounts and rates for programs and activities at certain federal agencies. (An <em>improper payment</em>\u00a0is any payment that should not have been made or that was made in an incorrect amount, including an overpayment or underpayment, under a statutory, contractual, administrative, or other legally applicable requirement.)</p><p>Specifically, the President's budget must include (1) a narrative description, including a detailed explanation of why any improper payment amounts and\u00a0rates occurred and related trends for programs and activities; and (2) corrective actions and steps the agencies will take to address improper payment amount and rate issues.\u00a0</p>"
        },
        "title": "Improper Payments Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1771.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improper Payments Transparency Act</strong></p><p>This bill requires the President's annual budget to include specified information regarding improper payment amounts and rates for programs and activities at certain federal agencies. (An <em>improper payment</em>\u00a0is any payment that should not have been made or that was made in an incorrect amount, including an overpayment or underpayment, under a statutory, contractual, administrative, or other legally applicable requirement.)</p><p>Specifically, the President's budget must include (1) a narrative description, including a detailed explanation of why any improper payment amounts and\u00a0rates occurred and related trends for programs and activities; and (2) corrective actions and steps the agencies will take to address improper payment amount and rate issues.\u00a0</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1771"
    },
    "title": "Improper Payments Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improper Payments Transparency Act</strong></p><p>This bill requires the President's annual budget to include specified information regarding improper payment amounts and rates for programs and activities at certain federal agencies. (An <em>improper payment</em>\u00a0is any payment that should not have been made or that was made in an incorrect amount, including an overpayment or underpayment, under a statutory, contractual, administrative, or other legally applicable requirement.)</p><p>Specifically, the President's budget must include (1) a narrative description, including a detailed explanation of why any improper payment amounts and\u00a0rates occurred and related trends for programs and activities; and (2) corrective actions and steps the agencies will take to address improper payment amount and rate issues.\u00a0</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1771"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1771ih.xml"
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
      "title": "Improper Payments Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improper Payments Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T02:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 31, United States Code, to include information on improper payments under Federal programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T02:48:22Z"
    }
  ]
}
```
