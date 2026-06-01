# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4970?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4970
- Title: Orland Project Water Management Act
- Congress: 119
- Bill type: HR
- Bill number: 4970
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2025-09-29T13:56:29Z
- Update date including text: 2025-09-29T13:56:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-08-29 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-09-03 - Committee: Subcommittee Hearings Held
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-08-29 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-09-03 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4970",
    "number": "4970",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "L000578",
        "district": "1",
        "firstName": "Doug",
        "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
        "lastName": "LaMalfa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Orland Project Water Management Act",
    "type": "HR",
    "updateDate": "2025-09-29T13:56:29Z",
    "updateDateIncludingText": "2025-09-29T13:56:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
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
      "actionDate": "2025-08-29",
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
      "actionDate": "2025-08-15",
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
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:01:50Z",
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
                "date": "2025-09-03T13:20:38Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-08-29T20:24:16Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4970ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4970\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. LaMalfa introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Reclamation States Emergency Drought Relief Act of 1991 to facilitate the transfer of water from the Orland Project to the Central Valley Project.\n#### 1. Short title\nThis Act may be cited as the Orland Project Water Management Act .\n#### 2. Amendment to Reclamation States Emergency Drought Relief Act of 1991\nSection 104 of the Reclamation States Emergency Drought Relief Act of 1991 ( 43 U.S.C. 2214 ) is amended\u2014\n**(1)**\nby redesignating subsections (b) and (c) as subsections (c) and (d) respectively;\n**(2)**\nby inserting after subsection (a) the following:\n(b) Exception The Secretary may make available, upon the request of the Orland Unit Water Users Association and through the programs and authorities established under this title, water from the Orland Project to the Sacramento Canal Unit of the Central Valley Project at any time, without regard to water year type, if the Secretary determines that such action is consistent with the purposes of the Central Valley Project. ; and\n**(3)**\nby adding at the end the following:\n(e) Rules of construction Nothing in this section may be construed to\u2014 (1) be a new or supplemental benefit for the purposes of the Reclamation Reform Act of 1982 ( 43 U.S.C. 390aa et seq. ); (2) affect any valid or vested water right in existence as of the date of the enactment of this subsection; (3) affect any application for water rights pending before the date of the enactment of this subsection; or (4) result in any redirected impacts to the Orland Project from a temporary contract for the supply of water executed under this section. .",
      "versionDate": "2025-08-15",
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
            "name": "California",
            "updateDate": "2025-09-29T13:56:19Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2025-09-29T13:56:29Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-09-29T13:56:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-09-12T19:53:00Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4970ih.xml"
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
      "title": "Orland Project Water Management Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-19T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Orland Project Water Management Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Reclamation States Emergency Drought Relief Act of 1991 to facilitate the transfer of water from the Orland Project to the Central Valley Project.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-19T04:33:16Z"
    }
  ]
}
```
