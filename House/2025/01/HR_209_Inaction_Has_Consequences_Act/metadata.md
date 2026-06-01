# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/209?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/209
- Title: Inaction Has Consequences Act
- Congress: 119
- Bill type: HR
- Bill number: 209
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-11-20T09:06:29Z
- Update date including text: 2025-11-20T09:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on House Administration.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/209",
    "number": "209",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Inaction Has Consequences Act",
    "type": "HR",
    "updateDate": "2025-11-20T09:06:29Z",
    "updateDateIncludingText": "2025-11-20T09:06:29Z"
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
          "date": "2025-01-03T16:17:40Z",
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
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr209ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 209\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Wittman introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo hold the salaries of Members of a House of Congress in escrow if the House of Congress does not pass regular appropriation bills on a timely basis during a Congress, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Inaction Has Consequences Act .\n#### 2. Holding salaries of Members of Congress in escrow upon failure to pass regular appropriation bills\n##### (a) Holding Salaries in Escrow\nIf by the first day of a fiscal year (beginning with fiscal year 2026), a House of Congress has not passed each of the regular appropriation bills for such fiscal year, during the period described in subsection (b) the payroll administrator of that House of Congress shall deposit in an escrow account all payments otherwise required to be made during such period for the compensation of Members of Congress who serve in that House of Congress, and shall release such payments to such Members only upon the expiration of such period.\n##### (b) Period Described\nWith respect to a House of Congress and a fiscal year, the period described in this paragraph is the period which begins on the first day of the fiscal year and ends on the earlier of\u2014\n**(1)**\nthe first day by which the House of Congress has passed each of the regular appropriation bills for such fiscal year; or\n**(2)**\nthe last day of the Congress during which that fiscal year begins.\n##### (c) Regular Appropriation Bill Defined\nThe term regular appropriation bill means any annual appropriation bill which, with respect to the Congress involved, is under the jurisdiction of a single subcommittee of the Committee on Appropriations of the House of Representatives (pursuant to the Rules of the House of Representatives for that Congress) and a single subcommittee of the Committee on Appropriations of the Senate (pursuant to the Standing Rules of the Senate).\n#### 3. Administration of escrow\n##### (a) Withholding and Remittance of Amounts From Payments Held in Escrow\nThe payroll administrator shall provide for the same withholding and remittance with respect to a payment deposited in an escrow account under section 2 that would apply to the payment if the payment were not subject to such section.\n##### (b) Role of Secretary of the Treasury\nThe Secretary of the Treasury shall provide the payroll administrators of the Houses of Congress with such assistance as may be necessary to enable the payroll administrators to carry out this Act.\n#### 4. Release of amounts at end of a Congress\nIn order to ensure that this Act is carried out in a manner consistent with the twenty-seventh article of amendment to the Constitution of the United States, the payroll administrator of a House of Congress shall release for payments to Members of that House of Congress any amounts remaining in any escrow account under section 2 on the last day of the Congress during which the amounts were deposited in such account.\n#### 5. Definitions\nIn this Act\u2014\n**(1)**\nthe term Member includes a Delegate or Resident Commissioner to the Congress; and\n**(2)**\nthe payroll administrator of a House of Congress means\u2014\n**(A)**\nin the case of the House of Representatives, the Chief Administrative Officer of the House of Representatives, or an employee of the Office of the Chief Administrative Officer who is designated by the Chief Administrative Officer to carry out this Act; and\n**(B)**\nin the case of the Senate, the Secretary of the Senate, or an employee of the Office of the Secretary of the Senate who is designated by the Secretary to carry out this Act.",
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
            "name": "Appropriations",
            "updateDate": "2025-03-03T16:08:48Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-03-03T16:08:48Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-03-03T16:08:48Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-03T16:08:48Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-03-03T16:08:48Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-03-03T16:08:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-02-25T15:02:44Z"
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
          "measure-id": "id119hr209",
          "measure-number": "209",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr209v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Inaction Has Consequences Act </strong></p><p>This bill withholds the salaries of Members of a chamber of Congress that has not passed each of the annual appropriations bills before the beginning of the fiscal year, beginning with FY2026. Salaries are released on the earlier of (1) the date on which the chamber of Congress passes the bills, or (2) the last day of the Congress.</p>"
        },
        "title": "Inaction Has Consequences Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr209.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Inaction Has Consequences Act </strong></p><p>This bill withholds the salaries of Members of a chamber of Congress that has not passed each of the annual appropriations bills before the beginning of the fiscal year, beginning with FY2026. Salaries are released on the earlier of (1) the date on which the chamber of Congress passes the bills, or (2) the last day of the Congress.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr209"
    },
    "title": "Inaction Has Consequences Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Inaction Has Consequences Act </strong></p><p>This bill withholds the salaries of Members of a chamber of Congress that has not passed each of the annual appropriations bills before the beginning of the fiscal year, beginning with FY2026. Salaries are released on the earlier of (1) the date on which the chamber of Congress passes the bills, or (2) the last day of the Congress.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr209"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr209ih.xml"
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
      "title": "Inaction Has Consequences Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T09:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Inaction Has Consequences Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T09:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To hold the salaries of Members of a House of Congress in escrow if the House of Congress does not pass regular appropriation bills on a timely basis during a Congress, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T09:03:33Z"
    }
  ]
}
```
