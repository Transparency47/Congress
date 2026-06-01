# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1782?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1782
- Title: Charlotte Woodward Organ Transplant Discrimination Prevention Act
- Congress: 119
- Bill type: S
- Bill number: 1782
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2026-05-14T11:03:27Z
- Update date including text: 2026-05-14T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1782",
    "number": "1782",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Charlotte Woodward Organ Transplant Discrimination Prevention Act",
    "type": "S",
    "updateDate": "2026-05-14T11:03:27Z",
    "updateDateIncludingText": "2026-05-14T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
            "date": "2025-05-15T17:23:24Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-15T17:23:24Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NH"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MN"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MS"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "RI"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "TN"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "VA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MO"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "GA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "DE"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "WV"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "KS"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "AZ"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MD"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "RI"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1782is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1782\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mrs. Moody (for herself, Ms. Hassan , Mr. Scott of Florida , Ms. Smith , Mr. Daines , Mr. Kaine , Mrs. Hyde-Smith , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit discrimination on the basis of mental or physical disability in cases of organ transplants.\n#### 1. Short title\nThis Act may be cited as the Charlotte Woodward Organ Transplant Discrimination Prevention Act .\n#### 2. Definitions\nIn this Act:\n**(1) Auxiliary aids and services**\nThe term auxiliary aids and services has the meaning given the term in section 4 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12103 ).\n**(2) Covered entity**\nThe term covered entity means any licensed provider of health care services (including licensed health care practitioners, hospitals, nursing facilities, laboratories, intermediate care facilities, psychiatric residential treatment facilities, institutions for individuals with intellectual or developmental disabilities, and prison health centers), and any transplant hospital (as defined in section 121.2 of title 42, Code of Federal Regulations or a successor regulation), that\u2014\n**(A)**\nis in interstate commerce; or\n**(B)**\nprovides health care services in a manner that\u2014\n**(i)**\nsubstantially affects or has a substantial relation to interstate commerce; or\n**(ii)**\nincludes use of an instrument (including an instrument of transportation or communication) of interstate commerce.\n**(3) Disability**\nThe term disability has the meaning given the term in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ).\n**(4) Human organ**\nThe term human organ has the meaning given the term in section 301(c) of the National Organ Transplant Act ( 42 U.S.C. 274e(c) ).\n**(5) Organ transplant**\nThe term organ transplant means the transplantation or transfusion of a donated human organ into the body of another human for the purpose of treating a medical condition.\n**(6) Qualified individual**\nThe term qualified individual means an individual who, with or without a support network, provision of auxiliary aids and services, or reasonable modifications to policies or practices, meets eligibility requirements for the receipt of a human organ.\n**(7) Reasonable modifications to policies or practices**\nThe term reasonable modifications to policies or practices includes\u2014\n**(A)**\ncommunication with persons responsible for supporting a qualified individual with postsurgical or other care following an organ transplant or related services, including support with medication;\n**(B)**\nconsideration, in determining whether a qualified individual will be able to comply with health requirements following an organ transplant or receipt of related services, of support networks available to the qualified individual, including family, friends, and providers of home and community-based services, including home and community-based services funded through the Medicare or Medicaid program under title XVIII or XIX, respectively, of the Social Security Act ( 42 U.S.C. 1395 et seq. , 1396 et seq.), another health plan in which the qualified individual is enrolled, or any program or source of funding available to the qualified individual; and\n**(C)**\nthe use of supported decision-making, when needed, by a qualified individual.\n**(8) Related services**\nThe term related services means services related to an organ transplant that consist of\u2014\n**(A)**\nevaluation;\n**(B)**\ncounseling;\n**(C)**\ntreatment, including postoperative treatment, and care;\n**(D)**\nprovision of information; and\n**(E)**\nany other service recommended or required by a physician.\n**(9) Supported decision-making**\nThe term supported decision-making means the use of a support person to assist a qualified individual in making health care decisions, communicate information to the qualified individual, or ascertain a qualified individual\u2019s wishes. Such term includes\u2014\n**(A)**\nthe inclusion of the individual\u2019s attorney-in-fact or health care proxy, or any person of the individual\u2019s choice, in communications about the individual\u2019s health care;\n**(B)**\npermitting the individual to designate a person of the individual\u2019s choice for the purposes of supporting that individual in communicating, processing information, or making health care decisions;\n**(C)**\nproviding auxiliary aids and services to facilitate the individual\u2019s ability to communicate and process health-related information, including providing use of assistive communication technology;\n**(D)**\nproviding health information to persons designated by the individual, consistent with the regulations promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996 ( 42 U.S.C. 1320d\u20132 note) and other applicable laws and regulations governing disclosure of health information;\n**(E)**\nproviding health information in a format that is readily understandable by the individual; and\n**(F)**\nworking with a court-appointed guardian or other person responsible for making health care decisions on behalf of the individual, to ensure that the individual is included in decisions involving the health care of the individual and that health care decisions are in accordance with the individual\u2019s own expressed interests.\n**(10) Support network**\nThe term support network means, with respect to a qualified individual, 1 or more people who are\u2014\n**(A)**\nselected by the qualified individual or by the qualified individual and the guardian of the qualified individual, to provide assistance to the qualified individual or guidance to that qualified individual in understanding issues, making plans for the future, or making complex decisions; and\n**(B)**\nwho may include the family members, friends, unpaid supporters, members of the religious congregation, and appropriate personnel at a community center, of or serving the qualified individual.\n#### 3. Prohibition of discriminatory policy\nThe board of directors described in section 372(b)(1)(B) of the Public Health Service Act ( 42 U.S.C. 274(b)(1)(B) ) shall not issue policies, recommendations, or other memoranda that would prohibit, or otherwise hinder, a qualified individual\u2019s access to an organ transplant solely on the basis of that individual\u2019s disability.\n#### 4. Prohibition of discrimination\n##### (a) In general\nSubject to subsection (b), a covered entity may not, solely on the basis of a qualified individual\u2019s disability\u2014\n**(1)**\ndetermine that the individual is ineligible to receive an organ transplant or related services;\n**(2)**\ndeny the individual an organ transplant or related services;\n**(3)**\nrefuse to refer the individual to an organ transplant center or other related specialist for the purpose of receipt of an organ transplant or other related services; or\n**(4)**\nrefuse to place the individual on an organ transplant waiting list.\n##### (b) Exception\n**(1) In general**\n**(A) Medically significant disabilities**\nNotwithstanding subsection (a), a covered entity may take a qualified individual\u2019s disability into account when making a health care treatment or coverage recommendation or decision, solely to the extent that the disability has been found by a physician, following an individualized evaluation of the potential recipient, to be medically significant to the receipt of the organ transplant or related services, as the case may be.\n**(B) Construction**\nSubparagraph (A) shall not be construed to require a referral or recommendation for, or the performance of, a medically inappropriate organ transplant or medically inappropriate related services.\n**(2) Clarification**\nIf a qualified individual has the necessary support network to provide a reasonable assurance that the qualified individual will be able to comply with health requirements following an organ transplant or receipt of related services, as the case may be, the qualified individual\u2019s inability to independently comply with those requirements may not be construed to be medically significant for purposes of paragraph (1).\n##### (c) Reasonable modifications\nA covered entity shall make reasonable modifications to policies or practices (including procedures) of such entity if such modifications are necessary to make an organ transplant or related services available to qualified individuals with disabilities, unless the entity can demonstrate that making such modifications would fundamentally alter the nature of such policies or practices.\n##### (d) Clarifications\n**(1) No denial of services because of absence of auxiliary aids and services**\nFor purposes of this section, a covered entity shall take such steps as may be necessary to ensure that a qualified individual with a disability is not denied a procedure associated with the receipt of an organ transplant or related services, because of the absence of auxiliary aids and services, unless the covered entity can demonstrate that taking such steps would fundamentally alter the nature of the procedure being offered or would result in an undue burden on the entity.\n**(2) Compliance with other law**\nNothing in this section shall be construed\u2014\n**(A)**\nto prevent a covered entity from providing organ transplants or related services at a level that is greater than the level that is required by this section; or\n**(B)**\nto limit the rights of an individual with a disability under, or to replace or limit the scope of obligations imposed by, the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) including the provisions added to such Act by the ADA Amendments Act of 2008 ( Public Law 110\u2013325 ), section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), section 1557 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18116 ), or any other applicable law.\n##### (e) Enforcement\n**(1) In general**\nAny individual who alleges that a qualified individual was subject to a violation of this section by a covered entity may bring a claim regarding the allegation to the Office for Civil Rights of the Department of Health and Human Services, for expedited resolution, as appropriate.\n**(2) Rule of construction**\nNothing in this subsection is intended to limit or replace available remedies under the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) or any other applicable law.\n#### 5. Application to each part of process\nThe provisions of this Act\u2014\n**(1)**\nthat apply to an organ transplant, also apply to the evaluation and listing of a qualified individual, and to the organ transplant and post-organ-transplant treatment of such an individual; and\n**(2)**\nthat apply to related services, also apply to the process for receipt of related services by such an individual.\n#### 6. Effect on other laws\nNothing in this Act shall be construed to supersede any provision of any State or local law that provides greater rights to qualified individuals with respect to organ transplants than the rights established under this Act.",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in Senate"
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
        "text": "Received in the Senate and Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1520",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Charlotte Woodward Organ Transplant Discrimination Prevention Act",
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
            "name": "Administrative remedies",
            "updateDate": "2026-04-27T18:01:41Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-04-27T18:01:41Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2026-04-27T18:01:41Z"
          },
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2026-04-27T18:01:41Z"
          },
          {
            "name": "Organ and tissue donation and transplantation",
            "updateDate": "2026-04-27T18:01:41Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-04-27T18:01:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-06-02T14:49:43Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1782is.xml"
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
      "title": "Charlotte Woodward Organ Transplant Discrimination Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Charlotte Woodward Organ Transplant Discrimination Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit discrimination on the basis of mental or physical disability in cases of organ transplants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:48Z"
    }
  ]
}
```
