# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4240?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4240
- Title: American Homes First Act
- Congress: 119
- Bill type: S
- Bill number: 4240
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-15T01:10:14Z
- Update date including text: 2026-04-15T01:10:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4240",
    "number": "4240",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "American Homes First Act",
    "type": "S",
    "updateDate": "2026-04-15T01:10:14Z",
    "updateDateIncludingText": "2026-04-15T01:10:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T19:14:17Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4240is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4240\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Ms. Cortez Masto introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo provide funding for the Low-Income Home Energy Assistance Program.\n#### 1. Short title\nThis Act may be cited as the American Homes First Act .\n#### 2. Low-Income Home Energy Assistance Program\nNotwithstanding any provision of the Full-Year Continuing Appropriations and Extensions Act, 2025 or the National Security, Department of State, and Related Programs Appropriations Act, 2026, from the funds appropriated under either such Act, the Secretary of State and the President shall\u2014\n**(1)**\nnot make available, after the date of enactment of this Act, any of those appropriated funds for the Board of Peace designated by President Trump through Executive Order 14375 (91 Fed. Reg. 2837; relating to designating the Board of Peace as a public international organization entitled to enjoy certain privileges, exemptions, and immunities); and\n**(2)**\ntransfer $1,000,000,000 of those appropriated funds to the Secretary of Health and Human Services to carry out the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8621 et seq. ), who shall treat the transferred funds as if the funds were appropriated under section 2602(b) of that Act ( 42 U.S.C. 8621 ) for fiscal year 2026.",
      "versionDate": "2026-03-26",
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
        "name": "International Affairs",
        "updateDate": "2026-04-15T01:10:14Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4240is.xml"
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
      "title": "American Homes First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Homes First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide funding for the Low-Income Home Energy Assistance Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:31Z"
    }
  ]
}
```
