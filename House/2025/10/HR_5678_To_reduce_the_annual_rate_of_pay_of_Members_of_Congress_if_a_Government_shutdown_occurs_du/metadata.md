# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5678?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5678
- Title: No Pay for Disarray Act
- Congress: 119
- Bill type: HR
- Bill number: 5678
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2025-10-21T14:55:28Z
- Update date including text: 2025-10-21T14:55:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-03: Introduced in House

## Actions

- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5678",
    "number": "5678",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001119",
        "district": "2",
        "firstName": "Angie",
        "fullName": "Rep. Craig, Angie [D-MN-2]",
        "lastName": "Craig",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "No Pay for Disarray Act",
    "type": "HR",
    "updateDate": "2025-10-21T14:55:28Z",
    "updateDateIncludingText": "2025-10-21T14:55:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T19:30:45Z",
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
          "date": "2025-10-03T19:30:40Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5678ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5678\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Ms. Craig introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reduce the annual rate of pay of Members of Congress if a Government shutdown occurs during a year, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Pay for Disarray Act .\n#### 2. Requiring reduction of pay of Members of Congress if Government shutdown occurs\n##### (a) Reduction of pay for each day of Government shutdown\nIf on any day during a year a Government shutdown is in effect, the annual rate of pay applicable under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ) with respect to each Member of Congress for the year shall be reduced by an amount equal to the product of\u2014\n**(1)**\nan amount equal to one day\u2019s worth of pay under such annual rate; and\n**(2)**\nthe number of 24-hour periods during which the Government shutdown is in effect.\n##### (b) Effective date\nThis section shall apply with respect to days occurring after the date of the regularly scheduled general election for Federal office held in November 2026.\n#### 3. Special rule for One Hundred Nineteenth Congress\n##### (a) Holding salaries in escrow\nIf on any day during the One Hundred Nineteenth Congress a Government shutdown is in effect, the payroll administrator of that House of Congress shall\u2014\n**(1)**\nwithhold from the payments otherwise required to be made with respect to a pay period for the compensation of each Member of Congress who serves in that House of Congress an amount equal to the product of\u2014\n**(A)**\nan amount equal to one day\u2019s worth of pay under the annual rate of pay applicable to the Member under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ); and\n**(B)**\nthe number of 24-hour periods during which the Government shutdown is in effect which occur during the pay period; and\n**(2)**\ndeposit in an escrow account all amounts withheld under paragraph (1).\n##### (b) Release of amounts at end of the Congress\nIn order to ensure that this section is carried out in a manner that shall not vary the compensation of Senators or Representatives in violation of the twenty-seventh article of amendment to the Constitution of the United States, the payroll administrator of a House of Congress shall release for payments to Members of that House of Congress any amounts remaining in any escrow account under this section on the last day of the One Hundred Nineteenth Congress.\n##### (c) Role of Secretary of the Treasury\nThe Secretary of the Treasury shall provide the payroll administrators of the Houses of Congress with such assistance as may be necessary to enable the payroll administrators to carry out this section.\n##### (d) Payroll administrator defined\nIn this section, the payroll administrator of a House of Congress means\u2014\n**(1)**\nin the case of the House of Representatives, the Chief Administrative Officer of the House of Representatives, or an employee of the Office of the Chief Administrative Officer who is designated by the Chief Administrative Officer to carry out this section; and\n**(2)**\nin the case of the Senate, the Secretary of the Senate, or an employee of the Office of the Secretary of the Senate who is designated by the Secretary to carry out this section.\n##### (e) Exception for days occurring after general election\nThis section does not apply with respect to any day during the One Hundred Nineteenth Congress which occurs after the date of the regularly scheduled general election for Federal office held in November 2026.\n#### 4. Determination of Government shutdown\nFor purposes of this Act, a Government shutdown shall be considered to be in effect if there is a lapse in appropriations for any Federal agency or department as a result of a failure to enact a regular appropriations bill or continuing resolution.\n#### 5. Member of Congress defined\nIn this Act, the term Member of Congress means an individual serving in a position under subparagraph (A), (B), or (C) of section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ).",
      "versionDate": "2025-10-03",
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
        "updateDate": "2025-10-17T12:46:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-03",
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
          "measure-id": "id119hr5678",
          "measure-number": "5678",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-03",
          "originChamber": "HOUSE",
          "update-date": "2025-10-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5678v00",
            "update-date": "2025-10-21"
          },
          "action-date": "2025-10-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Pay for Disarray Act</strong></p><p>This bill withholds or eliminates the pay of Members of Congress during a government shutdown.</p><p>Through the day of the general election in November 2026, any salary earned by Members during a government shutdown must be held in escrow and released on the last day of the 119th Congress.</p><p>After the November 2026 general election, a Member shall not be paid for any day during which a government shutdown is in effect.\u00a0</p>"
        },
        "title": "No Pay for Disarray Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5678.xml",
    "summary": {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Pay for Disarray Act</strong></p><p>This bill withholds or eliminates the pay of Members of Congress during a government shutdown.</p><p>Through the day of the general election in November 2026, any salary earned by Members during a government shutdown must be held in escrow and released on the last day of the 119th Congress.</p><p>After the November 2026 general election, a Member shall not be paid for any day during which a government shutdown is in effect.\u00a0</p>",
      "updateDate": "2025-10-21",
      "versionCode": "id119hr5678"
    },
    "title": "No Pay for Disarray Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Pay for Disarray Act</strong></p><p>This bill withholds or eliminates the pay of Members of Congress during a government shutdown.</p><p>Through the day of the general election in November 2026, any salary earned by Members during a government shutdown must be held in escrow and released on the last day of the 119th Congress.</p><p>After the November 2026 general election, a Member shall not be paid for any day during which a government shutdown is in effect.\u00a0</p>",
      "updateDate": "2025-10-21",
      "versionCode": "id119hr5678"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5678ih.xml"
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
      "title": "No Pay for Disarray Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Pay for Disarray Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T05:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reduce the annual rate of pay of Members of Congress if a Government shutdown occurs during a year, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T05:48:31Z"
    }
  ]
}
```
