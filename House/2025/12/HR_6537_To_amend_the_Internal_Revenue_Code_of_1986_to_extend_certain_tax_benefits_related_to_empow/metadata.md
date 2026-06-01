# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6537?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6537
- Title: To amend the Internal Revenue Code of 1986 to extend certain tax benefits related to empowerment zones to the District of Columbia.
- Congress: 119
- Bill type: HR
- Bill number: 6537
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-01-06T16:10:17Z
- Update date including text: 2026-01-06T16:10:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-12-09 - IntroReferral: Sponsor introductory remarks on measure. (CR E1161)
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-12-09 - IntroReferral: Sponsor introductory remarks on measure. (CR E1161)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6537",
    "number": "6537",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to extend certain tax benefits related to empowerment zones to the District of Columbia.",
    "type": "HR",
    "updateDate": "2026-01-06T16:10:17Z",
    "updateDateIncludingText": "2026-01-06T16:10:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E1161)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:01:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6537ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6537\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend certain tax benefits related to empowerment zones to the District of Columbia.\n#### 1. District of Columbia treated as empowerment zone\n##### (a) In general\nSection 1391(b)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following: There shall be treated as an empowerment zone designated under this section so much of the District of Columbia as would result in the largest area within such District meeting the eligibility requirements for designation under section 1391. Deemed treatment under the preceding sentence shall not be taken into account in determining the number of empowerment zones which may be designated under this section. .\n##### (b) Effective date\nThe amendments made by this section shall apply to periods beginning after December 31, 2025.",
      "versionDate": "2025-12-09",
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
        "name": "Taxation",
        "updateDate": "2026-01-06T16:10:17Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6537ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to extend certain tax benefits related to empowerment zones to the District of Columbia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:24Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to extend certain tax benefits related to empowerment zones to the District of Columbia.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T09:05:56Z"
    }
  ]
}
```
