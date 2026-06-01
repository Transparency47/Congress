# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/125?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/125
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Office of the Secretary of the Department of Health and Human Services relating to "Policy on Adhering to the Text of the Administrative Procedure Act".
- Congress: 119
- Bill type: HJRES
- Bill number: 125
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-04-17T14:32:54Z
- Update date including text: 2026-04-17T14:32:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/125",
    "number": "125",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000468",
        "district": "7",
        "firstName": "Lizzie",
        "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
        "lastName": "Fletcher",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Office of the Secretary of the Department of Health and Human Services relating to \"Policy on Adhering to the Text of the Administrative Procedure Act\".",
    "type": "HJRES",
    "updateDate": "2026-04-17T14:32:54Z",
    "updateDateIncludingText": "2026-04-17T14:32:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres125ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 125\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mrs. Fletcher submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Office of the Secretary of the Department of Health and Human Services relating to Policy on Adhering to the Text of the Administrative Procedure Act .\nThat Congress disapproves the rule submitted by the Office of the Secretary of the Department of Health and Human Services relating to Policy on Adhering to the Text of the Administrative Procedure Act (published on March 3, 2025, and a letter of opinion from the Government Accountability Office dated August 27, 2025, printed in the Congressional Record on September 3, 2025, on pages S6003\u2013S6005, concluding that such Policy Statement is a rule under chapter 8 of title 5, United States Code), and such rule shall have no force or effect.",
      "versionDate": "2025-09-18",
      "versionType": "IH"
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
        "actionDate": "2025-12-18",
        "text": "Failed of passage in Senate by Yea-Nay Vote. 50 - 50. Record Vote Number: 654."
      },
      "number": "82",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Office of the Secretary of the Department of Health and Human Services relating to \"Policy on Adhering to the Text of the Administrative Procedure Act\".",
      "type": "SJRES"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-12-12T20:59:52Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-12T21:00:05Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-12-12T20:59:56Z"
          },
          {
            "name": "Public participation and lobbying",
            "updateDate": "2025-12-12T21:00:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-19T15:49:42Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres125ih.xml"
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
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Office of the Secretary of the Department of Health and Human Services relating to \"Policy on Adhering to the Text of the Administrative Procedure Act\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T08:18:20Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Office of the Secretary of the Department of Health and Human Services relating to \"Policy on Adhering to the Text of the Administrative Procedure Act\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T08:06:59Z"
    }
  ]
}
```
