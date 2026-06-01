# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/274
- Title: A resolution commending Federal, State, and local law enforcement for their efforts in protecting Americans by combating drug trafficking and agroterrorism and for their recent actions in Kansas and across the country.
- Congress: 119
- Bill type: SRES
- Bill number: 274
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3392-3393)
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3392-3393)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/274",
    "number": "274",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "A resolution commending Federal, State, and local law enforcement for their efforts in protecting Americans by combating drug trafficking and agroterrorism and for their recent actions in Kansas and across the country.",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S3392-3393)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T18:27:19Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres274is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 274\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Marshall submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCommending Federal, State, and local law enforcement for their efforts in protecting Americans by combating drug trafficking and agroterrorism and for their recent actions in Kansas and across the country.\nThat the Senate\u2014\n**(1)**\ncommends Federal, State, and local law enforcement agencies and personnel for their tireless efforts in combating drug trafficking and agroterrorism;\n**(2)**\nexpresses gratitude for their bravery and dedication to protecting American communities, public health, and our Nation\u2019s food supply; and\n**(3)**\nencourages them to continue their efforts to keep our communities and food supply safe and secure.",
      "versionDate": "2025-06-12",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-30T13:23:17Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres274is.xml"
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
      "title": "A resolution commending Federal, State, and local law enforcement for their efforts in protecting Americans by combating drug trafficking and agroterrorism and for their recent actions in Kansas and across the country.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:33:22Z"
    },
    {
      "title": "A resolution commending Federal, State, and local law enforcement for their efforts in protecting Americans by combating drug trafficking and agroterrorism and for their recent actions in Kansas and across the country.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T10:56:16Z"
    }
  ]
}
```
