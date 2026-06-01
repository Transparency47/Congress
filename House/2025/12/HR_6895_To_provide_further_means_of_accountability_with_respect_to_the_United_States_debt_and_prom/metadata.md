# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6895?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6895
- Title: Debt Solution and Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 6895
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-21T08:08:12Z
- Update date including text: 2026-05-21T08:08:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6895",
    "number": "6895",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Debt Solution and Accountability Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:12Z",
    "updateDateIncludingText": "2026-05-21T08:08:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NC"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "WI"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NE"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "HI"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "VA"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6895ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6895\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Smucker (for himself and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide further means of accountability with respect to the United States debt and promote fiscal responsibility.\n#### 1. Short title\nThis Act may be cited as the Debt Solution and Accountability Act .\n#### 2. Secretary of the Treasury report to Congress before debt limit is increased\n##### (a) In general\nSubchapter II of chapter 31 of title 31, United States Code, is amended by adding at the end the following:\n3131. Report before debt limit is increased (a) In general On each specified reporting date, the Secretary of the Treasury shall submit a report to the Committee on Ways and Means of the House of Representatives, the Committee on Appropriations of the House of Representatives, the Committee on the Budget of the House of Representatives, the Committee on Finance of the Senate, the Committee on Appropriations of the Senate, and the Committee on the Budget of the Senate consisting of the following: (1) Debt Report A report on the state of the public debt, including\u2014 (A) the historical levels of the debt, current amount and composition of the debt, and future projections of the debt; (B) the drivers and composition of future debt; and (C) how the United States will meet debt obligations, including principal and interest. (2) Statement of intent A detailed explanation of\u2014 (A) proposals of the President to reduce or slow the growth of the public debt in the short term (the current and following three fiscal years), medium term (approximately five to nine fiscal years), and long term (approximately ten to twenty-five fiscal years), and proposals of the President to lower the debt-to-gross domestic product ratio; (B) the impact (including the impact on future Government spending, debt service, and the position of the United States dollar as the international reserve currency) of increasing the debt limit and of leaving the debt limit unchanged; and (C) projections of fiscal health and sustainability of major direct-spending entitlement programs (including Social Security, Medicare, and Medicaid). (b) Progress report Not more than 180 days after any date on which any increase, or suspension, of the limitation imposed under section 3101 takes effect, the Secretary of the Treasury shall submit a detailed report on the progress of implementing all proposals of the President described under subsection (a)(2)(A). (c) Specified reporting date For purposes of this section, the term specified reporting date means\u2014 (1) any date on which the debt subject to limit under section 3101 reaches 99.5 percent of the limitation imposed under such section; and (2) with respect to any period for which the limitation imposed under section 3101 is suspended, the date which is 1 month before the expiration of such suspension. (d) Public access to information The Secretary of the Treasury shall furnish publicly accessible links on the web page of the Department of the Treasury to each report submitted under this section. Such links shall be available for not less than the 6-month period following the date of such submission. .\n##### (b) Clerical amendment\nThe table of analysis for chapter 31 of title 31, United States Code, is amended by inserting after the item relating to section 3130 the following:\n3131. Report after debt limit is increased. .\n#### 3. Access to certain Treasury Department data\nNot later than thirty days after receipt of a written request from the Chairman of the Committee on Ways and Means of the House of Representatives or the Committee on Finance of the Senate, the Secretary of the Treasury shall provide to the requesting Chairman financial and economic data relevant to determining the amount of the public debt of the United States, including\u2014\n**(1)**\ncash flow and debt transaction information used in preparing the Daily Treasury Statement, including current balances, receipts, and payments;\n**(2)**\noperating cash balance projections; and\n**(3)**\nrelevant information regarding any extraordinary measures taken to prevent the public debt from exceeding the limitation imposed by section 3101 of title 31, United States Code.",
      "versionDate": "2025-12-18",
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
        "updateDate": "2026-01-22T20:43:30Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6895ih.xml"
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
      "title": "Debt Solution and Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Debt Solution and Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide further means of accountability with respect to the United States debt and promote fiscal responsibility.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:19Z"
    }
  ]
}
```
