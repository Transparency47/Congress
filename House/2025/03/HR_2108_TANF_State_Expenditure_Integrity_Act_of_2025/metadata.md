# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2108
- Title: TANF State Expenditure Integrity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2108
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-05-30T19:41:22Z
- Update date including text: 2026-05-30T19:41:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2108",
    "number": "2108",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "D000096",
        "district": "7",
        "firstName": "Danny",
        "fullName": "Rep. Davis, Danny K. [D-IL-7]",
        "lastName": "Davis",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "TANF State Expenditure Integrity Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T19:41:22Z",
    "updateDateIncludingText": "2026-05-30T19:41:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:07:05Z",
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
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "PA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "WI"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MS"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "VA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NV"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2108ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2108\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Davis of Illinois (for himself, Ms. Chu , Mr. Evans of Pennsylvania , Mr. Gomez , Ms. Moore of Wisconsin , and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo prevent and address intentional misuse of subrecipient TANF funds.\n#### 1. Short title\nThis Act may be cited as the TANF State Expenditure Integrity Act of 2025 .\n#### 2. Authority to prevent and address intentional misuse of subrecipient funds under the TANF program\n##### (a) In general\nSection 417 of the Social Security Act ( 42 U.S.C. 617 ) is amended\u2014\n**(1)**\nby inserting (a) In general.\u2014 before No ; and\n**(2)**\nby adding at the end the following:\n(b) Authority To prevent intentional misuse of subrecipient funds (1) Subrecipient monitoring (A) In general The Secretary\u2014 (i) shall develop a framework for the monitoring of subrecipient use of funds provided under section 403(a)(1) of this Act, for the purpose of identifying intentional misuse, to supplement single State audits conducted under chapter 75 of title 31, United States Code; (ii) may establish State plan requirements or formats relating to clause (i); and (iii) may require States to report to the Secretary such information to supplement the report provided under section 411(a) as the Secretary determines is necessary to enable the Secretary to comply with clauses (i) and (ii) of this subparagraph. (B) No effect on single State audit authority Clause (i) of this subparagraph shall not be interpreted to limit the authority of the Secretary to conduct single State audits under chapter 75 of title 31, United States Code. (2) Program Integrity Unit authorization and funding (A) TANF Program Integrity Unit The Secretary shall create a TANF Program Integrity Unit at the Administration for Children & Families, which shall conduct the monitoring described in paragraph (1)(A)(i). (B) Appropriation Out of any money in the Treasury not otherwise appropriated, the amount made available in section 403(a)(1)(C) for each fiscal year shall be increased by $10,000,000, and the amount of the increase shall be available for the staffing and operations of the TANF Program Integrity Unit and related functions. (3) Annual report to the Congress The Secretary shall submit an annual report to the Congress on the activities undertaken under paragraph (2)(A) in the fiscal year covered by the report. .\n##### (b) Remedies\nSection 409(a)(1)(B) of such Act ( 42 U.S.C. 609(a)(1)(B) ) is amended\u2014\n**(1)**\nby striking (B) Enhanced penalty for intentional violations.\u2014 If and inserting the following:\n(B) Enhanced penalty for intentional violations (i) In general If ; and\n**(2)**\nby adding at the end the following:\n(ii) Additional remedies If the Secretary finds, as a result of subrecipient monitoring under section 417(b)(1) of this Act, that an amount has been intentionally misused in violation of this part, then the Secretary shall\u2014 (I) notify the State involved of the finding; and (II) in addition to any penalty imposed under clause (i), require the State to expend, in addition to any other amount required to be expended under the State program funded under this part, an amount equal to the amount so misused, for the provision of cash assistance directly to families with an income below 100 percent of the poverty line (as defined in section 673(2) of the Omnibus Budget Reconciliation Act of 1981, including any revision required by such section, applicable to a family of the size involved). .\n##### (c) Deadline for publication of notice of rulemaking\nWithin 2 years after the date of the enactment of this Act, the Secretary of Health and Human Services shall publish a notice of rulemaking to implement the amendments made by this section.\n##### (d) Effective date\nThe amendments made by this section shall take effect on the later of\u2014\n**(1)**\nthe 1st day of the 5th calendar quarter that begins after the date of the enactment of this Act; or\n**(2)**\nthe 1st day of the 1st Federal fiscal year that begins after such date of enactment.",
      "versionDate": "2025-03-14",
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
        "name": "Social Welfare",
        "updateDate": "2025-05-13T15:51:19Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2108ih.xml"
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
      "title": "TANF State Expenditure Integrity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TANF State Expenditure Integrity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent and address intentional misuse of subrecipient TANF funds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:20Z"
    }
  ]
}
```
