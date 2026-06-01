# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/950?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/950
- Title: Commemorating the 25th anniversary of the Comprehensive Everglades Restoration Plan.
- Congress: 119
- Bill type: HRES
- Bill number: 950
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-02-03T09:05:39Z
- Update date including text: 2026-02-03T09:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-12 - IntroReferral: Submitted in House
- 2025-12-12 - IntroReferral: Submitted in House
- 2025-12-12 - IntroReferral: Submitted in House
- 2025-12-12 - IntroReferral: Submitted in House
- 2026-02-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-12-12: Submitted in House

## Actions

- 2025-12-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-12 - IntroReferral: Submitted in House
- 2025-12-12 - IntroReferral: Submitted in House
- 2025-12-12 - IntroReferral: Submitted in House
- 2025-12-12 - IntroReferral: Submitted in House
- 2026-02-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/950",
    "number": "950",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000808",
        "district": "24",
        "firstName": "Frederica",
        "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
        "lastName": "Wilson",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Commemorating the 25th anniversary of the Comprehensive Everglades Restoration Plan.",
    "type": "HRES",
    "updateDate": "2026-02-03T09:05:39Z",
    "updateDateIncludingText": "2026-02-03T09:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-12-12T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:40:00Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres950ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 950\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Ms. Wilson of Florida (for herself, Mr. Soto , and Mr. Frost ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nCommemorating the 25th anniversary of the Comprehensive Everglades Restoration Plan.\nThat the House of Representatives\u2014\n**(1)**\ncommemorates the 25th anniversary of the Comprehensive Everglades Restoration Plan;\n**(2)**\nrecognizes that the Water Resources Development Act of 2000 established the modern framework for CERP and that subsequent water resources development actions remain essential to authorizing and advancing individual restoration projects;\n**(3)**\nhonors the enduring bipartisan leadership that has sustained momentum for Everglades restoration across the administrations of Presidents Bill Clinton, George W. Bush, Barack Obama, Donald Trump, and Joe Biden and the Administrations of Governors Jeb Bush, Charlie Crist, Rick Scott, and Ron DeSantis; and\n**(4)**\nreaffirms the importance of continued bipartisan commitment to completing authorized CERP projects that improve water quality, strengthen ecosystem resilience, and protect the health, safety, and economic vitality of communities across Florida.",
      "versionDate": "2025-12-12",
      "versionType": "IH"
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-22T16:08:34Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres950ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Commemorating the 25th anniversary of the Comprehensive Everglades Restoration Plan.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T09:05:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commemorating the 25th anniversary of the Comprehensive Everglades Restoration Plan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T09:05:45Z"
    }
  ]
}
```
