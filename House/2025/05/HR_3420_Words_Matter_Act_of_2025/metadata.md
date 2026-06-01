# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3420?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3420
- Title: Words Matter Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3420
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-27T14:20:28Z
- Update date including text: 2026-05-27T14:20:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3420",
    "number": "3420",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S000250",
        "district": "17",
        "firstName": "Pete",
        "fullName": "Rep. Sessions, Pete [R-TX-17]",
        "lastName": "Sessions",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Words Matter Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-27T14:20:28Z",
    "updateDateIncludingText": "2026-05-27T14:20:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
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
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
            "date": "2026-03-26T18:31:03Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-15T14:06:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "WI"
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
      "sponsorshipDate": "2025-05-15",
      "state": "DC"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MT"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "KS"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "IN"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "LA"
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
      "sponsorshipDate": "2025-09-02",
      "state": "VA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-18",
      "state": "PA"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "IL"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3420ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3420\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Sessions (for himself, Mr. Pocan , Ms. Norton , Mr. Hudson , and Mr. Zinke ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend Federal law to remove the terms mentally retarded and mental retardation , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Words Matter Act of 2025 .\n#### 2. Removal of mentally retarded and mental retardation from Federal law\n##### (a) Contracts for medical care for spouses and children\nSection 1079(d)(3)(B) of title 10, United States Code, is amended by striking is moderately or severely mentally retarded, has a serious physical disability, or has and inserting has a moderate to severe intellectual disability, a serious physical disability, or .\n##### (b) Mortgage insurance for nursing homes, intermediate care facilities, and board and care homes\nSection 232(d)(4)(A) of the National Housing Act ( 12 U.S.C. 1715w(d)(4)(A) ) is amended by striking the mentally retarded or developmentally disabled and inserting individuals with intellectual or developmental disabilities .\n##### (c) Implementation of a sentence of death\nSection 3596(c) of title 18, United States Code, is amended by striking is mentally retarded and inserting has an intellectual disability .\n##### (d) Fetal alcohol syndrome definition\nSection 4(9)(A) of the Indian Health Care Improvement Act ( 25 U.S.C. 1603(9)(A) ) is amended by striking mental retardation and inserting intellectual disability .\n##### (e) General programs definitions\nSection 701 of the Indian Health Care Improvement Act ( 25 U.S.C. 1665 ) is amended by striking mental retardation and inserting intellectual disability each place it appears.\n##### (f) Grant authority\nSection 2201 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10471 ) is amended\u2014\n**(1)**\nin paragraph (1) by striking mental retardation and inserting intellectual disabilities ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A) by striking a mentally ill or mentally retarded offender and inserting an offender who has a mental illness or intellectual disability ; and\n**(B)**\nin subparagraph (C) by striking of a mentally ill or mentally retarded defendant\u2019s cases and inserting cases of a defendant who has a mental illness or intellectual disability .\n##### (g) Mental health courts definitions\nSection 2202(2) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10472(2) ) is amended by striking mental retardation and inserting intellectual disability each place it appears.\n##### (h) Donation of personal property through state agencies\nSection 549(c)(3)(B)(iv) of title 40, United States Code, is amended by striking the mentally retarded or physically handicapped and inserting individuals with intellectual or physical disabilities .\n##### (i) Training opportunities for direct care workers\nSection 747A(a) of the Public Health Service Act ( 42 U.S.C. 293k\u20131(a) ) is amended by striking mental retardation and inserting intellectual disabilities .\n##### (j) Criminal penalties for acts involving Federal health care programs\nSection 1128B of the Social Security Act ( 42 U.S.C. 1320a\u20137b ) is amended by striking the mentally retarded and inserting individuals with intellectual disabilities each place it appears.\n##### (k) Long-Term care facility or provider\nSection 6201(a)(6)(E)(ix) of the Patient Protection and Affordable Care Act (42 U.S.C. 1320a\u20137l(a)(6)(E)(ix)) is amended by striking the mentally retarded and inserting individuals with intellectual disabilities .\n##### (l) Grants for planning comprehensive action To respond to the needs of individuals with intellectual disabilities\nTitle XVII of the Social Security Act ( 42 U.S.C. 1391 et seq. ) is amended\u2014\n**(1)**\nin the title heading by striking combat mental retardation and inserting meet the needs of individuals with intellectual disabilities ;\n**(2)**\nin section 1701, by striking combat mental retardation and inserting meet the needs of individuals with intellectual disabilities each place it appears;\n**(3)**\nin section 1702\u2014\n**(A)**\nby striking needed to combat mental retardation and inserting needed to meet the needs of individuals with intellectual disabilities ;\n**(B)**\nby striking the mental retardation problem and of the need for combating it and inserting such needs ;\n**(C)**\nby striking relating to the various aspects of mental retardation and its prevention, treatment, or amelioration and inserting to meet such needs ; and\n**(D)**\nby striking community action to combat mental retardation and inserting community action to meet such needs ; and\n**(4)**\nin section 1703 by striking the mentally retarded and inserting individuals with intellectual disabilities .\n##### (m) Requirements for, and assuring quality care in, skilled nursing facilities\nSection 1819(b)(4) of the Social Security Act ( 42 U.S.C. 1395i\u20133(b)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A)(vii) by striking mentally ill and mentally retarded residents and inserting residents with mental illnesses or intellectual disabilities ; and\n**(2)**\nin subparagraph (C)(ii)(IV) by striking the mentally ill and the mentally retarded and inserting individuals with mental illnesses or intellectual disabilities .\n##### (n) Grants to States for medical assistance programs\nTitle XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) is amended\u2014\n**(1)**\nby striking intermediate care facility for the mentally retarded and inserting intermediate care facility for individuals with intellectual disabilities each place it appears;\n**(2)**\nby striking intermediate care facilities for the mentally retarded and inserting intermediate care facilities for individuals with intellectual disabilities each place it appears;\n**(3)**\nin section 1905(d)\u2014\n**(A)**\nin the matter preceding paragraph (1) by striking the mentally retarded or persons with and inserting individuals with intellectual disabilities or ;\n**(B)**\nin paragraph (1) by striking mentally retarded individuals and inserting individuals with intellectual disabilities ; and\n**(C)**\nin paragraph (2) by striking mentally retarded individual and inserting individual who has an intellectual disability ;\n**(4)**\nin the section heading of section 1910 by striking the mentally retarded and inserting individuals with intellectual disabilities ;\n**(5)**\nin section 1915(c)(7)(C) by striking mental retardation or a related condition and inserting intellectual disabilities or related conditions ;\n**(6)**\nin section 1919\u2014\n**(A)**\nin subsection (b)(3)\u2014\n**(i)**\nin subparagraph (E)\u2014\n**(I)**\nby striking mental retardation and inserting intellectual ; and\n**(II)**\nby striking is mentally ill or mentally retarded and inserting has a mental illness or intellectual disability ; and\n**(ii)**\nin subparagraph (F)\u2014\n**(I)**\nin the subparagraph heading by striking mentally ill and mentally retarded individuals and inserting individuals who have mental illnesses or intellectual disabilities ;\n**(II)**\nby striking State mental retardation and inserting State intellectual each place it appears;\n**(III)**\nin clause (i) by striking is mentally ill and inserting has a mental illness ; and\n**(IV)**\nin clause (ii)\u2014\n**(aa)**\nby striking is mentally retarded and inserting has an intellectual disability ; and\n**(bb)**\nby striking for mental retardation and inserting for such intellectual disability ;\n**(B)**\nin subsection (b)(4)\u2014\n**(i)**\nin subparagraph (A)(vii) by striking mentally ill and mentally retarded residents and inserting residents with mental illnesses or intellectual disabilities ; and\n**(ii)**\nin subparagraph (C)(ii)(IV) by striking the mentally ill and the mentally retarded and inserting individuals with mental illnesses or intellectual disabilities ; and\n**(C)**\nin subsection (e)(7)\u2014\n**(i)**\nin subparagraph (A)(i) by striking mentally ill and mentally retarded individuals and inserting individuals with mental illnesses or intellectual disabilities ;\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby striking State mental retardation and inserting State intellectual each place it appears;\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nin the clause heading by striking mentally retarded residents and inserting residents with intellectual disabilities ;\n**(bb)**\nin the matter preceding clause (I) by striking is mentally retarded and inserting has an intellectual disability ; and\n**(cc)**\nin subclause (II) by striking mental retardation and inserting an intellectual disability ; and\n**(III)**\nin clause (iii) by striking mentally ill or mentally retarded resident and inserting resident who has a mental illness or intellectual disability ;\n**(iii)**\nin subparagraph (C) by striking mental retardation and inserting intellectual disability in each place it appears;\n**(iv)**\nin subparagraph (E)\u2014\n**(I)**\nby striking are mentally retarded or mentally ill and inserting have an intellectual disability or mental illness ; and\n**(II)**\nby striking mental retardation and inserting intellectual disability ; and\n**(v)**\nin subparagraph (G)\u2014\n**(I)**\nin clause (i) by inserting or have a mental illness after mentally ill ; and\n**(II)**\nin clause (ii) by striking be mentally retarded if the individual is mentally retarded or a person with and inserting have an intellectual disability if the individual has an intellectual disability or ; and\n**(7)**\nin the section heading of section 1922 by striking the mentally retarded and inserting individuals with intellectual disabilities .\n##### (o) Payments to States\nSection 2002(a)(2)(A) of the Social Security Act ( 42 U.S.C. 1397a(a)(2)(A) ) is amended by striking the mentally retarded and inserting individuals with intellectual disabilities .\n##### (p) Miscellaneous provisions\nSection 12(d)(5) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1760(d)(5) ) is amended by striking the mentally retarded and inserting individuals with intellectual disabilities .\n##### (q) Child nutrition definitions\nSection 15(3) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1784(3) ) is amended by striking the mentally retarded and inserting individuals with intellectual disabilities .\n##### (r) Institutionalized persons definitions\nSection 2(1)(B) of the Civil Rights of Institutionalized Persons Act ( 42 U.S.C. 1997(1)(B) ) is amended\u2014\n**(1)**\nin clause (i) by striking disabled, or retarded, or chronically ill or handicapped and inserting physically or intellectually disabled, or chronically ill ; and\n**(2)**\nin clause (iv)(III) by striking mentally ill or disabled, mentally retarded, or chronically ill or handicapped and inserting mentally ill, physically or intellectually disabled, or chronically ill .\n##### (s) Programs for individuals with developmental disabilities\nTitle I of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15001 et seq. ) is amended\u2014\n**(1)**\nby striking Intermediate Care Facility (Mental Retardation) and inserting intermediate care facility for individuals with intellectual disabilities each place it appears;\n**(2)**\nin section 109(a)(4)(B)(i) by striking the mentally retarded and inserting individuals with intellectual disabilities ; and\n**(3)**\nin section 125(c)(7)(F)(i) by striking Intermediate Care Facilities (Mental Retardation) and inserting intermediate care facilities for individuals with intellectual disabilities .\n#### 3. Regulations\nFor the purposes of a regulation issued to carry out a provision amended by this Act\u2014\n**(1)**\nbefore the regulation is amended to carry out this Act\u2014\n**(A)**\na reference in the regulation to mental retardation shall be considered to be a reference to an intellectual disability ; and\n**(B)**\na reference in the regulation to the mentally retarded , or individuals who are mentally retarded , shall be considered to be a reference to individuals with intellectual disabilities ; and\n**(2)**\nin amending a regulation to carry out this Act, a Federal agency shall ensure that the regulation clearly states\u2014\n**(A)**\nthat an intellectual disability was formerly termed mental retardation ; and\n**(B)**\nthat individuals with intellectual disabilities were formerly termed the mentally retarded or individuals who are mentally retarded .\n#### 4. Rule of construction\nThis Act shall be construed to amend Federal law to remove the term mentally retarded and mental retardation without any intent to\u2014\n**(1)**\nchange the coverage, eligibility, rights, responsibilities, or definitions referred to in the amended provisions; or\n**(2)**\ncompel States to change terminology in State laws for individuals covered by a provision amended by this Act.",
      "versionDate": "2025-05-15",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-04-06T20:25:17Z"
          },
          {
            "name": "Birth defects",
            "updateDate": "2026-04-06T20:24:14Z"
          },
          {
            "name": "Child health",
            "updateDate": "2026-04-06T20:25:01Z"
          },
          {
            "name": "Contracts and agency",
            "updateDate": "2026-04-06T20:23:52Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2026-04-06T20:24:08Z"
          },
          {
            "name": "Disability and paralysis",
            "updateDate": "2026-04-06T20:23:48Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-04-06T20:25:13Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-04-06T20:24:26Z"
          },
          {
            "name": "Food assistance and relief",
            "updateDate": "2026-04-06T20:25:10Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-04-06T20:23:58Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2026-04-06T20:24:46Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2026-04-06T20:24:18Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-04-06T20:24:54Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2026-04-06T20:24:04Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2026-04-06T20:24:32Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2026-04-06T20:24:36Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-04-06T20:24:22Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2026-04-06T20:24:40Z"
          },
          {
            "name": "Nutrition and diet",
            "updateDate": "2026-04-06T20:25:05Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-04-06T20:24:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-28T12:24:31Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3420ih.xml"
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
      "title": "Words Matter Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Words Matter Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend Federal law to remove the terms \"mentally retarded\" and \"mental retardation\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-23T02:48:19Z"
    }
  ]
}
```
