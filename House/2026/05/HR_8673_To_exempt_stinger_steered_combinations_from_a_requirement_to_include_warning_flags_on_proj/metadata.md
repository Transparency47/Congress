# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8673?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8673
- Title: To exempt stinger-steered combinations from a requirement to include warning flags on projecting loads.
- Congress: 119
- Bill type: HR
- Bill number: 8673
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-21T19:49:28Z
- Update date including text: 2026-05-21T19:49:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8673",
    "number": "8673",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "To exempt stinger-steered combinations from a requirement to include warning flags on projecting loads.",
    "type": "HR",
    "updateDate": "2026-05-21T19:49:28Z",
    "updateDateIncludingText": "2026-05-21T19:49:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:05:30Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8673ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8673\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Barrett introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo exempt stinger-steered combinations from a requirement to include warning flags on projecting loads.\n#### 1. Exemption of certain automobile transporters from requirement to include warning flags on projecting loads\n##### (a) In general\nBeginning on the date of enactment of this Act, section 393.87 of title 49, Code of Federal Regulations (or a successor regulation), shall not apply to a stinger-steered combination (as defined in section 658.5 of title 23, Code of Federal Regulations (or a successor regulation)), that is transporting assembled highway vehicles.\n##### (b) Revision\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary of Transportation shall revise section 393.87 of title 49, Code of Federal Regulations, to exempt from the requirements of that regulation stinger-steered combinations (as defined in section 658.5 of title 23, Code of Federal Regulations (or a successor regulation)), that are transporting assembled highway vehicles.\n**(2) Exemption**\nNotwithstanding any other provision of law, the Secretary of Transportation shall carry out paragraph (1) without engaging in notice and comment or any other formal rulemaking process.",
      "versionDate": "2026-05-07",
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
        "updateDate": "2026-05-21T19:49:27Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8673ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To exempt stinger-steered combinations from a requirement to include warning flags on projecting loads.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T05:18:29Z"
    },
    {
      "title": "To exempt stinger-steered combinations from a requirement to include warning flags on projecting loads.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:06:04Z"
    }
  ]
}
```
