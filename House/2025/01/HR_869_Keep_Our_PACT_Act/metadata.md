# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/869?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/869
- Title: Keep Our PACT Act
- Congress: 119
- Bill type: HR
- Bill number: 869
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-12-17T09:06:29Z
- Update date including text: 2025-12-17T09:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/869",
    "number": "869",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "L000590",
        "district": "3",
        "firstName": "Susie",
        "fullName": "Rep. Lee, Susie [D-NV-3]",
        "lastName": "Lee",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Keep Our PACT Act",
    "type": "HR",
    "updateDate": "2025-12-17T09:06:29Z",
    "updateDateIncludingText": "2025-12-17T09:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-31T15:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "DE"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NJ"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "HI"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MN"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MD"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "KY"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "AZ"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "OR"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "VT"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NY"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NJ"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MO"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NJ"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "WA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr869ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 869\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. Lee of Nevada introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require full funding of part A of title I of the Elementary and Secondary Education Act of 1965 and the Individuals with Disabilities Education Act.\n#### 1. Short title\nThis Act may be cited as the Keep Our Promise to America\u2019s Children and Teachers Act or the Keep Our PACT Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nChildren are our Nation\u2019s future and greatest treasure.\n**(2)**\nA high-quality education is the surest way for every child to reach his or her full potential.\n**(3)**\nPart A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ) helps address inequity in education in school districts across the United States to provide a high-quality education to every student.\n**(4)**\nThe Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ) guarantees all children with disabilities a first-rate education.\n**(5)**\nThe amendments made to such Act by the Individuals with Disabilities Education Improvement Act of 2004 ( Public Law 108\u2013446 ; 118 Stat. 2647) committed Congress to providing 40 percent of the national current average per-pupil expenditure for students with disabilities.\n**(6)**\nA promise made must be a promise kept.\n#### 3. Mandatory funding of part A of title I of ESEA\n##### (a) Definition of fiscal year 2025 part A of title I appropriation\nIn this section, the term fiscal year 2025 part A of title I appropriation means the amount appropriated for fiscal year 2025 for programs under part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ).\n##### (b) Funding\nThere are appropriated, out of any money in the Treasury not otherwise appropriated\u2014\n**(1)**\nfor fiscal year 2026, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$20,509,878,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(2)**\nfor fiscal year 2027, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$22,853,242,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(3)**\nfor fiscal year 2028, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$25,464,349,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(4)**\nfor fiscal year 2029, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$28,373,788,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(5)**\nfor fiscal year 2030, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$31,615,646,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(6)**\nfor fiscal year 2031, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$35,227,904,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(7)**\nfor fiscal year 2032, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$39,252,882,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(8)**\nfor fiscal year 2033, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$43,737,735,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater;\n**(9)**\nfor fiscal year 2034, an amount that equals the difference between\u2014\n**(A)**\nthe fiscal year 2025 part A of title I appropriation; and\n**(B)**\n$48,735,007,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater; and\n**(10)**\nfor fiscal year 2035, $54,303,244,000 or the full amount authorized to be appropriated for the fiscal year for those programs, whichever is greater.\n#### 4. Mandatory funding of the Individuals With Disabilities Education Act\nSection 611(i) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1411(i) ) is amended to read as follows:\n(i) Funding (1) In general For the purpose of carrying out this part, other than section 619, there are authorized to be appropriated\u2014 (A) $16,661,928,000 or 11.6 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2026, and there are hereby appropriated $6,425,048,000 or 4.5 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2026, which shall become available for obligation on July 1, 2026, and shall remain available through September 30, 2027; (B) $19,531,844,000 or 13.4 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2027, and there are hereby appropriated $8,372,932,000 or 5.7 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2027, which shall become available for obligation on July 1, 2027, and shall remain available through September 30, 2028; (C) $22,896,084,000 or 15.3 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2028, and there are hereby appropriated $10,911,357,000 or 7.3 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2028, which shall become available for obligation on July 1, 2028, and shall remain available through September 30, 2029; (D) $26,839,795,000 or 17.6 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2029, and there are hereby appropriated $14,219,357,000 or 9.3 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2029, which shall become available for obligation on July 1, 2029, and shall remain available through September 30, 2030; (E) $31,462,786,000 or 20.2 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2030, and there are hereby appropriated $18,530,244,000 or 11.9 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2030, which shall become available for obligation on July 1, 2030, and shall remain available through September 30, 2031; (F) $36,882,058,000 or 23.1 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2031, and there are hereby appropriated $24,148,064,000 or 15.2 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2031, which shall become available for obligation on July 1, 2031, and shall remain available through September 30, 2032; (G) $43,234,768,000 or 26.5 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2032, and there are hereby appropriated $31,469,041,000 or 19.3 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2032, which shall become available for obligation on July 1, 2032, and shall remain available through September 30, 2033; (H) $50,681,693,000 or 30.4 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2033, and there are hereby appropriated $41,009,521,000 or 24.6 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2033, which shall become available for obligation on July 1, 2033, and shall remain available through September 30, 2034; (I) $59,411,305,000 or 34.9 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2034, and there are hereby appropriated $53,442,392,000 or 31.4 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2034, which shall become available for obligation on July 1, 2034, and shall remain available through September 30, 2035; and (J) $69,644,540,000 or 40 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2035 and each subsequent fiscal year, and there are hereby appropriated $69,644,540,000 or 40 percent of the amount determined under paragraph (2), whichever is greater, for fiscal year 2035 and each subsequent fiscal year, which\u2014 (i) shall become available for obligation with respect to fiscal year 2035 on July 1, 2034, and shall remain available through September 30, 2036; and (ii) shall become available for obligation with respect to each subsequent fiscal year on July 1 of that fiscal year and shall remain available through September 30 of the succeeding fiscal year. (2) Amount With respect to each subparagraph of paragraph (1), the amount determined under this paragraph is the product of\u2014 (A) the total number of children with disabilities in all States who\u2014 (i) received special education and related services during the last school year that concluded before the first day of the fiscal year for which the determination is made; and (ii) were aged\u2014 (I) 3 through 5 (with respect to the States that were eligible for grants under section 619); and (II) 6 through 21; and (B) the average per-pupil expenditure in public elementary schools and secondary schools in the United States. .\n#### 5. Emergency designation\n##### (a) In general\nThe amounts provided by the amendments made by this Act are designated as an emergency requirement pursuant to section 4(g) of the Statutory Pay-As-You-Go Act of 2010 ( 2 U.S.C. 933(g) ).\n##### (b) Designation in house and senate\nThe amendments made by this Act are designated as being for an emergency requirement pursuant to section 4001(a)(1) of S. Con. Res. 14 (117th Congress), the concurrent resolution on the budget for fiscal year 2022, and to legislation establishing fiscal year 2026 through 2035 budget enforcement in the House of Representatives.",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "343",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Keep Our PACT Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-02",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2598",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "IDEA Full Funding Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-03",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1277",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "IDEA Full Funding Act",
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
            "name": "Appropriations",
            "updateDate": "2025-03-24T16:05:59Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-24T16:05:59Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-03-24T16:05:59Z"
          },
          {
            "name": "Special education",
            "updateDate": "2025-03-24T16:05:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-04T16:46:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr869",
          "measure-number": "869",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr869v00",
            "update-date": "2025-03-28"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keep Our Promise to America's Children and Teachers Act or the Keep Our PACT Act </strong></p><p>This bill provides funding through FY2035 for grant programs operated by local educational agencies to provide supplementary educational and related services to low-achieving students and other students who attend elementary and secondary schools with relatively high concentrations of students from low-income families. Additionally, the bill permanently reauthorizes the grant program to assist states and outlying areas in providing special education and related services to children with disabilities.</p><p>The amounts provided by the bill are designated as an emergency requirement for the purposes of Pay-As-You-Go (PAYGO) rules and other budget enforcement procedures.</p>"
        },
        "title": "Keep Our PACT Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr869.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep Our Promise to America's Children and Teachers Act or the Keep Our PACT Act </strong></p><p>This bill provides funding through FY2035 for grant programs operated by local educational agencies to provide supplementary educational and related services to low-achieving students and other students who attend elementary and secondary schools with relatively high concentrations of students from low-income families. Additionally, the bill permanently reauthorizes the grant program to assist states and outlying areas in providing special education and related services to children with disabilities.</p><p>The amounts provided by the bill are designated as an emergency requirement for the purposes of Pay-As-You-Go (PAYGO) rules and other budget enforcement procedures.</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119hr869"
    },
    "title": "Keep Our PACT Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep Our Promise to America's Children and Teachers Act or the Keep Our PACT Act </strong></p><p>This bill provides funding through FY2035 for grant programs operated by local educational agencies to provide supplementary educational and related services to low-achieving students and other students who attend elementary and secondary schools with relatively high concentrations of students from low-income families. Additionally, the bill permanently reauthorizes the grant program to assist states and outlying areas in providing special education and related services to children with disabilities.</p><p>The amounts provided by the bill are designated as an emergency requirement for the purposes of Pay-As-You-Go (PAYGO) rules and other budget enforcement procedures.</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119hr869"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr869ih.xml"
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
      "title": "Keep Our PACT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Our PACT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Our Promise to America\u2019s Children and Teachers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require full funding of part A of title I of the Elementary and Secondary Education Act of 1965 and the Individuals with Disabilities Education Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:18:27Z"
    }
  ]
}
```
