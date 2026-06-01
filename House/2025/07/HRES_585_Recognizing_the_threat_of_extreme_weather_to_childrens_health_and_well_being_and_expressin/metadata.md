# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/585?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/585
- Title: Recognizing the threat of extreme weather to children's health and well-being, and expressing the sense of Congress that solutions must be rapidly and equitably developed and deployed to address the unique vulnerabilities and needs of children.
- Congress: 119
- Bill type: HRES
- Bill number: 585
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-04-06T19:29:47Z
- Update date including text: 2026-04-06T19:29:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-07-16 - IntroReferral: Submitted in House
- 2025-07-16 - IntroReferral: Submitted in House
- Latest action: 2025-07-16: Submitted in House

## Actions

- 2025-07-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-07-16 - IntroReferral: Submitted in House
- 2025-07-16 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/585",
    "number": "585",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001227",
        "district": "4",
        "firstName": "Jennifer",
        "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
        "lastName": "McClellan",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Recognizing the threat of extreme weather to children's health and well-being, and expressing the sense of Congress that solutions must be rapidly and equitably developed and deployed to address the unique vulnerabilities and needs of children.",
    "type": "HRES",
    "updateDate": "2026-04-06T19:29:47Z",
    "updateDateIncludingText": "2026-04-06T19:29:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-07-16T14:00:15Z",
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
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "FL"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "OR"
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
      "sponsorshipDate": "2025-07-16",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NM"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "FL"
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
      "sponsorshipDate": "2025-07-16",
      "state": "NC"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "TN"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
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
      "sponsorshipDate": "2025-07-16",
      "state": "LA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NV"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "GA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "FL"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NV"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "TX"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NY"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "OR"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MN"
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
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NC"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "IN"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MO"
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
      "sponsorshipDate": "2025-07-16",
      "state": "IL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NJ"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres585ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 585\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Ms. McClellan (for herself, Ms. Castor of Florida , Ms. Bonamici , Ms. Norton , Ms. Tlaib , Ms. Stansbury , Ms. Barrag\u00e1n , Mr. Mullin , Mr. Thanedar , Mrs. Cherfilus-McCormick , Mrs. Foushee , Mr. Cohen , Mr. Huffman , Mr. Carter of Louisiana , Ms. Titus , Mr. Johnson of Georgia , Mr. Soto , Ms. Scanlon , Mr. Horsford , Ms. Garcia of Texas , Mr. Tonko , Mr. Evans of Pennsylvania , Ms. Dexter , Mr. Takano , Ms. McCollum , Ms. Lee of Pennsylvania , Mr. DeSaulnier , Mr. Peters , Ms. Adams , Mr. Carson , Mr. Cleaver , Mr. Davis of Illinois , and Mrs. Watson Coleman ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the threat of extreme weather to children\u2019s health and well-being, and expressing the sense of Congress that solutions must be rapidly and equitably developed and deployed to address the unique vulnerabilities and needs of children.\nThat the House of Representatives\u2014\n**(1)**\nexpresses the sense that adaptations to and protections from extreme weather conditions must be developed and deployed rapidly and equitably, with consideration for the physical and mental health needs of both the current generation and all future generations of young people;\n**(2)**\nexpresses the sense that legislation and funding addressing adaptation to and protections from extreme weather conditions must include considerations and solutions tailored to the unique physical and mental health vulnerabilities and needs of babies, children, adolescents, and their families; and\n**(3)**\nexpresses the sense that adaptive measures may include, but are not limited to\u2014\n**(A)**\naccurate, timely, and easily accessible public alerts before, during, and after extreme weather events, such as hazardous air quality days, wildfires, extreme heat, strong storms, or anticipated flooding;\n**(B)**\nmutual aid networks, caregiver support, and community resilience programs;\n**(C)**\nlanguage-accessible public information campaigns, such as for air quality, extreme heat, or disaster preparedness;\n**(D)**\nincorporation of education about the unique vulnerabilities of children and pregnant people to extreme weather into professional training for health care professionals, educators, and child care providers;\n**(E)**\nincorporation of perspectives of parents, caregivers, and other child care providers into disaster resilience planning efforts;\n**(F)**\ninclusion of education about the consequences of heat exposure and first-aid treatment measures for hyperthermia;\n**(G)**\nimproved guidance for schools and child care providers on extreme weather, extreme heat, and air pollution for schools;\n**(H)**\nimproved air filtration systems in homes, schools, and child care facilities to address numerous sources of air pollution, including wildfire smoke, vehicle exhaust, and pollen;\n**(I)**\nupdated physical and technological infrastructure of schools, child care facilities, and health care delivery systems serving children to withstand extreme weather disruption;\n**(J)**\nexpanded access to public shaded green space, particularly in urban heat islands;\n**(K)**\nexpanded access to safe places for children and families during extreme weather and air pollution events, such as indoor play spaces, child-friendly cooling centers, and child-friendly clean rooms during wildfire smoke events;\n**(L)**\naccess to diapers, baby bottles and formula, safe and hygienic nursing spaces, and other critical supplies for babies in spaces where families may congregate during and after extreme weather, such as evacuation centers, emergency shelters, and cooling centers;\n**(M)**\ndistribution of infant feeding kits before, during, and after emergencies;\n**(N)**\nadequate shade at playgrounds and school bus stops;\n**(O)**\ndistribution of appropriate child-sized masks during wildfire smoke events or days of unhealthy air quality; and\n**(P)**\nexpanded access to hydration and refilling stations.",
      "versionDate": "2025-07-16",
      "versionType": "IH"
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
        "name": "Environmental Protection",
        "updateDate": "2025-07-29T13:58:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-16",
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
          "measure-id": "id119hres585",
          "measure-number": "585",
          "measure-type": "hres",
          "orig-publish-date": "2025-07-16",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres585v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-07-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses the sense that adaptations to and protections from extreme weather conditions must be developed and deployed rapidly and equitably, with consideration for the physical and mental health needs of current and future generations of young people.</p>"
        },
        "title": "Recognizing the threat of extreme weather to children's health and well-being, and expressing the sense of Congress that solutions must be rapidly and equitably developed and deployed to address the unique vulnerabilities and needs of children."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres585.xml",
    "summary": {
      "actionDate": "2025-07-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses the sense that adaptations to and protections from extreme weather conditions must be developed and deployed rapidly and equitably, with consideration for the physical and mental health needs of current and future generations of young people.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres585"
    },
    "title": "Recognizing the threat of extreme weather to children's health and well-being, and expressing the sense of Congress that solutions must be rapidly and equitably developed and deployed to address the unique vulnerabilities and needs of children."
  },
  "summaries": [
    {
      "actionDate": "2025-07-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses the sense that adaptations to and protections from extreme weather conditions must be developed and deployed rapidly and equitably, with consideration for the physical and mental health needs of current and future generations of young people.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres585"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres585ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Recognizing the threat of extreme weather to children's health and well-being, and expressing the sense of Congress that solutions must be rapidly and equitably developed and deployed to address the unique vulnerabilities and needs of children.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T13:18:19Z"
    },
    {
      "title": "Recognizing the threat of extreme weather to children's health and well-being, and expressing the sense of Congress that solutions must be rapidly and equitably developed and deployed to address the unique vulnerabilities and needs of children.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:31Z"
    }
  ]
}
```
