# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5305?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5305
- Title: Congressional MRA Act
- Congress: 119
- Bill type: HR
- Bill number: 5305
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-24T14:41:35Z
- Update date including text: 2025-09-24T14:41:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5305",
    "number": "5305",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Congressional MRA Act",
    "type": "HR",
    "updateDate": "2025-09-24T14:41:35Z",
    "updateDateIncludingText": "2025-09-24T14:41:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "VA"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "AZ"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5305ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5305\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Arrington (for himself, Mr. Vindman , Mr. Gosar , and Mr. Grothman ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo require any amounts remaining in the Members\u2019 Representational Allowance at the end of a fiscal year to be deposited in the Treasury and used for deficit reduction or to reduce the Federal debt, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Congressional Money Returned to America Act or the Congressional MRA Act .\n#### 2. Requiring amounts remaining in Members\u2019 Representational Allowance to be used for deficit reduction or to reduce the Federal debt\n##### (a) In general\nNotwithstanding any other provision of law, any amounts appropriated for the Members\u2019 Representational Allowance of the House of Representatives for a fiscal year which remain after all payments are made under such Allowance for the year shall be deposited in the Treasury and used for deficit reduction (or, if there is no Federal budget deficit after all such payments have been made, for reducing the Federal debt, in such manner as the Secretary of the Treasury considers appropriate).\n##### (b) Regulations\nThe Committee on House Administration of the House of Representatives shall have authority to prescribe regulations to carry out this Act.\n##### (c) Effective date\nThis section shall apply with respect to fiscal year 2026 and each succeeding fiscal year.",
      "versionDate": "2025-09-11",
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
        "name": "Congress",
        "updateDate": "2025-09-24T13:35:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-11",
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
          "measure-id": "id119hr5305",
          "measure-number": "5305",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-11",
          "originChamber": "HOUSE",
          "update-date": "2025-09-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5305v00",
            "update-date": "2025-09-24"
          },
          "action-date": "2025-09-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Congressional Money Returned to America Act or the Congressional\u00a0MRA Act</strong></p><p>This bill requires funds that were provided to House offices for the Members' Representational Allowance (MRA) and remain in the MRA account after all payments for the year are made to be deposited in the Treasury and used for deficit or debt reduction.\u00a0</p><p>The\u00a0MRA is an allowance that Members of the House of Representatives receive each year to operate their offices. It must be used to support official and representational duties and may not be used for personal or campaign purposes.\u00a0</p><p>Annual appropriations acts that fund the legislative branch have generally included a provision that requires unused amounts remaining in the\u00a0MRA to be used for deficit reduction or to reduce the federal debt. This bill makes this requirement permanent.\u00a0</p>"
        },
        "title": "Congressional MRA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5305.xml",
    "summary": {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Money Returned to America Act or the Congressional\u00a0MRA Act</strong></p><p>This bill requires funds that were provided to House offices for the Members' Representational Allowance (MRA) and remain in the MRA account after all payments for the year are made to be deposited in the Treasury and used for deficit or debt reduction.\u00a0</p><p>The\u00a0MRA is an allowance that Members of the House of Representatives receive each year to operate their offices. It must be used to support official and representational duties and may not be used for personal or campaign purposes.\u00a0</p><p>Annual appropriations acts that fund the legislative branch have generally included a provision that requires unused amounts remaining in the\u00a0MRA to be used for deficit reduction or to reduce the federal debt. This bill makes this requirement permanent.\u00a0</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119hr5305"
    },
    "title": "Congressional MRA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Money Returned to America Act or the Congressional\u00a0MRA Act</strong></p><p>This bill requires funds that were provided to House offices for the Members' Representational Allowance (MRA) and remain in the MRA account after all payments for the year are made to be deposited in the Treasury and used for deficit or debt reduction.\u00a0</p><p>The\u00a0MRA is an allowance that Members of the House of Representatives receive each year to operate their offices. It must be used to support official and representational duties and may not be used for personal or campaign purposes.\u00a0</p><p>Annual appropriations acts that fund the legislative branch have generally included a provision that requires unused amounts remaining in the\u00a0MRA to be used for deficit reduction or to reduce the federal debt. This bill makes this requirement permanent.\u00a0</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119hr5305"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5305ih.xml"
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
      "title": "Congressional MRA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-23T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional MRA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-23T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Money Returned to America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-23T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require any amounts remaining in the Members' Representational Allowance at the end of a fiscal year to be deposited in the Treasury and used for deficit reduction or to reduce the Federal debt, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-23T04:18:24Z"
    }
  ]
}
```
