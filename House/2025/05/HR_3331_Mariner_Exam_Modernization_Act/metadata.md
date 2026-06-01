# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3331?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3331
- Title: Mariner Exam Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 3331
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2026-01-05T22:00:58Z
- Update date including text: 2026-01-05T22:00:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-14 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- 2025-06-11 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-11 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 12.
- 2025-06-11 - Committee: Subcommittee on Coast Guard and Maritime Transportation Discharged
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-14 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- 2025-06-11 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-11 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 12.
- 2025-06-11 - Committee: Subcommittee on Coast Guard and Maritime Transportation Discharged

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3331",
    "number": "3331",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001112",
        "district": "24",
        "firstName": "Salud",
        "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
        "lastName": "Carbajal",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Mariner Exam Modernization Act",
    "type": "HR",
    "updateDate": "2026-01-05T22:00:58Z",
    "updateDateIncludingText": "2026-01-05T22:00:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 12.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Coast Guard and Maritime Transportation Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-13",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
        "item": [
          {
            "date": "2025-06-11T14:50:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-11T14:49:00Z",
            "name": "Discharged from"
          },
          {
            "date": "2025-05-13T16:05:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-14T14:29:40Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "MS"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3331ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3331\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Carbajal (for himself and Mr. Ezell ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 46, United States Code, with respect to merchant mariner credential examination working groups, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mariner Exam Modernization Act .\n#### 2. Examinations for merchant mariner credentials\nSection 7510 of title 46, United States Code, is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin the subsection heading by striking Exam review and inserting Working group ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking 90 days and inserting 180 days ;\n**(ii)**\nby striking Coast Guard Authorization Act of 2016 and insert Mariner Exam Modernization Act ;\n**(iii)**\nby striking new questions for inclusion in and inserting questions, content, and relevancy of ;\n**(iv)**\nby redesignating subparagraphs (E), (F), and (G) as subparagraphs (F), (G), and (H), respectively; and\n**(v)**\nby inserting after subparagraph (D) the following:\n(E) at least 2 individuals that have taken and passed the examination in the 5 years before the commissioning of the working group; ;\n**(C)**\nin paragraph (4)\u2014\n**(i)**\nin the paragraph heading by striking Baseline review and inserting Review ;\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nby striking Within 1 year and inserting Not later than 270 days ;\n**(II)**\nby striking Coast Guard Authorization Act of 2016 and inserting Mariner Exam Modernization Act ;\n**(III)**\nby striking Secretary and inserting Commandant ;\n**(IV)**\nby redesignating clauses (i), (ii), (iii), and (iv) as clauses (ii), (iii), (iv), and (vii), respectively;\n**(V)**\nin clause (iv), as so redesignated, by striking ; and and inserting a semicolon;\n**(VI)**\nby inserting before clause (ii) the following:\n(i) industry standards, practices, and technology to be considered in the Merchant Mariner Credentialing Examination; ; and\n**(VII)**\nby inserting after clause (iv) the following:\n(v) the relevancy of examination topics and contents; (vi) any redundancy of core competencies between the Merchant Mariner Credentialing Examination and Standards of Training, Certification, and Watchingkeeping competencies; and ;\n**(iii)**\nby striking subparagraph (B) and inserting the following:\n(B) Report to Commandant Upon completion of the review under this paragraph, a report shall be provided to the Commandant which shall include findings of the review with recommendations for updates to the Merchant Marine Credentialling Examination. ;\n**(D)**\nby striking paragraphs (3), (5), and (8);\n**(E)**\nby redesignating paragraphs (4) and (9) as paragraphs (5) and (8), respectively; and\n**(F)**\nby inserting after paragraph (2) the following:\n(3) Meeting of working group (A) In general The Commandant shall convene the working group annually or at the creation of new examination questions, whichever occurs sooner. (B) Remote participation The Commandant shall allow any member of the working group to participate remotely if the member of the working group does not have the means to participate in person. (4) Use of questions The Commandant may not use questions developed for use in the Merchant Mariner Credentialing Examination until such questions are reviewed and approved by the working group. ;\n**(2)**\nby redsignating subsection (d) as subsection (e); and\n**(3)**\nby inserting after subsection (c) the following:\n(d) Plan (1) Requirement Not later than 270 days after the completion of the review under paragraph (4) of subsection (c), the Commandant shall develop a plan to update and modernize the Merchant Mariner Credentialing Examination and implement the recommendations developed by the review under such paragraph. (2) Contents The plan developed under paragraph (1) shall include\u2014 (A) the elimination or updating of outdated topics, contents, core competencies, or questions covered by the Merchant Mariner Credentialing Examination; (B) the modernization of testing procedures consistent with contemporary procedures for standardized testing administration and evaluation; and (C) the development of methods to collect examination data on pass and fail rates for questions and the overall examination for future analysis and comparison uses. (3) Coordination In developing the plan under paragraph (1), the Commandant shall develop such plan in consultation with the working group and individuals with expertise in modern best practices for relevant standardized testing. (4) Briefing required Not later than 1 year after the date of enactment of the Mariner Exam Modernization Act , the Coast Guard shall provide to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a briefing on the review and plan developed under this subsection. .",
      "versionDate": "2025-05-13",
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
            "name": "Advisory bodies",
            "updateDate": "2025-06-18T19:41:00Z"
          },
          {
            "name": "Coast guard",
            "updateDate": "2025-06-18T19:41:26Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-06-18T19:41:10Z"
          },
          {
            "name": "Marine and inland water transportation",
            "updateDate": "2025-06-18T19:41:19Z"
          },
          {
            "name": "Transportation employees",
            "updateDate": "2025-06-18T19:41:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-10T15:05:45Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3331ih.xml"
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
      "title": "Mariner Exam Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mariner Exam Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 46, United States Code, with respect to merchant mariner credential examination working groups, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:35Z"
    }
  ]
}
```
