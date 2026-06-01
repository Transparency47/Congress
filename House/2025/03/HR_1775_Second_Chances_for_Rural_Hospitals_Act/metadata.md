# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1775?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1775
- Title: Second Chances for Rural Hospitals Act
- Congress: 119
- Bill type: HR
- Bill number: 1775
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-03-17T08:05:48Z
- Update date including text: 2026-03-17T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1775",
    "number": "1775",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Second Chances for Rural Hospitals Act",
    "type": "HR",
    "updateDate": "2026-03-17T08:05:48Z",
    "updateDateIncludingText": "2026-03-17T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-03T17:05:25Z",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "HI"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MS"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NE"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "KS"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "NM"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1775ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1775\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Arrington (for himself, Ms. Tokuda , and Mr. Pfluger ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to modify the criteria for designation of rural emergency hospitals.\n#### 1. Short title\nThis Act may be cited as the Second Chances for Rural Hospitals Act .\n#### 2. Expanding the definition of rural emergency hospital under the Medicare program\n##### (a) In general\nSection 1861(kkk) of the Social Security Act ( 42 U.S.C. 1395x(kkk) ) is amended\u2014\n**(1)**\nin paragraph (2)(A), by striking is enrolled under section 1866(j) and inserting except in the case of a facility described in paragraph (3)(B) ;\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (B), by striking the period at the end and inserting ; or ;\n**(B)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and adjusting the margins accordingly;\n**(C)**\nby striking facility that as of and inserting\nfacility\u2014 (A) that as of ; and\n**(D)**\nby adding at the end the following new subparagraph:\n(B) that\u2014 (i) during the period beginning January 1, 2014, and ending December 26, 2020\u2014 (I) was a critical access hospital; or (II) was a subsection (d) hospital (as defined in section 1886(d)(1)(B)) located in a county (or equivalent unit of local government) in a rural area (as defined in section 1886(d)(2)(D)); and (ii) as of the date of the enactment of this subparagraph, had ceased operations. ; and\n**(3)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraph (A)(i), by striking An action plan and inserting Except in the case of a facility described in paragraph (3)(B), an action plan ; and\n**(B)**\nin subparagraph (B)(i), by inserting except in the case of a facility described in paragraph (3)(B), before the facility .\n##### (b) Amendments to payment rules\nSection 1834(x) of the Social Security Act ( 42 U.S.C. 1395m(x) ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting , except that, in the case of a facility described in section 1861(kkk)(3)(B) that, as of the date on which such facility submits an application under section 1866(j) to enroll under this title as a rural emergency hospital, is located less than 35 miles away from the nearest hospital, critical access hospital, or rural emergency hospital, such increase shall not apply before the period at the end; and\n**(2)**\nin paragraph (2)(A), by inserting (other than a facility described in section 1861(kkk)(3)(B) that, as of the date on which such facility submits an application under section 1866(j) to enroll under this title as a rural emergency hospital, is located less than 10 miles away from the nearest hospital, critical access hospital, or rural emergency hospital) after rural emergency hospital .\n##### (c) Effective date\nThe amendments made by this section shall apply beginning January 1, 2027.",
      "versionDate": "2025-03-03",
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
        "name": "Health",
        "updateDate": "2025-03-19T13:21:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119hr1775",
          "measure-number": "1775",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2026-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1775v00",
            "update-date": "2026-02-13"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Second Chances for Rural Hospitals Act</strong></p><p>This bill allows additional hospitals to qualify as rural emergency hospitals (REHs) under Medicare.</p><p>In 2020, Congress established REHs as a new Medicare provider designation for hospitals in rural areas providing emergency department services, observation care, and other outpatient medical and health services for which the annual per patient average length of stay does not exceed 24 hours. These hospitals must have been open as of December 27, 2020, in order to qualify for the new REH designation.\u00a0</p><p>The bill allows hospitals that were open between January 1, 2014, and December 26, 2020, to also qualify for the REH designation, and it provides for a specific payment structure for these hospitals. The bill's changes take effect beginning in 2027.</p>"
        },
        "title": "Second Chances for Rural Hospitals Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1775.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Second Chances for Rural Hospitals Act</strong></p><p>This bill allows additional hospitals to qualify as rural emergency hospitals (REHs) under Medicare.</p><p>In 2020, Congress established REHs as a new Medicare provider designation for hospitals in rural areas providing emergency department services, observation care, and other outpatient medical and health services for which the annual per patient average length of stay does not exceed 24 hours. These hospitals must have been open as of December 27, 2020, in order to qualify for the new REH designation.\u00a0</p><p>The bill allows hospitals that were open between January 1, 2014, and December 26, 2020, to also qualify for the REH designation, and it provides for a specific payment structure for these hospitals. The bill's changes take effect beginning in 2027.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1775"
    },
    "title": "Second Chances for Rural Hospitals Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Second Chances for Rural Hospitals Act</strong></p><p>This bill allows additional hospitals to qualify as rural emergency hospitals (REHs) under Medicare.</p><p>In 2020, Congress established REHs as a new Medicare provider designation for hospitals in rural areas providing emergency department services, observation care, and other outpatient medical and health services for which the annual per patient average length of stay does not exceed 24 hours. These hospitals must have been open as of December 27, 2020, in order to qualify for the new REH designation.\u00a0</p><p>The bill allows hospitals that were open between January 1, 2014, and December 26, 2020, to also qualify for the REH designation, and it provides for a specific payment structure for these hospitals. The bill's changes take effect beginning in 2027.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1775"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1775ih.xml"
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
      "title": "Second Chances for Rural Hospitals Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Second Chances for Rural Hospitals Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to modify the criteria for designation of rural emergency hospitals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T03:03:22Z"
    }
  ]
}
```
