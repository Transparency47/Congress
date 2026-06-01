# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8195?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8195
- Title: Responsible Cormorant Management and Control Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8195
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-05-13T08:06:31Z
- Update date including text: 2026-05-13T08:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-09 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-16 - Committee: Subcommittee Hearings Held
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-09 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-16 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8195",
    "number": "8195",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Responsible Cormorant Management and Control Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:31Z",
    "updateDateIncludingText": "2026-05-13T08:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-09",
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
      "actionDate": "2026-04-02",
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
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
          "date": "2026-04-02T12:31:20Z",
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
                "date": "2026-04-16T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-04-09T14:34:35Z",
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "MS"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8195ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8195\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Mr. Walberg introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of the Interior to develop regional management frameworks for the take of double-crested cormorants.\n#### 1. Short title\nThis Act may be cited as the Responsible Cormorant Management and Control Act of 2026 .\n#### 2. Regional management frameworks for take of double-crested cormorants\n##### (a) In general\nNot later than 180 days after the date of the enactment of this section, the Secretary, in coordination with the applicable Regional Flyway Council, shall develop a regional management framework for the take of double-crested cormorants for each region covered by a Regional Flyway Council based on existing information.\n##### (b) Requirements\nEach regional management framework developed under subsection (a) shall\u2014\n**(1)**\nensure the breeding population of double-crested cormorants is maintained at a sustainable level\u2014\n**(A)**\nin accordance with the Migratory Bird Treaty Act ( 16 U.S.C. 703 et seq. ); and\n**(B)**\nbeginning with the first update required by subsection (e), as informed by the most recent survey carried out under subsection (d);\n**(2)**\ninclude, with respect to double-crested cormorants\u2014\n**(A)**\nallowed methods of take; and\n**(B)**\nallowed time periods of take;\n**(3)**\nidentify entities that may take double-crested cormorants, which shall include\u2014\n**(A)**\nState and Tribal agencies; and\n**(B)**\nentities licensed or otherwise authorized in a manner the Secretary determines appropriate, which shall include\u2014\n**(i)**\nState licensed or otherwise authorized hunters;\n**(ii)**\nlake managers; and\n**(iii)**\npond managers;\n**(4)**\nprovide for\u2014\n**(A)**\nStates and Indian Tribes to take specific management actions with respect to double-crested cormorants in accordance with the regional management framework; and\n**(B)**\nthe implementation of management actions identified under subsection (c); and\n**(5)**\naccount for the effects of an overabundant population of double-crested cormorants on\u2014\n**(A)**\nfisheries;\n**(B)**\nsensitive vegetation;\n**(C)**\npopulations of other migratory birds;\n**(D)**\nhuman health and safety;\n**(E)**\nwater quality; and\n**(F)**\nspecies listed as threatened species or endangered species under section 4 of the Endangered Species Act of 1973 ( 16 U.S.C. 1533 ).\n##### (c) Incorporation of National Wildlife Refuge System\nIn developing each regional management framework under subsection (a), the Secretary, in cooperation with the heads of State and Tribal game and fish agencies and the applicable Regional Flyway Council, shall identify appropriate management actions that can be taken within units of the National Wildlife Refuge System to meet management objectives of States, Indian Tribes, the Regional Flyway Councils, and such units with respect to double-crested cormorants while fulfilling the primary purposes of such units.\n##### (d) Population surveys\nNot later than 5 years after the date of the enactment of this section and every 5 years thereafter, the Secretary, in coordination with the Regional Flyway Councils, shall carry out a survey of the population of double-crested cormorants.\n##### (e) Updates\n**(1) In general**\nNot later than 5 years after the date of the enactment of this section and every 5 years thereafter, the Secretary, in coordination with the applicable Regional Flyway Council, shall review and update each regional management framework developed under subsection (a).\n**(2) Incorporation of population surveys**\nIn reviewing and updating a regional management framework under paragraph (1), the Secretary shall incorporate the results of the most recent survey carried out under subsection (d).\n##### (f) Definitions\nIn this section:\n**(1) Double-crested cormorant**\nThe term double-crested cormorant means the species Nannopterum auritum.\n**(2) Regional Flyway Council**\nThe term Regional Flyway Council means\u2014\n**(A)**\nthe Atlantic Flyway Council;\n**(B)**\nthe Central Flyway Council;\n**(C)**\nthe Mississippi Flyway Council; and\n**(D)**\nthe Pacific Flyway Council.\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Lake manager**\nThe term lake manager means a person that is licensed or otherwise authorized by a State regulatory agency to manage a private lake.\n**(5) Migratory bird**\nThe term migratory bird has the meaning given the term migratory birds in section 11 of the Migratory Bird Conservation Act ( 16 U.S.C. 715j ).\n**(6) Pond manager**\nThe term pond manager means a person that is licensed or otherwise authorized by a State regulatory agency to manage a private pond.\n**(7) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service.\n**(8) Take**\nThe term take has the meaning given the term in section 10.12 of title 50, Code of Federal Regulations (as in effect on the date of the enactment of this section).",
      "versionDate": "2026-04-02",
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
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2026-04-27T14:29:38Z"
          },
          {
            "name": "Birds",
            "updateDate": "2026-04-27T14:29:28Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-04-27T14:29:53Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-04-27T14:30:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2026-04-14T15:51:54Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8195ih.xml"
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
      "title": "Responsible Cormorant Management and Control Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Responsible Cormorant Management and Control Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Interior to develop regional management frameworks for the take of double-crested cormorants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T05:18:30Z"
    }
  ]
}
```
