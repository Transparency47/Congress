# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2940?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2940
- Title: OPT Fair Tax Act
- Congress: 119
- Bill type: S
- Bill number: 2940
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2026-01-06T15:56:08Z
- Update date including text: 2026-01-06T15:56:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2940",
    "number": "2940",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "OPT Fair Tax Act",
    "type": "S",
    "updateDate": "2026-01-06T15:56:08Z",
    "updateDateIncludingText": "2026-01-06T15:56:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T15:30:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2940is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2940\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to include optional practical training for F\u20131 visa holders as employment for purposes of taxes under the Federal Insurance Contribution Act and the Social Security Act.\n#### 1. Short title\nThis Act may be cited as the OPT Fair Tax Act .\n#### 2. Inclusion of optional practical training for F-1 visa holders as employment\n##### (a) Federal Insurance Contribution Act\nSection 3121(b)(19) of the Internal Revenue Code of 1986 is amended by striking as the case may be and inserting as the case may be, except that this paragraph shall not apply to service performed by an alien present in the United States as a nonimmigrant described in section 101(a)(15)(F)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F)(i) ) who is participating in optional practical training .\n##### (b) Social Security Act\nSection 210(a)(19) of the Social Security Act ( 42 U.S.C. 410(a)(19) ) is amended by striking as the case may be and inserting as the case may be, except that this paragraph shall not apply to service performed by an alien present in the United States as a nonimmigrant described in section 101(a)(15)(F)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F)(i) ) who is participating in optional practical training .\n##### (c) Effective date\nThe amendments made by this section shall apply to services performed in calendar months beginning after the date of enactment of this Act.",
      "versionDate": "2025-09-30",
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
        "name": "Taxation",
        "updateDate": "2026-01-06T15:56:08Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2940is.xml"
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
      "title": "OPT Fair Tax Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "OPT Fair Tax Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to include optional practical training for F-1 visa holders and employment for purposes of taxes under the Federal Insurance Contribution Act and the Social Security Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:26Z"
    }
  ]
}
```
