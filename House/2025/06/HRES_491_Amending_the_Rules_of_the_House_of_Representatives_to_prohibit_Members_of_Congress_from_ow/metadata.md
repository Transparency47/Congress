# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/491?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/491
- Title: NO STOCK Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 491
- Origin chamber: House
- Introduced date: 2025-06-09
- Update date: 2025-09-19T08:06:59Z
- Update date including text: 2025-09-19T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-06-09 - IntroReferral: Submitted in House
- 2025-06-09 - IntroReferral: Submitted in House
- Latest action: 2025-06-09: Submitted in House

## Actions

- 2025-06-09 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-06-09 - IntroReferral: Submitted in House
- 2025-06-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/491",
    "number": "491",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001119",
        "district": "2",
        "firstName": "Angie",
        "fullName": "Rep. Craig, Angie [D-MN-2]",
        "lastName": "Craig",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "NO STOCK Resolution",
    "type": "HRES",
    "updateDate": "2025-09-19T08:06:59Z",
    "updateDateIncludingText": "2025-09-19T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-09",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ethics.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-06-09T16:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres491ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 491\nIN THE HOUSE OF REPRESENTATIVES\nJune 9, 2025 Ms. Craig submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nAmending the Rules of the House of Representatives to prohibit Members of Congress from owning individual stocks.\n#### 1. Short title\nThis resolution may be cited as the NO STOCK Resolution or the No Option for Stock Trading and Ownership as a Check to Keep congress clean Resolution .\n#### 2. Prohibiting Members of House of Representatives from owning individual stocks\nRule XXIII of the Rules of the House of Representatives (known as the Code of Official Conduct ) is amended by redesignating clause 22 as clause 23 and inserting after clause 21 the following:\n(22) Prohibiting members of house of representatives from owning individual stocks A Member, Delegate, or Resident Commissioner may not own the common stock of any individual public corporation. .",
      "versionDate": "2025-06-09",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2025-06-24T13:53:21Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres491ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "NO STOCK Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-10T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Option for Stock Trading and Ownership as a Check to Keep congress clean Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NO STOCK Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Amending the Rules of the House of Representatives to prohibit Members of Congress from owning individual stocks.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-10T08:18:15Z"
    }
  ]
}
```
