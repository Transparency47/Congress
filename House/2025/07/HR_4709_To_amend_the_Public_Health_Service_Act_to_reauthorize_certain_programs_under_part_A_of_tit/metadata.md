# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4709?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4709
- Title: Newborn Screening Saves Lives Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4709
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-04-15T08:05:45Z
- Update date including text: 2026-04-15T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-09-10 - Committee: Referred to the Subcommittee on Health.
- 2025-09-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-09-10 - Committee: Referred to the Subcommittee on Health.
- 2025-09-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4709",
    "number": "4709",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001234",
        "district": "3",
        "firstName": "Kelly",
        "fullName": "Rep. Morrison, Kelly [D-MN-3]",
        "lastName": "Morrison",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Newborn Screening Saves Lives Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:45Z",
    "updateDateIncludingText": "2026-04-15T08:05:45Z"
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
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
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
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:14:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-09-10T17:52:24Z",
                "name": "Reported by"
              },
              {
                "date": "2025-09-10T17:46:21Z",
                "name": "Markup by"
              },
              {
                "date": "2025-09-10T17:46:15Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
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
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "ID"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "AZ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4709ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4709\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Morrison (for herself, Mr. Simpson , Ms. Schrier , and Mr. Langworthy ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to reauthorize certain programs under part A of title XI of such Act relating to genetic diseases, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Newborn Screening Saves Lives Reauthorization Act of 2025 .\n#### 2. Improved newborn and child screening and follow-up for heritable disorders\n##### (a) Purposes\nSection 1109(a) of the Public Health Service Act ( 42 U.S.C. 300b\u20138(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking enhance, improve or and inserting facilitate, enhance, improve, or ;\n**(2)**\nby amending paragraph (3) to read as follows:\n(3) to develop, and deliver to parents, families, and patient advocacy and support groups, educational programs that\u2014 (A) address newborn screening counseling, testing (including newborn screening pilot studies), follow-up, treatment, specialty services, and long-term care; (B) assess the target audience\u2019s current knowledge, incorporate health communications strategies, and measure impact; and (C) are at appropriate literacy levels; ; and\n**(3)**\nin paragraph (4)\u2014\n**(A)**\nby striking followup and inserting follow-up ; and\n**(B)**\nby inserting before the semicolon at the end the following: , including re-engaging patients who have not received recommended follow-up services and supports .\n##### (b) Approval factors\nSection 1109(c) of the Public Health Service Act ( 42 U.S.C. 300b\u20138(c) ) is amended\u2014\n**(1)**\nby striking or will use and inserting will use ; and\n**(2)**\nby inserting , or will use amounts received under such grant to enhance capacity and infrastructure to facilitate the adoption of, before the guidelines and recommendations .\n#### 3. Advisory committee on heritable disorders in newborns and children\nSection 1111 of the Public Health Service Act ( 42 U.S.C. 300b\u201310 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (5), by inserting and adopt process improvements after take appropriate steps ;\n**(B)**\nin paragraph (7) by striking and at the end;\n**(C)**\nby redesignating paragraph (8) as paragraph (9);\n**(D)**\nby inserting after paragraph (7) the following:\n(8) develop, maintain, and publish on a publicly accessible website consumer-friendly materials detailing\u2014 (A) the uniform screening panel nomination process, including data requirements, standards, and the use of international data in nomination submissions; and (B) the process for obtaining technical assistance for submitting nominations to the uniform screening panel and detailing the instances in which the provision of technical assistance would introduce a conflict of interest for members of the Advisory Committee; and ; and\n**(E)**\nin paragraph (9), as redesignated\u2014\n**(i)**\nby redesignating subparagraphs (K) and (L) as subparagraphs (L) and (M), respectively; and\n**(ii)**\nby inserting after subparagraph (J) the following:\n(K) the appropriate and recommended use of safe and effective genetic testing by health care professionals in newborns and children with an initial diagnosis of a disease or condition characterized by a variety of genetic causes and manifestations; ; and\n**(2)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1) by striking 2019 and inserting 2030 ; and\n**(B)**\nin paragraph (2) by striking 2019 and inserting 2030 .\n#### 4. Clearinghouse of newborn screening information\nSection 1112(c) of the Public Health Service Act ( 42 U.S.C. 300b\u201311(c) ) is amended by striking and supplement, not supplant, existing information sharing efforts and inserting and complement other Federal newborn screening information sharing activities .\n#### 5. Laboratory quality and surveillance\nSection 1113 of the Public Health Service Act ( 42 U.S.C. 300b\u201312 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking performance evaluation services, and inserting development of new screening tests, ; and\n**(ii)**\nby striking and at the end;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking performance test materials and inserting test performance materials ; and\n**(ii)**\nby striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(3) performance evaluation services to enhance disease detection, including the development of tools, resources, and infrastructure to improve data analysis, test result interpretation, data harmonization, and dissemination of laboratory best practices. ; and\n**(2)**\nin subsection (b) to read as follows:\n(b) Surveillance activities The Secretary, acting through the Director of the Centers for Disease Control and Prevention, and taking into consideration the expertise of the Advisory Committee on Heritable Disorders in Newborns and Children established under section 1111, shall provide for the coordination of national surveillance activities, including\u2014 (1) standardizing data collection and reporting through the use of electronic and other forms of health records to achieve real-time data for tracking and monitoring the newborn screening system, from the initial positive screen through diagnosis and long-term care management; and (2) by promoting data sharing linkages between State newborn screening programs and State-based birth defects and developmental disabilities surveillance programs to help families connect with services to assist in evaluating long-term outcomes. .\n#### 6. Hunter Kelly research program\nSection 1116 of the Public Health Service Act ( 42 U.S.C. 300b\u201315 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nby striking may and inserting shall ; and\n**(B)**\nin subparagraph (D)\u2014\n**(i)**\nby inserting , or with a high probability of being recommended by, after recommended by ; and\n**(ii)**\nby striking that screenings are ready for nationwide implementation and inserting that reliable newborn screening technologies are piloted and ready for use ; and\n**(2)**\nin subsection (b) to read as follows:\n(b) Funding In carrying out the research program under this section, the Secretary and the Director shall ensure that entities receiving funding through the program will provide assurances, as practicable, that such entities will work in consultation with State departments of health, as appropriate. .\n#### 7. Authorization of appropriations for newborn screening programs and activities\nSection 1117 of the Public Health Service Act ( 42 U.S.C. 300b\u201316 ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking $11,900,000 and inserting $20,883,000 ;\n**(B)**\nby striking 2015 and inserting 2026 ; and\n**(C)**\nby striking 2019 and inserting 2030 ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking $8,000,000 and inserting $22,250,000 ;\n**(B)**\nby striking 2015 and inserting 2026 ; and\n**(C)**\nby striking 2019 and inserting 2030 .\n#### 8. Institutional review boards; ethics guidance program\nSection 12 of the Newborn Screening Saves Lives Reauthorization Act of 2014 ( 42 U.S.C. 289 note) is amended to read as follows:\n12. Institutional review boards; ethics guidance program Research on nonidentified newborn dried blood spots shall be considered secondary research (as that term is defined in section 46.104(d)(4) of title 45, Code of Federal Regulations (or successor regulations)) with nonidentified biospecimens for purposes of federally funded research conducted pursuant to the Public Health Service Act ( 42 U.S.C. 200 et seq. ). .",
      "versionDate": "2025-07-23",
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
            "name": "Advisory bodies",
            "updateDate": "2025-09-24T20:15:54Z"
          },
          {
            "name": "Child health",
            "updateDate": "2025-09-24T20:15:46Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-09T15:58:32Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-09-24T20:16:05Z"
          },
          {
            "name": "Genetics",
            "updateDate": "2025-09-24T20:15:35Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-24T20:16:01Z"
          },
          {
            "name": "Hereditary and development disorders",
            "updateDate": "2025-09-24T20:15:41Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-09-24T20:16:19Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-09-24T20:15:50Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-09-24T20:16:10Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-09-24T20:16:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-16T17:46:54Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4709ih.xml"
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
      "title": "Newborn Screening Saves Lives Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Newborn Screening Saves Lives Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to reauthorize certain programs under part A of title XI of such Act relating to genetic diseases, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:40Z"
    }
  ]
}
```
