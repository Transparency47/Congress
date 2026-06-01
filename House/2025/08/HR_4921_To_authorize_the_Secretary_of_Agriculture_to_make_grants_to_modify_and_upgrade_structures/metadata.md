# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4921?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4921
- Title: PUPP Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4921
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2026-03-27T08:06:46Z
- Update date including text: 2026-03-27T08:06:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-08 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-08 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4921",
    "number": "4921",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "PUPP Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:46Z",
    "updateDateIncludingText": "2026-03-27T08:06:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:30:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-08T15:30:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "PA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CO"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "NY"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MD"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MN"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "WI"
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
      "sponsorshipDate": "2025-12-10",
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
      "sponsorshipDate": "2025-12-10",
      "state": "NV"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MI"
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
      "sponsorshipDate": "2025-12-10",
      "state": "VA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4921ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4921\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Crow (for himself, Mr. Fitzpatrick , Ms. Pettersen , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the Secretary of Agriculture to make grants to modify and upgrade structures to serve as interim and permanent housing to accommodate unhoused individuals with pets, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing for Unhoused People and Pets Act of 2025 or the PUPP Act of 2025 .\n#### 2. Grant program for upgrading structures to serve as interim and permanent housing to accommodate unhoused individuals with pets\n##### (a) Authority\nThe Secretary of Agriculture, acting in direct consultation with the Secretary of Housing and Urban Development, may carry out a program under this section to make grants to eligible entities for providing interim and permanent housing that accommodates homeless persons, and homeless families, who have pets.\n##### (b) Use\nAmounts from a grant under this section may be used only for\u2014\n**(1)**\ncosts of acquiring, renovating, rehabilitating, re-purposing, retrofitting, or constructing a property to be used as interim or permanent housing that accommodates homeless persons, and homeless families, who have pets;\n**(2)**\npet-related costs of operating such housing as provided in this section; and\n**(3)**\ncosts of training staff and volunteers associated with such housing in basic pet care, including nutrition, behavioral training, and health maintenance.\n##### (c) Requirements\nInterim or permanent housing assisted with amounts from a grant under this Act shall comply with the following requirements:\n**(1) Services**\n**(A) Supportive services**\nAppropriate supportive services, including mental health, employment, substance use disorder, and wellness services, shall be made available to occupants of the housing.\n**(B) Veterinary services**\nBasic veterinary care and behavioral support for pets, including spay and neuter, basic wellness examinations, vaccinations, dental care, heartworm treatment and prevention, flea and tick treatment and prevention, and basic medical procedures, shall be made available for pets of occupants of the housing.\n**(C) Location**\nServices required under this paragraph shall be made available on-site in such housing, except that services that cannot be furnished on-site may be made available off-site, but only if direct linkage to transportation services is made available to occupants to access such services.\n**(2) Animal housing**\nThe housing shall provide accommodations for pets of occupants of the housing that are appropriate for the layout and type of the interim or permanent housing, which may include crates and kennels.\n**(3) Coordination**\nThe manager of the housing shall\u2014\n**(A)**\ncoordinate with public services and such agencies as the Secretary determines appropriate to provide services and safety for the housing, as the Secretary shall require;\n**(B)**\ncoordinate with local veterinary service and animal care providers to provide care for pets that accompany occupants of the housing; and\n**(C)**\nin making occupancy available in the housing, coordinate with the administrative entity for the Continuum of Care under subtitle C of title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11381 et seq. ) for the area in which the housing is located.\n##### (d) Applications; plan\n**(1) Application**\nThe Secretary shall provide for eligible entities to submit applications for grants under this section and shall require such applications to include a plan under paragraph (2).\n**(2) Plan**\nA plan under this paragraph shall\u2014\n**(A)**\nidentify existing housing, shelters, or unused structures or land within the area served by the eligible entity submitting the application that will be used for providing the housing to be assisted under subsection (b) with amounts from a grant under this section;\n**(B)**\nidentify the extent of need, in the area of such housing, shelters, structures, or land identified, for interim or permanent housing for homeless persons with pets;\n**(C)**\nidentify partnering veterinary service and animal care providers that will provide care for pets that accompany occupants of the housing and any partnering animal welfare organization;\n**(D)**\ninclude such assurances as the Secretary considers necessary to ensure that such housing will be provided using grant amounts, that such housing will accommodate homeless persons, and homeless families, who have pets, and that such housing will comply with the requirements under subsection (c); and\n**(E)**\nprovide for targeted outreach to individuals experiencing homelessness within the area served by the eligible entity receiving a grant under this section to inform such individuals regarding the availability of the housing assisted with grant amounts.\n**(3) Selection**\nThe Secretary shall select applications to be awarded such grants on a competitive basis, based on criteria that the Secretary shall establish.\n##### (e) Reports\nEach eligible entity that receives a grant under this section for a fiscal year shall submit a report to the Secretary, not later than 90 days after the end of the fiscal year for which the grant was made, that shall include the following information:\n**(1)**\nA description of the activities undertaken by the eligible entity using such grant amounts.\n**(2)**\nIdentification of the costs of each of the services provided in connection with the housing assisted with such grant amounts.\n**(3)**\nAn assessment of the effectiveness of the program grants under this section and any recommendations for improving the program.\n##### (f) Definitions\nFor purposes of this section, the following definitions shall apply:\n**(1) Eligible entity**\n**(A) In general**\nThe term eligible entity means\u2014\n**(i)**\na unit of general local government;\n**(ii)**\na nonprofit organization; and\n**(iii)**\nan entity providing housing or shelters for homeless persons.\n**(B) Limitation**\nSuch term does not include an animal wellness or welfare organization or an animal shelter, except that this subparagraph may not be construed to prevent any such organization or shelter from partnering with an eligible entity to provide interim or permanent housing assisted with amounts from a grant under this Act.\n**(2) Homeless**\nThe term homeless has the meaning given such term in section 103 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11302 ).\n**(3) Interim housing**\nThe term interim housing means any housing or shelter that does not provide permanent housing. Such term includes transitional housing (as such term is defined in such section 401) and emergency shelters (as such term is defined in section 321 of such Act ( 42 U.S.C. 13351 )).\n**(4) Permanent housing**\nThe term permanent housing has the meaning given such term in section 401 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 ).\n**(5) Pet**\nThe term pet means any domesticated animal that is normally maintained as a companion or pet animal near the owner or person who cares for the animal, such as a domestic dog (including a service dog), domestic cat, ferret, gerbil, mouse, rat, guinea pig, rabbit, hamster, or bird.\n**(6) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(7) Unit of general local government**\nThe term unit of general local government has the meaning given such term in the first sentence of paragraph (1) of section 102(a) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302(a)(1) ).\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $5,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-08-08",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-18T19:56:33Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4921ih.xml"
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
      "title": "PUPP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PUPP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for Unhoused People and Pets Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Agriculture to make grants to modify and upgrade structures to serve as interim and permanent housing to accommodate unhoused individuals with pets, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T04:18:44Z"
    }
  ]
}
```
