# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1036?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1036
- Title: Expressing support for the annual designation of the first Saturday after the Spring Equinox as ''National Day of Play''.
- Congress: 119
- Bill type: HRES
- Bill number: 1036
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-02-12T15:02:58Z
- Update date including text: 2026-02-12T15:02:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-04 - IntroReferral: Submitted in House
- 2026-02-04 - IntroReferral: Submitted in House
- Latest action: 2026-02-04: Submitted in House

## Actions

- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-04 - IntroReferral: Submitted in House
- 2026-02-04 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1036",
    "number": "1036",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001287",
        "district": "6",
        "firstName": "Ami",
        "fullName": "Rep. Bera, Ami [D-CA-6]",
        "lastName": "Bera",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the annual designation of the first Saturday after the Spring Equinox as ''National Day of Play''.",
    "type": "HRES",
    "updateDate": "2026-02-12T15:02:58Z",
    "updateDateIncludingText": "2026-02-12T15:02:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1036ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1036\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Bera (for himself and Mr. Flood ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the annual designation of the first Saturday after the Spring Equinox as National Day of Play .\nThat the House of Representatives\u2014\n**(1)**\ndesignates a \u2018\u2018National Day of Play\u2019\u2019;\n**(2)**\nexpresses support for the annual designation of a \u2018\u2018National Day of Play\u2019\u2019;\n**(3)**\nrecognizes the importance of social connection for mental, physical, and social development; and\n**(4)**\nencourages people to put their electronics down and play.",
      "versionDate": "2026-02-04",
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
        "name": "Health",
        "updateDate": "2026-02-12T15:02:58Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1036ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the annual designation of the first Saturday after the Spring Equinox as ''National Day of Play''.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T09:18:37Z"
    },
    {
      "title": "Expressing support for the annual designation of the first Saturday after the Spring Equinox as ''National Day of Play''.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T09:06:57Z"
    }
  ]
}
```
