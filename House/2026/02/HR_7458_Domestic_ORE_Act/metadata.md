# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7458
- Title: Domestic ORE Act
- Congress: 119
- Bill type: HR
- Bill number: 7458
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-04-14T15:23:05Z
- Update date including text: 2026-04-14T15:23:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-17 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-02-24 - Committee: Subcommittee Hearings Held
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-17 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-02-24 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7458",
    "number": "7458",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Domestic ORE Act",
    "type": "HR",
    "updateDate": "2026-04-14T15:23:05Z",
    "updateDateIncludingText": "2026-04-14T15:23:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
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
      "actionDate": "2026-02-17",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:01:00Z",
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
                "date": "2026-02-24T15:30:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-02-17T16:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-10T15:01:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7458ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7458\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo codify notice requirements for mineral exploration activities on certain public lands, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Domestic Opportunities for Resource Exploration Act or the Domestic ORE Act .\n#### 2. Notice for mineral exploration activities with limited surface disturbance\n##### (a) In general\nNot later than 15 days before commencing an exploration activity with a surface disturbance of not more than 25 acres of public lands, the operator of such exploration activity shall submit to the Secretary concerned a notice of such exploration activity.\n##### (b) Inclusions\nA notice submitted under subsection (a) shall include such information the Secretary concerned may require, which may include information described in section 3809.301 of title 43, Code of Federal Regulations (or any successor regulation).\n##### (c) Review\nNot later than 15 days after the Secretary concerned receives a notice of an exploration activity submitted under subsection (a), the Secretary concerned shall\u2014\n**(1)**\nallow the exploration activity to proceed if\u2014\n**(A)**\nthe surface disturbance of such exploration activity will not be more than 25 acres of public lands;\n**(B)**\nthe Secretary concerned determines that the notice includes the information required under subsection (b); and\n**(C)**\nthe operator provides financial assurance that the Secretary concerned determines is adequate; or\n**(2)**\nnotify the operator that information is missing from the notice and specify any information that is required to be included in the notice under subsection (b).\n##### (d) Definitions\nIn this section:\n**(1) Casual use**\nThe term casual use has the meaning given such term in section 3809.5 of title 43, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(2) Exploration activity**\nThe term exploration activity \u2014\n**(A)**\nmeans creating a surface disturbance greater than casual use that includes sampling, drilling, or developing surface or underground workings to evaluate the type, extent, quantity, or quality of minerals present;\n**(B)**\nincludes constructing drill roads and drill pads, drilling, trenching, excavating test pits, and conducting geotechnical tests and geophysical surveys; and\n**(C)**\ndoes not include an activity in which material is extracted for commercial use or sale.\n**(3) Mineral**\nThe term mineral means any mineral of a kind that is locatable under the Act of May 10, 1872 (Chapter 152; 17 Stat. 91).\n**(4) Operator**\nThe term operator has the meaning given such term in section 3809.5 of title 43, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(5) Public land**\nThe term public land means land owned by the United States that is open to location under the Act of May 10, 1872 (Chapter 152; 17 Stat. 91).\n**(6) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nwith respect to land administered by the Secretary of the Interior, the Secretary of the Interior; and\n**(B)**\nwith respect to National Forest System land, the Secretary of Agriculture.",
      "versionDate": "2026-02-10",
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
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-03-06T20:51:19Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-03-06T20:51:25Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-03-06T20:51:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-04-14T15:23:05Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7458ih.xml"
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
      "title": "Domestic ORE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T06:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Domestic ORE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Domestic Opportunities for Resource Exploration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To codify notice requirements for mineral exploration activities on certain public lands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T06:48:24Z"
    }
  ]
}
```
