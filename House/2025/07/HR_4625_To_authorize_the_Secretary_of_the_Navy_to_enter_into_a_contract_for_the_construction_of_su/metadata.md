# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4625?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4625
- Title: NEPTUNE Act
- Congress: 119
- Bill type: HR
- Bill number: 4625
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-11-21T12:04:07Z
- Update date including text: 2025-11-21T12:04:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4625",
    "number": "4625",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001222",
        "district": "7",
        "firstName": "Max",
        "fullName": "Rep. Miller, Max L. [R-OH-7]",
        "lastName": "Miller",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "NEPTUNE Act",
    "type": "HR",
    "updateDate": "2025-11-21T12:04:07Z",
    "updateDateIncludingText": "2025-11-21T12:04:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:14:15Z",
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
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "OH"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4625ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4625\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Miller of Ohio introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo authorize the Secretary of the Navy to enter into a contract for the construction of submarine cable laying and repair ships, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Naval Enhancement for Protection of Telecommunications Undersea Network Equipment Act or the NEPTUNE Act .\n#### 2. Procurement authority for submarine cable laying and repair ships\n##### (a) Contract authority\nThe Secretary of the Navy may enter into a contract for the construction of up to two submarine cable laying and repair ships and associated material.\n##### (b) Liability\nAny contract entered into under subsection (a) shall provide that\u2014\n**(1)**\nany obligation of the United States to make a payment under the contract is subject to the availability of appropriations for that purpose; and\n**(2)**\nthe total liability of the Federal Government for termination of the contract shall be limited to the total amount of funding obligated to the contract at the time of termination.\n#### 3. Limitation on retirement of submarine cable laying and repair ship\n##### (a) In general\nThe Secretary of the Navy may not retire, prepare to retire, or place in storage the USNS Zeus until the date on which a replacement ship with capabilities equal to or exceeding those of the USNS Zeus has achieved full operational capability.\n##### (b) Replacement ship defined\nIn this section, the term replacement ship \u2014\n**(1)**\nmeans a submarine cable laying and repair ship designated USNS and maintained in the inventory of the Navy; and\n**(2)**\ndoes not include a commercial vessel leased or chartered by the Navy.",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-09-19T17:31:48Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4625ih.xml"
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
      "title": "NEPTUNE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T09:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NEPTUNE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T09:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Naval Enhancement for Protection of Telecommunications Undersea Network Equipment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T09:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of the Navy to enter into a contract for the construction of submarine cable laying and repair ships, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T09:33:18Z"
    }
  ]
}
```
