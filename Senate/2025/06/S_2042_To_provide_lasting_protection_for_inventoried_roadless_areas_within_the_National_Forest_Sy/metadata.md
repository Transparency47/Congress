# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2042?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2042
- Title: Roadless Area Conservation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2042
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2042",
    "number": "2042",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Roadless Area Conservation Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-11",
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
        "item": {
          "date": "2025-06-11T21:56:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:46Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "AZ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MN"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "OR"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "IL"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-11",
      "state": "VT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "WA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CO"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "MA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "VA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NY"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CO"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MD"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "NM"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "RI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "IL"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "AZ"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2042is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2042\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Ms. Cantwell (for herself, Mr. Gallego , Mr. Padilla , Mr. Booker , Ms. Smith , Mr. Wyden , Mr. Durbin , Mr. Sanders , Mr. Welch , Mr. Merkley , Mrs. Murray , Ms. Hirono , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo provide lasting protection for inventoried roadless areas within the National Forest System.\n#### 1. Short title\nThis Act may be cited as the Roadless Area Conservation Act of 2025 .\n#### 2. Findings and purpose\n##### (a) In general\nCongress finds that\u2014\n**(1)**\nthere is a compelling need to establish national protection for inventoried roadless areas of the National Forest System in order to protect the unique social and ecological values of those irreplaceable resources;\n**(2)**\nroadless areas protect healthy watersheds and the numerous benefits of healthy watersheds, which include\u2014\n**(A)**\nproviding the setting for many forms of outdoor recreation;\n**(B)**\nensuring a supply of clean water for domestic, agricultural, and industrial uses;\n**(C)**\nproviding drinking water to tens of millions of citizens of the United States; and\n**(D)**\nhelping maintain abundant and healthy fish and wildlife populations and habitats;\n**(3)**\nmaintaining roadless areas in a relatively undisturbed condition\u2014\n**(A)**\nsaves downstream communities millions of dollars in water filtration costs; and\n**(B)**\nis crucial to preserve the flow of affordable, clean water to a growing population;\n**(4)**\nthe protection of roadless areas can maintain biological strongholds and refuges for many imperiled species by halting the ongoing fragmentation of the landscape into smaller and smaller parcels of land divided by road corridors;\n**(5)**\nroadless areas conserve native biodiversity by serving as a bulwark against the spread of nonnative invasive species;\n**(6)**\nroadless areas provide important back\u00adcountry fish and game habitat, creating opportunities for hunting and commercial and sport fishing;\n**(7)**\nroadless areas provide unparalleled opportunities for outdoor recreation, including hiking, camping, picnicking, wildlife viewing, hunting, fishing, cross-country skiing, canoeing, mountain biking, and similar activities;\n**(8)**\nwhile roadless areas may have many wilderness-like attributes, unlike wilderness areas, the use of mechanized means of travel is allowed in many roadless areas;\n**(9)**\nroadless areas contain many sites sacred to Native Americans, Alaska Natives, and other groups that use roadless areas for spiritual and religious practices and access, including customary and traditional uses and activities;\n**(10)**\nfrom the inception of Federal land management, the mission of the Forest Service has been to manage the National Forest System for multiple uses, including resource utilization, conservation, and other uses;\n**(11)**\nconsistent with the multiple-use mission described in paragraph (10), this Act\u2014\n**(A)**\nensures the continued protection of social and ecological values, while allowing for many multiple uses of inventoried roadless areas; and\n**(B)**\ndoes not impose any new limitations on\u2014\n**(i)**\ninventoried roadless areas; or\n**(ii)**\nthe use of, or access to, National Forest System, State, or private land outside inventoried roadless areas;\n**(12)**\nenacting a law for the protection of inventoried roadless areas\u2014\n**(A)**\nprovides additional reliability to areas with recreation-based economies that depend on public land without roads for jobs, revenue, and consumer spending; and\n**(B)**\nencourages forest managers to continue giving priority to conducting fuel reduction treatments in the areas in which the treatments will have the most impact;\n**(13)**\nwildfires are almost twice as likely to occur in roaded areas as in roadless areas, because road\u00adless areas are generally located further away from communities and are harder to access;\n**(14)**\nthe Forest Service has an enormous backlog of maintenance needs for the existing 368,102-mile road system of the Forest Service that will cost $5,980,000,000 to eliminate; and\n**(15)**\ncontinued protection of roadless areas will continue to allow for the development of hydropower projects.\n##### (b) Purpose\nThe purpose of this Act is to provide, within the context of multiple-use management, lasting protection for inventoried roadless areas within the National Forest System.\n#### 3. Definitions\nIn this Act:\n**(1) Inventoried roadless area**\nThe term inventoried roadless area means any area in which road construction, road reconstruction, or logging is subject to regulation under the Roadless Rule.\n**(2) Roadless Rule**\nThe term Roadless Rule means part 294 of title 36, Code of Federal Regulations, as adopted on January 12, 2001, and modified for Idaho on October 16, 2008, and for Colorado on July 3, 2012, and December 19, 2016.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n#### 4. Protection of inventoried roadless areas\nThe Secretary shall not allow road construction, road reconstruction, or logging in an inventoried roadless area where those activities are prohibited by the Roadless Rule.",
      "versionDate": "2025-06-11",
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
        "actionDate": "2025-06-11",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3930",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Roadless Area Conservation Act of 2025",
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
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-15T15:31:05Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-12-15T15:31:05Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2025-12-15T15:31:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-14T17:45:23Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2042is.xml"
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
      "title": "Roadless Area Conservation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Roadless Area Conservation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide lasting protection for inventoried roadless areas within the National Forest System.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:19Z"
    }
  ]
}
```
