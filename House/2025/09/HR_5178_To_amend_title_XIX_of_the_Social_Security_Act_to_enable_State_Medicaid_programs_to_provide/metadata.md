# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5178?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5178
- Title: Sickle Cell Disease Comprehensive Care Act
- Congress: 119
- Bill type: HR
- Bill number: 5178
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2026-04-23T08:07:14Z
- Update date including text: 2026-04-23T08:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5178",
    "number": "5178",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Sickle Cell Disease Comprehensive Care Act",
    "type": "HR",
    "updateDate": "2026-04-23T08:07:14Z",
    "updateDateIncludingText": "2026-04-23T08:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
          "date": "2025-09-08T16:02:45Z",
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
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "IL"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "GA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "AL"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-08",
      "state": "DC"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NJ"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "LA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "TX"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "MI"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "GA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "IL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NC"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "IL"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "AL"
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
      "sponsorshipDate": "2025-09-08",
      "state": "MS"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "MA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "IN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MI"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MD"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "DE"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "WA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "SC"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "VI"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "WI"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5178ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5178\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Mr. Dunn of Florida (for himself, Mr. Davis of Illinois , Mr. Carter of Georgia , Mr. Figures , Mr. Bilirakis , Ms. Johnson of Texas , Ms. Norton , Mrs. McIver , Mr. Fields , Mr. Green of Texas , Mr. Gottheimer , Ms. Tlaib , Mr. Johnson of Georgia , Mr. Jackson of Illinois , Mr. Davis of North Carolina , Mr. Soto , Ms. Budzinski , Ms. Sewell , Mr. Thompson of Mississippi , and Mr. Moulton ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to enable State Medicaid programs to provide comprehensive, coordinated care through a health home to individuals with sickle cell disease.\n#### 1. Short title\nThis Act may be cited as the Sickle Cell Disease Comprehensive Care Act .\n#### 2. Enabling State Medicaid programs to provide care through health homes to individuals with sickle cell disease\nSection 1945 of the Social Security Act ( 42 U.S.C. 1396w\u20134 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting (and, beginning January 1, 2026, to eligible individuals with sickle cell disease (as defined in subsection (c)(5))) after chronic conditions ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by inserting and each eligible individual with sickle cell disease after chronic conditions ; and\n**(B)**\nby adding at the end the following new paragraph:\n(5) Special rule relating to sickle cell disease health homes (A) In general Beginning January 1, 2026, the Secretary may approve a State plan amendment under this section that is designed to provide health home services primarily to eligible individuals with sickle cell disease (in this section referred to as a sickle cell disease-focused State plan amendment ). (B) Requirement to provide dental and vision services In the case of a sickle cell disease-focused State plan amendment approved by the Secretary on or after January 1, 2026, a State shall ensure the provision of dental and vision services to eligible individuals with sickle cell disease who are enrolled in such health home. Such requirement shall apply irrespective of existing requirements related to comparability or whether or not the State provides dental or vision services to other Medicaid beneficiaries. (C) Report requirements (i) In general In the case of a State with a sickle cell disease-focused State plan amendment, such State shall, not later than the last day of the 8th fiscal year quarter that such State plan amendment is in effect, submit to the Secretary a report on the following, with respect to eligible individuals with sickle cell disease provided health home services under such State plan amendment: (I) The quality of health care provided to such individuals, with a focus on outcomes relevant to the recovery of each such individual. (II) The access of such individuals to health care. (III) The total expenditures of such individuals for health care. (ii) Applicable measures For purposes of the report required under this subparagraph, the Secretary shall specify all applicable measures for determining quality of health care provided to eligible individuals with sickle cell disease, access to health care by such individuals, and expenditures on health care by such individuals. (D) Best practices Not later than June 30, 2026, the Secretary shall make publicly available on the website of the Centers for Medicare & Medicaid Services best practices for designing and implementing a sickle cell disease-focused State plan amendment, based on clinical practice guidelines for sickle cell disease developed by medical specialty societies and in consultation with sickle cell disease providers and patient advocacy organizations. (E) Definitions For purposes of this section: (i) Eligible individual with sickle cell disease The term eligible individual with sickle cell disease means, with respect to a State, an individual who satisfies all of the following: (I) The individual is eligible for medical assistance under the State plan of such State or under a waiver of such plan. (II) The individual has sickle cell disease. (III) The individual may or may not have previously received health home services under any other State plan amendment approved for the State under this section by the Secretary. (ii) Sickle cell disease The term sickle cell disease means an inherited blood disorder affecting red blood cells that occurs when an individual has inherited a sickle cell gene from each parent, as identified by a newborn screening or other genetic test. ; and\n**(3)**\nin subsection (h)(5), by inserting or a health home for eligible individuals with sickle cell disease after chronic conditions .",
      "versionDate": "2025-09-08",
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
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "721",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Sickle Cell Disease Comprehensive Care Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-23T17:37:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-08",
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
          "measure-id": "id119hr5178",
          "measure-number": "5178",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-08",
          "originChamber": "HOUSE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5178v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-09-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sickle Cell Disease Comprehensive Care Act</strong></p><p>This bill allows state Medicaid programs to establish health homes to provide coordinated care for individuals with sickle-cell disease. (Under current law, state Medicaid programs may establish health homes to provide coordinated care for individuals with specified chronic conditions.) States must ensure that such care includes dental and vision services.</p><p>The Centers for Medicare & Medicaid Services must issue best practices for states on how to design and implement such health homes.</p>"
        },
        "title": "Sickle Cell Disease Comprehensive Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5178.xml",
    "summary": {
      "actionDate": "2025-09-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sickle Cell Disease Comprehensive Care Act</strong></p><p>This bill allows state Medicaid programs to establish health homes to provide coordinated care for individuals with sickle-cell disease. (Under current law, state Medicaid programs may establish health homes to provide coordinated care for individuals with specified chronic conditions.) States must ensure that such care includes dental and vision services.</p><p>The Centers for Medicare & Medicaid Services must issue best practices for states on how to design and implement such health homes.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr5178"
    },
    "title": "Sickle Cell Disease Comprehensive Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sickle Cell Disease Comprehensive Care Act</strong></p><p>This bill allows state Medicaid programs to establish health homes to provide coordinated care for individuals with sickle-cell disease. (Under current law, state Medicaid programs may establish health homes to provide coordinated care for individuals with specified chronic conditions.) States must ensure that such care includes dental and vision services.</p><p>The Centers for Medicare & Medicaid Services must issue best practices for states on how to design and implement such health homes.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr5178"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5178ih.xml"
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
      "title": "Sickle Cell Disease Comprehensive Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sickle Cell Disease Comprehensive Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to enable State Medicaid programs to provide comprehensive, coordinated care through a health home to individuals with sickle cell disease.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:23Z"
    }
  ]
}
```
