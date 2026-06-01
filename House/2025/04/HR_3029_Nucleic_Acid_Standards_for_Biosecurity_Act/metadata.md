# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3029?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3029
- Title: Nucleic Acid Standards for Biosecurity Act
- Congress: 119
- Bill type: HR
- Bill number: 3029
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2025-06-24T20:20:18Z
- Update date including text: 2025-06-24T20:20:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-29 - Committee: Ordered to be Reported by Voice Vote.
- Latest action: 2025-04-28: Introduced in House

## Actions

- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-29 - Committee: Ordered to be Reported by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3029",
    "number": "3029",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
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
    "title": "Nucleic Acid Standards for Biosecurity Act",
    "type": "HR",
    "updateDate": "2025-06-24T20:20:18Z",
    "updateDateIncludingText": "2025-06-24T20:20:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
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
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-28",
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
            "date": "2025-04-29T21:11:11Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-28T16:01:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "DE"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3029ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3029\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Ms. Salinas (for herself and Mr. McCormick ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the Research and Development, Competition, and Innovation Act to support nucleic acid screening, and for other purposes.\n#### 1. Short title\nThis Act may be cited Nucleic Acid Standards for Biosecurity Act .\n#### 2. Supporting nucleic acid screening\nSection 10221 of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 18931 ; enacted as part of title II of division B of Public Law 117\u2013167 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin subparagraph (C), by striking and after the semicolon;\n**(B)**\nby redesignating subparagraph (D) as subparagraph (E); and\n**(C)**\nby inserting after subparagraph (C) the following new subparagraph:\n(D) best practices, guidelines, and technical standards for risk management associated with engineering biology and biomanufacturing, including risks associated with the use of artificial intelligence; and ;\n**(2)**\nby redesignating subsections (b) and (c) as subsections (c) and (d), respectively; and\n**(3)**\nby inserting after subsection (a) the following new subsection:\n(b) Nucleic acid synthesis screening tools and standards (1) In general The Director, in consultation with heads of Federal agencies the Director considers appropriate, shall carry out measurement research to support the development and improvement of best practices and technical standards for biosecurity measures related to nucleic acid synthesis, including the following: (A) Testing to improve the accuracy, efficacy, and reliability of screening for nucleic acid synthesis. (B) Best practices, including security and access controls, for operational security and managing sequence-of-concern databases to support such screening. (C) Technical implementation guidance to ensure such screening is effective and secure. (D) Conformity-assessment best practices and technical standards. (E) Methods to evaluate the impact and effectiveness of the implementation of subparagraphs (A) through (D). (2) Consortium In carrying out this subsection, the Director shall convene a consortium of stakeholders, including industry, institutions of higher education, nonprofit organizations, and customers to carry out the following: (A) Develop and periodically update consensus priorities and best practices, as appropriate, for synthetic nucleic acid procurement screening mechanisms. (B) Develop roadmaps to inform the activities carried out under paragraph (1). (3) Report Not later than 18 months after the first meeting of the consortium under paragraph (2), the Director shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report summarizing the findings of the consortium. (4) Authorization of appropriations Of the funds authorized to be appropriated for the National Institute of Standards and Technology pursuant to this section for scientific and technical research and services laboratory activities, there is authorized to be appropriated $5,000,000 for each of fiscal years 2026 through 2030 to carry out this subsection. .",
      "versionDate": "2025-04-28",
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
            "name": "Biological and life sciences",
            "updateDate": "2025-05-28T16:18:37Z"
          },
          {
            "name": "Cell biology and embryology",
            "updateDate": "2025-05-28T16:18:37Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-05-28T16:18:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-28T16:06:11Z"
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
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3029ih.xml"
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
      "title": "Nucleic Acid Standards for Biosecurity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T18:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nucleic Acid Standards for Biosecurity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-08T18:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Research and Development, Competition, and Innovation Act to support nucleic acid screening, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T04:33:22Z"
    }
  ]
}
```
