# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/849?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/849
- Title: The Allegiance Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 849
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2026-02-17T20:12:05Z
- Update date including text: 2026-02-17T20:12:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/849",
    "number": "849",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "The Allegiance Act of 2025",
    "type": "S",
    "updateDate": "2026-02-17T20:12:05Z",
    "updateDateIncludingText": "2026-02-17T20:12:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T17:07:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s849is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 849\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Moreno introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit displaying the flag of a country other than the United States on Capitol Hill and to prohibit Members of Congress from using official funds to purchase the flag of a country other than the United States.\n#### 1. Short title\nThis Act may be cited as the The Allegiance Act of 2025 .\n#### 2. Prohibition on displaying or purchasing flags of countries other than the United States\n##### (a) Prohibition on display\nThe flag of a country other than the United States may not be displayed at any location on the United States Capitol Grounds, as described in section 5102 of title 40, United States Code.\n##### (b) Prohibition on purchase\nAmounts made available to a Member or Member-elect of the House of Representatives for the Members' Representational Allowance established under section 101 of the House of Representatives Administrative Reform Technical Corrections Act ( 2 U.S.C. 5341 ) or to a Senator for the Senators\u2019 Official Personnel and Office Expense Account may not be used to purchase the flag of a country other than the United States.",
      "versionDate": "2025-03-05",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Members of Congress",
            "updateDate": "2026-02-17T20:12:01Z"
          },
          {
            "name": "National symbols",
            "updateDate": "2026-02-17T20:11:56Z"
          },
          {
            "name": "U.S. Capitol",
            "updateDate": "2026-02-17T20:12:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-03-31T14:28:33Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s849is.xml"
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
      "title": "The Allegiance Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T11:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "The Allegiance Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T11:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit displaying the flag of a country other than the United States on Capitol Hill and to prohibit Members of Congress from using official funds to purchase the flag of a country other than the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T11:18:38Z"
    }
  ]
}
```
