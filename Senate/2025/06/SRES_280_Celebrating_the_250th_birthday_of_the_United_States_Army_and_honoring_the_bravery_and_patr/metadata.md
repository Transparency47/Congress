# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/280?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/280
- Title: A resolution celebrating the 250th birthday of the United States Army and honoring the bravery and patriotism of soldiers and veterans from Fort Leavenworth, Kansas and Fort Riley, Kansas.
- Congress: 119
- Bill type: SRES
- Bill number: 280
- Origin chamber: Senate
- Introduced date: 2025-06-16
- Update date: 2025-07-16T15:33:08Z
- Update date including text: 2025-07-16T15:33:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-16: Introduced in Senate
- 2025-06-16 - IntroReferral: Introduced in Senate
- 2025-06-16 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S3405)
- Latest action: 2025-06-16: Introduced in Senate

## Actions

- 2025-06-16 - IntroReferral: Introduced in Senate
- 2025-06-16 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S3405)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-16",
    "latestAction": {
      "actionDate": "2025-06-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/280",
    "number": "280",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "A resolution celebrating the 250th birthday of the United States Army and honoring the bravery and patriotism of soldiers and veterans from Fort Leavenworth, Kansas and Fort Riley, Kansas.",
    "type": "SRES",
    "updateDate": "2025-07-16T15:33:08Z",
    "updateDateIncludingText": "2025-07-16T15:33:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-16",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Armed Services. (text: CR S3405)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-16",
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
          "date": "2025-06-16T21:20:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres280is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 280\nIN THE SENATE OF THE UNITED STATES\nJune 16, 2025 Mr. Marshall submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nCelebrating the 250th birthday of the United States Army and honoring the bravery and patriotism of soldiers and veterans from Fort Leavenworth, Kansas and Fort Riley, Kansas.\nThat the Senate\u2014\n**(1)**\ncongratulates the United States Army on its 250th anniversary, commemorating its establishment on June 14, 1775;\n**(2)**\nhonors the extraordinary service, sacrifice, and commitment of all who have served in the United States Army;\n**(3)**\nexpresses profound gratitude to the soldiers and veterans of the United States Army for their unwavering dedication to protecting the United States;\n**(4)**\nhonors the bravery and patriotism of the soldiers and veterans from Fort Leavenworth, Kansas and Fort Riley, Kansas; and\n**(5)**\ncalls upon the people of the United States to join in celebrating the 250th anniversary of the United States Army with appropriate ceremonies, activities, and expressions of appreciation for its enduring legacy and service to the United States.",
      "versionDate": "2025-06-16",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-16T15:33:08Z"
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
      "date": "2025-06-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres280is.xml"
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
      "title": "A resolution celebrating the 250th birthday of the United States Army and honoring the bravery and patriotism of soldiers and veterans from Fort Leavenworth, Kansas and Fort Riley, Kansas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:20Z"
    },
    {
      "title": "A resolution celebrating the 250th birthday of the United States Army and honoring the bravery and patriotism of soldiers and veterans from Fort Leavenworth, Kansas and Fort Riley, Kansas.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T10:56:15Z"
    }
  ]
}
```
