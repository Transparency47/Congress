# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/113?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/113
- Title: Budget Process Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 113
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-10T00:26:13Z
- Update date including text: 2025-12-10T00:26:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/113",
    "number": "113",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
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
    "title": "Budget Process Enhancement Act",
    "type": "HR",
    "updateDate": "2025-12-10T00:26:13Z",
    "updateDateIncludingText": "2025-12-10T00:26:13Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
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
      "text": "Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the Committee on the Budget, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-01-03T16:11:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:11:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:11:40Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr113ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 113\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on the Budget , and in addition to the Committees on House Administration , and Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo remove the discretionary inflater from the baseline and to provide that the salaries of Members of a House of Congress will be held in escrow if that House has not agreed to a concurrent resolution on the budget for fiscal year 2026, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Budget Process Enhancement Act .\nI\nChanges in the Baseline\n#### 101. Changes in the baseline\nSection 257(c) of the Balanced Budget and Emergency Deficit Control Act of 1985 is amended\u2014\n**(1)**\nin the second sentence of paragraph (1), by striking everything that follows current year, and inserting excluding resources designated as an emergency requirement and any resources provided in supplemental appropriation laws. ;\n**(2)**\nby striking paragraphs (2), (3), (4), and (5);\n**(3)**\nby redesignating paragraph (6) as paragraph (2); and\n**(4)**\nby inserting after paragraph (2) the following new paragraph:\n(3) No adjustment for inflation No adjustment shall be made for inflation or for any other factor. .\nII\nBudget Accountability of Members of Congress\n#### 201. Holding salaries of Members of Congress in escrow upon failure to agree to budget resolution\n##### (a) Holding salaries in escrow\n**(1) In general**\nIf by April 15, 2025, a House of Congress has not agreed to a concurrent resolution on the budget for fiscal year 2026 pursuant to section 301 of the Congressional Budget Act of 1974, during the period described in paragraph (2) the payroll administrator of that House of Congress shall deposit in an escrow account all payments otherwise required to be made during such period for the compensation of Members of Congress who serve in that House of Congress, and shall release such payments to such Members only upon the expiration of such period.\n**(2) Period described**\nWith respect to a House of Congress, the period described in this paragraph is the period which begins on April 16, 2025, and ends on the earlier of\u2014\n**(A)**\nthe day on which the House of Congress agrees to a concurrent resolution on the budget for fiscal year 2026 pursuant to section 301 of the Congressional Budget Act of 1974; or\n**(B)**\nthe last day of the One Hundred Eighteenth Congress.\n**(3) Withholding and remittance of amounts from payments held in escrow**\nThe payroll administrator shall provide for the same withholding and remittance with respect to a payment deposited in an escrow account under paragraph (1) that would apply to the payment if the payment were not subject to paragraph (1).\n**(4) Release of amounts at end of the Congress**\nIn order to ensure that this section is carried out in a manner that shall not vary the compensation of Senators or Representatives in violation of the twenty-seventh article of amendment to the Constitution of the United States, the payroll administrator of a House of Congress shall release for payments to Members of that House of Congress any amounts remaining in any escrow account under this section on the last day of the One Hundred Eighteenth Congress.\n**(5) Role of Secretary of the Treasury**\nThe Secretary of the Treasury shall provide the payroll administrators of the Houses of Congress with such assistance as may be necessary to enable the payroll administrators to carry out this section.\n##### (b) Treatment of Delegates as Members\nIn this section, the term Member of Congress includes a Delegate or Resident Commissioner to the Congress.\n##### (c) Payroll administrator defined\nIn this section, the term payroll administrator of a House of Congress means\u2014\n**(1)**\nin the case of the House of Representatives, the Chief Administrative Officer of the House of Representatives, or an employee of the Office of the Chief Administrative Officer who is designated by the Chief Administrative Officer to carry out this section; and\n**(2)**\nin the case of the Senate, the Secretary of the Senate, or an employee of the Office of the Secretary of the Senate who is designated by the Secretary to carry out this section.\n#### 202. Determination of compliance with statutory requirement to submit the President\u2019s budget\nNot later than 3 days after the President\u2019s budget is due, the Inspector General of the Office of Personnel Management shall\u2014\n**(1)**\nmake an annual determination of whether the Director of the Office of Management and Budget and the President are in compliance with section 1105 of title 31, United States Code; and\n**(2)**\nprovide a written notification of such determination to the Chairs of the Committee on the Budget and the Committee on Appropriations of the Senate and the Chairs of the Committee on the Budget and the Committee on Appropriations of the House of Representatives.\n#### 203. No pay upon failure to timely submit the President\u2019s budget to Congress\n##### (a) In general\nNotwithstanding any other provision of law, no funds may be appropriated or otherwise be made available from the United States Treasury for the pay of the Director of the Office of Management and Budget, the Deputy Director of the Office, or the Deputy Director for Management of the Office during any period of noncompliance determined by the Inspector General of the Office of Personnel Management under section 202.\n##### (b) No retroactive pay\nThe Director of the Office of Management and Budget, the Deputy Director of the Office, and the Deputy Director for Management of the Office may not receive pay for any period of noncompliance determined by the Inspector General of the Office of Personnel Management under section 202 at any time after the end of that period.\n#### 204. Effective date\nSections 202 and 203 shall take effect upon the date of enactment of this Act.",
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
        "text": "Referred to the House Committee on House Administration."
      },
      "number": "208",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Budget, No Pay Act",
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
            "updateDate": "2025-02-05T21:00:54Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-02-05T21:00:54Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-05T21:00:54Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-02-05T21:00:54Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-02-05T21:00:54Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-02-05T21:00:54Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-02-05T21:00:54Z"
          },
          {
            "name": "Office of Management and Budget (OMB)",
            "updateDate": "2025-02-05T21:00:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-01-31T17:01:23Z"
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
          "measure-id": "id119hr113",
          "measure-number": "113",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr113v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Budget Process Enhancement Act</strong></p> <p>This bill modifies the federal budget process to withhold the salaries of Members of Congress and cancel the salaries of certain employees of the Office of Management and Budget when certain budget process requirements are not met.</p> <p>The bill also changes the assumptions that the Congressional Budget Office uses to calculate its baseline for discretionary spending to eliminate certain adjustments for inflation and other factors. (A baseline is a projection of federal spending and receipts during a fiscal year under current law.) </p>"
        },
        "title": "Budget Process Enhancement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr113.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Budget Process Enhancement Act</strong></p> <p>This bill modifies the federal budget process to withhold the salaries of Members of Congress and cancel the salaries of certain employees of the Office of Management and Budget when certain budget process requirements are not met.</p> <p>The bill also changes the assumptions that the Congressional Budget Office uses to calculate its baseline for discretionary spending to eliminate certain adjustments for inflation and other factors. (A baseline is a projection of federal spending and receipts during a fiscal year under current law.) </p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr113"
    },
    "title": "Budget Process Enhancement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Budget Process Enhancement Act</strong></p> <p>This bill modifies the federal budget process to withhold the salaries of Members of Congress and cancel the salaries of certain employees of the Office of Management and Budget when certain budget process requirements are not met.</p> <p>The bill also changes the assumptions that the Congressional Budget Office uses to calculate its baseline for discretionary spending to eliminate certain adjustments for inflation and other factors. (A baseline is a projection of federal spending and receipts during a fiscal year under current law.) </p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr113"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr113ih.xml"
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
      "title": "Budget Process Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Budget Process Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To remove the discretionary inflater from the baseline and to provide that the salaries of Members of a House of Congress will be held in escrow if that House has not agreed to a concurrent resolution on the budget for fiscal year 2026, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T06:18:28Z"
    }
  ]
}
```
