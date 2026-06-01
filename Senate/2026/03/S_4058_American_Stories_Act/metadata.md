# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4058?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4058
- Title: American Stories Act
- Congress: 119
- Bill type: S
- Bill number: 4058
- Origin chamber: Senate
- Introduced date: 2026-03-11
- Update date: 2026-03-30T15:25:41Z
- Update date including text: 2026-03-30T15:25:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-11: Introduced in Senate
- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-11: Introduced in Senate

## Actions

- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-11",
    "latestAction": {
      "actionDate": "2026-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4058",
    "number": "4058",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "American Stories Act",
    "type": "S",
    "updateDate": "2026-03-30T15:25:41Z",
    "updateDateIncludingText": "2026-03-30T15:25:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-11",
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
          "date": "2026-03-11T18:30:49Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4058is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4058\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2026 Mr. Kim introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo authorize the National Foundation for the Arts and the National Foundation for the Humanities to support activities for the purpose of broadening public understanding of civics and the United States Constitution.\n#### 1. Short title\nThis Act may be cited as the American Stories Act .\n#### 2. Amendments to the National Foundation on the Arts and the Humanities Act of 1965\n##### (a) National Endowment for the Arts\nSection 5(c) of the National Foundation on the Arts and the Humanities Act of 1965 ( 20 U.S.C. 954(c) ) is amended\u2014\n**(1)**\nin paragraph (9), by striking and after the semicolon;\n**(2)**\nby redesignating paragraph (10) as paragraph (11); and\n**(3)**\nby inserting after paragraph (9) the following:\n(10) projects, productions, and workshops through film, radio, video, and similar media, for the purpose of broadening public understanding of civics and the United States Constitution; and .\n##### (b) National Endowment for the Humanities\nSection 7(c) of the National Foundation on the Arts and the Humanities Act of 1965 ( 20 U.S.C. 956(c) ) is amended\u2014\n**(1)**\nin paragraph (9), by striking and after the semicolon;\n**(2)**\nby redesignating paragraph (10) as paragraph (11); and\n**(3)**\nby inserting after paragraph (9) the following:\n(10) foster projects, productions, and workshops through film, radio, video, and similar media, for the purpose of broadening public understanding of civics and the United States Constitution; and .",
      "versionDate": "2026-03-11",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2026-03-30T15:25:41Z"
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
      "date": "2026-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4058is.xml"
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
      "title": "American Stories Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Stories Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the National Foundation for the Arts and the National Foundation for the Humanities to support activities for the purpose of broadening public understanding of civics and the United States Constitution.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T04:03:34Z"
    }
  ]
}
```
