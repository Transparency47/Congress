# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6660?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6660
- Title: Replace Animal Tests Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6660
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-05-16T08:07:36Z
- Update date including text: 2026-05-16T08:07:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6660",
    "number": "6660",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Replace Animal Tests Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:36Z",
    "updateDateIncludingText": "2026-05-16T08:07:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:06:42Z",
                "name": "Referred to"
              }
            },
            "name": "Conservation, Research, and Biotechnology Subcommittee",
            "systemCode": "hsag14"
          },
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:06:42Z",
                "name": "Referred to"
              }
            },
            "name": "Livestock, Dairy, and Poultry Subcommittee",
            "systemCode": "hsag29"
          }
        ]
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-11T16:05:45Z",
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
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MI"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "DC"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NV"
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
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6660ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6660\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Moskowitz (for himself, Ms. Schakowsky , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo ensure that non-animal methods for regulatory testing are used in lieu of animal tests whenever scientifically satisfactory non-animal test methods are available and accepted by regulatory agencies for meeting regulatory requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Replace Animal Tests Act of 2025 .\n#### 2. Animal testing\n##### (a) In general\nExcept as otherwise provided by this section, it shall be unlawful for any entity to submit to a covered agency, with respect to a product or substance, data that has been derived using an animal test method if\u2014\n**(1)**\na non-animal test method is available to meet the information requirement concerned, as determined by the covered agency; or\n**(2)**\nthe covered agency has issued a waiver exempting the entity from a requirement for data derived from an animal test method.\n##### (b) Exceptions\nSubsection (a) shall not apply with respect to\u2014\n**(1)**\ndata generated before the date of enactment of this Act;\n**(2)**\ndata generated from an animal test method conducted outside the United States in order to comply with a requirement from a foreign regulatory authority;\n**(3)**\ndata requested by a covered agency following a determination by the covered agency that\u2014\n**(A)**\nexisting data is insufficient for satisfying the information requirement concerned; and\n**(B)**\nno scientifically satisfactory non-animal test method was practicably available when the testing was conducted despite reasonable efforts to access a non-animal test method; and\n**(4)**\ndata generated from specified animal test methods requested in writing by a covered agency, which request shall include a clear justification by the covered agency that available non-animal test methods (if any) are not appropriate for the product or substance concerned.\n##### (c) Limiting harm to animals\nIn a case in which no appropriate non-animal test method is available and a waiver has not been granted by the covered agency concerned, the regulated entity shall\u2014\n**(1)**\nensure that the number of animals used in any animal test method is reduced to the minimum number possible without compromising the objectives of the test; and\n**(2)**\nreduce to a minimum any possible pain, suffering, distress, or lasting harm to the animals used.\n##### (d) Penalties\n**(1) Refusals to accept data**\nA covered agency may refuse to accept animal testing data generated in violation of this section.\n**(2) Civil penalties**\nIn addition to any other penalties under applicable law, a covered agency may impose on any person who violates this section a civil penalty in an amount of not more than $10,000 for each such violation, as determined by the regulatory authority of the covered agency.\n##### (e) Guidance; regulations\nA covered agency shall\u2014\n**(1)**\nnot later than one year after the date of enactment of this Act, issue guidance on the acceptability and use of non-animal test methods for products and substances regulated by the covered agency; and\n**(2)**\nto the extent the covered agency determines appropriate\u2014\n**(A)**\nrevise regulations to reflect the acceptability of non-animal test methods; and\n**(B)**\neliminate requirements for the corresponding animal test data.\n##### (f) Reporting\n**(1) Publication**\nNot later than one year after the date of enactment of this Act, and annually thereafter, each covered agency shall publish a progress report on the use of non-animal test methods by the covered agency and the entities regulated by the covered agency.\n**(2) Contents**\nA report published by a covered agency under paragraph (1) shall specify for all research that is conducted or supported by the covered agency or is submitted to the covered agencies by regulated entities\u2014\n**(A)**\nthe number of animals used;\n**(B)**\nthe species of animals used;\n**(C)**\nthe types of testing for which the animals were used;\n**(D)**\nthe number of waivers issued; and\n**(E)**\nthe purpose of animal test methods, non-animal test methods, and waivers accepted or issued by the covered agency.\n**(3) Public availability**\n**(A) In general**\nThe information collected by a covered agency for purposes of this subsection shall be made publicly available, as soon as practicable, on an internet website of the covered agency.\n**(B) Personally identifiable or proprietary information**\nBefore making such information publicly available, the covered agency shall omit personally identifiable information and proprietary information.\n##### (g) Definitions\nIn this section:\n**(1) Animal**\nThe term animal means a live vertebrate non-human animal or cephalopod.\n**(2) Animal test method**\nThe term animal test method means a test method that involves the use of live animals.\n**(3) Covered agency**\nThe term covered agency means\u2014\n**(A)**\nthe Consumer Product Safety Commission;\n**(B)**\nthe Department of Agriculture;\n**(C)**\nthe Environmental Protection Agency; and\n**(D)**\nthe Food and Drug Administration.\n**(4) Non-animal test method**\nThe term non-animal test method means a test method that\u2014\n**(A)**\ndoes not involve the use of live animals; and\n**(B)**\nhas been identified and accepted for use by the covered agency concerned.\n**(5) Test method**\nThe term test method means a process, procedure, or approach used to obtain information on the properties of a product or its ingredients.",
      "versionDate": "2025-12-11",
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
        "name": "Animals",
        "updateDate": "2026-04-10T14:09:19Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6660ih.xml"
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
      "title": "Replace Animal Tests Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Replace Animal Tests Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that non-animal methods for regulatory testing are used in lieu of animal tests whenever scientifically satisfactory non-animal test methods are available and accepted by regulatory agencies for meeting regulatory requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:27Z"
    }
  ]
}
```
