# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5379
- Title: HOPE Act
- Congress: 119
- Bill type: HR
- Bill number: 5379
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-09-25T15:29:24Z
- Update date including text: 2025-09-25T15:29:24Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5379",
    "number": "5379",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000557",
        "district": "1",
        "firstName": "John",
        "fullName": "Rep. Larson, John B. [D-CT-1]",
        "lastName": "Larson",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "HOPE Act",
    "type": "HR",
    "updateDate": "2025-09-25T15:29:24Z",
    "updateDateIncludingText": "2025-09-25T15:29:24Z"
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
          "date": "2025-09-16T14:02:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5379ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5379\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Larson of Connecticut introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo guarantee that grants are made under the health profession opportunity grant program under section 2008 of the Social Security Act to grantees in each State that is not a territory, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Health Opportunities to Promote Equity Act or the HOPE Act .\n#### 2. Guarantee of grantees in each State and the District of Columbia; reports to the Congress\nSection 2008 of the Social Security Act ( 42 U.S.C. 1397g ) is amended by redesignating subsections (c) and (d) as subsections (d) and (e), respectively, and by inserting after subsection (b) the following:\n(c) Guarantee of grantees in each State and the District of Columbia (1) In general For each grant cycle, the Secretary shall award a grant under this section to at least 2 eligible entities in each State that is not a territory, to the extent there are a sufficient number of applications submitted by the entities that meet the requirements applicable with respect to such a grant. If, for a grant cycle, there are fewer than 2 eligible entities in such a State, the Secretary shall include that information in the report required by paragraph (2) that covers the fiscal year. (2) Reports to the congress During each Congress, the Secretary shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a report on, with respect to the period since the period covered in the most recent prior report submitted under this paragraph\u2014 (A) the number of applications submitted under each subsection of this section; (B) the number of the applications that were approved; and (C) a description of how grants were made in any case described in the last sentence of paragraph (1). .\n#### 3. Effective date\nThe amendments made by this Act shall take effect on October 1, 2025.",
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
        "updateDate": "2025-09-25T15:29:24Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5379ih.xml"
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
      "title": "To guarantee that grants are made under the health profession opportunity grant program under section 2008 of the Social Security Act to grantees in each State that is not a territory, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-25T06:55:49Z"
    },
    {
      "title": "HOPE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-25T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOPE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T06:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health Opportunities to Promote Equity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T06:53:15Z"
    }
  ]
}
```
