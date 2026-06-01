# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/902?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/902
- Title: Wildfire Response and Preparedness Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 902
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-05-20T11:03:28Z
- Update date including text: 2026-05-20T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/902",
    "number": "902",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Wildfire Response and Preparedness Act of 2025",
    "type": "S",
    "updateDate": "2026-05-20T11:03:28Z",
    "updateDateIncludingText": "2026-05-20T11:03:28Z"
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
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T20:38:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-02T20:00:14Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-12-02T20:00:14Z",
                "name": "Hearings By (subcommittee)"
              }
            ]
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NJ"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s902is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 902\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Sheehy (for himself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of Agriculture and the Secretary of the Interior to establish a standard for the response time to wildfire incidents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire Response and Preparedness Act of 2025 .\n#### 2. Standards for response time to wildfire incidents\n##### (a) Definitions\nIn this section:\n**(1) Relevant congressional committees**\nThe term relevant congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate;\n**(B)**\nthe Committee on Agriculture, Nutrition, and Forestry of the Senate;\n**(C)**\nthe Committee on Natural Resources of the House of Representatives; and\n**(D)**\nthe Committee on Agriculture of the House of Representatives.\n**(2) Response time**\nThe term response time , with respect to a wildland fire incident, means the period of time between ignition of the wildland fire and evaluation for purposes of suppression of that wildland fire, on the ground or in an aircraft, by\u2014\n**(A)**\na Federal, State, or local public safety officer; or\n**(B)**\na public safety volunteer.\n**(3) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Agriculture, with respect to Federal land administered by the Forest Service;\n**(B)**\nthe Secretary of the Interior, with respect to Federal land administered by the Bureau of Land Management, the Bureau of Indian Affairs, the National Park Service, or the United States Fish and Wildlife Service; and\n**(C)**\nthe Administrator of the Federal Emergency Management Agency, with respect to consultation with the United States Fire Administration relating to wildland fires in the wildland-urban interface.\n##### (b) Standards\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Secretary concerned shall establish a standard for the response time to any wildland fire incident occurring on Federal land administered by the Secretary concerned.\n**(2) Goal**\nTo the extent practicable, the response time established by the Secretary concerned for a wildland fire incident under paragraph (1) shall\u2014\n**(A)**\nbe not more than 30 minutes; and\n**(B)**\ninclude the deployment of fire suppression assets in a response time of not more than 3 hours.\n##### (c) Report to Congress\nNot later than 1 year after the date of enactment of this Act, the Secretaries concerned shall jointly submit to the relevant congressional committees a report that includes\u2014\n**(1)**\nidentification of a single point of contact for Federal wildland fire response at the Department of the Interior;\n**(2)**\na unified budget request that covers all wildland fire activities of the Secretaries concerned;\n**(3)**\na description of key performance indicators for wildland fire response for each of\u2014\n**(A)**\nthe Forest Service;\n**(B)**\nthe Bureau of Land Management;\n**(C)**\nthe Bureau of Indian Affairs;\n**(D)**\nthe National Park Service; and\n**(E)**\nthe United States Fish and Wildlife Service;\n**(4)**\n**(A)**\na description of the composition of the aviation and ground wildland firefighting fleet as of the date on which the report is submitted; and\n**(B)**\nan estimation of the size of that fleet required to provide a response time of not more than 30 minutes for wildland fires occurring in the United States, including the deployment of fire suppression assets in a response time of not more than 3 hours;\n**(5)**\na description of necessary changes to the Federal ordering and dispatch system to enable Federal wildland firefighting assets to be dispatched faster;\n**(6)**\na description of Federal contracting mechanisms relating to wildland firefighting assets that may be streamlined to ensure that contract activation and awards may be provided within a 1-year period; and\n**(7)**\na description of all resources and authorities needed to ensure that wildland firefighting assets under Federal contracts are available year-round and nationwide.",
      "versionDate": "2025-03-06",
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
        "actionDate": "2026-01-14",
        "text": "Subcommittee Hearings Held"
      },
      "number": "4038",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Wildfire Response and Preparedness Act of 2025",
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
            "name": "Congressional oversight",
            "updateDate": "2025-12-15T21:02:41Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-12-15T21:02:46Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-12-15T21:02:23Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-12-15T21:02:35Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-15T21:02:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T18:26:49Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s902is.xml"
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
      "title": "Wildfire Response and Preparedness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture and the Secretary of the Interior to establish a standard for the response time to wildfire incidents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:33:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wildfire Response and Preparedness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:23:20Z"
    }
  ]
}
```
