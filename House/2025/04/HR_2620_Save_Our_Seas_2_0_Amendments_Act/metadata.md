# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2620?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2620
- Title: Save Our Seas 2.0 Amendments Act
- Congress: 119
- Bill type: HR
- Bill number: 2620
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-01-05T21:58:28Z
- Update date including text: 2026-01-05T21:58:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2620",
    "number": "2620",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Save Our Seas 2.0 Amendments Act",
    "type": "HR",
    "updateDate": "2026-01-05T21:58:28Z",
    "updateDateIncludingText": "2026-01-05T21:58:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-03T20:52:15Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-03T15:00:50Z",
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
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "AS"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2620ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2620\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Ms. Bonamici (for herself, Mrs. Radewagen , and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Save Our Seas 2.0 Act to improve the administration of the Marine Debris Foundation, to amend the Marine Debris Act to improve the administration of the Marine Debris Program of the National Oceanic and Atmospheric Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Save Our Seas 2.0 Amendments Act .\n#### 2. Modifications to the marine debris program of the national oceanic and atmospheric administration\n##### (a) In general\nThe Marine Debris Act ( Public Law 109\u2013449 ) is amended\u2014\n**(1)**\nby inserting before section 3 the following:\nA NOAA And Coast Guard Programs ; and\n**(2)**\nby redesignating sections 3 through 6 as sections 101 through 104, respectively.\n##### (b) Grants, cooperative agreements, contracts, and other agreements\nSection 101(d) of the Marine Debris Act ( 33 U.S.C. 1952(d) ), as redesignated by this Act, is amended\u2014\n**(1)**\nin the subsection heading by striking AND CONTRACTS and inserting CONTRACTS, AND OTHER AGREEMENTS ;\n**(2)**\nin paragraph (1) by striking and contracts and inserting , contracts, and other agreements ;\n**(3)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (B)\u2014\n**(i)**\nby striking part of the and inserting part of a ; and\n**(ii)**\nby inserting or (C) after subparagraph (A) ; and\n**(B)**\nin subparagraph (C) in the matter preceding clause (i) by inserting and except as provided in subparagraph (B) after subparagraph (A) ; and\n**(4)**\nby adding at the end the following:\n(7) In-kind contributions With respect to any project carried out pursuant to a contract or other agreement entered into under paragraph (1) that is not a cooperative agreement or an agreement to provide financial assistance in the form of a grant, the Under Secretary may contribute on an in-kind basis the portion of the costs of the project that the Under Secretary determines represents the amount of benefit the National Oceanic and Atmospheric Administration derives from the project. .\n#### 3. Modifications to the marine debris foundation\n##### (a) In general\nSubtitle B of title I of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ) is transferred to appear after section 104 of the Marine Debris Act ( Public Law 109\u2013449 ), as redesignated by this Act.\n##### (b) Status of foundation\nSection 111(a) of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred by this Act, is amended, in the second sentence, by striking organization and inserting corporation .\n##### (c) Purposes\nSection 111(b) of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred and redesignated by this Act, is amended\u2014\n**(1)**\nin paragraph (3) by inserting Indian Tribes, after Tribal governments, ; and\n**(2)**\nin paragraph (4) by striking title II and inserting subtitle C .\n##### (d) Board of directors\n**(1) Appointment, vacancies, and removal**\nSection 112(b) of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred by this Act, is amended\u2014\n**(A)**\nby redesignating paragraphs (1) through (5) as paragraphs (2) through (6) respectively;\n**(B)**\nby inserting before paragraph (2), as redesignated, the following:\n(1) Recommendations of board regarding appointments For appointments made under paragraph (2), the Board shall submit to the Under Secretary recommendations on candidates for appointment. ;\n**(C)**\nin paragraph (2), as redesignated, in the matter preceding subparagraph (A)\u2014\n**(i)**\nby striking and considering and inserting considering ; and\n**(ii)**\nby inserting and with the approval of the Secretary of Commerce, after by the Board, ;\n**(D)**\nby amending paragraph (3), as redesignated, to read as follows:\n(3) Terms Any Director appointed under paragraph (2) shall be appointed for a term of 6 years. ;\n**(E)**\nin paragraph (4)(A), as redesignated, by inserting with the approval of the Secretary of Commerce after the Board ; and\n**(F)**\nin paragraph (6), as redesignated\u2014\n**(i)**\nby inserting the Administrator of the United States Agency for International Development, after Service, ; and\n**(ii)**\nby inserting and with the approval of the Secretary of Commerce after EPA Administrator .\n**(2) General powers**\nSection 112(g) of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred by this Act, is amended\u2014\n**(A)**\nin paragraph (1)(A) by striking officers and employees and inserting the initial officers and employees ; and\n**(B)**\nin paragraph (2)(B)(i) by striking its chief operating officer and inserting the chief executive officer of the Foundation .\n**(3) Chief executive officer**\nSection 112 of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred by this Act, is amended by adding at the end the following:\n(h) Chief executive officer (1) Appointment; removal; review The Board shall appoint and review the performance of, and may remove, the chief executive officer of the Foundation. (2) Powers The chief executive officer of the Foundation may appoint, remove, and review the performance of any officer or employee of the Foundation. .\n##### (e) Powers of foundation\nSection 113(c)(1) of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred by this Act, is amended in the matter preceding subparagraph (A)\u2014\n**(1)**\nby inserting nonprofit before corporation ; and\n**(2)**\nby striking acting as a trustee and inserting formed .\n##### (f) Principal office\nSection 113 of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred by this Act, is amended by adding at the end the following:\n(g) Principal office The Board shall locate the principal office of the Foundation in the National Capital Region, as such term is defined in section 2674(f)(2) of title 10, United States Code, or a coastal shoreline community. .\n##### (g) Best practices; rule of construction\nSection 113 of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred by this Act and amended by subsection (e), is further amended by adding at the end the following:\n(h) Best practices (1) In general The Foundation shall develop and implement best practices for conducting outreach to Indian Tribes and Tribal Governments. (2) Requirements The best practices developed under paragraph (1) shall\u2014 (A) include a process to support technical assistance and capacity building to improve outcomes; and (B) promote an awareness of programs and grants available under this Act. (i) Rule of construction Nothing in this Act may be construed\u2014 (1) to satisfy any requirement for government-to-government consultation with Tribal Governments; or (2) to affect or modify any treaty or other right of any Tribal Government. .\n##### (h) Authorization of appropriations\nSection 118(a) of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred by this Act, is amended\u2014\n**(1)**\nin paragraph (1), by inserting and $2,000,000 for fiscal year 2025 after through 2024 ; and\n**(2)**\nin paragraph (2), by striking and State and local government agencies and inserting , State and local government agencies, regional organizations, Indian Tribes, Tribal organizations, and foreign governments .\n##### (i) Reauthorization\nSection 9(a) of the Marine Debris Act ( Public Law 109\u2013449 ) is amended by striking for the first place it appears and all that follows through carrying out and inserting for each of fiscal years 2018 through 2029 for carrying out .\n#### 4. Transfers\n##### (a) Save our seas 2.0 act\nSubtitle C of title I of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ) is transferred to appear after section 119 of the Marine Debris Act ( Public Law 109\u2013449 ) as transferred and redesignated by this Act.\n##### (b) Marine debris act\nThe Marine Debris Act ( Public Law 109\u2013449 ) is amended\u2014\n**(1)**\nby transferring sections 7, 8, 9 (as amended), and 10 to appear after section 127, as transferred by this Act, and redesignated as sections 131, 132, 133, and 134, respectively; and\n**(2)**\nby inserting before section 131, as so transferred and redesignated, the following:\nD Administration .\n#### 5. Definitions\n##### (a) In general\nSection 131 of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred and redesignated by this Act, is amended\u2014\n**(1)**\nby striking paragraph (1);\n**(2)**\nby redesignating paragraphs (2), (3), (4), (5), (6), and (7) as paragraphs (5), (6), (7), (11), (12), and (13), respectively;\n**(3)**\nby inserting before paragraph (5), as so redesignated, the following:\n(1) Circular economy The term circular economy has the meaning given such term in section 2 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ). (2) Coastal shoreline community The term coastal shoreline community means a city or county directly adjacent to the open ocean, major estuaries, or the Great Lakes. (3) EPA administrator The term EPA Administrator has the meaning given such term in section 2 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ). (4) Indian Tribe The term Indian Tribe has the meaning given that term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). ;\n**(4)**\nby inserting before paragraph (11), as so redesignated, the following:\n(9) Nonprofit organization The term nonprofit organization has the meaning given such term in section 2 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ). (10) Post-consumer materials management The term post-consumer materials management has the meaning given such term in section 2 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ). ;\n**(5)**\nby inserting after paragraph (13), as so redesignated, the following:\n(14) Tribal Government The term Tribal Government means the recognized governing body of any Indian or Alaska Native Tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently as of the date of the enactment of the Save Our Seas 2.0 Amendments Act pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ). (15) Tribal organization The term Tribal organization has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (16) Under secretary The term Under Secretary has the meaning given such term in section 2 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ). ; and\n**(6)**\nin paragraph (13), as so redesignated\u2014\n**(A)**\nby redesignating subparagraphs (B), (C), and (D) as subparagraphs (C), (D), and (E); and\n**(B)**\nby inserting after subparagraph (A) the following:\n(B) Indian Tribe; .\n##### (b) Transfer\n**(1) In general**\nSection 2(7) of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ) is transferred to section 131 of the Marine Debris Act ( Public Law 109\u2013449 ), inserted after paragraph (7) (as redesignated), and redesignated as paragraph (8).\n**(2) Redesignation**\nSection 2 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ) is amended by redesignating paragraphs (8) through (11) as paragraphs (7) through (10), respectively.\n##### (c) Non-federal funds\nParagraph (8)(D) of section 131 of the Marine Debris Act ( Public Law 109\u2013449 ), as transferred and redesignated by this Act, is amended by striking (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) .\n#### 6. Conforming amendments\n##### (a) In general\nSections 1 and 2 of the Marine Debris Act, sections 101, 102, and 104 of the Marine Debris Act, as redesignated by this Act, and section 133 of the Marine Debris Act, as transferred and so redesignated by this Act, are amended by striking Administrator and inserting Under Secretary .\n##### (b) Section 103\nSection 103 of the Marine Debris Act is amended by\u2014\n**(1)**\nstriking Administrator of the National Oceanic and Atmospheric Administration and inserting Under Secretary ;\n**(2)**\nstriking Administrator of the Environmental Protection Agency and inserting EPA Administrator ; and\n**(3)**\nin subsection (e)(3) by striking section 3 and inserting section 101 .\n##### (c) Section 123\nSection 123 of the Marine Debris Act, as transferred and so redesignated by this Act, is amended by striking title I and inserting subtitle B .\n##### (d) Section 133\nSection 133 of the Marine Debris Act, as transferred and so redesignated by this Act, is amended by striking sections 3, 5, and 6 and inserting sections 101, 103, and 104 .\n##### (e) Section 134\nSection 134 of the Marine Debris Act, as transferred and so redesignated by this Act, is amended by striking Administrator of the Environmental Protection Agency and inserting EPA Administrator .\n##### (f) Tribal Government\nSubtitle A of the Marine Debris Act, as designated in this Act, is amended by striking tribal government and inserting Tribal Government .",
      "versionDate": "2025-04-03",
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
        "actionDate": "2025-12-26",
        "text": "Signed by President."
      },
      "number": "216",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Save Our Seas 2.0 Amendments Act",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-28T14:22:25Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2620ih.xml"
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
      "title": "Save Our Seas 2.0 Amendments Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save Our Seas 2.0 Amendments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Save Our Seas 2.0 Act to improve the administration of the Marine Debris Foundation, to amend the Marine Debris Act to improve the administration of the Marine Debris Program of the National Oceanic and Atmospheric Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T05:48:25Z"
    }
  ]
}
```
