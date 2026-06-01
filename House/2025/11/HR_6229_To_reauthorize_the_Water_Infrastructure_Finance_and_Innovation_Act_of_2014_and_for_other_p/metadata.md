# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6229
- Title: Water Infrastructure Finance and Innovation Act Amendments of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6229
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-01-07T09:05:50Z
- Update date including text: 2026-01-07T09:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-22 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-22 - Committee: Referred to the Subcommittee on Water Resources and Environment.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6229",
    "number": "6229",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "S001216",
        "district": "8",
        "firstName": "Kim",
        "fullName": "Rep. Schrier, Kim [D-WA-8]",
        "lastName": "Schrier",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Water Infrastructure Finance and Innovation Act Amendments of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:50Z",
    "updateDateIncludingText": "2026-01-07T09:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-22",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-22T18:26:23Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:02:05Z",
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
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "KS"
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
      "sponsorshipDate": "2025-12-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6229ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6229\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Schrier (for herself, Mr. Newhouse , Mr. Garamendi , Mr. LaMalfa , Mr. Costa , Mr. Fong , and Ms. Davids of Kansas ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reauthorize the Water Infrastructure Finance and Innovation Act of 2014, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Water Infrastructure Finance and Innovation Act Amendments of 2025 .\n#### 2. Clarifications regarding small communities and rural water projects\n##### (a) Definitions\nSection 5022 of the Water Resources Reform and Development Act of 2014 ( 33 U.S.C. 3901 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (11) through (15) as paragraphs (13) through (17), respectively;\n**(2)**\nby redesignating paragraph (10) as paragraph (11);\n**(3)**\nby inserting after paragraph (9) the following:\n(10) Rural water project The term rural water project includes\u2014 (A) a rural water supply project authorized under the Reclamation Rural Water Supply Act of 2006 ( 43 U.S.C. 2401 ); (B) any project authorized under part III of subtitle A of title X of the Omnibus Public Land Management Act of 2009 ( Public Law 111\u201311 ), for a federally recognized Indian Tribe; and (C) any rural water project or rural water supply project authorized under\u2014 (i) section 1110 of title XI of division FF of the Consolidated Appropriations Act, 2021 ( Public Law 116\u2013260 ); or (ii) any other Federal law. ; and\n**(4)**\nby inserting after paragraph (11), as so redesignated, the following:\n(12) Small community The term small community means a city, town, or unincorporated area that has a population of not more than 25,000 inhabitants. .\n##### (b) Eligible project costs\nSection 5028(a)(2)(B) of the Water Resources Reform and Development Act of 2014 ( 33 U.S.C. 3907(a)(2)(B) ) is amended by striking $5,000,000 and inserting $1,000,000 .\n##### (c) Authority To provide assistance for project development\nSection 5023 of the Water Resources Reform and Development Act of 2014 ( 33 U.S.C. 3902 ) is amended by adding at the end the following:\n(c) Technical assistance to small communities (1) In general The Administrator may provide technical assistance to small communities to aid such communities in developing a proposal for an eligible project and seeking assistance under this subtitle to carry out such project. (2) Types of assistance Assistance under paragraph (1) may be in the form of engineering and financial planning assistance. .\n##### (d) Conforming amendments\n**(1) Eligible project costs**\nSection 5028(a)(2)(B) of the Water Resources Reform and Development Act of 2014 ( 33 U.S.C. 3907(a)(2)(B) ) is further amended by striking a community of not more than 25,000 individuals and inserting a small community .\n**(2) Funding**\nSection 5033 of the Water Resources Reform and Development Act of 2014 ( 33 U.S.C. 3912 ) is amended\u2014\n**(A)**\nin subsection (b)(2) by inserting (other than technical assistance under section 5023(c)) after technical assistance ; and\n**(B)**\nin subsection (c)(1) by inserting and for technical assistance to small communities under section 5023(c) before the period at the end.\n**(3) Outreach plans**\nSection 5036 of the Water Resources Reform and Development Act of 2014 ( 33 U.S.C. 3915 ) is amended to read as follows:\n5036. Outreach plan to small communities Not later than 180 days after the date of enactment of the Water Infrastructure Finance and Innovation Act Amendments of 2025, the Administrator, in consultation with relevant Federal agencies, shall develop and begin implementation of an outreach plan to promote financial assistance available under this subtitle to small communities. .\n#### 3. Clarifying eligibility for certain projects\nThe Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3901 et seq. ) is amended\u2014\n**(1)**\nin section 5023(b)(3) ( 33 U.S.C. 3902(b)(3) ), by striking under paragraph (8) or (10) and inserting under paragraphs (8), (10), (11), (12), or (13) ; and\n**(2)**\nin section 5026 ( 33 U.S.C. 3905 )\u2014\n**(A)**\nin paragraph (10), by striking or (8) and inserting (8), (11), (12), or (13) ; and\n**(B)**\nby adding at the end the following:\n(11) A State-led storage project (as such term is defined in section 4007(a) of the Water Infrastructure Improvements for the Nation Act ( 43 U.S.C. 390b note)). (12) Transferred works (as such term is defined in section 9601 of the Omnibus Public Land Management Act of 2009 ( 43 U.S.C. 510 )). (13) A congressionally authorized water resources development project that is owned or operated by a non-Federal entity. .\n#### 4. Collaborative project delivery methods\n##### (a) In general\nSection 5028 of the Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3907 ) is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Collaborative project delivery methods (1) Authorization The Secretary or the Administrator, as applicable, may select, in accordance with this section, a project to be carried out using a collaborative project delivery method (consistent with any applicable State or local law), including a construction management at-risk method and a design-build method. (2) Definitions In this subsection: (A) Collaborative project delivery method The term collaborative project delivery method means a method for carrying out a capital project that involves close collaboration among the eligible entity, the owner of the project (if different from the eligible entity), the designer of the project, and the contractor for the project, from design through completion of construction. (B) Construction management at-risk method The term construction management at-risk method means a collaborative project delivery method in which an engineering firm and a construction management at-risk firm are retained under 2 separate contracts for design and construction, respectively. (C) Design-build method The term design-build method means a collaborative project delivery method under which a single lead contract is entered into with a design-builder for design and construction. .\n##### (b) Study on the use of collaborative project delivery methods\nNot later than 180 days after the date of enactment of this Act, the Administrator of the Environmental Protection Agency, in coordination with the Regional Administrators, and the Secretary of the Army, acting through the Chief of Engineers, shall carry out, and make public the results of, a study that\u2014\n**(1)**\nevaluates the use of collaborative project delivery methods in projects carried out using assistance received under the Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3901 et seq. );\n**(2)**\ndetermines barriers to increased use of collaborative project delivery methods in such projects;\n**(3)**\nassesses the potential benefits of using collaborative project delivery methods in such projects; and\n**(4)**\nidentifies areas of need to educate agency staff in collaborative project delivery method implementation and best practices.\n#### 5. Maturity date\nSection 5029(b)(5) of the Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3908(b)(5) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking The final maturity date and inserting Notwithstanding subparagraphs (A) and (B), the final maturity date ;\n**(2)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(3)**\nby inserting after subparagraph (A) the following:\n(B) Projects with a useful life of more than 35 years Notwithstanding subparagraph (A), for a project with a useful life of more than 35 years (as determined by the Secretary or the Administrator, as applicable), the final maturity date of a secured loan under this section shall be not later than the earlier of\u2014 (i) the date that is 55 years after the date of substantial completion of the relevant project (as determined by the Secretary or the Administrator, as applicable); and (ii) if the useful life of the project is less than 55 years, the useful life of the project. .\n#### 6. Reauthorization of Corps of Engineers water infrastructure financing funding\nSection 5033 of the Water Resources Reform and Development Act of 2014 ( 33 U.S.C. 3912 ) is further amended\u2014\n**(1)**\nby amending subsection (a)(3) to read as follows:\n(3) Fiscal years 2025 through 2029 There is authorized to be appropriated to carry out this subtitle, to remain available until expended\u2014 (A) $68,000,000 to the Administrator for each of fiscal years 2025 through 2029; and (B) $15,000,000 to the Secretary for each of fiscal years 2025 through 2029. ; and\n**(2)**\nin subsection (b)(2), by striking the Administrator and inserting the Secretary or the Administrator, as applicable, .\n#### 7. Budgetary treatment of certain amounts of financial assistance\nThe Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3901 et seq. ) is amended by adding at the end the following:\n5037. Budgetary treatment of certain amounts of financial assistance If the recipient of financial assistance for a project under this subtitle is an eligible entity other than a Federal entity, agency, or instrumentality, and the dedicated sources of repayment of that financial assistance are non-Federal revenue sources, such financial assistance shall, for purposes of budgetary treatment under the Federal Credit Reform Act of 1990 ( 2 U.S.C. 661 et seq. )\u2014 (1) be deemed to be non-Federal; and (2) be treated as a direct loan or loan guarantee (as such terms are defined, respectively, in such Act). .\n#### 8. Reports to Congress\n##### (a) EPA report\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Environmental Protection Agency shall submit to Congress a report on the implementation of\u2014\n**(1)**\nsection 4301 of America\u2019s Water Infrastructure Act of 2018 ( 33 U.S.C. 3909 note); and\n**(2)**\nany agreement entered into under section 5030(g) of the Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3909(g) ) pursuant to such section 4301.\n##### (b) Corps of Engineers report\nNot later than 1 year after the date of enactment of this Act, the Secretary of the Army, acting through the Chief of Engineers, shall submit to Congress a report on the implementation of the Corps Water Infrastructure Financing Program carried out pursuant to the Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3901 et seq. ), including issues pertaining to such implementation with respect to levees and congressionally authorized projects described in section 5026(1) of such Act.\n##### (c) GAO report\nSection 5034(b) of the Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3913(b) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking Not later than 3 years after the date of enactment of the Water Resources Development Act of 2018 and inserting Not later than 4 years after the date of enactment of the Water Infrastructure Finance and Innovation Act Amendments of 2025 ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (C) and (D), respectively, and inserting after subparagraph (A) the following:\n(B) an evaluation of the implementation of this subtitle by the Secretary; ; and\n**(B)**\nin subparagraph (D) (as so redesignated)\u2014\n**(i)**\nby inserting evaluations and before recommendations ; and\n**(ii)**\nby striking subparagraphs (A) and (B) and inserting subparagraphs (A), (B), and (C) .\n#### 9. Technical and conforming amendments\nThe Water Resources Reform and Development Act of 2014 ( 33 U.S.C. 2201 et seq. ) is amended\u2014\n**(1)**\nin section 1(b)\u2014\n**(A)**\nin the item relating to the heading for subtitle C of title V, by striking Pilot ;\n**(B)**\nin the item relating to section 5034, by striking pilot ; and\n**(C)**\nby inserting after the item relating to section 5035 the following:\n5036. Outreach plan to small communities. 5037. Budgetary treatment of certain amounts of financial assistance. ;\n**(2)**\nin the heading for subtitle C of title V, by striking Pilot ; and\n**(3)**\nin section 5022(12), by striking et. and inserting et .",
      "versionDate": "2025-11-20",
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
        "name": "Water Resources Development",
        "updateDate": "2025-12-12T14:30:13Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6229ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the Water Infrastructure Finance and Innovation Act of 2014, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-12T17:24:34Z"
    },
    {
      "title": "Water Infrastructure Finance and Innovation Act Amendments of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T14:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Water Infrastructure Finance and Innovation Act Amendments of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-12T14:23:19Z"
    }
  ]
}
```
