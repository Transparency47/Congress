# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5637?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5637
- Title: No Work, No Pay Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5637
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-04-13T15:08:46Z
- Update date including text: 2026-04-13T15:08:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5637",
    "number": "5637",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "K000403",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Kennedy, Mike [R-UT-3]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "No Work, No Pay Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-13T15:08:46Z",
    "updateDateIncludingText": "2026-04-13T15:08:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:04:20Z",
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
          "date": "2025-09-30T16:04:15Z",
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
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5637ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5637\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Kennedy of Utah introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the pay of Members of Congress during periods in which a Government shutdown is in effect, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Work, No Pay Act of 2025 .\n#### 2. Prohibiting pay of Members of Congress in response to government shutdown\n##### (a) Prohibition of Pay\nIf on any day during a pay period a Government shutdown is in effect, the payroll administrator of each House of Congress shall exclude from the payments otherwise required to be made with respect to that pay period for the compensation of each Member of Congress who serves in that House of Congress an amount equal to the product of\u2014\n**(1)**\nan amount equal to one day\u2019s worth of pay under the annual rate of pay applicable to the Member under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ); and\n**(2)**\nthe number of 24-hour periods during which the Government shutdown is in effect which occur during the pay period.\n##### (b) Role of Secretary of the Treasury\nThe Secretary of the Treasury shall provide the payroll administrators of the Houses of Congress with such assistance as may be necessary to enable the payroll administrators to carry out this section.\n##### (c) Payroll administrator defined\nIn this section, the payroll administrator of a House of Congress means\u2014\n**(1)**\nin the case of the House of Representatives, the Chief Administrative Officer of the House of Representatives, or an employee of the Office of the Chief Administrative Officer who is designated by the Chief Administrative Officer to carry out this section; and\n**(2)**\nin the case of the Senate, the Secretary of the Senate, or an employee of the Office of the Secretary of the Senate who is designated by the Secretary to carry out this section.\n##### (d) Effective date\nThis section shall apply with respect to days occurring during the One Hundred Twentieth Congress and each succeeding Congress.\n#### 3. Determination of Government shutdown\nFor purposes of this Act, a Government shutdown shall be considered to be in effect if there is a lapse in appropriations for any Federal agency or department as a result of a failure to enact a regular appropriations bill or continuing resolution.\n#### 4. Member of Congress defined\nIn this Act, the term Member of Congress means an individual serving in a position under subparagraph (A), (B), or (C) of section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ).",
      "versionDate": "2025-09-30",
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
        "actionDate": "2026-03-27",
        "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8140",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Money Where Our Mouths Are Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-10-06T16:30:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
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
          "measure-id": "id119hr5637",
          "measure-number": "5637",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2025-10-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5637v00",
            "update-date": "2025-10-07"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Work, No Pay Act of 2025</strong></p><p>This bill prohibits Members of Congress from being paid during a government shutdown, beginning with the 120th Congress. Under the bill, a government shutdown is in effect when there is a lapse in appropriations for any federal agency or department as a result of a failure to enact a regular appropriations bill or a continuing resolution.</p>"
        },
        "title": "No Work, No Pay Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5637.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Work, No Pay Act of 2025</strong></p><p>This bill prohibits Members of Congress from being paid during a government shutdown, beginning with the 120th Congress. Under the bill, a government shutdown is in effect when there is a lapse in appropriations for any federal agency or department as a result of a failure to enact a regular appropriations bill or a continuing resolution.</p>",
      "updateDate": "2025-10-07",
      "versionCode": "id119hr5637"
    },
    "title": "No Work, No Pay Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Work, No Pay Act of 2025</strong></p><p>This bill prohibits Members of Congress from being paid during a government shutdown, beginning with the 120th Congress. Under the bill, a government shutdown is in effect when there is a lapse in appropriations for any federal agency or department as a result of a failure to enact a regular appropriations bill or a continuing resolution.</p>",
      "updateDate": "2025-10-07",
      "versionCode": "id119hr5637"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5637ih.xml"
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
      "title": "No Work, No Pay Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Work, No Pay Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the pay of Members of Congress during periods in which a Government shutdown is in effect, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:25Z"
    }
  ]
}
```
