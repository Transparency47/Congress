# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3787?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3787
- Title: Emergency Spending Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 3787
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-07-15T18:44:17Z
- Update date including text: 2025-07-15T18:44:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-05 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-12 - IntroReferral: Sponsor introductory remarks on measure. (CR H2661)
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-05 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-12 - IntroReferral: Sponsor introductory remarks on measure. (CR H2661)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3787",
    "number": "3787",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001188",
        "district": "3",
        "firstName": "Marlin",
        "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
        "lastName": "Stutzman",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Emergency Spending Accountability Act",
    "type": "HR",
    "updateDate": "2025-07-15T18:44:17Z",
    "updateDateIncludingText": "2025-07-15T18:44:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2661)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
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
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-05T14:04:40Z",
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
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "AZ"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "PA"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IN"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "WI"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "SC"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3787ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3787\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Stutzman (for himself, Mr. Gosar , Mr. Perry , Mr. Gooden , Mr. Shreve , Mr. Grothman , Mr. Self , and Mr. Norman ) introduced the following bill; which was referred to the Committee on the Budget , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Director of the Office of Management and Budget to offset emergency spending, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Emergency Spending Accountability Act .\n#### 2. Sequestration to offset emergency spending\n##### (a) Sequestration\n**(1) In general**\nWith respect to any direct spending or discretionary spending that is appropriated or otherwise made available during a fiscal year that is emergency spending, the Director of the Office of Management and Budget shall, on October 1 of the subsequent fiscal year and each of the 4 following fiscal years, issue a sequestration order that reduces total budgetary resources such that outlay savings equal one-fifth of the total amount of such emergency spending.\n**(2) Notification**\nThe Director shall submit written notice to Congress on the date of any sequestration order under paragraph (1). Such notice shall include a list of any account affected by such order.\n**(3) Discretionary and direct spending application**\nIf emergency spending made available during a fiscal year is discretionary spending, any sequestration under subsection (a) with respect to such emergency spending may only be made with respect to discretionary accounts. If emergency spending made available during a fiscal year is direct spending, any sequestration required under subsection (a) with respect to such emergency spending may only be made to direct spending accounts.\n##### (b) Application\nWith respect to any sequestration under subsection (a)\u2014\n**(1)**\nexcept as provided in subsection (c), and notwithstanding any other provision of law, no account is exempted from reduction;\n**(2)**\nsuch reduction shall be at a uniform rate across all programs and activities that are subject to sequestration; and\n**(3)**\nthe total amount of the sequestration shall be reduced by the amount of any offsetting reduction in discretionary spending or direct spending (as the case may be) in the measure enacted into law that provided the applicable emergency spending.\n##### (c) Exempt programs\nThe following programs and accounts shall be exempt from sequestration under this section:\n**(1)**\nBenefits payable under the old-age, survivors, and disability insurance program established under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ), and benefits payable under sections 3 and 4 of the Railroad Retirement Act of 1937 ( 45 U.S.C. 231 et seq. ).\n**(2)**\nAny account within budget function 050 (National Defense).\n**(3)**\nAll programs administered by the Department of Veterans Affairs.\n**(4)**\nThe Medicare program under title XVIII of the Social Security Act.\n##### (d) Requirement for measures containing emergency spending\n**(1) Reported measures**\nWith respect to any bill or joint resolution favorably reported by any standing committee of Congress that includes emergency spending, the report accompanying such measure shall include a detailed justification of why each instance of such spending is necessary.\n**(2) Other measures**\nAny measure considered by the House of Representatives not described in paragraph (1) that includes emergency spending shall include such a detailed explanation, to be published in the Congressional Record prior to consideration.\n**(3) Requirements**\nAny justification under paragraph (1) or (2) shall include reasons why such spending meets the definitions of the terms emergency and unanticipated (as those terms are defined in section 250(c) of the Balanced Budget and Emergency Deficit Control Act of 1985).\n##### (e) Definitions\nIn this Act\u2014\n**(1)**\nthe terms budget authority and outlays have the meaning given those terms in section 3 of the Congressional Budget and Impoundment Control Act of 1974;\n**(2)**\nthe terms budgetary resources , discretionary spending , direct spending , and sequestration have the meaning given those terms in section 250(c) of the Balanced Budget and Emergency Deficit Control Act of 1985; and\n**(3)**\nthe term emergency spending means any budget authority\u2014\n**(A)**\nthat is designated\u2014\n**(i)**\nunder section 251(b)(2)(A), (D), or (F) of the Balanced Budget and Emergency Deficit Control Act of 1985;\n**(ii)**\nunder section 4(g) of the Statutory-Pay-As-You-Go Act of 2010; or\n**(iii)**\nunder a concurrent resolution on the budget as being for an emergency; and\n**(B)**\nthat is otherwise exempted from counting against any Federal spending limitation, including the discretionary spending limits in section 251(c) of the Balanced Budget and Emergency Deficit Control Act of 1985 or the PAYGO scorecards.",
      "versionDate": "2025-06-05",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-07-15T18:44:17Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3787ih.xml"
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
      "title": "Emergency Spending Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Emergency Spending Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Director of the Office of Management and Budget to offset emergency spending, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:49:06Z"
    }
  ]
}
```
