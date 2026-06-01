# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5380?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5380
- Title: Labor Market Response Act
- Congress: 119
- Bill type: HR
- Bill number: 5380
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-09-26T14:23:38Z
- Update date including text: 2025-09-26T14:23:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5380",
    "number": "5380",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001296",
        "district": "2",
        "firstName": "Brendan",
        "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
        "lastName": "Boyle",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Labor Market Response Act",
    "type": "HR",
    "updateDate": "2025-09-26T14:23:38Z",
    "updateDateIncludingText": "2025-09-26T14:23:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-09-16T14:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5380ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5380\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Boyle of Pennsylvania introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require applications for a health profession opportunity grant under section 2008 of the Social Security Act to contain evidence of in-demand jobs or worker shortages.\n#### 1. Short title\nThis Act may be cited as the Labor Market Response Act .\n#### 2. Requirement that application contain evidence of in-demand jobs or worker shortages\nSection 2008 of the Social Security Act ( 42 U.S.C. 1397g ) is amended by redesignating subsections (c) and (d) as subsections (d) and (e), respectively, and inserting after subsection (b) the following:\n(c) Application requirement An application for a grant under this section shall contain a description of the availability and relevance of recent labor market information and other pertinent evidence of in-demand jobs or worker shortages. .\n#### 3. Effective date\nThe amendment made by this Act shall take effect on October 1, 2025.",
      "versionDate": "2025-09-16",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-09-26T14:23:38Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5380ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require applications for a health profession opportunity grant under section 2008 of the Social Security Act to contain evidence of in-demand jobs or worker shortages.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-25T06:40:31Z"
    },
    {
      "title": "Labor Market Response Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-25T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Labor Market Response Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T06:38:15Z"
    }
  ]
}
```
