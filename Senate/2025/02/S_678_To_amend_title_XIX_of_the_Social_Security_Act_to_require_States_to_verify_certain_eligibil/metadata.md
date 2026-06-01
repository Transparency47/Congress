# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/678?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/678
- Title: LIVE Beneficiaries Act
- Congress: 119
- Bill type: S
- Bill number: 678
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-12-05T21:39:57Z
- Update date including text: 2025-12-05T21:39:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/678",
    "number": "678",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "LIVE Beneficiaries Act",
    "type": "S",
    "updateDate": "2025-12-05T21:39:57Z",
    "updateDateIncludingText": "2025-12-05T21:39:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T23:28:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s678is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 678\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to require States to verify certain eligibility criteria for individuals enrolled for medical assistance quarterly, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Leveraging Integrity and Verification of Eligibility for Beneficiaries Act or the LIVE Beneficiaries Act .\n#### 2. Verification of certain eligibility criteria for individuals enrolled for medical assistance\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (86), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (87)(D), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (87)(D) the following new paragraph:\n(88) provide that the State shall comply with the eligibility verification requirements under subsection (uu), except that this paragraph shall apply only in the case of the 50 States and the District of Columbia. ; and\n**(2)**\nby adding at the end the following new subsection:\n(uu) Verification of certain eligibility criteria (1) In general For purposes of subsection (a)(88), the eligibility verification requirements, beginning January 1, 2027, are as follows: (A) Quarterly screening to verify enrollee status The State shall, not less frequently than quarterly, review the Death Master File (as such term is defined in section 203(d) of the Bipartisan Budget Act of 2013) to determine whether any individuals enrolled for medical assistance under the State plan (or waiver of such plan) are deceased. (B) Disenrollment under State plan If the State determines, based on information obtained from the Death Master File, that an individual enrolled for medical assistance under the State plan (or waiver of such plan) is deceased, the State shall\u2014 (i) treat such information as factual information confirming the death of a beneficiary for purposes of section 431.213(a) of title 42, Code of Federal Regulations (or any successor regulation); (ii) disenroll such individual from the State plan (or waiver of such plan); and (iii) discontinue any payments for medical assistance under this title made on behalf of such individual (other than payments for any items or services furnished to such individual prior to the death of such individual). (C) Reinstatement of coverage in the event of error If a State determines that an individual was misidentified as deceased based on information obtained from the Death Master File, and was erroneously disenrolled from medical assistance under the State plan (or waiver of such plan) based on such misidentification, the State shall immediately reenroll such individual under the State plan (or waiver of such plan), retroactive to the date of such disenrollment. (2) Rule of construction Nothing under this subsection shall be construed to preclude the ability of a State to use other electronic data sources to timely identify potentially deceased beneficiaries, so long as the State is also in compliance with the requirements of this subsection (and all other requirements under this title relating to Medicaid eligibility determination and redetermination). .",
      "versionDate": "2025-02-20",
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-18",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1403",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LIVE Beneficiaries Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "An act to provide for reconciliation pursuant to title II of H. Con. Res. 14.",
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
            "name": "Health care coverage and access",
            "updateDate": "2025-06-13T19:13:54Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-06-13T19:13:54Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-06-13T19:13:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-13T15:18:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
    "originChamber": "Senate",
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
          "measure-id": "id119s678",
          "measure-number": "678",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s678v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Leveraging Integrity and Verification of Eligibility for Beneficiaries Act or the LIVE Beneficiaries Act</strong></p><p>This bill requires state Medicaid programs to check the Social Security Administration's Death Master File on at least a quarterly basis to determine whether Medicaid enrollees are deceased.</p>"
        },
        "title": "LIVE Beneficiaries Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s678.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Leveraging Integrity and Verification of Eligibility for Beneficiaries Act or the LIVE Beneficiaries Act</strong></p><p>This bill requires state Medicaid programs to check the Social Security Administration's Death Master File on at least a quarterly basis to determine whether Medicaid enrollees are deceased.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s678"
    },
    "title": "LIVE Beneficiaries Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Leveraging Integrity and Verification of Eligibility for Beneficiaries Act or the LIVE Beneficiaries Act</strong></p><p>This bill requires state Medicaid programs to check the Social Security Administration's Death Master File on at least a quarterly basis to determine whether Medicaid enrollees are deceased.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s678"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s678is.xml"
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
      "title": "LIVE Beneficiaries Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LIVE Beneficiaries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Leveraging Integrity and Verification of Eligibility for Beneficiaries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to require States to verify certain eligibility criteria for individuals enrolled for medical assistance quarterly, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:46Z"
    }
  ]
}
```
