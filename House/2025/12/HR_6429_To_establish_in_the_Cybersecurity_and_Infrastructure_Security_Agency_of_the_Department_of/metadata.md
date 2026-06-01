# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6429?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6429
- Title: Expanding Cybersecurity Workforce Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6429
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-16T08:07:34Z
- Update date including text: 2026-05-16T08:07:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-12-05 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-12-05 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6429",
    "number": "6429",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001313",
        "district": "11",
        "firstName": "Shontel",
        "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
        "lastName": "Brown",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Expanding Cybersecurity Workforce Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:34Z",
    "updateDateIncludingText": "2026-05-16T08:07:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-05",
      "committees": {
        "item": {
          "name": "Cybersecurity and Infrastructure Protection Subcommittee",
          "systemCode": "hshm08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-05T05:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Cybersecurity and Infrastructure Protection Subcommittee",
          "systemCode": "hshm08"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MI"
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
      "sponsorshipDate": "2025-12-04",
      "state": "IL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
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
      "sponsorshipDate": "2025-12-04",
      "state": "DC"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-04",
      "state": "IL"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "IN"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "AZ"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "TX"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "OH"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-04",
      "state": "MS"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "OH"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "WA"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "VI"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CT"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "GA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MO"
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
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NV"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "TX"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "PA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NC"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "LA"
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
      "sponsorshipDate": "2025-12-09",
      "state": "HI"
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
      "sponsorshipDate": "2026-02-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6429ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6429\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Ms. Brown (for herself, Ms. Stevens , Mrs. Ramirez , Ms. Wasserman Schultz , Ms. Norton , Mr. Quigley , Ms. Kelly of Illinois , Mr. Lynch , Mr. Carson , Ms. Ansari , Ms. Crockett , Mrs. Beatty , Ms. Brownley , Mr. Thompson of Mississippi , Mr. Landsman , Ms. Vel\u00e1zquez , Mr. Larsen of Washington , Ms. Plaskett , Mrs. Hayes , Mr. Min , Mrs. McBath , Mr. Bell , Mr. Goldman of New York , Mrs. Cherfilus-McCormick , Mr. Horsford , Ms. Johnson of Texas , Mr. Evans of Pennsylvania , Mrs. Foushee , and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo establish in the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security a program to promote the cybersecurity field to disadvantaged communities, including older individuals, racial and ethnic minorities, people with disabilities, geographically diverse communities, socioeconomically diverse communities, women, individuals from nontraditional educational paths, individuals who are veterans, and individuals who were formerly incarcerated, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Cybersecurity Workforce Act of 2025 .\n#### 2. Expansion of CISA\u2019s Cybersecurity Education and Training Assistance Program\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security shall establish within the Cybersecurity Education and Training Assistance Program of the Agency a program (in this section referred to as the Program ) to promote the cybersecurity field to disadvantaged communities, including older individuals, racial and ethnic minorities, people with disabilities, geographically diverse communities, socioeconomically diverse communities, women, individuals from nontraditional educational paths, individuals who are veterans, and individuals who were formerly incarcerated.\n##### (b) Outreach\nTo carry out subsection (a) and promote awareness of the Program, the Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security shall conduct outreach to different institutions to raise awareness of and promote the cybersecurity workforce, including to educators, unions, chambers of commerce, State and local workforce development offices, private sector entities, community colleges, parents of K-12 students, and other institutions as the Director determines appropriate.\n##### (c) Applicability\nThe Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security shall tailor the Program to the unique needs of each region and sector across the United States.\n##### (d) Annual reports\nNot later than one year after the date of the enactment of this Act and annually thereafter, the Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on the efficacy of the Program, including how the Program is impacting the general characteristics of the cyber workforce throughout the United States, and suggestions for Congress regarding how to improve the Program.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to the Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security $20,000,000 for fiscal year 2026 and each fiscal year thereafter through 2031.\n##### (f) Definitions\nIn this section:\n**(1) Disability**\nThe term disability means an intellectual or developmental disability.\n**(2) Geographically diverse**\nThe term geographically diverse means that the participants should be represented as close as possible to an equal spread of high-density urban areas, suburban areas, and rural areas of the United States or over-represent low-income communities.\n**(3) Nontraditional educational path**\nThe term nontraditional educational path means a graduate of any of the following:\n**(A)**\nA two year degree program, trade school, or community college.\n**(B)**\nA historically Black college or university.\n**(C)**\nA Hispanic-serving institution (as such term is defined in section 502(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1101a(a) )).\n**(D)**\nA Tribal College or University (as such term is defined in section 316(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059c(b) )).\n**(E)**\nAn Alaska Native-serving institution (as such term is defined in section 317(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059d(b) )).\n**(F)**\nA Native Hawaiian-serving institution (as such term is defined in section 317(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059d(b) )).\n**(G)**\nA Predominantly Black Institution (as such term is defined in section 318(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059e(b) )).\n**(H)**\nA Native American-serving, nontribal institution (as such term is defined in section 319(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059f(b) )).\n**(I)**\nAn Asian-American and Native American Pacific Islander-serving institution (as such term is defined in section 320(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059g(b) )).\n**(4) Older**\nThe term older means an individual who has attained the age of 40 or older as of the date on which such individual is scheduled to begin participation in the Program.\n**(5) Racial and ethnic minority**\nThe term racial and ethnic minority means Black or African American, Hispanic or Latino, Asian American, or Native American.\n**(6) Socioeconomically diverse**\nThe term socioeconomically diverse means a spread of income levels, including low-income individuals.",
      "versionDate": "2025-12-04",
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
        "name": "Labor and Employment",
        "updateDate": "2025-12-06T14:17:58Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6429ih.xml"
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
      "title": "Expanding Cybersecurity Workforce Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T09:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Cybersecurity Workforce Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T09:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish in the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security a program to promote the cybersecurity field to disadvantaged communities, including older individuals, racial and ethnic minorities, people with disabilities, geographically diverse communities, socioeconomically diverse communities, women, individuals from nontraditional educational paths, individuals who are veterans, and individuals who were formerly incarcerated, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-05T09:18:20Z"
    }
  ]
}
```
