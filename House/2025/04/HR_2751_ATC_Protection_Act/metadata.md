# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2751?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2751
- Title: ATC Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 2751
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-06-12T08:06:44Z
- Update date including text: 2025-06-12T08:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-08 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-08 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2751",
    "number": "2751",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "ATC Protection Act",
    "type": "HR",
    "updateDate": "2025-06-12T08:06:44Z",
    "updateDateIncludingText": "2025-06-12T08:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-08T20:49:08Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2751ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2751\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mrs. Torres of California introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require approval from Congress for a certain reduction of Federal Aviation Administration workforce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Air Traffic Controller Protection Act or the ATC Protection Act .\n#### 2. Reduction, replacement, or outsource of FAA staffing\n##### (a) Reduction in staffing\n**(1) In general**\nNotwithstanding any other provision of law, in order for the Secretary of Transportation to reduce, replace, or outsource 1 percent or more of the workforce of the Federal Aviation Administration, the Secretary shall obtain explicit approval from Congress.\n**(2) Report to Congress**\nBefore seeking approval from Congress under paragraph (1), the Secretary of Transportation shall submit to Congress a report detailing the rationale for any decision to reduce, replace, or outsource 1 percent or more of the workforce of the Federal Aviation Administration as well as any analysis on how such decision will impact the aviation and transportation system at large.\n##### (b) DOGE control\nThe Administrator of the Department of Governmental Efficiency may not exercise control over the Federal Aviation Administration.\n##### (c) ATC privatization\nNotwithstanding any other provision of law, the air traffic control system of the Federal Aviation Administration may not be privatized or outsourced from the Federal Aviation Administration.",
      "versionDate": "2025-04-08",
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
        "updateDate": "2025-05-15T17:40:16Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2751ih.xml"
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
      "title": "ATC Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-22T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ATC Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-22T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Air Traffic Controller Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-22T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require approval from Congress for a certain reduction of Federal Aviation Administration workforce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-22T03:48:38Z"
    }
  ]
}
```
