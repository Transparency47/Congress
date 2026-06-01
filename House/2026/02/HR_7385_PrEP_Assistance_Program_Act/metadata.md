# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7385?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7385
- Title: PrEP Assistance Program Act
- Congress: 119
- Bill type: HR
- Bill number: 7385
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-04-17T08:07:00Z
- Update date including text: 2026-04-17T08:07:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7385",
    "number": "7385",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "PrEP Assistance Program Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:00Z",
    "updateDateIncludingText": "2026-04-17T08:07:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:04:15Z",
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
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
      "sponsorshipDate": "2026-02-04",
      "state": "DC"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "TN"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7385ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7385\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mrs. Watson Coleman (for herself, Mr. Carson , Ms. Waters , Ms. Tlaib , Ms. Sewell , Mr. Pocan , Ms. Norton , Ms. Moore of Wisconsin , Mr. Davis of Illinois , Mr. Keating , Mr. Thompson of Mississippi , Ms. Ansari , and Ms. Kelly of Illinois ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, to establish a grant program related to pre-exposure prophylaxis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the PrEP Assistance Program Act .\n#### 2. Pre-exposure prophylaxis grant program\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention (in this section referred to as the Secretary ) and in collaboration with the Administrator of the Health Resources and Services Administration, shall establish a program that provides grants to eligible entities to establish and support PrEP programs.\n##### (b) Applications\nTo be eligible to receive a grant under subsection (a), an eligible entity shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including a description of how any amounts awarded shall be used.\n##### (c) Preference\nIn making grants under this section, the Secretary shall give preference to an eligible entity that demonstrates a record of\u2014\n**(1)**\nserving communities with disproportionately high rate of incidence for human immunodeficiency virus (in this section referred to as HIV ), including individuals located in rural communities, uninsured individuals, or individuals in demographic groups at high risk of contracting HIV; or\n**(2)**\nimplementing innovative models to provide items or services, including the use of vending machines, pop-up clinics, and peer-led interventions.\n##### (d) Amount\nAny grant provided to an eligible entity under this section may not exceed $10,000,000.\n##### (e) Use of funds\n**(1) In general**\nAny eligible entity that is awarded an amount under subsection (a) shall use such amount for expenses associated with establishing a PrEP program or supporting an existing PrEP program.\n**(2) Eligible expenses**\nThe Secretary shall publish a list of eligible expenses associated with establishing a PrEP program or supporting an existing PrEP program. Such list shall include\u2014\n**(A)**\nclinic and laboratory fees;\n**(B)**\noffice visits, including telehealth visits;\n**(C)**\nPrEP medication;\n**(D)**\nblood and urine testing as required in association with the use of PrEP medication;\n**(E)**\nsexually transmitted disease testing in accordance with guidelines issued by the Centers for Disease Control and Prevention;\n**(F)**\nadherence services and counseling;\n**(G)**\noutreach activities directed toward assisting health professionals to become eligible to prescribe pre-exposure prophylaxis medications in the State or Indian Tribal government where the program is operating;\n**(H)**\noutreach activities directed toward physicians that provide education about PrEP;\n**(I)**\npeer navigation;\n**(J)**\ncase management;\n**(K)**\ntransportation support;\n**(L)**\nmental health services; and\n**(M)**\nother similar items or services.\n##### (f) Payment for services\nAn individual that receives a service or item from a PrEP program established or supported using amounts under this section may not be required to provide payment for such service or item.\n##### (g) Matching\n**(1) In general**\nExcept with respect to an Indian Tribal government, a grantee under this section shall contribute, to the PrEP program established or supported by the grant, an amount equal to not less than 10 percent of the amount of the grant.\n**(2) Exception**\nThe Secretary may waive the requirement under paragraph (1) for a Federally qualified health center, rural health clinic, community-based organization, hospital-based clinic, or university-based clinic if the Secretary determines such a waiver is necessary.\n##### (h) Report to Congress\n**(1) In general**\nThe Secretary shall, in each of the first 5 years beginning 1 year after the date of the enactment of this Act, submit to Congress, and make public on the internet website of the Department of Health and Human Services, a report on the impact of grants provided to eligible entities under this Act.\n**(2) Contents**\nA report submitted under paragraph (1) shall\u2014\n**(A)**\ninclude disaggregated data by race, gender identity, age, and geographic location; and\n**(B)**\nevaluate, with respect to the period covered by the report, any reduction in\u2014\n**(i)**\nthe disparity of the prevalence of PrEP services provided within the demographics described in this paragraph; and\n**(ii)**\nthe prevalence of PrEP.\n##### (i) Authorization of Appropriations\nThere are authorized to be appropriated to carry out this Act $400,000,000 for each of fiscal years 2027 through 2031.\n##### (j) Definitions\nIn this Act:\n**(1) Community-based organization**\nThe term community-based organization means a nonprofit or private organization that\u2014\n**(A)**\nrepresents a community or significant segments of a community;\n**(B)**\nprovides health care or health-related services to high-risk or high-need individuals in a community; and\n**(C)**\ndemonstrates effectiveness with respect to such health care or health-related services.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State;\n**(B)**\na local government;\n**(C)**\nan Indian Tribal government;\n**(D)**\na Federally qualified health center (as defined in section 1861(aa) of the Social Security Act ( 42 U.S.C. 1395x(aa) ));\n**(E)**\na rural health clinic (as defined in section 1861(aa) of the Social Security Act ( 42 U.S.C. 1395x(aa) ));\n**(F)**\na community-based organization;\n**(G)**\na hospital-based clinic; or\n**(H)**\na university-based clinic.\n**(3) Indian Tribal government**\nThe term Indian Tribal government means the governing body of any Indian tribe (as defined in section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130 )).\n**(4) PrEP program**\nThe term PrEP program means a program designed to provide pre-exposure prophylaxis and pre-exposure prophylaxis-related services to individuals.\n**(5) PrEP medication**\nThe term PrEP medication means any medication approved by the Federal Drug Administration and designed to prevent individuals at risk of contracting HIV from contracting HIV.\n**(6) State**\nThe term State means each State of the United States, the District of Columbia, Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n#### 3. Requiring the Secretary of Health and Human Services to establish a program to reimburse health care providers for furnishing specified HIV prevention items and services to uninsured individuals\n##### (a) In general\nNot later than 1 year after the date of the enactment of this section, the Secretary of Health and Human Services shall establish a program under which\u2014\n**(1)**\nprogram-registered providers submit claims to the Secretary with respect to the furnishing of specified HIV prevention items and services to uninsured individuals;\n**(2)**\nthe Secretary, subject to the availability of appropriations, pays each such provider for such items and services in an amount established under subsection (b) ; and\n**(3)**\nthe Secretary provides for the development and distribution of a card (or other technology), to be referred to as a PrEP Pass , that may be used by an uninsured individual to assure access to specified HIV prevention items and services from program-registered providers at no cost to such individual.\n##### (b) Payment amount\n**(1) In general**\nSubject to paragraph (2) , the Secretary shall establish a payment amount for each specified HIV prevention item or service under the program under subsection (a) . The Secretary shall review such payment amount not less frequently than once every 2 years.\n**(2) Laboratory tests**\nIn the case of a specified HIV prevention item or service that is a clinical diagnostic laboratory test covered under part B of title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), the payment amount for such test under the program under subsection (a) shall be equal to the payment amount determined with respect to such test under section 1834A of such Act.\n##### (c) Definitions\nIn this section:\n**(1) Specified HIV prevention items and services**\nThe term specified HIV prevention items and services means\u2014\n**(A)**\nany drug approved by the Federal Drug Administration for the prevention of HIV, including any such drug approved for use as pre-exposure prophylaxis (commonly referred to as PrEP ), and administrative fees for such drugs; and\n**(B)**\nlaboratory and other diagnostic procedures associated with the use of such drugs that are recommended in the most recent clinical practice guidelines of the Centers for Disease Control and Prevention.\n**(2) Program-registered provider**\nThe term program-registered provider means a health care provider that\u2014\n**(A)**\nis licensed or otherwise authorized to furnish a specified HIV prevention item or service in the State in which such provider furnishes such item or service under the program established under this section; and\n**(B)**\nenters into an agreement with the Secretary under which the provider agrees not to hold an uninsured individual liable for the cost of specified HIV prevention items and services with respect to which a payment is made under subsection (a)(2) .\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration.\n**(4) Uninsured individual**\nThe term uninsured individual means, with respect to an individual furnishing a specified HIV prevention item or service, an individual who is not enrolled in\u2014\n**(A)**\na Federal health care program (as defined in section 1128B(f) of the Social Security Act (42 U.S.C. 1320a\u20137b(f)));\n**(B)**\na group health plan or health insurance coverage offered by a health insurance issuer in the group or individual market (as such terms are defined in section 2791 of the Public Health Service Act ( 42 U.S.C. 300gg\u201391 )); or\n**(C)**\na health plan offered under chapter 89 of title 5, United States Code.",
      "versionDate": "2026-02-04",
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
        "name": "Health",
        "updateDate": "2026-02-19T16:42:25Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7385ih.xml"
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
      "title": "PrEP Assistance Program Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T04:43:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PrEP Assistance Program Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-13T04:43:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, to establish a grant program related to pre-exposure prophylaxis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-13T04:18:32Z"
    }
  ]
}
```
