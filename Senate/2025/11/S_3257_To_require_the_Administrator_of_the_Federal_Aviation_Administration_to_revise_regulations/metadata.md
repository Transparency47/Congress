# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3257?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3257
- Title: Mental Health in Aviation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3257
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-05-26T20:35:36Z
- Update date including text: 2026-05-26T20:35:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3257",
    "number": "3257",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Mental Health in Aviation Act of 2025",
    "type": "S",
    "updateDate": "2026-05-26T20:35:36Z",
    "updateDateIncludingText": "2026-05-26T20:35:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
            "date": "2026-04-14T14:00:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-20T18:59:08Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-20T18:59:08Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "NE"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CO"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AK"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "UT"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "RI"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KS"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "ID"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "OR"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "OH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NM"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "AK"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "WI"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "LA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "GA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MS"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NH"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "SD"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "AZ"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-03-23",
      "state": "ID"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-23",
      "state": "DE"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "MT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3257is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3257\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Hoeven (for himself, Ms. Duckworth , Mrs. Britt , Mr. Durbin , Mrs. Fischer , Mr. Hickenlooper , Ms. Murkowski , Ms. Klobuchar , Mr. Curtis , Mr. Reed , Mr. Moran , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Administrator of the Federal Aviation Administration to revise regulations for certain individuals carrying out aviation activities who disclose a mental health diagnosis or condition, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mental Health in Aviation Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Aviation Administration.\n**(2) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Transportation and Infrastructure of the House of Representatives;\n**(B)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(C)**\nthe Committee on Appropriations of the House of Representatives; and\n**(D)**\nthe Committee on Appropriations of the Senate.\n**(3) FAA**\nThe term FAA means the Federal Aviation Administration.\n**(4) Special issuance**\nThe term special issuance has the meaning given such term in section 67.401 of title 14, Code of Federal Regulations.\n#### 3. Regulations for individuals carrying out aviation activities\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Administrator shall update regulations, including in part 67 of title 14, Code of Federal Regulations, and issue relevant guidance as appropriate to encourage individuals to\u2014\n**(1)**\nseek help for mental health conditions or symptoms of mental health conditions; and\n**(2)**\nto disclose conditions or symptoms described in paragraph (1).\n##### (b) Consultation; report requirements\nSection 411(d) of the FAA Reauthorization Act of 2024 ( 49 U.S.C. 44703 note) is amended\u2014\n**(1)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraphs (A) and (B), by striking and at the end;\n**(B)**\nin subparagraph (C), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following new subparagraphs:\n(D) a review and evaluation of any recommendations reached by the National Transportation Safety Board related to aviation workforce mental health; and (E) a description of relevant clinical studies, research, diagnostic manuals, and protocols used by the licensed professionals as of the date of the enactment of this subparagraph. ; and\n**(2)**\nby adding at the end the following new paragraph:\n(5) Consultation In carrying out this subsection, the task group shall consult with relevant stakeholders from the aviation and medical communities, as necessary, including\u2014 (A) the exclusive bargaining representatives of air traffic controllers of the FAA certified under section 7111 of title 5, United States Code; (B) organizations representing collective bargaining representatives of airline pilots; (C) institutions of higher education that are accredited by the Aviation Accreditation Board International; and (D) any other stakeholder determined relevant by the task group, including any stakeholders described in paragraph (3)(B). .\n##### (c) Implementation\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, and for any report issued thereafter, not later than 180 days after the submission of each report required under section 411(f) of the FAA Reauthorization Act of 2024 ( 49 U.S.C. 44703 note), the Administrator shall take appropriate action to implement the recommendations of such report.\n**(2) Justification**\nIn the event that the Administrator decides not to implement a recommendation described in paragraph (1), the Administrator shall submit to the appropriate committees of Congress the justification for such decision not later than 90 days after receiving the report containing such recommendation.\n#### 4. Annual review of mental health special issuance process\nBeginning on the date that is 180 days after the Administrator submits the first report pursuant to section 411(f) of the FAA Reauthorization Act of 2024 ( 49 U.S.C. 44703 note), and annually thereafter, the Administrator shall conduct an annual review of the special issuance process, and update, as appropriate, the applicable regulations, policies, orders, and guidance on mental health-related special issuance for pilots and air traffic controllers to\u2014\n**(1)**\nconsider the reclassification of additional medications and evidence-based treatments that may be safely prescribed to treat mental health conditions;\n**(2)**\nimprove mental health knowledge and training for aviation medical examiners;\n**(3)**\nif the Administrator determines appropriate, expand mental-health related situations in which an aviation medical examiner may issue a certificate consistent with the recommendations of the Mental Health and Aviation Medical Clearances Rulemaking Committee described in section 6; and\n**(4)**\nimprove the special issuance process for pilots and air traffic controllers.\n#### 5. Improving capacity for the Office of Aerospace Medicine\nOf the amounts made available pursuant to section 106(k)(1) of title 49, United States Code, the Administrator shall designate not more than $15,000,000 for each of fiscal years 2026 through 2029 to\u2014\n**(1)**\nrecruit, select, and train additional aviation medical examiners and human intervention motivation study aviation medical examiners, including those who are psychiatrists;\n**(2)**\nexpand capacity to provide oversight of aviation medical examiners and clear the backlog of special issuance requests and cases awaiting review at the Office of Aerospace Medicine of the FAA;\n**(3)**\nprovide enhanced mental health training to aviation medical examiners to ensure such personnel have requisite knowledge and the ability to appropriately evaluate individuals for FAA medical certification; and\n**(4)**\nsupport any other related activities, as determined appropriate by the Administrator.\n#### 6. Implementation of aviation rulemaking committee recommendations\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Administrator shall implement, as appropriate, the recommendations of the Mental Health and Aviation Medical Clearances Aviation Rulemaking Committee, which were submitted to the Administrator on April 1, 2024.\n##### (b) Consultation\nIn carrying out subsection (a), the Administrator shall consult with the stakeholders described in section 411(d)(5) of the FAA Reauthorization Act of 2024 (as added by this Act).\n##### (c) Justification\nIf the Administrator decides not to implement a recommendation described in subsection (a), the Administrator shall submit to the appropriate committees of Congress the justification for such decision not later than 90 days after the deadline described in such subsection.\n#### 7. Public information campaign\n##### (a) In general\nOf the amounts made available pursuant to section 106(k)(1) of title 49, United States Code, the Administrator shall designate not more than $1,500,000 for each of fiscal years 2026 through 2029 for a public information campaign or similar public education efforts to\u2014\n**(1)**\ndestigmatize individuals in (or interested in joining) the aviation industry who seek mental health care;\n**(2)**\nbroaden awareness of available supportive services; and\n**(3)**\nimprove trust between the FAA and pilots and air traffic controllers.\n##### (b) Requirements\nThe public information campaign or similar public education efforts described in subsection (a) shall include\u2014\n**(1)**\nmaking publicly available (in an easily accessible format and location online)\u2014\n**(A)**\ninformation that would help destigmatize the reporting of mental health concerns impacting the aviation workforce, and encourage individuals to seek help for such concerns; and\n**(B)**\nother information to effectuate the outcomes described in subsection (a);\n**(2)**\nposting the information described in paragraph (1) at Aviation Medical Examiner offices; and\n**(3)**\ncollaborating with air carriers (as defined in section 40102 of title 49, United States Code), flight training institutions and entities (as described in parts 61 and 141 of title 14, Code of Federal Regulations), and small, medium, and large hub airports (as defined in such section 40102) to encourage such entities to make such information easily accessible to airmen and air traffic controllers.\n##### (c) Briefing and report to Congress\n**(1) Briefing**\nNot later than 90 days after the Administrator establishes the public information campaign described in subsection (a), the Administrator shall brief the appropriate committees of Congress on the actions taken to develop the campaign and the plans to implement the campaign.\n**(2) Report**\nNot later than 2 years after the Administrator implements the public information campaign, the Administrator shall submit to the appropriate committees of Congress a report describing the engagement and outreach resulting from such campaign, including a description of any applicable feedback from aviation industry stakeholders on the efficacy of the campaign.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-05-04T20:17:49Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2026-05-04T20:17:23Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-04T20:18:05Z"
          },
          {
            "name": "Department of Transportation",
            "updateDate": "2026-05-04T20:17:56Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2026-05-04T20:18:13Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-04T20:18:26Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2026-05-04T20:20:18Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-05-04T20:18:34Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-05-04T20:17:31Z"
          },
          {
            "name": "Transportation employees",
            "updateDate": "2026-05-04T20:20:18Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2026-05-04T20:17:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-19T16:35:16Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3257is.xml"
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
      "title": "Mental Health in Aviation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mental Health in Aviation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T06:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Federal Aviation Administration to revise regulations for certain individuals carrying out aviation activities who disclose a mental health diagnosis or condition, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T06:33:38Z"
    }
  ]
}
```
