# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3379
- Title: HUMPS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3379
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 23.
- 2025-06-25 - Calendars: Placed on the Union Calendar, Calendar No. 136.
- 2025-06-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-170.
- 2025-06-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-170.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 23.
- 2025-06-25 - Calendars: Placed on the Union Calendar, Calendar No. 136.
- 2025-06-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-170.
- 2025-06-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-170.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3379",
    "number": "3379",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000471",
        "district": "5",
        "firstName": "Scott",
        "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
        "lastName": "Fitzgerald",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "HUMPS Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-06-25",
      "calendarNumber": {
        "calendar": "U00136"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 136.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-170.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-170.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
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
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
            "date": "2025-06-25T14:48:11Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-21T16:06:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-14T14:02:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3379ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3379\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Fitzgerald introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Federal Financial Institutions Examination Council Act of 1978 to require the Federal financial institutions regulatory agencies to update the CAMELS Rating System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Halting Uncertain Methods and Practices in Supervision Act of 2025 or the HUMPS Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nCAMELS ratings (Capital adequacy, Asset quality, Management, Earnings, Liquidity, and Sensitivity to market risk) are a critical tool for evaluating the safety and soundness of financial institutions, and the basis for determining significant regulatory matters such as the evaluation for mergers and acquisitions and a bank\u2019s deposit insurance premiums;\n**(2)**\nthe CAMELS rating system relies heavily on examiner judgment, which can lead to subjective and inconsistent ratings across similar institutions;\n**(3)**\nestablishing clear, objective measures for each CAMELS component and their relative weighting in determining composite ratings will promote fairness, consistency, and accountability in supervisory assessments; and\n**(4)**\nexamination and supervision, as well as the CAMELS rating system, should focus on a financial institution\u2019s core financial condition or solvency.\n#### 3. Amendments to the CAMELS Rating System\n##### (a) In general\nThe Federal Financial Institutions Examination Council Act of 1978 ( 12 U.S.C. 3301 et seq. ) is amended by adding at the end the following:\n1012. Amendments to the CAMELS Rating System (a) In general The Council shall make recommendations to amend the Uniform Financial Institutions Rating System, and the CAMELS components thereunder, to\u2014 (1) establish clear and objective criteria for assessing each CAMELS component; (2) revise the weighting of each CAMELS component to derive a composite rating that more accurately reflects the financial condition and risk profile of the financial institutions being rated; (3) either\u2014 (A) eliminate the management component of the CAMELS rating system; or (B) revise the management component of the CAMELS rating system to limit the assessment under such component to objective measures of the governance and controls used to manage an institution\u2019s risk profile; and (4) ensure that composite ratings are determined based on a transparent methodology that is limited to the objective criteria established for each CAMELS component. (b) Rulemaking Not later than 12 months after the Council makes the recommendations required under subsection (a), the Federal financial institutions regulatory agencies shall, jointly, issue rules to carry out the recommendations described under subsection (a). (c) Public comment period In issuing the rules required under subsection (b), the Federal financial institutions regulatory agencies shall\u2014 (1) publish a notice of proposed rulemaking with respect to such rules; and (2) provide for a public comment period of not less than 60 days. (d) Rule of construction Nothing in this section may be construed to limit the authority of the Federal financial institutions regulatory agencies to take supervisory or enforcement actions to ensure the safety and soundness of financial institutions. .\n##### (b) Well managed definition\nSection 2(o)(9)(A) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1841(o)(9)(A) ) is amended\u2014\n**(1)**\nby striking achievement of and all that follows through a CAMEL and inserting achievement of a CAMEL ;\n**(2)**\nby striking ; and and inserting a period; and\n**(3)**\nby striking clause (ii).",
      "versionDate": "2025-05-14",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3379rh.xml",
      "text": "IB\nUnion Calendar No. 136\n119th CONGRESS\n1st Session\nH. R. 3379\n[Report No. 119\u2013170]\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Fitzgerald introduced the following bill; which was referred to the Committee on Financial Services\nJune 25, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on May 14, 2025\nA BILL\nTo amend the Federal Financial Institutions Examination Council Act of 1978 to require the Federal financial institutions regulatory agencies to update the CAMELS Rating System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Halting Uncertain Methods and Practices in Supervision Act of 2025 or the HUMPS Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nCAMELS ratings (Capital adequacy, Asset quality, Management, Earnings, Liquidity, and Sensitivity to market risk) are a critical tool for evaluating the safety and soundness of financial institutions, and the basis for determining significant regulatory matters such as the evaluation for mergers and acquisitions and a bank\u2019s deposit insurance premiums;\n**(2)**\nthe CAMELS rating system relies heavily on examiner judgment, which can lead to subjective and inconsistent ratings across similar institutions;\n**(3)**\nestablishing clear, objective measures for each CAMELS component and their relative weighting in determining composite ratings will promote fairness, consistency, and accountability in supervisory assessments; and\n**(4)**\nexamination and supervision, as well as the CAMELS rating system, should focus on a financial institution\u2019s core financial condition or solvency.\n#### 3. Amendments to the CAMELS Rating System\n##### (a) In general\nThe Federal Financial Institutions Examination Council Act of 1978 ( 12 U.S.C. 3301 et seq. ) is amended by adding at the end the following:\n1012. Amendments to the CAMELS Rating System (a) In general The Council shall make recommendations to amend the Uniform Financial Institutions Rating System, and the CAMELS components thereunder, to\u2014 (1) establish clear and objective criteria for assessing each CAMELS component; (2) revise the factors affecting each CAMELS component to derive a composite rating that more accurately reflects the financial condition and risk profile of the financial institutions being rated; (3) either\u2014 (A) eliminate the management component of the CAMELS rating system; or (B) revise the management component of the CAMELS rating system to limit the assessment under such component to objective measures of the governance and controls used to manage an institution\u2019s risk profile; (4) ensure that composite ratings consider the financial institution\u2019s compliance with\u2014 (A) section 21 of the Federal Deposit Insurance Act ( 12 U.S.C. 1829b ); (B) chapter 2 of title I of Public Law 91\u2013508 ( 12 U.S.C. 1951 et seq. ); (C) subchapter II of chapter 53 of title 31, United States Code; and (D) any other applicable requirements and implementing regulations relating to the prevention of money laundering and terrorist financing; and (5) ensure that composite ratings are determined based on a transparent methodology that is limited to the objective criteria established for each CAMELS component. (b) Rulemaking Not later than 12 months after the Council makes the recommendations required under subsection (a), the Federal financial institutions regulatory agencies shall, jointly, issue rules to carry out the recommendations described under subsection (a). (c) Public comment period In issuing the rules required under subsection (b), the Federal financial institutions regulatory agencies shall\u2014 (1) publish a notice of proposed rulemaking with respect to such rules; and (2) provide for a public comment period of not less than 90 days. (d) Rule of construction Nothing in this section may be construed to limit the authority of the Federal financial institutions regulatory agencies to take supervisory or enforcement actions to ensure the safety and soundness of financial institutions. .\n##### (b) Well managed definition\nSection 2(o)(9)(A) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1841(o)(9)(A) ) is amended\u2014\n**(1)**\nby striking achievement of and all that follows through a CAMEL and inserting achievement of a CAMEL ;\n**(2)**\nby striking ; and and inserting a period; and\n**(3)**\nby striking clause (ii).",
      "versionDate": "2025-06-25",
      "versionType": "Reported in House"
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
        "actionDate": "2026-04-20",
        "text": "Placed on the Union Calendar, Calendar No. 535."
      },
      "number": "6955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Act",
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
            "name": "Advisory bodies",
            "updateDate": "2025-05-28T15:34:33Z"
          },
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-05-28T15:31:18Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-05-28T15:30:55Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2025-05-28T15:35:03Z"
          },
          {
            "name": "Financial crises and stabilization",
            "updateDate": "2025-05-28T15:31:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-22T17:51:46Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3379ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3379rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "HUMPS Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-06-26T07:08:19Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Halting Uncertain Methods and Practices in Supervision Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-06-26T07:08:19Z"
    },
    {
      "title": "HUMPS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T08:54:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HUMPS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T08:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Halting Uncertain Methods and Practices in Supervision Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T08:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Financial Institutions Examination Council Act of 1978 to require the Federal financial institutions regulatory agencies to update the CAMELS Rating System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T08:44:50Z"
    }
  ]
}
```
