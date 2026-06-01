# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1403?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1403
- Title: LIVE Beneficiaries Act
- Congress: 119
- Bill type: HR
- Bill number: 1403
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-02-27T21:41:19Z
- Update date including text: 2026-02-27T21:41:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1403",
    "number": "1403",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "LIVE Beneficiaries Act",
    "type": "HR",
    "updateDate": "2026-02-27T21:41:19Z",
    "updateDateIncludingText": "2026-02-27T21:41:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "MN"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1403ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1403\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Bilirakis (for himself and Ms. Craig ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to require States to verify certain eligibility criteria for individuals enrolled for medical assistance quarterly, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Leveraging Integrity and Verification of Eligibility for Beneficiaries Act or the LIVE Beneficiaries Act .\n#### 2. Modifying certain State requirements for ensuring deceased individuals do not remain enrolled\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (86), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (87)(D), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (87) the following new paragraph:\n(88) provide that the State shall comply with the eligibility verification requirements under subsection (uu), except that this paragraph shall apply only in the case of the 50 States and the District of Columbia. ; and\n**(2)**\nby adding at the end the following new subsection:\n(uu) Verification of certain eligibility criteria (1) In general For purposes of subsection (a)(88), the eligibility verification requirements, beginning January 1, 2027, are as follows: (A) Quarterly screening to verify enrollee status The State shall, not less frequently than quarterly, review the Death Master File (as such term is defined in section 203(d) of the Bipartisan Budget Act of 2013) to determine whether any individuals enrolled for medical assistance under the State plan (or waiver of such plan) are deceased. (B) Disenrollment under State plan If the State determines, based on information obtained from the Death Master File, that an individual enrolled for medical assistance under the State plan (or waiver of such plan) is deceased, the State shall\u2014 (i) treat such information as factual information confirming the death of a beneficiary for purposes of section 431.213(a) of title 42, Code of Federal Regulations (or any successor regulation); (ii) disenroll such individual from the State plan (or waiver of such plan); and (iii) discontinue any payments for medical assistance under this title made on behalf of such individual (other than payments for any items or services furnished to such individual prior to the death of such individual). (C) Reinstatement of coverage in the event of error If a State determines that an individual was misidentified as deceased based on information obtained from the Death Master File, and was erroneously disenrolled from medical assistance under the State plan (or waiver of such plan) based on such misidentification, the State shall immediately re-enroll such individual under the State plan (or waiver of such plan), retroactive to the date of such disenrollment. (2) Rule of construction Nothing under this subsection shall be construed to preclude the ability of a State to use other electronic data sources to timely identify potentially deceased beneficiaries, so long as the State is also in compliance with the requirements of this subsection (and all other requirements under this title relating to Medicaid eligibility determination and redetermination). .",
      "versionDate": "2025-02-18",
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
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "678",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LIVE Beneficiaries Act",
      "type": "S"
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
            "updateDate": "2025-06-13T19:13:42Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-06-13T19:13:42Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-06-13T19:13:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-14T11:58:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119hr1403",
          "measure-number": "1403",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1403v00",
            "update-date": "2025-03-26"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Leveraging Integrity and Verification of Eligibility for Beneficiaries Act or the LIVE Beneficiaries Act</strong></p><p>This bill requires state Medicaid programs to check the Social Security Administration's Death Master File on at least a quarterly basis to determine whether Medicaid enrollees are deceased.</p>"
        },
        "title": "LIVE Beneficiaries Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1403.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Leveraging Integrity and Verification of Eligibility for Beneficiaries Act or the LIVE Beneficiaries Act</strong></p><p>This bill requires state Medicaid programs to check the Social Security Administration's Death Master File on at least a quarterly basis to determine whether Medicaid enrollees are deceased.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1403"
    },
    "title": "LIVE Beneficiaries Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Leveraging Integrity and Verification of Eligibility for Beneficiaries Act or the LIVE Beneficiaries Act</strong></p><p>This bill requires state Medicaid programs to check the Social Security Administration's Death Master File on at least a quarterly basis to determine whether Medicaid enrollees are deceased.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1403"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1403ih.xml"
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
      "title": "LIVE Beneficiaries Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LIVE Beneficiaries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Leveraging Integrity and Verification of Eligibility for Beneficiaries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to require States to verify certain eligibility criteria for individuals enrolled for medical assistance quarterly, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:19:27Z"
    }
  ]
}
```
