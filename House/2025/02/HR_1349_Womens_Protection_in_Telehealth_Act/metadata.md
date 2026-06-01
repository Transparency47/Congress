# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1349?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1349
- Title: Women’s Protection in Telehealth Act
- Congress: 119
- Bill type: HR
- Bill number: 1349
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-12-02T09:05:54Z
- Update date including text: 2025-12-02T09:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1349",
    "number": "1349",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Women\u2019s Protection in Telehealth Act",
    "type": "HR",
    "updateDate": "2025-12-02T09:05:54Z",
    "updateDateIncludingText": "2025-12-02T09:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:05:00Z",
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
          "date": "2025-02-13T14:04:50Z",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "VA"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AZ"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "SC"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "FL"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1349ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1349\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Steube (for himself, Ms. Tenney , Mr. Haridopolos , Mr. McGuire , and Mr. Biggs of Arizona ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XI of the Social Security Act to exclude providers of certain abortion services from participation in the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Women\u2019s Protection in Telehealth Act .\n#### 2. Excluding providers of certain abortion services from participation in the Medicare program\nSection 1128 of the Social Security Act ( 42 U.S.C. 1320a\u20137 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by inserting (or, in the case of individuals and entities described in paragraph (5), from participation in the Medicare program under title XVIII) after (as defined in section 1128B(f)) ; and\n**(B)**\nby inserting after paragraph (4) the following new paragraph:\n(5) Provision of abortion-inducing drugs Any individual or entity that, on or after the date of the enactment of this paragraph, prescribes, administers, dispenses, or furnishes an abortion-inducing drug to a patient, unless such individual or entity\u2014 (A) is a physician; (B) physically examines the patient; (C) is physically present in the same room with the patient at the time the patient is administered, takes, or uses (as applicable) such drug; and (D) schedules an in-person follow-up visit for the patient to occur not more than 14 days after the patient is administered, takes, or uses (as applicable) such drug. ; and\n**(2)**\nin subsection (c)(3)\u2014\n**(A)**\nin subparagraph (A), by striking subsection (b)(12) and inserting subsection (a)(5) or (b)(12) ;\n**(B)**\nin subparagraph (B), by striking subparagraph (G) and inserting subparagraphs (G) and (H) ;\n**(C)**\nin subparagraph (G), by inserting (other than under paragraph (5) of such subsection) after subsection (a) ; and\n**(D)**\nby adding at the end the following new subparagraph:\n(H) In the case of an exclusion under subsection (a)(5), the exclusion shall be permanent. ;\n**(3)**\nin subsection (d), by adding at the end the following new paragraph:\n(4) The provisions of this subsection shall not apply in the case of an exclusion under subsection (a)(5). ;\n**(4)**\nin subsection (g), by adding at the end the following new paragraph:\n(4) The provisions of this subsection shall not apply in the case of an exclusion under subsection (a)(5). ; and\n**(5)**\nby adding at the end the following new subsection:\n(k) Abortion-Inducing drug defined (1) In general For purposes of subsection (a), the term abortion-inducing drug means any medicine, drug, or any other substance that is prescribed, administered, dispensed, or furnished with the intent of terminating the clinically diagnosable pregnancy of a woman and with knowledge that the termination will with reasonable likelihood cause the death of the unborn child (including the off-label use of any such drug). (2) Unborn child The term unborn child has the meaning given such term in section 1841 of title 18, United States Code. .",
      "versionDate": "2025-02-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-07-08T12:39:17Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-07-08T12:39:53Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2025-07-08T12:39:28Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-08T12:40:06Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-07-08T12:39:45Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-07-08T12:39:22Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-07-08T12:39:34Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-07-08T12:39:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T17:37:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1349",
          "measure-number": "1349",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-08-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1349v00",
            "update-date": "2025-08-05"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Women\u2019s Protection in Telehealth Act</strong></p><p>This bill excludes providers of abortion-inducing drugs from participating in Medicare unless the provider is a physician who physically examines the patient, is physically present when the drug is administered, and schedules an in-person follow-up visit with the patient within 14 days of administering the drug.</p>"
        },
        "title": "Women\u2019s Protection in Telehealth Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1349.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Women\u2019s Protection in Telehealth Act</strong></p><p>This bill excludes providers of abortion-inducing drugs from participating in Medicare unless the provider is a physician who physically examines the patient, is physically present when the drug is administered, and schedules an in-person follow-up visit with the patient within 14 days of administering the drug.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr1349"
    },
    "title": "Women\u2019s Protection in Telehealth Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Women\u2019s Protection in Telehealth Act</strong></p><p>This bill excludes providers of abortion-inducing drugs from participating in Medicare unless the provider is a physician who physically examines the patient, is physically present when the drug is administered, and schedules an in-person follow-up visit with the patient within 14 days of administering the drug.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr1349"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1349ih.xml"
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
      "title": "Women\u2019s Protection in Telehealth Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Women\u2019s Protection in Telehealth Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XI of the Social Security Act to exclude providers of certain abortion services from participation in the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:30Z"
    }
  ]
}
```
