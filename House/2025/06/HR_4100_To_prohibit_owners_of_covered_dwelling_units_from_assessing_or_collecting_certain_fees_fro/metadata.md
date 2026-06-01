# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4100?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4100
- Title: End Junk Fees for Renters Act
- Congress: 119
- Bill type: HR
- Bill number: 4100
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2026-04-15T08:05:53Z
- Update date including text: 2026-04-15T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-19 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-19 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4100",
    "number": "4100",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "F000476",
        "district": "10",
        "firstName": "Maxwell",
        "fullName": "Rep. Frost, Maxwell [D-FL-10]",
        "lastName": "Frost",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "End Junk Fees for Renters Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:53Z",
    "updateDateIncludingText": "2026-04-15T08:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:02:33Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-24T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "TX"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "PA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MI"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "WI"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MN"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "WA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VT"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "AZ"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "CT"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4100ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4100\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Frost (for himself, Mr. Gomez , Ms. Chu , Mr. Casar , Mr. Khanna , Ms. Schakowsky , Ms. Lee of Pennsylvania , Ms. Tlaib , Ms. Ocasio-Cortez , Mr. Goldman of New York , Mr. Pocan , Mr. Garcia of California , Ms. Omar , Mrs. McIver , Mr. Mullin , Ms. Jayapal , Mr. Lieu , Mrs. Watson Coleman , Ms. Clarke of New York , Ms. Balint , and Mrs. Ramirez ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Veterans\u2019 Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit owners of covered dwelling units from assessing or collecting certain fees from tenants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Junk Fees for Renters Act .\n#### 2. Rental Junk Fees\n##### (a) Application fees\nThe appropriate regulator shall prohibit the owner of a covered dwelling unit from assessing or collecting a fee or charge, from any household in connection with the submission of an application for rental of such dwelling unit.\n##### (b) Tenant screening fees\nThe appropriate regulator shall prohibit the owner of a covered dwelling unit from assessing to or collecting from any household applying to rent such dwelling unit any fee or charge for costs of conducting any criminal history, tenant screening, consumer report, or other background check of such household.\n##### (c) Late fees\nThe appropriate regulator shall require that owners of covered dwelling units\u2014\n**(1)**\nonly impose fees or charges on tenants in connection with the late payment of rent for a covered dwelling unit if the amount of such fee or charge is less than 3 percent of the monthly rent the tenant pays for such covered dwelling unit;\n**(2)**\nonly impose fees or charges on tenants in connection with the late payment of rent for a covered dwelling unit if 15 days have elapsed since the date on which the rent was due; and\n**(3)**\ndisclose the requirements imposed under paragraphs (1) and (2) in any lease entered for a covered dwelling unit on or after the date on which rules are issued under section 3.\n##### (d) Required disclosures\nThe appropriate regulator shall require each owner of a covered dwelling unit to disclose to the tenant before a lease is signed\u2014\n**(1)**\nthe total amount due each month, including any fees;\n**(2)**\nto the degree practicable, a summary of any past litigation between the such owner and any former or current tenants;\n**(3)**\na description of any ongoing pest and maintenance issues; and\n**(4)**\nthe amount rent increase for the property in each of the 10 previous years.\n##### (e) Definitions\nIn this section:\n**(1) Appropriate regulator**\nThe term appropriate regulator means\u2014\n**(A)**\nthe Secretary of Housing and Urban Development, with respect to covered dwelling units described in\u2014\n**(i)**\nparagraph (2)(A);\n**(ii)**\nparagraph (2)(B), to the extent the Federally backed mortgage loan referred to in such paragraph is described in subparagraph (A), (B), or (C) of paragraph (3); or\n**(iii)**\nparagraph (2)(B), to the extent the Federally backed mortgage loan referred to in such paragraph is described in paragraph (4) and is made in whole or in part, or insured, guaranteed, supplemented, or assisted in any way under or in connection with a housing or urban development program administered by the Secretary of Housing and Urban Development;\n**(B)**\nthe Secretary of Veterans Affairs, with respect to covered dwelling units described in paragraph (2)(B), to the extent the Federally backed mortgage loan referred to in such paragraph is described in\u2014\n**(i)**\nparagraph (3)(D); or\n**(ii)**\nparagraph (4) and is made in whole or in part, or insured, guaranteed, supplemented, or assisted in any way, by the Secretary of Veterans Affairs or under or in connection with a housing or related program administered by Secretary of Veterans Affairs;\n**(C)**\nthe Secretary of Agriculture, with respect to covered dwelling units described in paragraph (2)(B), to the extent the Federally backed mortgage loan referred to in such paragraph is described in\u2014\n**(i)**\nsubparagraph (E) or (F) of paragraph (3); or\n**(ii)**\nparagraph (4) and is made in whole or in part, or insured, guaranteed, supplemented, or assisted in any way, by the Secretary of Agriculture or under or in connection with a housing or related program administered by Secretary of Agriculture; and\n**(D)**\nthe Director of the Federal Housing Finance Agency, with respect to covered dwelling units described in paragraph (2)(B), to the extent the Federally backed mortgage loan referred to in such paragraph is described in\u2014\n**(i)**\nparagraph (3)(G); or\n**(ii)**\nparagraph (4) and is purchased or securitized by the Federal Home Loan Mortgage Corporation or the Federal National Mortgage Association.\n**(2) Covered dwelling unit**\nThe term covered dwelling unit means a dwelling unit that\u2014\n**(A)**\nis provided assistance within the jurisdiction of the Department, as such term is defined in section 102(m) of the Department of Housing and Urban Development Reform Act of 1989 ( 42 U.S.C. 3545(m) ); or\n**(B)**\nis subject to, or is on or in a property that is subject to a Federally backed single-family mortgage loan or a Federally backed multifamily mortgage loan.\n**(3) Federally backed single-family mortgage loan**\nThe term Federally backed single-family mortgage loan includes any loan that is secured by a first or subordinate lien on residential real property (including individual units of condominiums and cooperatives) designed principally for the occupancy of from 1- to 4-families that is\u2014\n**(A)**\ninsured by the Federal Housing Administration under title II of the National Housing Act ( 12 U.S.C. 1707 et seq. );\n**(B)**\ninsured under section 255 of the National Housing Act ( 12 U.S.C. 1715z\u201320 );\n**(C)**\nguaranteed under section 184 or 184A of the Housing and Community Development Act of 1992 (12 U.S.C. 1715z\u201313a, 1715z\u201313b);\n**(D)**\nguaranteed or insured by the Department of Veterans Affairs;\n**(E)**\nguaranteed or insured by the Department of Agriculture;\n**(F)**\nmade by the Department of Agriculture; or\n**(G)**\npurchased or securitized by the Federal Home Loan Mortgage Corporation or the Federal National Mortgage Association.\n**(4) Federally backed multifamily mortgage loan**\nThe term Federally backed multifamily mortgage loan includes any loan (other than temporary financing such as a construction loan) that\u2014\n**(A)**\nis secured by a first or subordinate lien on residential multifamily real property designed principally for the occupancy of 5 or more families, including any such secured loan, the proceeds of which are used to prepay or pay off an existing loan secured by the same property; and\n**(B)**\nis made in whole or in part, or insured, guaranteed, supplemented, or assisted in any way, by any officer or agency of the Federal Government or under or in connection with a housing or urban development program administered by the Secretary of Housing and Urban Development or a housing or related program administered by any other such officer or agency, or is purchased or securitized by the Federal Home Loan Mortgage Corporation or the Federal National Mortgage Association.\n**(5) Owner**\nThe term owner means, with respect to a dwelling unit, any private person or entity, including a cooperative, an agency of the Federal Government, or a public housing agency, having the legal right to lease or sublease the dwelling unit.\n#### 3. Rulemaking\nThe Bureau of Consumer Financial Protection and the Federal Trade Commission shall, not later than 180 days after the date of the enactment of this section issue a rule that\u2014\n**(1)**\ndefines the term junk fee with respect to rental housing; and\n**(2)**\nfinds the furnishing of any information about a unpaid junk fee (as such term is defined pursuant to paragraph (1)) to a consumer reporting agency to be a unfair or unconscionable means to collect or attempt to collect debt in violation of section 808 of the Fair Debt Collection Practices Act.",
      "versionDate": "2025-06-24",
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
        "actionDate": "2025-06-24",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "End Junk Fees for Renters Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-07-15T11:06:50Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4100ih.xml"
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
      "title": "End Junk Fees for Renters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End Junk Fees for Renters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit owners of covered dwelling units from assessing or collecting certain fees from tenants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T09:18:29Z"
    }
  ]
}
```
