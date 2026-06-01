# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3491?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3491
- Title: DeOndra Dixon INCLUDE Project Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3491
- Origin chamber: House
- Introduced date: 2025-05-19
- Update date: 2026-05-23T08:07:15Z
- Update date including text: 2026-05-23T08:07:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported by the Yeas and Nays: 46 - 0.
- Latest action: 2025-05-19: Introduced in House

## Actions

- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported by the Yeas and Nays: 46 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3491",
    "number": "3491",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000197",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. DeGette, Diana [D-CO-1]",
        "lastName": "DeGette",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "DeOndra Dixon INCLUDE Project Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:15Z",
    "updateDateIncludingText": "2026-05-23T08:07:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 46 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
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
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-19",
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
            "date": "2026-05-21T13:47:47Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-19T16:01:45Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "NC"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "CT"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "OK"
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
      "sponsorshipDate": "2025-05-19",
      "state": "DC"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "MN"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CO"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "MN"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CO"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CO"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "WI"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "MO"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "TN"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "VA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "VA"
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
      "sponsorshipDate": "2026-03-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3491ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3491\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2025 Ms. DeGette (for herself, Mr. Hudson , Ms. DeLauro , Mr. Cole , Ms. Norton , and Mr. Stauber ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize the Secretary of Health and Human Services to carry out a program of research, training, and investigation related to Down syndrome, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the DeOndra Dixon INCLUDE Project Act of 2025 .\n#### 2. DeOndra Dixon INCLUDE Project\nPart B of title IV of the Public Health Service Act ( 42 U.S.C. 284 et seq. ) is amended by adding at the end the following:\n409K. Down syndrome research (a) In general The Director of NIH shall carry out a program of research, training, and investigation related to Down syndrome to be known as the INvestigation of Co-occurring conditions across the Lifespan to Understand Down syndromE Project or the INCLUDE Project . (b) Program elements The program under subsection (a) shall include\u2014 (1) high-risk, high-reward research on the effects of trisomy 21 on human development and health; (2) promoting research for participants with Down syndrome across the lifespan, including cohort studies to facilitate improved understanding of Down syndrome and co-occurring conditions and development of new interventions; (3) expanding the number of clinical trials that are inclusive of, or expressly for, participants with Down syndrome, including novel biomedical and pharmacological interventions and other therapies designed to promote or enhance activities of daily living; (4) research on the biological mechanisms in individuals with Down syndrome pertaining to structural, functional, and behavioral anomalies and dysfunction as well as stunted growth; (5) supporting research to improve diagnosis and treatment of conditions co-occurring with Down syndrome, including the identification of biomarkers related to risk factors, diagnosis, and clinical research and therapeutics; (6) research on the causes of increased prevalence, and concurrent treatment, of co-occurring conditions, such as Alzheimer\u2019s disease and related dementias and autoimmunity, in individuals with Down syndrome; and (7) research, training, and investigation on improving the quality of life of individuals with Down syndrome and their families. (c) Coordination; prioritizing nonduplicative research The Director of NIH shall ensure that\u2014 (1) the programs and activities of the institutes and centers of the National Institutes of Health relating to Down syndrome and co-occurring conditions are coordinated, including through the Office of the Director of NIH and priority-setting reviews conducted pursuant to section 402(b)(3); and (2) such institutes and centers, prioritize, as appropriate, Down syndrome research that does not duplicate existing research activities of the National Institutes of Health. (d) Consultation with stakeholders In carrying out activities under this section, the Director of NIH shall, as appropriate and to the maximum extent feasible, consult with relevant stakeholders, including patient advocates, to ensure that such activities take into consideration the needs of individuals with Down syndrome. (e) Biennial reports to Congress (1) In general The Director of NIH shall submit, on a biennial basis, to the Committee on Energy and Commerce and the Subcommittee on Labor, Health and Human Services, Education, and Related Agencies of the Committee on Appropriations of the House of Representatives and the Committee on Health, Education, Labor, and Pensions and the Subcommittee on Labor, Health and Human Services, Education, and Related Agencies of the Committee on Appropriations of the Senate, a report that catalogs the research conducted or supported under this section. (2) Contents Each report under paragraph (1) shall include\u2014 (A) identification of the institute or center involved; (B) a statement of whether the research is or was being carried out directly by such institute or center or by multiple institutes and centers; and (C) identification of any resulting real-world evidence that is or may be used for clinical research and medical care for patients with Down syndrome. .",
      "versionDate": "2025-05-19",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-28T17:16:04Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3491ih.xml"
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
      "title": "DeOndra Dixon INCLUDE Project Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DeOndra Dixon INCLUDE Project Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize the Secretary of Health and Human Services to carry out a program of research, training, and investigation related to Down syndrome, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:20Z"
    }
  ]
}
```
