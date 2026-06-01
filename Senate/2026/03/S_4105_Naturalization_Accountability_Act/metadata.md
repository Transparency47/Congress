# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4105?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4105
- Title: Naturalization Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 4105
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-04-01T16:59:16Z
- Update date including text: 2026-04-01T16:59:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-17: Introduced in Senate

## Actions

- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4105",
    "number": "4105",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
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
    "title": "Naturalization Accountability Act",
    "type": "S",
    "updateDate": "2026-04-01T16:59:16Z",
    "updateDateIncludingText": "2026-04-01T16:59:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
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
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T15:11:57Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4105is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4105\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo include any felony conviction as a ground for revocation of naturalization, to strike the 5-year limitation on the revocation of naturalization for membership in certain totalitarian or treasonous organizations, and to eliminate the 10-year statute of limitation for certain criminal penalties that would disqualify a person from naturalization.\n#### 1. Short title\nThis Act may be cited as the Naturalization Accountability Act .\n#### 2. Revocation of naturalization\nSection 340(c) of the Immigration and Nationality Act ( 8 U.S.C. 1451 ) is amended\u2014\n**(1)**\nby striking shall within five years next following such naturalization become and inserting becomes ; and\n**(2)**\nby inserting or has been convicted at any time of any felony, after section 313, .\n#### 3. Elimination of 10-year statute of limitation for criminal penalties for procurement of citizenship or naturalization unlawfully\nSection 3291 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking No person and inserting the following:\n(a) Ten-Year limitation No person ;\n**(2)**\nby striking sections 1423 to 1428 and inserting sections 1423, 1424, and 1426 to 1428 ; and\n**(3)**\nby adding at the end the following:\n(b) No limitation Notwithstanding any other law, an indictment may be found or an information instituted at any time without limitation for any offense under section 1425. .",
      "versionDate": "2026-03-17",
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
        "updateDate": "2026-04-01T16:59:16Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4105is.xml"
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
      "title": "Naturalization Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Naturalization Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to include any felony conviction as a ground for revocation of naturalization, to strike the 5-year limitation on the revocation of naturalization for membership in certain totalitarian or treasonous organizations, and to eliminate the 10-year statute of limitation for certain criminal penalties that would disqualify a person from naturalization.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:27Z"
    }
  ]
}
```
