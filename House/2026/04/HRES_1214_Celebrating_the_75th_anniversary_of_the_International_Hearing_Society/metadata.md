# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1214?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1214
- Title: Celebrating the 75th anniversary of the International Hearing Society.
- Congress: 119
- Bill type: HRES
- Bill number: 1214
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-04-27T23:04:34Z
- Update date including text: 2026-04-27T23:04:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-04-23 - IntroReferral: Submitted in House
- Latest action: 2026-04-23: Submitted in House

## Actions

- 2026-04-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-04-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1214",
    "number": "1214",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Celebrating the 75th anniversary of the International Hearing Society.",
    "type": "HRES",
    "updateDate": "2026-04-27T23:04:34Z",
    "updateDateIncludingText": "2026-04-27T23:04:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionCode": "1025",
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
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
          "date": "2026-04-23T13:02:10Z",
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
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "MI"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MI"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MI"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1214ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1214\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Ms. Scholten (for herself, Mr. Barrett , Ms. McDonald Rivet , Ms. Stevens , and Mrs. Dingell ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nCelebrating the 75th anniversary of the International Hearing Society.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes and celebrates the 75th anniversary of the International Hearing Society and its predecessor organizations;\n**(2)**\ncommemorates the legacy of the International Hearing Society and the lasting contributions of the International Hearing Society to the advancement of hearing health care and uniting generations through improved communication; and\n**(3)**\ncongratulates the members of the International Hearing Society on 75 years of caring for patients in need of assistance with their hearing health care needs.",
      "versionDate": "2026-04-23",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-27T23:04:33Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1214ih.xml"
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
      "title": "Celebrating the 75th anniversary of the International Hearing Society.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-24T08:18:36Z"
    },
    {
      "title": "Celebrating the 75th anniversary of the International Hearing Society.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T08:06:23Z"
    }
  ]
}
```
