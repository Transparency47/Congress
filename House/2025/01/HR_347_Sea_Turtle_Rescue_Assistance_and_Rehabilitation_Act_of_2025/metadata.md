# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/347?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/347
- Title: Sea Turtle Rescue Assistance and Rehabilitation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 347
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2026-05-15T08:08:15Z
- Update date including text: 2026-05-15T08:08:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/347",
    "number": "347",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "K000375",
        "district": "9",
        "firstName": "William",
        "fullName": "Rep. Keating, William R. [D-MA-9]",
        "lastName": "Keating",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Sea Turtle Rescue Assistance and Rehabilitation Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-15T08:08:15Z",
    "updateDateIncludingText": "2026-05-15T08:08:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MO"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "SC"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "RI"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "VA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "SC"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "OK"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
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
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "SC"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "CA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NC"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "GA"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "VA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "CT"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "GA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "SC"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "OH"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "SC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr347ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 347\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Keating introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of Commerce to establish the Sea Turtle Rescue Assistance Grant Program.\n#### 1. Short title\nThis Act may be cited as the Sea Turtle Rescue Assistance and Rehabilitation Act of 2025 .\n#### 2. Sea turtle rescue, rehabilitation, and response\nSection 408 of the Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1421f\u20131 ) is amended\u2014\n**(1)**\nin subsection (b), by adding at the end the following:\n(10) Sea turtle rescue, rehabilitation, and response (A) In general Subject to the availability of appropriations specific to address sea turtle rescue, rehabilitation, and response, the Secretary of Commerce and the Director of the United States Fish and Wildlife Service shall include separate eligibility for grants under this subsection to address the purposes described in paragraph (2) with respect to sea turtles. (B) Conditions of grant A grant awarded under this subsection to address sea turtle rescue, rehabilitation, and response shall\u2014 (i) include the equivalent grant criteria and administration authorities and requirements described under paragraph (3), subparagraphs (A) and (B) of paragraph (4), and paragraphs (5) through (9), developed, as appropriate, and awarded separately for sea turtles and in consultation with the United States Fish and Wildlife Service in lieu of the Marine Mammal Commission; and (ii) in addition to the considerations under paragraph (4)(B), also consider rehabilitation of stranded sea turtles. (C) Eligibility criteria In order to apply for a grant awarded under this subsection to address sea turtle rescue, rehabilitation, and response, an entity shall\u2014 (i) submit an application described in paragraph (5) to the Secretary of Commerce with respect to sea turtles; (ii) be authorized by and in compliance with\u2014 (I) an authorization issued under section 10(a)(1)(A) of the Endangered Species Act of 1973 ( 16 U.S.C. 1539(a)(1)(A) ) with respect to sea turtles; or (II) a cooperative agreement entered into under section 6 of the Endangered Species Act of 1973 ( 16 U.S.C. 1535 ) with respect to sea turtles; (iii) comply with the standard conditions for care and maintenance of captive sea turtles prescribed by the Secretary of the Interior when relevant facilities will be utilized for such purposes; and (iv) comply with all relevant data reporting requirements, such as the Sea Turtle Stranding and Salvage Network data collection requirements. (D) Sunset The authority of the Secretary of Commerce and the Director of the United States Fish and Wildlife Service to carry out this paragraph shall terminate on the date that is 7 years after the date of the enactment of this paragraph. ;\n**(2)**\nby striking subsection (c) and inserting the following:\n(c) Rescue and rapid response funds (1) In general There is established in the Treasury of the United States\u2014 (A) an interest-bearing fund to known as the Joseph R. Geraci Marine Mammal Rescue and Rapid Response Fund ; and (B) an interest-bearing fund to be known as the Sea Turtle Rescue, Rehabilitation, and Rapid Response Fund . (2) Use of funds Amounts in the funds established under paragraph (1) shall be available only for use by the Secretary to provide emergency assistance. ; and\n**(3)**\nin subsection (d)(1)(A), by inserting marine mammal rescue and response after to carry out the .",
      "versionDate": "2025-01-13",
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
        "actionDate": "2026-03-24",
        "actionTime": "14:11:33",
        "text": "Held at the desk."
      },
      "number": "843",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Sea Turtle Rescue Assistance and Rehabilitation Act of 2025",
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
        "name": "Animals",
        "updateDate": "2025-02-12T15:26:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr347",
          "measure-number": "347",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr347v00",
            "update-date": "2025-04-01"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sea Turtle Rescue Assistance and Rehabilitation Act of 2025</strong></p><p>This bill expands the John H. Prescott Marine Mammal Rescue and Response Grant Program to include separate grants to rescue sea turtles for the next seven years. The grants must be used for</p><ul><li>the recovery, care, or treatment of sick, injured, or entangled sea turtles;</li><li>responses to rescue stranded sea turtles;</li><li>the collection of data and samples from living or dead stranded sea turtles for scientific research or health assessments;</li><li>facility operating costs that are directly related to activities to assist sea turtles; or\u00a0</li><li>development of stranding network capacity where facilities do not exist or are sparse.</li></ul><p>In addition, the bill establishes the Sea Turtle Rescue, Rehabilitation, and Rapid Response Fund.</p>"
        },
        "title": "Sea Turtle Rescue Assistance and Rehabilitation Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr347.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sea Turtle Rescue Assistance and Rehabilitation Act of 2025</strong></p><p>This bill expands the John H. Prescott Marine Mammal Rescue and Response Grant Program to include separate grants to rescue sea turtles for the next seven years. The grants must be used for</p><ul><li>the recovery, care, or treatment of sick, injured, or entangled sea turtles;</li><li>responses to rescue stranded sea turtles;</li><li>the collection of data and samples from living or dead stranded sea turtles for scientific research or health assessments;</li><li>facility operating costs that are directly related to activities to assist sea turtles; or\u00a0</li><li>development of stranding network capacity where facilities do not exist or are sparse.</li></ul><p>In addition, the bill establishes the Sea Turtle Rescue, Rehabilitation, and Rapid Response Fund.</p>",
      "updateDate": "2025-04-01",
      "versionCode": "id119hr347"
    },
    "title": "Sea Turtle Rescue Assistance and Rehabilitation Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sea Turtle Rescue Assistance and Rehabilitation Act of 2025</strong></p><p>This bill expands the John H. Prescott Marine Mammal Rescue and Response Grant Program to include separate grants to rescue sea turtles for the next seven years. The grants must be used for</p><ul><li>the recovery, care, or treatment of sick, injured, or entangled sea turtles;</li><li>responses to rescue stranded sea turtles;</li><li>the collection of data and samples from living or dead stranded sea turtles for scientific research or health assessments;</li><li>facility operating costs that are directly related to activities to assist sea turtles; or\u00a0</li><li>development of stranding network capacity where facilities do not exist or are sparse.</li></ul><p>In addition, the bill establishes the Sea Turtle Rescue, Rehabilitation, and Rapid Response Fund.</p>",
      "updateDate": "2025-04-01",
      "versionCode": "id119hr347"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr347ih.xml"
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
      "title": "Sea Turtle Rescue Assistance and Rehabilitation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sea Turtle Rescue Assistance and Rehabilitation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Commerce to establish the Sea Turtle Rescue Assistance Grant Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:26Z"
    }
  ]
}
```
