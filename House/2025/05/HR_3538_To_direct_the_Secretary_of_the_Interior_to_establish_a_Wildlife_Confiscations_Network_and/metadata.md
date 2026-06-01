# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3538?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3538
- Title: Wildlife Confiscations Network Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3538
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-05-21T08:07:47Z
- Update date including text: 2026-05-21T08:07:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-06-23 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-06-24 - Committee: Subcommittee Hearings Held
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-06-23 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-06-24 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3538",
    "number": "3538",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Wildlife Confiscations Network Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:47Z",
    "updateDateIncludingText": "2026-05-21T08:07:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-24T17:39:10Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-23T16:44:50Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "IL"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "IL"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MD"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "WA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "GA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3538ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3538\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Garbarino (for himself and Mr. Quigley ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to establish a Wildlife Confiscations Network, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildlife Confiscations Network Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nWildlife trafficking is a continued and growing threat to our national security, hinders sustainable economic development, and undermines our laws.\n**(2)**\nThe connections between trafficking in illegal wildlife and natural resources with the financing of groups involved in transnational organized crime pose additional threats to the United States.\n**(3)**\nPresident Donald J. Trump\u2019s Executive Order No. 13773 demonstrated continued support for Enforcing Federal Law with Respect to Transnational Criminal Organizations and Preventing International Trafficking.\n**(4)**\nThe Lacey Act Amendments of 1981 ( 16 U.S.C. 3371 et seq. ) prohibits the importation, exportation, transportation, sale, receipt, acquisition, or purchase of any fish or wildlife or plant taken, possessed, transported, or sold in violation of any law, treaty, or regulation of the United States or any Indian tribal law, or foreign law.\n**(5)**\nCongress remains strongly committed to combating wildlife trafficking and transnational organized crime.\n**(6)**\nThe United States border is secured by Federal agents and inspectors responsible for identification, seizure, confiscation and holding of illegal imports, including a diverse array of live wild animals, notably at U.S. ports of entry or exit with an increased burden seen in Los Angeles, Miami, and across the Southern border.\n**(7)**\nCustoms and wildlife enforcement officers at ports of entry have limited holding capacity, care experience, and transportation options for interdicted live wildlife.\n**(8)**\nNumerous species of wildlife require extensive quarantine protocols to protect domestic livestock and wildlife, beyond the capacity of our ports and borders, that can be administered by facilities within the Wildlife Confiscations Network.\n**(9)**\nWhen illegally imported live wild animals and plants are seized at U.S. ports of entry, it is critical for law enforcement to obtain forensic documentation, maintain evidentiary integrity, and ensure the health, wellbeing, and proper care of all seized wildlife and plants in government custody.\n**(10)**\nFrom 2015 to 2019, the U.S. Fish and Wildlife Service had 834 cases involving live wildlife interdiction, which included 48,793 individual live animals, an average of nearly 30 per day, requiring placement and care.\n**(11)**\nIn 2023, the U.S. Fish and Wildlife Service and Association of Zoos and Aquariums formed a cooperative agreement to implement a pilot network in southern California to lessen the logistical burden by serving as a point of contact to coordinate placement and care of seized live animals while maintaining legal chain of custody.\n**(12)**\nThe Wildlife Confiscations Network provides a cooperative and coordinated response for the care and wellbeing of wildlife confiscated from illegal trade at United States border crossings and points of entry in Southern California from the point of seizure to placement or repatriation and, in just 2 years, has successfully placed over 4,100 individual animals into care.\n**(13)**\nConfiscation of trafficked plants and animals is critical to preventing their re-entry into illegal trade, empowering law enforcement to document and maintain evidence of and effectively combat illegal wildlife trafficking.\n**(14)**\nThe Wildlife Confiscations Network clearly aligns with OMB Circular A\u201376 by supporting wildlife law enforcement, an inherently governmental function, and removing the placement and care of confiscated live wildlife from government responsibility. It must be extended and expanded nationwide to allow law enforcement officers across the country to focus on their mission and mandate in combating wildlife crime.\n#### 3. Definitions\nIn this Act:\n**(1) CITES species**\nThe term CITES species means an animal species that is listed in one of the Appendices of the Convention on International Trade in Endangered Species of Wild Fauna and Flora.\n**(2) Committee**\nThe term Committee means the committee established under section 4(b)(3).\n**(3) Confiscated animal**\nThe term confiscated animal means an individual of a CITES species or a threatened or endangered species that is\u2014\n**(A)**\nseized at or en route to or from a port or border of the United States; and\n**(B)**\nplaced at a qualified animal care facility for provision of general care and welfare to such individual.\n**(4) Network**\nThe term Network means the Wildlife Confiscations Network established under section 4(a).\n**(5) Qualified animal care facility**\nThe term qualified animal care facility means a zoological facility, aquarium facility, wildlife sanctuary, animal rescue organization, animal rehabilitation organization, nongovernmental organization, university that has been reviewed by the Committee and\u2014\n**(A)**\nthat, as of the date of the enactment of this Act, provides care to an individual of a CITES species or a threatened or endangered species; or\n**(B)**\nhas expertise in the care of wildlife and has received and provided care for a confiscated animal within the 5 years preceding the date of the enactment of this Act.\n**(6) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service.\n**(7) Threatened or endangered species**\nThe term threatened or endangered species means an animal species that is listed under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. )\u2014\n**(A)**\nas a threatened species; or\n**(B)**\nas an endangered species.\n#### 4. Wildlife confiscations network\n##### (a) In general\nThe Secretary shall establish a voluntary, cooperative program, in partnership with a professional accrediting zoological association with existing capacity and expertise in wildlife confiscations, to assist Federal wildlife law enforcement agencies with the placement and care of confiscated animals, to be known as the Wildlife Confiscations Network .\n##### (b) Functions\nThe Network shall\u2014\n**(1)**\nestablish a cooperative and coordinated response protocol for the care and welfare of confiscated animals;\n**(2)**\ncreate and maintain a database of qualified animal care facilities to provide immediate triage needs and long-term housing and care for confiscated animals;\n**(3)**\nestablish a committee within the Network to review and approve or reject applications for inclusion in the Network submitted under subsection (c) by entities listed in paragraph (1) of that subsection; and\n**(4)**\nact as the single point of contact for Federal wildlife law enforcement agencies to assist in the placement and care of confiscated animals in qualified zoological facilities.\n##### (c) Membership\n**(1) In general**\nEach of the following entities may submit to the Committee an application to join the Network:\n**(A)**\nWildlife sanctuaries.\n**(B)**\nAquarium facilities.\n**(C)**\nZoological facilities.\n**(D)**\nAnimal rescue organizations.\n**(E)**\nAnimal rehabilitation organizations.\n**(F)**\nUniversities.\n**(G)**\nNongovernmental organizations.\n**(2) Contents of application**\nAn application submitted under paragraph (1) by an entity listed in that paragraph shall contain information sufficient for the Committee to determine whether such entity\u2014\n**(A)**\nhas, as determined by the Committee, the necessary credentials, including all necessary local, State, and Federal permits and licenses; and\n**(B)**\nis an effective, responsible, and appropriate entity capable of assisting Federal wildlife law enforcement agencies in the placement and care of confiscated animals.\n**(3) Determination**\nThe Committee shall review each application submitted under paragraph (1) and approve or reject each such application.\n##### (d) Committee\n**(1) Membership**\nThe Committee shall include representatives from each of the following entities, provided they are members of the Network:\n**(A)**\nThe United States Fish and Wildlife Service.\n**(B)**\nThe professional accrediting zoological association partner administering the Network as established under section 4(a).\n**(C)**\nZoological facility.\n**(D)**\nAquarium facility.\n**(E)**\nWildlife sanctuary.\n**(F)**\nNongovernmental organization.\n**(G)**\nWildlife rehabilitation facility, wildlife rescue organization, or other animal holding facility.\n**(2) Initial members**\nThe Secretary, in consultation with community stakeholders, including public and private entities that are actively involved in the care, rescue, and rehabilitation of any threatened or endangered species, and with advisement from the partnered professional accrediting zoological association, shall appoint each initial member to the Committee in accordance with paragraph (1).\n**(3) Subsequent members**\nExcept for the appointment of the initial members of the Committee under paragraph (2), each member of the Committee shall be elected by a majority vote of the members of the Committee through a call for service and application process implemented by the Committee.\n**(4) Term of membership**\n**(A) Initial members**\nOf the initial members appointed to the Committee by the Secretary\u2014\n**(i)**\n2 members shall be appointed for a term of 1 year;\n**(ii)**\n2 members shall be appointed for a term of 2 years; and\n**(iii)**\n3 members shall be appointed for a term of 3 years.\n**(B) Subsequent members**\nEach member of the Committee elected under paragraph (3) shall serve on the Committee for a term of 3 years.\n#### 5. Authorization of appropriations\nTo carry out this section, $5,000,000 is authorized to be appropriated to the Secretary for each of the fiscal years 2026 through 2030.",
      "versionDate": "2025-05-21",
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
            "name": "Advisory bodies",
            "updateDate": "2025-07-11T18:31:11Z"
          },
          {
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-07-11T18:31:00Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-07-11T18:31:05Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-07-11T18:30:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-18T15:40:07Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3538ih.xml"
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
      "title": "Wildlife Confiscations Network Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:01Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildlife Confiscations Network Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to establish a Wildlife Confiscations Network, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T06:48:33Z"
    }
  ]
}
```
