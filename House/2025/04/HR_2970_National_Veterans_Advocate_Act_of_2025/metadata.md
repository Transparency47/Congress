# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2970?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2970
- Title: National Veterans Advocate Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2970
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-12-12T09:07:28Z
- Update date including text: 2025-12-12T09:07:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2970",
    "number": "2970",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "Y000067",
        "district": "2",
        "firstName": "Rudy",
        "fullName": "Rep. Yakym, Rudy [R-IN-2]",
        "lastName": "Yakym",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "National Veterans Advocate Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:28Z",
    "updateDateIncludingText": "2025-12-12T09:07:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:32:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-12T15:37:08Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2970ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2970\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Yakym introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain improvements to the laws relating to advocacy for veterans who receive health care and other benefits furnished by the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Veterans Advocate Act of 2025 .\n#### 2. Independent Office of the National Veterans\u2019 Advocate in Department of Veterans Affairs\n##### (a) In general\nSection 7309A of title 38, United States Code, is amended\u2014\n**(1)**\nby striking the section heading and inserting the following new section heading:\n7309A. Office of the National Veterans\u2019 Advocate ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby striking within the Office of the Under Secretary for Health ;\n**(B)**\nby striking an office and inserting an independent office ; and\n**(C)**\nby striking Office of Patient Advocacy and inserting Office of the National Veterans\u2019 Advocate ;\n**(3)**\nby striking patient advocate each place it appears and inserting veteran advocate ;\n**(4)**\nin subsection (b)\u2014\n**(A)**\nby striking paragraph (1) and inserting the following new paragraph (1):\n(1) The Office of the National Veterans\u2019 Advocate shall be under the supervision and direction of an official to be known as the \u201cNational Veterans\u2019 Advocate\u201d. The National Veterans\u2019 Advocate shall report directly to the Secretary and shall be entitled to compensation at the same rate as the highest rate of basic pay established for the Senior Executive Service under section 5382 of title 5, United States Code. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking Office of Patient Advocacy and inserting Office of the National Veterans\u2019 Advocate ;\n**(ii)**\nby striking by the Under Secretary for Health and inserting by the Secretary ; and\n**(iii)**\nby striking shall report directly to the Under Secretary for Health and inserting shall be independent of the Secretary ;\n**(5)**\nby striking Director each place it appears and inserting National Veterans\u2019 Advocate ;\n**(6)**\nin subsection (c)\u2014\n**(A)**\nby striking the subsection heading and inserting (c) Functions .\u2014 ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking function and inserting functions ;\n**(ii)**\nby striking is and inserting are ; and\n**(iii)**\nby inserting before the period at the end the following: and to monitor Department processes and make recommendations to Congress on how to improve the Department\u2019s efficiency and care for veterans ;\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (B), by striking and after the semicolon;\n**(ii)**\nin subparagraph (C), by striking the period and inserting a semicolon; and\n**(iii)**\nby adding at the end the following new subparagraphs:\n(D) identify areas in which veterans have problems in dealings with the Department; (E) to the extent possible, propose changes in the administrative practices of the Department to mitigate problems identified under subparagraph (D); and (F) identify potential legislative changes which may be appropriate to mitigate such problems. ;\n**(D)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking and after the semicolon;\n**(ii)**\nby redesignating subparagraph (B) as subparagraph (C);\n**(iii)**\nby inserting after subparagraph (A) the following new subparagraph (B):\n(B) fill out forms to relating to casework problem that facilitate the rapid assignment of a local veteran advocate caseworker who can directly interface with the veteran if needed; and ; and\n**(iv)**\nin subparagraph (C), as redesignated by clause (ii), by inserting or forms after complaint both times it appears;\n**(E)**\nby adding at the end the following new paragraphs:\n(4) The Office shall have the authority to manage casework issues across the Department. (5) (A) Not later than March 30 and September 30 of each year, the National Veterans\u2019 Advocate shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the operations of the Office of the National Veterans\u2019 Advocate. Each such report shall include\u2014 (i) a description of the activities of the Office carried out pursuant so subsection (c)(2)(D) through (F); and (ii) independent legislative recommendations for the improvement of health outcomes for veterans, the quality of health care and benefits provided by the Department, and the cost efficiency of the Department. (B) Recommendations included in a report under this paragraph may not be reviewed by the Secretary or by any other official of the Department prior to submission. (C) Each report under this paragraph shall be transmitted to the Secretary and made publicly available on the website the National Veterans\u2019 Advocate. (6) The Office shall have a designated publicly accessible website that includes access to the information technology system required under paragraph (3). ;\n**(7)**\nin subsection (d)\u2014\n**(A)**\nin the subsection heading, by striking Patient advocacy and inserting Veteran advocacy ; and\n**(B)**\nby adding at the end the following new paragraph:\n(15) In coordination with the recommendation team, to identify problems experienced within the Department in the course of providing hospital care, medical services, and nursing home care and burial and interment benefits to veterans and to develop recommendations to address such problems. ;\n**(8)**\nin subsection (e)\u2014\n**(A)**\nby striking shall ensure that such training is consistent throughout the Department. and inserting shall\u2014 ;\n**(B)**\nby adding at the end the following new subparagraphs:\n(A) develop the curriculum for such training in coordination with the Under Secretary for Benefits, the Under Secretary for Health, the Director of each of the Veterans Integrated Service Networks, and veterans service organizations; (B) ensure that each veteran advocate is required to receive such training on an annual basis; (C) ensure that such training includes up-to-date information on Department policy, crisis management, health care, and such other matters as the Secretary determines appropriate; and (D) ensure that such training is consistent throughout the Department. ;\n**(9)**\nby redesignating subsection (f) as subsection (l); and\n**(10)**\nby inserting after subsection (e) the following new subsections:\n(f) Deputy National Veterans\u2019 Advocates (1) There is in each Veterans Integrated Service Network (hereinafter referred to as a VISN ) a Deputy National Veterans\u2019 Advocate who shall have responsibility for managing the employees of the Office with primary responsibility for casework. (2) The Deputy National Veterans\u2019 Advocate for a VISN shall ensure that for the geographic area served by that VISN, the Department employs at least one veteran advocate for every 12,000 veterans who reside in such area and are enrolled in the patient enrollment system under section 1705 of this title. (g) Office employees The Office of the National Veterans\u2019 Advocate shall have employees in the Washington, D.C., office in the Department. Such employees shall carry out the responsibilities under subsection (c)(2)(D) through (F), coordinate with Deputy National Veterans\u2019 Advocates and veteran advocates, and carry out such other responsibilities as the National Veterans\u2019 Advocate determines appropriate. (h) Casework request portal The National Veterans\u2019 Advocate shall establish, on the website of the National Veterans\u2019 Advocate, a casework request portal that veterans can use to request assistance with casework. (i) Outreach The Secretary shall conduct outreach to veterans receiving benefits under the laws administrated by the Secretary to provide information to such veterans about the Office and the assistance available to veterans through the Office. (j) Coordination To improve policies The Secretary, the National Veterans\u2019 Advocate, the Under Secretary for Health, and the Under Secretary for Benefits shall\u2014 (1) work closely together on a continual basis to improve the policies of the Department without the necessity for congressional action; and (2) communicate frequently to ensure such improvement. (k) Authorization of appropriations There is authorized to be appropriated to carry out this section $25,000,000 for each of fiscal years 2026 through 2030. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 73 of such title is amended by striking the item relating to section 7309A and inserting the following new item:\n7309A. Office of the National Veterans\u2019 Advocate. .",
      "versionDate": "2025-04-17",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T20:44:25Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2970ih.xml"
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
      "title": "National Veterans Advocate Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Veterans Advocate Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make certain improvements to the laws relating to advocacy for veterans who receive health care and other benefits furnished by the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T08:18:27Z"
    }
  ]
}
```
