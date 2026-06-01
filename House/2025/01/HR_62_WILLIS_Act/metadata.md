# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/62?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/62
- Title: WILLIS Act
- Congress: 119
- Bill type: HR
- Bill number: 62
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-12T19:24:53Z
- Update date including text: 2025-02-12T19:24:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/62",
    "number": "62",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "WILLIS Act",
    "type": "HR",
    "updateDate": "2025-02-12T19:24:53Z",
    "updateDateIncludingText": "2025-02-12T19:24:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:17:15Z",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr62ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 62\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Crane , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit Federal funds from being awarded or otherwise made available to the Fulton County District Attorney\u2019s Office.\n#### 1. Short title\nThis Act may be cited as the Withholding Investments from Lawless Litigators In States Act or the WILLIS Act .\n#### 2. Prohibition on Federal funding with respect to Fulton County District Attorney\n##### (a) Prohibition on Federal funding\nNotwithstanding any other provision of law, no Federal funds may be awarded or otherwise made available to the Fulton County District Attorney\u2019s Office.\n##### (b) Rescission and repayment of Federal funding\nThe unobligated balances of all amounts allocated for or otherwise made available to the Fulton County District Attorney\u2019s Office is hereby rescinded, and the Attorney General shall take such steps as may be necessary and practicable to require the Fulton County District Attorney\u2019s Office to reimburse the Federal Government for all amounts expended for such Office after the date of January 1, 2021.",
      "versionDate": "2025-01-03",
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
            "name": "Georgia",
            "updateDate": "2025-02-12T19:24:41Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-02-12T19:24:53Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-12T19:24:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-06T16:54:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr62",
          "measure-number": "62",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr62v00",
            "update-date": "2025-02-06"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Withholding Investments from Lawless Litigators In States Act or the WILLIS Act</strong></p><p>This bill prohibits federal funds from being awarded or otherwise made available to the Fulton County District Attorney\u2019s Office in Georgia.\u00a0</p><p>The bill also (1) rescinds any unobligated funds that were allocated for or otherwise made available to the office, and (2) directs the Department of Justice to require the office to reimburse the federal government for all funds that were expended for the office after January 1, 2021.</p>"
        },
        "title": "WILLIS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr62.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Withholding Investments from Lawless Litigators In States Act or the WILLIS Act</strong></p><p>This bill prohibits federal funds from being awarded or otherwise made available to the Fulton County District Attorney\u2019s Office in Georgia.\u00a0</p><p>The bill also (1) rescinds any unobligated funds that were allocated for or otherwise made available to the office, and (2) directs the Department of Justice to require the office to reimburse the federal government for all funds that were expended for the office after January 1, 2021.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr62"
    },
    "title": "WILLIS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Withholding Investments from Lawless Litigators In States Act or the WILLIS Act</strong></p><p>This bill prohibits federal funds from being awarded or otherwise made available to the Fulton County District Attorney\u2019s Office in Georgia.\u00a0</p><p>The bill also (1) rescinds any unobligated funds that were allocated for or otherwise made available to the office, and (2) directs the Department of Justice to require the office to reimburse the federal government for all funds that were expended for the office after January 1, 2021.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr62"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr62ih.xml"
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
      "title": "WILLIS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WILLIS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Withholding Investments from Lawless Litigators In States Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal funds from being awarded or otherwise made available to the Fulton County District Attorney's Office.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T07:48:34Z"
    }
  ]
}
```
