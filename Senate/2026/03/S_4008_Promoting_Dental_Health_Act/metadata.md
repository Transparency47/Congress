# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4008?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4008
- Title: Promoting Dental Health Act
- Congress: 119
- Bill type: S
- Bill number: 4008
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-24T19:36:19Z
- Update date including text: 2026-03-24T19:36:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S887)
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S887)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4008",
    "number": "4008",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Promoting Dental Health Act",
    "type": "S",
    "updateDate": "2026-03-24T19:36:19Z",
    "updateDateIncludingText": "2026-03-24T19:36:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S887)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T19:10:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4008is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4008\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Durbin introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reauthorize programs relating to oral health promotion and disease prevention.\n#### 1. Short title\nThis Act may be cited as the Promoting Dental Health Act .\n#### 2. Reauthorization of programs\nSection 317M of the Public Health Service Act ( 42 U.S.C. 247b\u201314 ) is amended\u2014\n**(1)**\nin subsection (d)(2), by striking 2010 through 2014 and inserting 2027 through 2031 ; and\n**(2)**\nin subsection (f), by striking 2001 through 2005 and inserting 2027 through 2031 .",
      "versionDate": "2026-03-05",
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
        "name": "Health",
        "updateDate": "2026-03-24T19:36:19Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4008is.xml"
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
      "title": "Promoting Dental Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Dental Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize programs relating to oral health promotion and disease prevention.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:03:27Z"
    }
  ]
}
```
