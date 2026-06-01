# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8661?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8661
- Title: Foreign Military Financing Loan Authorization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8661
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-14T08:08:33Z
- Update date including text: 2026-05-14T08:08:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 37 - 9.
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 37 - 9.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8661",
    "number": "8661",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Foreign Military Financing Loan Authorization Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:33Z",
    "updateDateIncludingText": "2026-05-14T08:08:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 37 - 9.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-04",
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
        "item": [
          {
            "date": "2026-05-13T15:31:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-04T14:32:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8661ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8661\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Mast introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo authorize the Secretary of State to provide certain direct loans and loan guarantees for the procurement of defense articles, defense services, and design and construction services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Military Financing Loan Authorization Act of 2026 .\n#### 2. Authorization for direct loans and loan guarantees\n##### (a) Authorization\nThe Secretary of State is authorized to provide, to any country or international organization the Secretary determines appropriate and consistent with United States national security interests\u2014\n**(1)**\ndirect loans for the purpose of financing the procurement of defense articles, defense services, and design and construction services pursuant to section 23 of the Arms Export Control Act ( 22 U.S.C. 2763 ); and\n**(2)**\nloan guarantees for the purpose of financing the procurement of defense articles, defense services, and design and construction services pursuant to section 24 of such Act ( 22 U.S.C. 2764 ).\n##### (b) Loan rate and repayment authority\nThe Secretary is authorized to establish the rate of interest, repayment schedule, and repayment terms applicable to direct loans authorized under subsection (a)(1).\n##### (c) Conditions and limitations\nExcept as authorized in subsection (b), any direct loan or loan guarantee authorized under subsection (a) shall be subject to\u2014\n**(1)**\nthe terms, conditions, eligibility requirements, and limitations set forth in section 23 of the Arms Export Control Act ( 22 U.S.C. 2763 );\n**(2)**\nsuch additional terms and conditions as the Secretary may prescribe; and\n**(3)**\nthe availability of funds appropriated by Congress for purposes of this section.\n#### 3. Authorizing the Department of State to obligate funds from the Foreign Military Sales Administrative Surcharge fund\nFunds deposited pursuant to section 21(e)(1)(A) of the Arms Export Control Act ( 22 U.S.C. 2761(e)(1)(A) ) may be obligated by the Department of State for the purpose of carrying out activities pursuant to such Act ( 22 U.S.C. 2751 et seq. ).\n#### 4. Reporting requirement\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the Secretary of State shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a report describing\u2014\n**(1)**\nany direct loan or loan guarantee provided pursuant to section 2(a);\n**(2)**\nthe recipient, amount, terms, and purpose of each such loan or guarantee;\n**(3)**\nan assessment of the impact of such loans or guarantees on United States national security objectives; and\n**(4)**\nan assessment of additional resources needed by the Department of State to carry out the provisions of this Act.\n#### 5. Definitions\nIn this Act, the terms defense articles , defense services , and design and construction services have the meanings given such terms in section 47 of the Arms Export Control Act ( 22 U.S.C. 2794 ).",
      "versionDate": "2026-05-04",
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
        "name": "International Affairs",
        "updateDate": "2026-05-08T20:31:26Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8661ih.xml"
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
      "title": "Foreign Military Financing Loan Authorization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T04:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreign Military Financing Loan Authorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of State to provide certain direct loans and loan guarantees for the procurement of defense articles, defense services, and design and construction services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:48:51Z"
    }
  ]
}
```
