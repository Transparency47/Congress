# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3116
- Title: Fairness in Filing Act
- Congress: 119
- Bill type: S
- Bill number: 3116
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-12-03T12:03:24Z
- Update date including text: 2025-12-03T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3116",
    "number": "3116",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Fairness in Filing Act",
    "type": "S",
    "updateDate": "2025-12-03T12:03:24Z",
    "updateDateIncludingText": "2025-12-03T12:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
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
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T16:18:21Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "AL"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3116is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3116\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Cassidy (for himself and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the National Labor Relations Act to restrict charges of unfair labor practices that are not filed in good faith or are frivolous, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fairness in Filing Act .\n#### 2. Restricting unfair labor practice charges that are not filed in good faith or are frivolous\n##### (a) Requirements for filing a charge\nSection 10(b) of the National Labor Relations Act ( 29 U.S.C. 160(b) ) is amended\u2014\n**(1)**\nby inserting in good faith after charged ; and\n**(2)**\nby striking Provided , and inserting Provided , That no complaint shall issue unless the charge filed with the Board includes (1) documentation of evidence (including an affidavit, photo, video, email, text message, or other evidence determined appropriate by the Board) from an identified source supporting the charge, or (2) a certification by the person filing the charge that the person is unable to include such documentation and a description of the relevant evidence: Provided further , .\n##### (b) Right To inspect evidence presented in a complaint\nSection 10(b) of the National Labor Relations Act ( 29 U.S.C. 160(b) ), as amended by subsection (a), is further amended by inserting The Board shall, before the hearing, produce to the person, and permit the person or a representative of the person to inspect, copy, test, or sample, any evidence to be used to determine whether the person has engaged in or is engaging in an unfair labor practice. after in the complaint. .\n##### (c) Penalties\nSection 12 of the National Labor Relations Act ( 29 U.S.C. 162 ) is amended\u2014\n**(1)**\nby striking Sec. 12. Any person and inserting the following:\n12. Penalties (a) Violations for interference with Board Any person ; and\n**(2)**\nby adding at the end the following:\n(b) Violations for filing bad faith or frivolous charges Any person who files a charge under section 10(b) not in good faith or engages in a pattern or practice of filing frivolous charges under such section, including a pattern or practice of filing charges that do not satisfy the requirement for documentation of evidence or certification under the first proviso of such section, shall be punished by a fine of not more than $5,000. .",
      "versionDate": "2025-11-06",
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
        "name": "Labor and Employment",
        "updateDate": "2025-11-19T15:25:23Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3116is.xml"
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
      "title": "Fairness in Filing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fairness in Filing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Labor Relations Act to restrict charges of unfair labor practices that are not filed in good faith or are frivolous, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:25Z"
    }
  ]
}
```
