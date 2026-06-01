# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5920?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5920
- Title: District of Columbia Flood Prevention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5920
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2025-12-02T21:57:27Z
- Update date including text: 2025-12-02T21:57:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5920",
    "number": "5920",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "District of Columbia Flood Prevention Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-02T21:57:27Z",
    "updateDateIncludingText": "2025-12-02T21:57:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-04",
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
          "date": "2025-11-04T19:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5920ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5920\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Coastal Zone Management Act of 1972 to allow the District of Columbia to receive Federal funding under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the District of Columbia Flood Prevention Act of 2025 .\n#### 2. Eligibility of District of Columbia for Federal funding under Coastal Zone Management Act of 1972\nSection 304(4) of the Coastal Zone Management Act of 1972 ( 16 U.S.C. 1453(4) ) is amended by inserting the District of Columbia, after the term also includes .",
      "versionDate": "2025-11-04",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-02T21:57:27Z"
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
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5920ih.xml"
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
      "title": "District of Columbia Flood Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T10:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "District of Columbia Flood Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T10:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Coastal Zone Management Act of 1972 to allow the District of Columbia to receive Federal funding under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T10:33:22Z"
    }
  ]
}
```
