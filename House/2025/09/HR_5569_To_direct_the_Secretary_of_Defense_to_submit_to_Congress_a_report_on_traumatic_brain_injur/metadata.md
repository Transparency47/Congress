# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5569?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5569
- Title: PILOT Act
- Congress: 119
- Bill type: HR
- Bill number: 5569
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-11-25T18:43:01Z
- Update date including text: 2025-11-25T18:43:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5569",
    "number": "5569",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "PILOT Act",
    "type": "HR",
    "updateDate": "2025-11-25T18:43:01Z",
    "updateDateIncludingText": "2025-11-25T18:43:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5569ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5569\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Crow (for himself and Mr. Luttrell ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to submit to Congress a report on traumatic brain injuries among certain pilots serving on active duty.\n#### 1. Short title\nThis Act may be cited as the Preventing and Identifying Lasting Operational TBI Act or the PILOT Act .\n#### 2. Report on traumatic brain injuries among certain pilots serving on active duty\n##### (a) Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall submit to the congressional defense committees a report that contains a study determining whether, and to what extent, members of the Armed Forces serving on active duty as pilots suffer from traumatic brain injury resulting from the cumulative effects of high-speed maneuvers, catapult launches, and other repetitive actions potentially harmful to brain health as a result of such service.\n##### (b) Matters included\nThe report under subsection (a) shall include the following:\n**(1)**\nThe results of the study under subsection (a).\n**(2)**\nA summary of existing policies and procedures of the Department of Defense, as of the date of the report, for identifying, documenting, and treating mild, moderate, and severe traumatic brain injury among pilots.\n**(3)**\nA strategy to better identify, document, and treat mild, moderate, and severe traumatic brain injury among pilots.\n**(4)**\nRecommendations of the Secretary with respect to potential regulatory and legislative actions to address challenges in identifying, documenting, and treating mild, moderate, and severe traumatic brain injury among pilots.",
      "versionDate": "2025-09-26",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-25T18:43:01Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5569ih.xml"
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
      "title": "PILOT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T07:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PILOT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T07:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing and Identifying Lasting Operational TBI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T07:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to submit to Congress a report on traumatic brain injuries among certain pilots serving on active duty.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T07:48:28Z"
    }
  ]
}
```
