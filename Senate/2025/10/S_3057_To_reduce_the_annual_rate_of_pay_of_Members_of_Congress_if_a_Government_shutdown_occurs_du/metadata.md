# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3057?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3057
- Title: Withhold Member Pay During Shutdowns Act
- Congress: 119
- Bill type: S
- Bill number: 3057
- Origin chamber: Senate
- Introduced date: 2025-10-27
- Update date: 2026-03-30T18:20:46Z
- Update date including text: 2026-03-30T18:20:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-27: Introduced in Senate
- 2025-10-27 - IntroReferral: Introduced in Senate
- 2025-10-27 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-10-27: Introduced in Senate

## Actions

- 2025-10-27 - IntroReferral: Introduced in Senate
- 2025-10-27 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-27",
    "latestAction": {
      "actionDate": "2025-10-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3057",
    "number": "3057",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Withhold Member Pay During Shutdowns Act",
    "type": "S",
    "updateDate": "2026-03-30T18:20:46Z",
    "updateDateIncludingText": "2026-03-30T18:20:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-10-27T21:59:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3057is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3057\nIN THE SENATE OF THE UNITED STATES\nOctober 27, 2025 Mr. Kennedy introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo reduce the annual rate of pay of Members of Congress if a Government shutdown occurs during a year, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Withhold Member Pay During Shutdowns Act .\n#### 2. No pay for Members of Congress during Government shutdowns\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term Government shutdown means a lapse in appropriations for 1 or more Federal agencies or departments;\n**(2)**\nthe term Member of Congress means an individual serving in a position under subparagraph (A), (B), or (C) of section 601(a)(1) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501(1) ); and\n**(3)**\nthe term payroll administrator , with respect to a House of Congress, means\u2014\n**(A)**\nin the case of the Senate, the Secretary of the Senate, or an employee of the Office of the Secretary of the Senate who is designated by the Secretary to carry out the requirements of this section; and\n**(B)**\nin the case of the House of Representatives, the Chief Administrative Officer of the House of Representatives, or an employee of the Office of the Chief Administrative Officer who is designated by the Chief Administrative Officer to carry out the requirements of this section.\n##### (b) Requiring reduction of pay of Members of Congress if Government shutdown occurs\n**(1) In general**\nIf on any day during a pay period a Government shutdown is in effect, the payroll administrator of each House of Congress shall exclude from the payments otherwise required to be made with respect to that pay period for the compensation of each Member of Congress who serves in that House of Congress an amount equal to the product of\u2014\n**(A)**\nan amount equal to one day's worth of pay under the annual rate of pay of the Member under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ); and\n**(B)**\nthe number of 24-hour periods during the pay period during which the Government shutdown is in effect.\n**(2) Effective date**\nThis subsection shall apply with respect to days occurring after the date of the regularly scheduled general election for Federal office held in November 2026 (in this section referred to as the pay reduction effective date ).\n##### (c) Special rule for Members of Congress before general election\n**(1) Holding salaries in escrow**\nIf on any day before the pay reduction effective date a Government shutdown is in effect, the payroll administrator of each House of Congress shall\u2014\n**(A)**\nwithhold from the payments otherwise required to be made with respect to a pay period for the compensation of each Member of Congress who serves in that House of Congress an amount equal to the product of\u2014\n**(i)**\nan amount equal to one day\u2019s worth of pay under the annual rate of pay applicable to the Member under section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ); and\n**(ii)**\nthe number of 24-hour periods during which the Government shutdown is in effect which occur during the pay period; and\n**(B)**\ndeposit in an escrow account all amounts withheld under subparagraph (A).\n**(2) Release of amounts at end of the Congress**\nIn order to ensure that this subsection is carried out in a manner that shall not vary the compensation of Senators or Representatives in violation of the 27th Amendment to the Constitution of the United States, the payroll administrator of a House of Congress shall release for payments to Members of that House of Congress any amounts remaining in any escrow account under this subsection on the pay reduction effective date.\n**(3) Applicability**\nThis subsection shall apply with respect to days during the period beginning on the date of enactment of this Act and ending on the pay reduction effective date.\n##### (d) Role of Secretary of the Treasury\nThe Secretary of the Treasury shall provide the payroll administrators of the Houses of Congress with such assistance as may be necessary to enable the payroll administrators to carry out this section.",
      "versionDate": "2025-10-27",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-03-18",
        "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 10 - 0."
      },
      "number": "5891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Withhold Member Pay During Shutdowns Act",
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
        "updateDate": "2026-03-30T18:20:46Z"
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
      "date": "2025-10-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3057is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Withhold Member Pay During Shutdowns Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-29T06:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Withhold Member Pay During Shutdowns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-29T06:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reduce the annual rate of pay of Members of Congress if a Government shutdown occurs during a year, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-29T06:03:13Z"
    }
  ]
}
```
