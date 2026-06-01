# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2297?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2297
- Title: Preventing Intelligence Gathering from Foreign Adversaries Act
- Congress: 119
- Bill type: S
- Bill number: 2297
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2025-09-05T17:07:09Z
- Update date including text: 2025-09-05T17:07:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2297",
    "number": "2297",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
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
    "title": "Preventing Intelligence Gathering from Foreign Adversaries Act",
    "type": "S",
    "updateDate": "2025-09-05T17:07:09Z",
    "updateDateIncludingText": "2025-09-05T17:07:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:20:46Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2297is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2297\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to include subjection to a foreign intelligence security law as a ground of inadmissibility and deportability.\n#### 1. Short title\nThis Act may be cited as the Preventing Intelligence Gathering from Foreign Adversaries Act .\n#### 2. Subjection to foreign intelligence security law as grounds of inadmissibility and deportability\n##### (a) Inadmissibility\nSection 212(a)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3) ) is amended by adding at the end the following:\n(H) Subjection to foreign intelligence security law Any alien who is subject to a law of any foreign country that requires such alien to provide access to, cooperation with, or support for, the intelligence-gathering activities or operations of such county is inadmissible. .\n##### (b) Deportability\nSection 237(a)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(4) ) is amended by adding at the end the following:\n(G) Subjection to foreign intelligence security law Any alien who is subject to a law of any foreign country that requires such alien to provide access to, cooperation with, or support for, the intelligence-gathering activities or operations of such county is deportable. .",
      "versionDate": "2025-07-17",
      "versionType": "Introduced in Senate"
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
        "name": "Immigration",
        "updateDate": "2025-09-05T17:07:09Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2297is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Preventing Intelligence Gathering from Foreign Adversaries Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-29T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Intelligence Gathering from Foreign Adversaries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to include subjection to a foreign intelligence security law as a ground of inadmissibility and deportability.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T04:18:16Z"
    }
  ]
}
```
