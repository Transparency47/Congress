# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8140?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8140
- Title: Money Where Our Mouths Are Act
- Congress: 119
- Bill type: HR
- Bill number: 8140
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-04-13T15:08:52Z
- Update date including text: 2026-04-13T15:08:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-27 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-27: Introduced in House

## Actions

- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-27 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8140",
    "number": "8140",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "J000307",
        "district": "10",
        "firstName": "John",
        "fullName": "Rep. James, John [R-MI-10]",
        "lastName": "James",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Money Where Our Mouths Are Act",
    "type": "HR",
    "updateDate": "2026-04-13T15:08:52Z",
    "updateDateIncludingText": "2026-04-13T15:08:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
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
      "actionDate": "2026-03-27",
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
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:32:30Z",
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
          "date": "2026-03-28T01:32:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8140ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8140\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Mr. James introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the pay of Members of Congress during periods in which a Government shutdown is in effect, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Money Where Our Mouths Are Act .\n#### 2. Prohibiting pay of Members of Congress in response to government shutdown\n##### (a) Prohibition of Pay\nIf on any day during a pay period a Government shutdown is in effect, the payroll administrator of each House of Congress shall exclude from the payments otherwise required to be made with respect to that pay period for the compensation of each Member of Congress who serves in that House of Congress an amount equal to the product of\u2014\n**(1)**\nan amount equal to one day\u2019s worth of pay under the annual rate of pay applicable to the Member under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ); and\n**(2)**\nthe number of 24-hour periods during which the Government shutdown is in effect which occur during the pay period.\n##### (b) Role of Secretary of the Treasury\nThe Secretary of the Treasury shall provide the payroll administrators of the Houses of Congress with such assistance as may be necessary to enable the payroll administrators to carry out this section.\n##### (c) Payroll administrator defined\nIn this section, the payroll administrator of a House of Congress means\u2014\n**(1)**\nin the case of the House of Representatives, the Chief Administrative Officer of the House of Representatives, or an employee of the Office of the Chief Administrative Officer who is designated by the Chief Administrative Officer to carry out this section; and\n**(2)**\nin the case of the Senate, the Secretary of the Senate, or an employee of the Office of the Secretary of the Senate who is designated by the Secretary to carry out this section.\n##### (d) Effective date\nThis section shall apply with respect to days occurring during the One Hundred Twentieth Congress and each succeeding Congress.\n#### 3. Determination of Government shutdown\nFor purposes of this Act, a Government shutdown shall be considered to be in effect if there is a lapse in appropriations for any Federal agency or department as a result of a failure to enact a regular appropriations bill or continuing resolution.\n#### 4. Member of Congress defined\nIn this Act, the term Member of Congress means an individual serving in a position under subparagraph (A), (B), or (C) of section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ).",
      "versionDate": "2026-03-27",
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
        "actionDate": "2025-09-30",
        "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5637",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Work, No Pay Act of 2025",
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
        "updateDate": "2026-04-13T15:08:52Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8140ih.xml"
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
      "title": "Money Where Our Mouths Are Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Money Where Our Mouths Are Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the pay of Members of Congress during periods in which a Government shutdown is in effect, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:28Z"
    }
  ]
}
```
