# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5381?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5381
- Title: Opioid Treatment Providers Act
- Congress: 119
- Bill type: HR
- Bill number: 5381
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-09-26T14:32:17Z
- Update date including text: 2025-09-26T14:32:17Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5381",
    "number": "5381",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001201",
        "district": "3",
        "firstName": "Thomas",
        "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
        "lastName": "Suozzi",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Opioid Treatment Providers Act",
    "type": "HR",
    "updateDate": "2025-09-26T14:32:17Z",
    "updateDateIncludingText": "2025-09-26T14:32:17Z"
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
          "date": "2025-09-16T14:04:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5381ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5381\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Suozzi introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo make opioid treatment programs eligible for grants under section 2008 of the Social Security Act.\n#### 1. Short title\nThis Act may be cited as the Opioid Treatment Providers Act .\n#### 2. Eligibility of opioid treatment programs for health professions opportunity grants\nSection 2008(a)(4)(A) of the Social Security Act ( 42 U.S.C. 1397g(a)(4)(A) ) is amended by striking or a community-based organization and inserting , a community-based organization, or an opioid treatment program (as defined in section 1861(jjj)(2)) and other high quality comprehensive addiction care providers .\n#### 3. Effective date\nThe amendment made by this Act shall take effect on October 1, 2025.",
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
        "updateDate": "2025-09-26T14:32:17Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5381ih.xml"
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
      "title": "To make opioid treatment programs eligible for grants under section 2008 of the Social Security Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-25T06:55:50Z"
    },
    {
      "title": "Opioid Treatment Providers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-25T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Opioid Treatment Providers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T06:53:15Z"
    }
  ]
}
```
