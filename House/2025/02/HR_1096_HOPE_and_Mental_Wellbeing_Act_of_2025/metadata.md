# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1096?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1096
- Title: HOPE and Mental Wellbeing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1096
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-04-28T20:21:20Z
- Update date including text: 2025-04-28T20:21:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1096",
    "number": "1096",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001226",
        "district": "6",
        "firstName": "Andrea",
        "fullName": "Rep. Salinas, Andrea [D-OR-6]",
        "lastName": "Salinas",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "HOPE and Mental Wellbeing Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-28T20:21:20Z",
    "updateDateIncludingText": "2025-04-28T20:21:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-06T15:02:25Z",
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
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "DC"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "NY"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "HI"
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
      "sponsorshipDate": "2025-03-11",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1096ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1096\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Ms. Salinas (for herself, Mrs. Watson Coleman , Ms. Norton , Mr. Doggett , and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to require coverage of 3 primary care visits without cost sharing each year under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Helping Out Patients for Emotional and Mental Wellbeing Act or the HOPE and Mental Wellbeing Act of 2025 .\n#### 2. Requiring coverage of 3 primary care visits without cost sharing each year under Medicare\n##### (a) Medicare\n**(1) In general**\nSection 1833 of the Social Security Act ( 42 U.S.C. 1395l ) is amended\u2014\n**(A)**\nin subsection (a)(1)\u2014\n**(i)**\nby striking and before (HH) ; and\n**(ii)**\nby inserting before the semicolon at the end the following: , and (II) with respect to the first 3 primary care visits (as defined in section 1861(nnn)) furnished to an individual during a year (beginning with 2026) for which payment may be made under a specified outpatient payment provision described in subsection (cc)(2), the amounts paid shall be 100 percent of the lesser of the actual charge or the payment amount otherwise recognized under such respective specified outpatient payment provision for such visit ; and\n**(B)**\nin subsection (b), in the first sentence\u2014\n**(i)**\nby striking and before (13) ;\n**(ii)**\nin paragraph (13), by striking .. and inserting a period; and\n**(iii)**\nby inserting before the period at the end the following: , and (13) shall not apply with respect to the first 3 primary care visits (as defined in section 1861(nnn)) furnished to an individual during a year (beginning with 2026) for which payment may be made under a specified outpatient payment provision described in subsection (cc)(2) .\n**(2) Medicare Advantage**\nSection 1852(a)(1)(B) of the Social Security Act ( 42 U.S.C. 1395w\u201322(a)(1)(B) ) is amended\u2014\n**(A)**\nin clause (iv)\u2014\n**(i)**\nby redesignating subclause (VIII) as subclause (IX); and\n**(ii)**\nby inserting after subclause (VII) the following new subclause:\n(VIII) the first 3 primary care visits (as defined in section 1861(nnn)) furnished to an enrollee during a year (beginning with 2026). ; and\n**(B)**\nin clause (v), by striking and (VII) and inserting (VII), and (VIII) .\n**(3) Definition**\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended by adding at the end the following new subsection:\n(nnn) Primary care visit The term primary care visit means outpatient mental and behavioral health services, nonspecialty medical services, and care coordination services furnished for the prevention, diagnosis, treatment, or management of a physical, mental, or behavioral health condition. .\n##### (b) Medicaid\n**(1) In general**\nSection 1916 of the Social Security Act ( 42 U.S.C. 1396o ) is amended\u2014\n**(A)**\nin subsection (a)(2)\u2014\n**(i)**\nin subparagraph (I), by striking or at the end;\n**(ii)**\nin subparagraph (J), by striking ; and at the end and inserting , or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(K) the first 3 primary care visits (as defined in section 1861(nnn)) furnished to an individual during a year (beginning with 2026) for which payment may be made under this title; and ; and\n**(B)**\nin subsection (b)(2)\u2014\n**(i)**\nin subparagraph (I), by striking or at the end;\n**(ii)**\nin subparagraph (J), by striking ; and at the end and inserting , or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(K) the first 3 primary care visits (as defined in section 1861(nnn)) furnished to an individual during a year (beginning with 2026); and .\n**(2) Application to alternative cost sharing**\nSection 1916A(b)(3)(B) of the Social Security Act ( 42 U.S.C. 1396o\u20131(b)(3)(B) ) is amended by adding at the end the following new clause:\n(xv) The first 3 primary care visits (as defined in section 1861(nnn)) furnished to an individual during a year (beginning with 2026). .",
      "versionDate": "2025-02-06",
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
            "name": "Health care coverage and access",
            "updateDate": "2025-04-24T15:51:43Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-04-24T15:51:43Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-04-24T15:51:43Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-04-24T15:51:43Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-24T15:51:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-11T13:31:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119hr1096",
          "measure-number": "1096",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-06",
          "originChamber": "HOUSE",
          "update-date": "2025-04-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1096v00",
            "update-date": "2025-04-28"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Helping Out Patients for Emotional and Mental Wellbeing Act or the HOPE and Mental Wellbeing Act of 2025</strong></p><p>This bill provides for coverage under Medicare and Medicaid of three primary care visits per year without cost-sharing. </p>"
        },
        "title": "HOPE and Mental Wellbeing Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1096.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Helping Out Patients for Emotional and Mental Wellbeing Act or the HOPE and Mental Wellbeing Act of 2025</strong></p><p>This bill provides for coverage under Medicare and Medicaid of three primary care visits per year without cost-sharing. </p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr1096"
    },
    "title": "HOPE and Mental Wellbeing Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Helping Out Patients for Emotional and Mental Wellbeing Act or the HOPE and Mental Wellbeing Act of 2025</strong></p><p>This bill provides for coverage under Medicare and Medicaid of three primary care visits per year without cost-sharing. </p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr1096"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1096ih.xml"
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
      "title": "HOPE and Mental Wellbeing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-08T06:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOPE and Mental Wellbeing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Out Patients for Emotional and Mental Wellbeing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to require coverage of 3 primary care visits without cost sharing each year under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:20Z"
    }
  ]
}
```
