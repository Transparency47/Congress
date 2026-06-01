# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/912?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/912
- Title: 9–8–8 Lifeline Cybersecurity Responsibility Act
- Congress: 119
- Bill type: HR
- Bill number: 912
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-04-03T19:54:56Z
- Update date including text: 2026-04-03T19:54:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/912",
    "number": "912",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "9\u20138\u20138 Lifeline Cybersecurity Responsibility Act",
    "type": "HR",
    "updateDate": "2026-04-03T19:54:56Z",
    "updateDateIncludingText": "2026-04-03T19:54:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:02:05Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-15",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr912ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 912\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Obernolte (for himself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title V of the Public Health Service Act to secure the suicide prevention lifeline from cybersecurity incidents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 9\u20138\u20138 Lifeline Cybersecurity Responsibility Act .\n#### 2. Protecting suicide prevention lifeline from cybersecurity incidents\n##### (a) National suicide prevention lifeline program\nSection 520E\u20133(b) of the Public Health Service Act (42 U.S.C. 290bb\u201336c(b)) is amended\u2014\n**(1)**\nin paragraph (4), by striking and at the end;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(6) taking such steps as may be necessary to ensure the suicide prevention hotline is protected from cybersecurity incidents and eliminates known cybersecurity vulnerabilities. .\n##### (b) Reporting\nSection 520E\u20133 of the Public Health Service Act ( 42 U.S.C. 290bb\u201336c ) is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (g); and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Cybersecurity reporting (1) Notification (A) In general The program\u2019s network administrator receiving Federal funding pursuant to subsection (a) shall report to the Assistant Secretary, in a manner that protects personal privacy, consistent with applicable Federal and State privacy laws\u2014 (i) any identified cybersecurity vulnerabilities to the program within a reasonable amount of time after identification of such a vulnerability; and (ii) any identified cybersecurity incidents to the program within a reasonable amount of time after identification of such incident. (B) Local and regional crisis centers Local and regional crisis centers participating in the program shall report to the program\u2019s network administrator identified under subparagraph (A), in a manner that protects personal privacy, consistent with applicable Federal and State privacy laws\u2014 (i) any identified cybersecurity vulnerabilities to the program within a reasonable amount of time after identification of such vulnerability; and (ii) any identified cybersecurity incidents to the program within a reasonable amount of time after identification of such incident. (2) Notification If the program\u2019s network administrator receiving funding pursuant to subsection (a) discovers, or is informed by a local or regional crisis center pursuant to paragraph (1)(B) of, a cybersecurity vulnerability or incident, within a reasonable amount of time after such discovery or receipt of information, such entity shall report the vulnerability or incident to the Assistant Secretary. (3) Clarification (A) Oversight (i) Local and regional crisis centers Except as provided in clause (ii), local and regional crisis centers participating in the program shall oversee all technology each center employs in the provision of services as a participant in the program. (ii) Network administrator The program\u2019s network administrator receiving Federal funding pursuant to subsection (a) shall oversee the technology each crisis center employs in the provision of services as a participant in the program if such oversight responsibilities are established in the applicable network participation agreement. (B) Supplement, not supplant The cybersecurity incident reporting requirements under this subsection shall supplement, and not supplant, cybersecurity incident reporting requirements under other provisions of applicable Federal law that are in effect on the date of the enactment of the 9\u20138\u20138 Lifeline Cybersecurity Responsibility Act. .\n##### (c) Study\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General of the United States shall\u2014\n**(1)**\nconduct and complete a study that evaluates cybersecurity risks and vulnerabilities associated with the 9\u20138\u20138 National Suicide Prevention Lifeline; and\n**(2)**\nsubmit a report on the findings of such study to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-06-18",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2121",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SUPPORT for Patients and Communities Reauthorization Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-01",
        "text": "Became Public Law No: 119-44."
      },
      "number": "2483",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SUPPORT for Patients and Communities Reauthorization Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-12",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1007",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "9\u20138\u20138 Lifeline Cybersecurity Responsibility Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
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
            "name": "Computer security and identity theft",
            "updateDate": "2025-04-11T14:29:28Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-11T14:29:28Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-04-11T14:29:28Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-11T14:29:28Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-11T14:29:28Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-11T14:29:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-07T16:42:25Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr912ih.xml"
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
      "title": "9\u20138\u20138 Lifeline Cybersecurity Responsibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T10:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "9\u20138\u20138 Lifeline Cybersecurity Responsibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title V of the Public Health Service Act to secure the suicide prevention lifeline from cybersecurity incidents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T10:03:49Z"
    }
  ]
}
```
