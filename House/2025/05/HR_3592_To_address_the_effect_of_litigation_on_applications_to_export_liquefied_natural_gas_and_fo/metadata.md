# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3592?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3592
- Title: Protect LNG Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3592
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-12-05T22:02:11Z
- Update date including text: 2025-12-05T22:02:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3592",
    "number": "3592",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "H001095",
        "district": "38",
        "firstName": "Wesley",
        "fullName": "Rep. Hunt, Wesley [R-TX-38]",
        "lastName": "Hunt",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Protect LNG Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:02:11Z",
    "updateDateIncludingText": "2025-12-05T22:02:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:05:05Z",
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
          "date": "2025-05-23T14:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "WI"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "TX"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "WA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3592ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3592\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Hunt introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo address the effect of litigation on applications to export liquefied natural gas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect LNG Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Covered application**\nThe term covered application means an application for\u2014\n**(A)**\nan authorization to export natural gas under section 3(a) of the Natural Gas Act ( 15 U.S.C. 717b(a) ); or\n**(B)**\nan authorization to site, construct, expand, or operate a covered facility under section 3(e) of the Natural Gas Act ( 15 U.S.C. 717b(e) ).\n**(2) Covered facility**\nThe term covered facility means a liquefied natural gas facility for which a proposal to site, construct, expand, or operate is required to be approved by\u2014\n**(A)**\nthe Secretary; and\n**(B)**\n**(i)**\nthe Federal Energy Regulatory Commission; or\n**(ii)**\nthe Maritime Administration.\n**(3) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 3. Effect of litigation on applications to export liquefied natural gas\n##### (a) Effect of litigation\nA civil action relating to an environmental review under the Natural Gas Act ( 15 U.S.C. 717 et seq. ) or the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) with respect to a covered facility shall not affect the validity of a permit, license, or approval issued to the covered facility that is the subject of the civil action.\n##### (b) Remand; processing of covered applications\nIf, in a civil action described in subsection (a), the environmental review for a permit, license, or approval issued to the covered facility that is the subject of the civil action is found by the applicable court to violate the Natural Gas Act ( 15 U.S.C. 717 et seq. ) or the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. )\u2014\n**(1)**\nnotwithstanding chapter 5 or 7 of title 5, United States Code (commonly referred to as the Administrative Procedure Act ), the applicable court shall not set aside or vacate the permit, license, or approval issued to the covered facility but instead remand the matter to the relevant Federal agency to resolve the violation; and\n**(2)**\nthe relevant Federal agency shall continue to process all covered applications.\n#### 4. Action on covered applications\n##### (a) Judicial review\nExcept for review in the Supreme Court of the United States, the court of appeals of the United States for the circuit in which a covered facility is, or will be, located pursuant to a covered application shall have original and exclusive jurisdiction over any civil action for the review of an order issued by a Federal agency with respect to the covered application.\n##### (b) Expedited review\nThe applicable United States Court of Appeals under subsection (a) shall\u2014\n**(1)**\nset any civil action brought under this subsection for expedited review; and\n**(2)**\nset the action on the docket as soon as practicable after the filing date of the initial pleading.\n##### (c) Transfer of existing actions\nIn the case of a covered application for which a petition for review has been filed as of the date of enactment of this Act, the petition shall be\u2014\n**(1)**\non a motion by the applicant, transferred to the court of appeals of the United States in which the covered facility that is the subject of the covered application is, or will be, located; and\n**(2)**\nadjudicated in accordance with this section.\n##### (d) Limitation on claims\nNotwithstanding any other provision of law, a claim arising under Federal law seeking judicial review of a permit, license, or approval issued by a Federal agency for a covered facility pursuant to a covered application shall be barred unless the claim is filed not later than 90 days after publication of a notice in the Federal Register announcing that the permit, license, or approval is final pursuant to the law under which the agency action is taken, unless a shorter time is specified in the Federal law pursuant to which judicial review is allowed.\n##### (e) Savings clause\nNothing in this section establishes a right to judicial review or places any limit on filing a claim that a person has violated the terms of a permit, license, or approval.",
      "versionDate": "2025-05-23",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "1901",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protect LNG Act of 2025",
      "type": "S"
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
            "name": "Civil actions and liability",
            "updateDate": "2025-09-19T19:47:52Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-19T19:47:43Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-09-19T19:48:00Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-19T19:47:47Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-09-19T19:47:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-06-12T14:58:42Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3592ih.xml"
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
      "title": "Protect LNG Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect LNG Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address the effect of litigation on applications to export liquefied natural gas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:33:40Z"
    }
  ]
}
```
