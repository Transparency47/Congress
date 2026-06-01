# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4012?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4012
- Title: National Airport Supersonic Readiness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4012
- Origin chamber: House
- Introduced date: 2025-06-13
- Update date: 2025-10-18T08:05:39Z
- Update date including text: 2025-10-18T08:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-13: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-14 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-06-13: Introduced in House

## Actions

- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-14 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-13",
    "latestAction": {
      "actionDate": "2025-06-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4012",
    "number": "4012",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "National Airport Supersonic Readiness Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-18T08:05:39Z",
    "updateDateIncludingText": "2025-10-18T08:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-14",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-13",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-13",
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
          "date": "2025-06-13T13:30:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-14T20:53:33Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NC"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4012ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4012\nIN THE HOUSE OF REPRESENTATIVES\nJune 13, 2025 Mr. Moore of North Carolina introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Aviation Administration to conduct a study on the readiness of certain airports to accommodate high-speed air travel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Airport Supersonic Readiness Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSupersonic and hypersonic commercial airliners have the potential to transform air travel by reducing long-haul flight times significantly.\n**(2)**\nExisting airport infrastructure may not be fully equipped to handle the unique requirements of such aircraft, including runway length, ground equipment, noise regulations, and fuel supply.\n**(3)**\nA comprehensive study is necessary to evaluate the ability of major United States airports to accommodate these aircraft safely and efficiently.\n#### 3. High-speed air travel readiness study\n##### (a) In general\nThe Administrator of the Federal Aviation Administration, in consultation with the Administrator of the National Aeronautics and Space Administration and any other relevant stakeholders the Administrator determines appropriate, including industry and academia, shall conduct a study to assess the capability of large hub airports, including the largest airports in the United States, to accommodate high-speed aircraft.\n##### (b) Considerations\nIn conducting the study required under subsection (a), the Administrator shall evaluate\u2014\n**(1)**\nrunway length and structural integrity;\n**(2)**\nground equipment compatibility, including fueling and maintenance facilities;\n**(3)**\nair traffic control systems and procedures;\n**(4)**\nenvironmental regulations that may prevent the use of high-speed aircraft at an airport described in subsection (a), including any such regulation relating to noise pollution or emissions; and\n**(5)**\npotential economic benefits and challenges relating to accommodating high-speed aircraft at any such airport.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the Administrator shall submit to the appropriate committees of Congress a report that includes\u2014\n**(1)**\nthe results of the study required under subsection (a);\n**(2)**\nrecommendations for policy changes and infrastructure improvements necessary to facilitate the use of high-speed aircraft at the airports described in subsection (a); and\n**(3)**\nestimated costs and a projected timeline for any such improvement.\n##### (d) Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means the Committee on Transportation and Infrastructure and the Committee on Science, Space, and Technology of the House of Representatives.\n**(2) High-speed aircraft**\nThe term high-speed aircraft means an aircraft operating at speeds in excess of Mach 1, including supersonic and hypersonic aircraft.\n**(3) Hypersonic**\nThe term hypersonic means flights operating at speeds that exceed Mach 5.\n**(4) Large hub airport**\nThe term large hub airport has the meaning given that term in section 40102 of title 49, United States Code.\n**(5) Supersonic**\nThe term supersonic means flights operating at speeds in excess of Mach 1 but less than Mach 5.",
      "versionDate": "2025-06-13",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-07T13:18:04Z"
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
      "date": "2025-06-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4012ih.xml"
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
      "title": "National Airport Supersonic Readiness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Airport Supersonic Readiness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Aviation Administration to conduct a study on the readiness of certain airports to accommodate high-speed air travel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T04:48:29Z"
    }
  ]
}
```
