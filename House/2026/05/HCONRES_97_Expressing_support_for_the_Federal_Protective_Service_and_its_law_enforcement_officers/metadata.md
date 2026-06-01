# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/97?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/97
- Title: Expressing support for the Federal Protective Service and its law enforcement officers.
- Congress: 119
- Bill type: HCONRES
- Bill number: 97
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-21T20:31:56Z
- Update date including text: 2026-05-21T20:31:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-05-12 - IntroReferral: Submitted in House
- Latest action: 2026-05-12: Submitted in House

## Actions

- 2026-05-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-05-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/97",
    "number": "97",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B000825",
        "district": "4",
        "firstName": "Lauren",
        "fullName": "Rep. Boebert, Lauren [R-CO-4]",
        "lastName": "Boebert",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Expressing support for the Federal Protective Service and its law enforcement officers.",
    "type": "HCONRES",
    "updateDate": "2026-05-21T20:31:56Z",
    "updateDateIncludingText": "2026-05-21T20:31:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "actionCode": "1025",
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
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
          "date": "2026-05-12T16:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "TX"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres97ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 97\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Ms. Boebert (for herself, Mr. Nehls , and Mr. Van Drew ) submitted the following concurrent resolution; which was referred to the Committee on Transportation and Infrastructure\nCONCURRENT RESOLUTION\nExpressing support for the Federal Protective Service and its law enforcement officers.\nThat Congress\u2014\n**(1)**\nrecognizes and appreciates the dedication and devotion demonstrated by the men and women of the Federal Protective Service (hereinafter referred to as FPS ) who protect Federal facilities and the United States;\n**(2)**\nextends its gratitude to all FPS law enforcement officers and their families for their sacrifice and service;\n**(3)**\nhonors the memory of FPS law enforcement officers who have fallen in the line of duty; and\n**(4)**\nencourages continued collaboration between the Federal Protective Service and the communities it serves to strengthen public safety, awareness, and trust.",
      "versionDate": "2026-05-12",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-21T20:31:56Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres97ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the Federal Protective Service and its law enforcement officers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T02:48:31Z"
    },
    {
      "title": "Expressing support for the Federal Protective Service and its law enforcement officers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T08:06:37Z"
    }
  ]
}
```
