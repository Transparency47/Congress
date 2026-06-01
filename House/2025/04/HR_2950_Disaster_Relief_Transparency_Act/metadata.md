# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2950?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2950
- Title: Disaster Relief Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 2950
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-12-19T09:08:09Z
- Update date including text: 2025-12-19T09:08:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2950",
    "number": "2950",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
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
    "title": "Disaster Relief Transparency Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:08:09Z",
    "updateDateIncludingText": "2025-12-19T09:08:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:34:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "LA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "TX"
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
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2950ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2950\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Moore of North Carolina (for himself and Mr. Fields ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of Housing and Urban Development to submit to the Congress a report that describes the methodology used to allocate amounts appropriated in covered provisions for the Community Development Block Grant Disaster Recovery Program and the Community Development Block Grant Mitigation Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Relief Transparency Act .\n#### 2. HUD Report\n##### (a) In general\nThe Secretary of Housing and Urban Development (in this section referred to as the Secretary ), after consultation with the Comptroller General of the United States, shall submit to the Financial Services, Oversight and Reform, and Transportation and Infrastructure Committees of the House of Representatives and Banking Committee of the Senate a report that\u2014\n**(1)**\ndescribes and explains the methodology used by the Department of Housing and Urban Development to allocate, to States, Tribes, Territories, and local governments, any amounts appropriated for the Community Development Block Grant Disaster Recovery Program and the Community Development Block Grant Mitigation Program;\n**(2)**\naddresses why such methodology may result in allocations to States, Tribes, Territories, and local governments differing between appropriations; and\n**(3)**\nprovides legislative and administrative recommendations for improving the consistency and timeliness of the allocation of amounts appropriated for the Community Development Block Grant Disaster Recovery Program and the Community Development Block Grant Mitigation Program.\n##### (b) First report\nThe Secretary shall\u2014\n**(1)**\nsubmit the first report described in subsection (a) not later than 90 days after the date of the enactment of this Act; and\n**(2)**\nexamine the amounts appropriated for fiscal years 2025 and 2024 in such report.\n##### (c) Subsequent reports\nAfter the submission of the first report described in subsection (b), the Secretary shall\u2014\n**(1)**\nbeginning in fiscal year 2026, submit the report described in subsection (a) not later than the final day of each fiscal year; and\n**(2)**\nexamine the amounts appropriated for the fiscal year.",
      "versionDate": "2025-04-17",
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
        "updateDate": "2025-05-20T14:01:16Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2950ih.xml"
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
      "title": "Disaster Relief Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:05Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disaster Relief Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Housing and Urban Development to submit to the Congress a report that describes the methodology used to allocate amounts appropriated in covered provisions for the Community Development Block Grant Disaster Recovery Program and the Community Development Block Grant Mitigation Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:37Z"
    }
  ]
}
```
