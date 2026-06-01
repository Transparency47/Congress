# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5741?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5741
- Title: TRUMP Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5741
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2025-12-09T18:14:31Z
- Update date including text: 2025-12-09T18:14:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5741",
    "number": "5741",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "TRUMP Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-09T18:14:31Z",
    "updateDateIncludingText": "2025-12-09T18:14:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:30:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5741ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5741\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mr. Torres of New York (for himself and Mr. Liccardo ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend title 31, United States Code, to prohibit representations of a living President on United States coins or currency, and to prohibit representations of any living person on any United States currency.\n#### 1. Short title\nThis Act may be cited as the The Restrict Ugly Money Portraits of 2025 or the TRUMP Act of 2025 .\n#### 2. Prohibition on certain representations on United States coins and currency\nSection 5112 of title 31, United States Code, is amended by adding at the end the following:\n(bb) Prohibition on certain representations (1) Representations of a living President No portrait or bust of any living President may be included in the design of any United States coins or currency, including commemorative coins. (2) Representations on currency No portrait or bust of any living person may be included in the design of any United States currency. .",
      "versionDate": "2025-10-10",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-09T18:14:31Z"
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
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5741ih.xml"
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
      "title": "TRUMP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRUMP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "The Restrict Ugly Money Portraits of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 31, United States Code, to prohibit representations of a living President on United States coins or currency, and to prohibit representations of any living person on any United States currency.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T11:18:16Z"
    }
  ]
}
```
