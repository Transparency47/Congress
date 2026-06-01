# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3896?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3896
- Title: Veterans Affairs Opportunity for Small Businesses Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3896
- Origin chamber: Senate
- Introduced date: 2026-02-24
- Update date: 2026-03-13T22:31:45Z
- Update date including text: 2026-03-13T22:31:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in Senate
- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2026-02-24: Introduced in Senate

## Actions

- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3896",
    "number": "3896",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Veterans Affairs Opportunity for Small Businesses Act of 2026",
    "type": "S",
    "updateDate": "2026-03-13T22:31:45Z",
    "updateDateIncludingText": "2026-03-13T22:31:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-24",
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
          "date": "2026-02-24T20:25:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3896is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3896\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2026 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to modify the Department of Veterans Affairs procurement hierarchy of small business preferences, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Affairs Opportunity for Small Businesses Act of 2026 .\n#### 2. Modification of Department of Veterans Affairs procurement hierarchy of small business preferences\nSection 8127(h) of title 38, United States Code, is amended\u2014\n**(1)**\nby striking paragraph (3);\n**(2)**\nby redesignating paragraph (4) as paragraph (3); and\n**(3)**\nin paragraph (3), as redesignated by paragraph (2), by inserting established under the Small Business Act ( 15 U.S.C. 631 et seq. ) before the period at the end.",
      "versionDate": "2026-02-24",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-13T22:31:45Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3896is.xml"
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
      "title": "Veterans Affairs Opportunity for Small Businesses Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Affairs Opportunity for Small Businesses Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to modify the Department of Veterans Affairs procurement hierarchy of small business preferences, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:33Z"
    }
  ]
}
```
