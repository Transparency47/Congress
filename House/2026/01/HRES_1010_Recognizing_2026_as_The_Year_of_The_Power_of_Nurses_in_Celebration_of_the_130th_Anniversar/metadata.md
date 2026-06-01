# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1010?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1010
- Title: Recognizing 2026 as "The Year of The Power of Nurses" in Celebration of the 130th Anniversary of the American Nurses Association.
- Congress: 119
- Bill type: HRES
- Bill number: 1010
- Origin chamber: House
- Introduced date: 2026-01-20
- Update date: 2026-01-22T15:25:55Z
- Update date including text: 2026-01-22T15:25:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-20: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-20 - IntroReferral: Submitted in House
- 2026-01-20 - IntroReferral: Submitted in House
- Latest action: 2026-01-20: Submitted in House

## Actions

- 2026-01-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-20 - IntroReferral: Submitted in House
- 2026-01-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-20",
    "latestAction": {
      "actionDate": "2026-01-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1010",
    "number": "1010",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Recognizing 2026 as \"The Year of The Power of Nurses\" in Celebration of the 130th Anniversary of the American Nurses Association.",
    "type": "HRES",
    "updateDate": "2026-01-22T15:25:55Z",
    "updateDateIncludingText": "2026-01-22T15:25:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-20",
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
      "actionDate": "2026-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-20",
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
          "date": "2026-01-20T17:02:30Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1010ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1010\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2026 Ms. Underwood submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing 2026 as The Year of The Power of Nurses in Celebration of the 130th Anniversary of the American Nurses Association.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes The Year of The Power of Nurses in recognition of the 130th Anniversary of the American Nurses Association; and\n**(2)**\nhonors the extraordinary contributions of nurses to the health, safety, and prosperity of the United States of America.",
      "versionDate": "2026-01-20",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-15",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S260)"
      },
      "number": "583",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution recognizing 2026 as \"The Year of The Power of Nurses\" in Celebration of the 130th Anniversary of the American Nurses Association.",
      "type": "SRES"
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
        "updateDate": "2026-01-22T15:25:55Z"
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
      "date": "2026-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1010ih.xml"
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
      "title": "Recognizing 2026 as \"The Year of The Power of Nurses\" in Celebration of the 130th Anniversary of the American Nurses Association.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:34Z"
    },
    {
      "title": "Recognizing 2026 as \"The Year of The Power of Nurses\" in Celebration of the 130th Anniversary of the American Nurses Association.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T09:05:25Z"
    }
  ]
}
```
