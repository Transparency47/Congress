# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1925?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1925
- Title: Expanding Access to Diabetes Self-Management Training Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1925
- Origin chamber: Senate
- Introduced date: 2025-06-02
- Update date: 2026-04-28T11:03:22Z
- Update date including text: 2026-04-28T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-02: Introduced in Senate
- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-02: Introduced in Senate

## Actions

- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-02",
    "latestAction": {
      "actionDate": "2025-06-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1925",
    "number": "1925",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Expanding Access to Diabetes Self-Management Training Act of 2025",
    "type": "S",
    "updateDate": "2026-04-28T11:03:22Z",
    "updateDateIncludingText": "2026-04-28T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-02",
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
      "actionDate": "2025-06-02",
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
        "item": [
          {
            "date": "2025-06-02T22:17:19Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-02T22:17:19Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "ME"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-12-08",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MN"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1925is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1925\nIN THE SENATE OF THE UNITED STATES\nJune 2, 2025 Mrs. Shaheen (for herself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to improve access to diabetes outpatient self-management training services, to require the Center for Medicare and Medicaid Innovation to test the provision of virtual diabetes outpatient self-management training services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Access to Diabetes Self-Management Training Act of 2025 .\n#### 2. Improving access to diabetes outpatient self-management training services\n##### (a) In general\nSection 1861(qq) of the Social Security Act ( 42 U.S.C. 1395x(qq) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking the Secretary determines appropriate and inserting specified in paragraph (3) ; and\n**(B)**\nby striking the physician who is managing the individual's diabetic condition and inserting a physician or qualified nonphysician practitioner ;\n**(2)**\nin paragraph (2)(B), by striking paragraph and inserting subparagraph ; and\n**(3)**\nby adding at the end the following new paragraph:\n(3)(A) For purposes of paragraph (1) and subject to subparagraph (B), the times specified in this paragraph are the following: (i) An initial 10 hours of individual or group educational and training services to remain available until used. (ii) An additional 2 hours of individual or group educational and training services each year, beginning with the year in which the initial 10 hours described in subparagraph (A) are completed. (B) The Secretary shall not limit the quantity or duration of educational and training services furnished by a certified provider to an individual with diabetes if such services are deemed medically necessary by a physician or qualified non-physician practitioner. .\n##### (b) Medical nutrition therapy services\nSection 1861(s)(2)(V) of the Social Security Act ( 42 U.S.C. 1395x(s)(2)(V) ) is amended\u2014\n**(1)**\nby striking clause (i);\n**(2)**\nby redesignating clauses (ii) and (iii) as clauses (i) and (ii), respectively; and\n**(3)**\nin clause (ii), as so redesignated, by striking after consideration of and inserting consistent with .\n##### (c) Cost-Sharing\nSection 1833 of the Social Security Act ( 42 U.S.C. 1395l ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nby striking and (HH) and inserting (HH) ; and\n**(B)**\nby inserting the following before the semicolon at the end: and (II) with respect to diabetes outpatient self-management training services (as defined in section 1861(qq)), the amount paid shall be 100 percent of the lesser of the actual charge for the services or the amount determined under the fee schedule that applies to such services under this part; ; and\n**(2)**\nin subsection (b), in the first sentence\u2014\n**(A)**\nby striking , and (13) and inserting (13) ; and\n**(B)**\nby striking 1861(n).. and inserting 1861(n), and (14) such deductible shall not apply with respect to diabetes outpatient self-management training services (as defined in section 1861(qq)) .\n##### (d) Application\nThe amendments made by this section shall apply with respect to items and services furnished on or after January 1, 2027.\n#### 3. CMI testing of providing virtual diabetes outpatient self-management training services\nSection 1115A of the Social Security Act ( 42 U.S.C. 1315a ) is amended\u2014\n**(1)**\nin subsection (b)(2)(A), by adding at the end the following new sentence: \u201cThe models selected under this subparagraph shall include the testing of the model described in subsection (h).\u201d; and\n**(2)**\nby adding at the end the following new subsection:\n(h) Testing of providing virtual diabetes outpatient self-Management training services (1) Establishment Not later than January 1, 2026, the Secretary shall implement a model to test the impact of providing coverage under title XVIII for virtual diabetes outpatient self-management training services furnished to applicable beneficiaries with respect to improved health outcomes for such applicable beneficiaries and reduced expenditures under such title XVIII. (2) Model design (A) In general The Secretary shall design the model under this subsection in such a manner to allow for the evaluation of demographic characteristics of applicable beneficiaries participating in such model and the extent to which such model accomplishes the following purposes: (i) Improvement in health outcomes with respect to the diabetic conditions, including by reducing A1c levels. (ii) Reduced hospitalizations due to diabetic-related complications. (iii) Increased utilization of diabetes outpatient self-management training services as evidenced by, for example, Medicare beneficiary participation and utilization of covered hours during the first year and subsequent years or use of diabetes outpatient self-management training services in rural and underserved communities. (iv) Improved medication adherence. (v) Reduced expenditures under this title attributable to the model. (B) Consultation In designing the model under this subsection, the Secretary shall, not later than 3 months after the date of the enactment of this subsection, consult with stakeholders in the field of diabetes care and education, clinicians in the primary care community, experts in digital health, and beneficiary groups. (3) Definitions In this subsection: (A) Applicable beneficiary The term applicable beneficiary means an individual with diabetes as described in section 1861(qq). (B) Qualified web-based program The term qualified web-based program means a web-based program\u2014 (i) designed to furnish educational and training services to an individual with diabetes to ensure therapy compliance with respect to the individual\u2019s diabetic condition or to provide the individual with necessary skills and knowledge (including skills related to the self-administration of injectable drugs) to participate in the individual\u2019s management of such condition; and (ii) that meets the quality standards described in section 1861(qq)(2)(B). (C) Virtual diabetes outpatient self-management training services The term virtual diabetes outpatient self-management training services means any diabetes outpatient self-management training services (as defined in section 1861(qq)) furnished by a qualified web-based program for synchronous or asynchronous diabetes outpatient self-management training services. .",
      "versionDate": "2025-06-02",
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
        "actionDate": "2025-06-06",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3826",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expanding Access to Diabetes Self-Management Training Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-06-16T17:27:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-02",
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
          "measure-id": "id119s1925",
          "measure-number": "1925",
          "measure-type": "s",
          "orig-publish-date": "2025-06-02",
          "originChamber": "SENATE",
          "update-date": "2025-07-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1925v00",
            "update-date": "2025-07-24"
          },
          "action-date": "2025-06-02",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Expanding Access to Diabetes Self-Management Training Act of </strong><strong>2025</strong></p><p>This bill expands Medicare coverage of diabetes outpatient self-management training. </p><p>Specifically, the bill specifies that in addition to physicians, other health care practitioners may also provide such services. It also specifies that coverage includes an initial 10 hours of training until used, as well as an additional 2 hours of training per year. The bill also prohibits the Centers for Medicare & Medicaid Services from limiting training that is deemed medically necessary.\u00a0</p><p>Additionally, the Center for Medicare and Medicaid Innovation must test a model in which such training is provided virtually and evaluate any effects on costs, services, and health outcomes.</p>"
        },
        "title": "Expanding Access to Diabetes Self-Management Training Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1925.xml",
    "summary": {
      "actionDate": "2025-06-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expanding Access to Diabetes Self-Management Training Act of </strong><strong>2025</strong></p><p>This bill expands Medicare coverage of diabetes outpatient self-management training. </p><p>Specifically, the bill specifies that in addition to physicians, other health care practitioners may also provide such services. It also specifies that coverage includes an initial 10 hours of training until used, as well as an additional 2 hours of training per year. The bill also prohibits the Centers for Medicare & Medicaid Services from limiting training that is deemed medically necessary.\u00a0</p><p>Additionally, the Center for Medicare and Medicaid Innovation must test a model in which such training is provided virtually and evaluate any effects on costs, services, and health outcomes.</p>",
      "updateDate": "2025-07-24",
      "versionCode": "id119s1925"
    },
    "title": "Expanding Access to Diabetes Self-Management Training Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expanding Access to Diabetes Self-Management Training Act of </strong><strong>2025</strong></p><p>This bill expands Medicare coverage of diabetes outpatient self-management training. </p><p>Specifically, the bill specifies that in addition to physicians, other health care practitioners may also provide such services. It also specifies that coverage includes an initial 10 hours of training until used, as well as an additional 2 hours of training per year. The bill also prohibits the Centers for Medicare & Medicaid Services from limiting training that is deemed medically necessary.\u00a0</p><p>Additionally, the Center for Medicare and Medicaid Innovation must test a model in which such training is provided virtually and evaluate any effects on costs, services, and health outcomes.</p>",
      "updateDate": "2025-07-24",
      "versionCode": "id119s1925"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1925is.xml"
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
      "title": "Expanding Access to Diabetes Self-Management Training Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expanding Access to Diabetes Self-Management Training Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to improve access to diabetes outpatient self-management training services, to require the Center for Medicare and Medicaid Innovation to test the provision of virtual diabetes outpatient self-management training services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:33Z"
    }
  ]
}
```
