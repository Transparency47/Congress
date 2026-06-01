# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5384?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5384
- Title: MORE Act
- Congress: 119
- Bill type: HR
- Bill number: 5384
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-09-26T15:01:03Z
- Update date including text: 2025-09-26T15:01:03Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5384",
    "number": "5384",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000296",
        "district": "3",
        "firstName": "Dwight",
        "fullName": "Rep. Evans, Dwight [D-PA-3]",
        "lastName": "Evans",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "MORE Act",
    "type": "HR",
    "updateDate": "2025-09-26T15:01:03Z",
    "updateDateIncludingText": "2025-09-26T15:01:03Z"
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
          "date": "2025-09-16T14:00:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5384ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5384\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Evans of Pennsylvania introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require preference to be given to applicants for health profession opportunity grants under section 2008 of the Social Security Act who have certain kinds of business and community partners.\n#### 1. Short title\nThis Act may be cited as the Making Opportunities Reachable for Everyone Act or the MORE Act .\n#### 2. Preference for health profession opportunity grant applicants who have certain kinds of business and community partners\nSection 2008 of the Social Security Act ( 42 U.S.C. 1397g ) is amended\u2014\n**(1)**\nby redesignating subsections (c) and (d) as subsections (d) and (e), respectively; and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Preference for grant applicants who have certain partners In considering applications for a grant under this section, the Secretary shall give preference to applications submitted by applicants who have business and community partners in each of the following categories: (1) State and local government agencies and social service providers, including a State or local entity that administers a State program funded under part A of this title; (2) institutions of higher education, apprenticeship programs, and local workforce development boards established under section 107 of the Workforce Innovation and Opportunity Act; and (3) health care employers, health care industry or sector partnerships, labor unions, and labor-management partnerships. .\n#### 3. Effective date\nThe amendments made by this Act shall take effect on October 1, 2025.",
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
        "updateDate": "2025-09-26T15:01:03Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5384ih.xml"
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
      "title": "To require preference to be given to applicants for health profession opportunity grants under section 2008 of the Social Security Act who have certain kinds of business and community partners.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-25T06:55:49Z"
    },
    {
      "title": "MORE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-25T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MORE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T06:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Making Opportunities Reachable for Everyone Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T06:53:15Z"
    }
  ]
}
```
