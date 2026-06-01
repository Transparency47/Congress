# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3158?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3158
- Title: National Defense Supply Chain Integrity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3158
- Origin chamber: Senate
- Introduced date: 2025-11-07
- Update date: 2025-11-25T19:29:58Z
- Update date including text: 2025-11-25T19:29:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in Senate
- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-11-07: Introduced in Senate

## Actions

- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3158",
    "number": "3158",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "National Defense Supply Chain Integrity Act of 2025",
    "type": "S",
    "updateDate": "2025-11-25T19:29:58Z",
    "updateDateIncludingText": "2025-11-25T19:29:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-07",
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
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:35:44Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3158is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3158\nIN THE SENATE OF THE UNITED STATES\nNovember 7, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 to clarify that the identification of Chinese military companies is not covered by the Administrative Procedure Act.\n#### 1. Short title\nThis Act may be cited as the National Defense Supply Chain Integrity Act of 2025 .\n#### 2. Treatment of identification of Chinese military companies for purposes of Administrative Procedure Act\nSection 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note) is amended\u2014\n**(1)**\nby redesignating subsection (g) as subsection (h); and\n**(2)**\nby inserting after subsection (f) the following new subsection (g):\n(g) Administrative procedure A determination made by the Secretary of Defense under subsection (a) shall be considered a military or foreign affairs function for purposes of section 554 of title 5, United States Code, and shall not be subject to sections 551, 553 through 559, and 701 through 706 of that title (commonly referred to as the Administrative Procedure Act ). .",
      "versionDate": "2025-11-07",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-11-25T19:29:58Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3158is.xml"
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
      "title": "National Defense Supply Chain Integrity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "National Defense Supply Chain Integrity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 to clarify that the identification of Chinese military companies is not covered by the Administrative Procedure Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:31Z"
    }
  ]
}
```
