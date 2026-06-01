# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/208?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/208
- Title: No Budget, No Pay Act
- Congress: 119
- Bill type: HR
- Bill number: 208
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-11-20T09:06:36Z
- Update date including text: 2025-11-20T09:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/208",
    "number": "208",
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
    "title": "No Budget, No Pay Act",
    "type": "HR",
    "updateDate": "2025-11-20T09:06:36Z",
    "updateDateIncludingText": "2025-11-20T09:06:36Z"
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
          "date": "2025-01-03T16:17:25Z",
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
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr208ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 208\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Wittman introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo provide that the salaries of Members of a House of Congress will be held in escrow if that House has not agreed to a concurrent resolution on the budget for the next fiscal year by April 15.\n#### 1. Short title\nThis Act may be cited as the No Budget, No Pay Act .\n#### 2. Holding salaries of members of congress in escrow upon failure to agree to budget resolution\n##### (a) Holding salaries in escrow\n**(1) In general**\nIf by April 15, a House of Congress has not agreed to a concurrent resolution on the budget for the next fiscal year pursuant to section 301 of the Congressional Budget Act of 1974, during the period described in paragraph (2) the payroll administrator of that House of Congress shall deposit in an escrow account all payments otherwise required to be made during such period for the compensation of Members of Congress who serve in that House of Congress, and shall release such payments to such Members only upon the expiration of such period.\n**(2) Period described**\nWith respect to a House of Congress, the period described in this paragraph is the period which begins on April 16 and ends on the earlier of\u2014\n**(A)**\nthe day on which the House of Congress agrees to a concurrent resolution on the budget for the next fiscal year pursuant to section 301 of the Congressional Budget Act of 1974; or\n**(B)**\nthe last day of the Congress.\n**(3) Withholding and remittance of amounts from payments held in escrow**\nThe payroll administrator shall provide for the same withholding and remittance with respect to a payment deposited in an escrow account under paragraph (1) that would apply to the payment if the payment were not subject to paragraph (1).\n**(4) Release of amounts at end of the Congress**\nIn order to ensure that this section is carried out in a manner that shall not vary the compensation of Senators or Representatives in violation of the twenty-seventh article of amendment to the Constitution of the United States, the payroll administrator of a House of Congress shall release for payments to Members of that House of Congress any amounts remaining in any escrow account under this section on the last day of the Congress.\n**(5) Role of Secretary of the Treasury**\nThe Secretary of the Treasury shall provide the payroll administrators of the Houses of Congress with such assistance as may be necessary to enable the payroll administrators to carry out this section.\n##### (b) Treatment of delegates as members\nIn this section, the term Member of Congress includes a Delegate or Resident Commissioner to the Congress.\n##### (c) Payroll administrator defined\nIn this section, the payroll administrator of a House of Congress means\u2014\n**(1)**\nin the case of the House of Representatives, the Chief Administrative Officer of the House of Representatives, or an employee of the Office of the Chief Administrative Officer who is designated by the Chief Administrative Officer to carry out this section; and\n**(2)**\nin the case of the Senate, the Secretary of the Senate, or an employee of the Office of the Secretary of the Senate who is designated by the Secretary to carry out this section.\n##### (d) Effective date\nThis Act shall apply with respect to fiscal year 2026 and each succeeding fiscal year.",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "113",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Budget Process Enhancement Act",
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
            "name": "Budget deficits and national debt",
            "updateDate": "2025-03-05T15:37:48Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-03-05T15:37:48Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-05T15:37:48Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-05T15:37:48Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-03-05T15:37:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-02-28T14:54:09Z"
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
          "measure-id": "id119hr208",
          "measure-number": "208",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr208v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Budget, No Pay Act </strong></p><p>This bill withholds the salaries of Members of a chamber of Congress that has not agreed to a budget resolution for the next fiscal year\u00a0by April 15, as required by the Congressional Budget Act of 1974.</p><p>Salaries are withheld from April 16 until the earlier of (1) the day on which the chamber of Congress agrees to a budget resolution for the next fiscal year, or (2) the last day of the Congress.</p>"
        },
        "title": "No Budget, No Pay Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr208.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Budget, No Pay Act </strong></p><p>This bill withholds the salaries of Members of a chamber of Congress that has not agreed to a budget resolution for the next fiscal year\u00a0by April 15, as required by the Congressional Budget Act of 1974.</p><p>Salaries are withheld from April 16 until the earlier of (1) the day on which the chamber of Congress agrees to a budget resolution for the next fiscal year, or (2) the last day of the Congress.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr208"
    },
    "title": "No Budget, No Pay Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Budget, No Pay Act </strong></p><p>This bill withholds the salaries of Members of a chamber of Congress that has not agreed to a budget resolution for the next fiscal year\u00a0by April 15, as required by the Congressional Budget Act of 1974.</p><p>Salaries are withheld from April 16 until the earlier of (1) the day on which the chamber of Congress agrees to a budget resolution for the next fiscal year, or (2) the last day of the Congress.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr208"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr208ih.xml"
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
      "title": "No Budget, No Pay Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Budget, No Pay Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T07:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that the salaries of Members of a House of Congress will be held in escrow if that House has not agreed to a concurrent resolution on the budget for the next fiscal year by April 15.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T07:48:27Z"
    }
  ]
}
```
