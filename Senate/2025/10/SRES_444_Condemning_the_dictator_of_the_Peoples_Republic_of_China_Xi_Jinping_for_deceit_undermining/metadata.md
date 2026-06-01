# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/444?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/444
- Title: A resolution condemning the dictator of the People's Republic of China, Xi Jinping, for deceit, undermining prospects for peace and security, and orchestrating crimes against humanity.
- Congress: 119
- Bill type: SRES
- Bill number: 444
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2025-11-19T21:15:31Z
- Update date including text: 2025-11-19T21:15:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Referred to the Committee on Foreign Relations.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/444",
    "number": "444",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A resolution condemning the dictator of the People's Republic of China, Xi Jinping, for deceit, undermining prospects for peace and security, and orchestrating crimes against humanity.",
    "type": "SRES",
    "updateDate": "2025-11-19T21:15:31Z",
    "updateDateIncludingText": "2025-11-19T21:15:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-09",
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
          "date": "2025-10-09T16:01:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres444is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 444\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Scott of Florida submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCondemning the dictator of the People\u2019s Republic of China, Xi Jinping, for deceit, undermining prospects for peace and security, and orchestrating crimes against humanity.\nThat the Senate\u2014\n**(1)**\ncondemns the dictator of the People\u2019s Republic of China, Xi Jinping, for engaging in a pattern of deceit, undermining prospects for peace and security, and orchestrating crimes against humanity;\n**(2)**\nstands in solidarity with the people of the People\u2019s Republic of China, and all people around the world who have endured the consequences of rule by the Chinese Communist Party; and\n**(3)**\nencourages the application of all applicable sanctions authorities against officials of the Chinese Communist Party, including sanctions authorized by the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 10101 et seq. ).",
      "versionDate": "2025-10-09",
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
        "name": "International Affairs",
        "updateDate": "2025-11-19T21:15:31Z"
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
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres444is.xml"
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
      "title": "A resolution condemning the dictator of the People's Republic of China, Xi Jinping, for deceit, undermining prospects for peace and security, and orchestrating crimes against humanity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T02:48:18Z"
    },
    {
      "title": "A resolution condemning the dictator of the People's Republic of China, Xi Jinping, for deceit, undermining prospects for peace and security, and orchestrating crimes against humanity.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T10:56:16Z"
    }
  ]
}
```
