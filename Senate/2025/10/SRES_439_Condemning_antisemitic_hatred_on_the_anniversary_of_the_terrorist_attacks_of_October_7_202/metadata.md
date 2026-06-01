# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/439?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/439
- Title: A resolution condemning antisemitic hatred on the anniversary of the terrorist attacks of October 7, 2023.
- Congress: 119
- Bill type: SRES
- Bill number: 439
- Origin chamber: Senate
- Introduced date: 2025-10-07
- Update date: 2025-12-05T15:48:25Z
- Update date including text: 2025-12-05T15:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-07: Introduced in Senate
- 2025-10-07 - IntroReferral: Introduced in Senate
- 2025-10-07 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6982-6983)
- Latest action: 2025-10-07: Introduced in Senate

## Actions

- 2025-10-07 - IntroReferral: Introduced in Senate
- 2025-10-07 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6982-6983)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-07",
    "latestAction": {
      "actionDate": "2025-10-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/439",
    "number": "439",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "A resolution condemning antisemitic hatred on the anniversary of the terrorist attacks of October 7, 2023.",
    "type": "SRES",
    "updateDate": "2025-12-05T15:48:25Z",
    "updateDateIncludingText": "2025-12-05T15:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-07",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S6982-6983)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-10-07T21:44:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres439is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 439\nIN THE SENATE OF THE UNITED STATES\nOctober 7, 2025 Mr. Welch submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCondemning antisemitic hatred on the anniversary of the terrorist attacks of October 7, 2023.\nThat the Senate\u2014\n**(1)**\ncondemns Hamas in the harshest terms for its premeditated, coordinated, and violent terrorist attacks on Israel;\n**(2)**\ncondemns the antisemitic attacks on Sarah Milgrim, Yaron Lischinsky, Karen Diamond, and the family of Governor Josh Shapiro, and all acts of antisemitism, whether expressed through threats, vandalism, or violence;\n**(3)**\nreaffirms the commitment to protecting the rights of all people in the United States to assemble peacefully and practice their faith without fear of violence;\n**(4)**\ncondemns hateful language that\u2014\n**(A)**\nmakes general claims about all Jewish people;\n**(B)**\nassociates Jewish Americans and Jewish people around the world with the military and government actions of the State of Israel; and\n**(C)**\naccuses Jewish people categorically of being hateful or harboring genocidal intent; and\n**(5)**\nurges elected officials, community leaders, and civil society to speak out against antisemitism.",
      "versionDate": "2025-10-07",
      "versionType": "IS"
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-12-05T15:48:25Z"
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
      "date": "2025-10-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres439is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution condemning antisemitic hatred on the anniversary of the terrorist attacks of October 7, 2023.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T05:48:15Z"
    },
    {
      "title": "A resolution condemning antisemitic hatred on the anniversary of the terrorist attacks of October 7, 2023.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-08T10:56:17Z"
    }
  ]
}
```
