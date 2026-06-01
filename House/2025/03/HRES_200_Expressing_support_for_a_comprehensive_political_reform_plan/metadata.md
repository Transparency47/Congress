# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/200?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/200
- Title: Expressing support for a comprehensive political reform plan.
- Congress: 119
- Bill type: HRES
- Bill number: 200
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-05-14T14:56:40Z
- Update date including text: 2025-05-14T14:56:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Submitted in House
- Latest action: 2025-03-06: Submitted in House

## Actions

- 2025-03-06 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/200",
    "number": "200",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for a comprehensive political reform plan.",
    "type": "HRES",
    "updateDate": "2025-05-14T14:56:40Z",
    "updateDateIncludingText": "2025-05-14T14:56:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:10:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-06T14:09:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres200ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 200\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Khanna submitted the following resolution; which was referred to the Committee on the Judiciary , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nExpressing support for a comprehensive political reform plan.\nThat the House of Representatives recognizes the importance of a comprehensive plan for political reform which\u2014\n**(1)**\nprohibits all Members of Congress and those running for a House or Senate seat from accepting contributions from political action committees and lobbyists, and imposes a lifetime lobbying ban on Members of Congress;\n**(2)**\nbans Members of Congress from holding and trading individual stocks during the Member\u2019s tenure and requires Members of Congress, as well as any spouse or dependent child of a Member, to place specified investments into a qualified blind trust until 180 days after the end of their tenure;\n**(3)**\nestablishes 12-year term limits for Members of Congress;\n**(4)**\ninstitutes a binding code of ethics for Supreme Court Justices; and\n**(5)**\nimplements 18-year term limits and regular appointments for Supreme Court Justices.",
      "versionDate": "2025-03-06",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-14T14:56:40Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres200ih.xml"
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
      "title": "Expressing support for a comprehensive political reform plan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T09:48:19Z"
    },
    {
      "title": "Expressing support for a comprehensive political reform plan.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T09:06:57Z"
    }
  ]
}
```
