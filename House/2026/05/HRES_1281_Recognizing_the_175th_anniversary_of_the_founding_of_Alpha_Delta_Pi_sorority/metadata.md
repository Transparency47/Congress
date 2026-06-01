# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1281?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1281
- Title: Recognizing the 175th anniversary of the founding of Alpha Delta Pi sorority.
- Congress: 119
- Bill type: HRES
- Bill number: 1281
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-29T14:59:29Z
- Update date including text: 2026-05-29T14:59:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-13 - IntroReferral: Submitted in House
- Latest action: 2026-05-13: Submitted in House

## Actions

- 2026-05-13 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-13 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1281",
    "number": "1281",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "F000450",
        "district": "5",
        "firstName": "Virginia",
        "fullName": "Rep. Foxx, Virginia [R-NC-5]",
        "lastName": "Foxx",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Recognizing the 175th anniversary of the founding of Alpha Delta Pi sorority.",
    "type": "HRES",
    "updateDate": "2026-05-29T14:59:29Z",
    "updateDateIncludingText": "2026-05-29T14:59:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
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
          "date": "2026-05-13T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1281ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1281\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2026 Ms. Foxx (for herself and Ms. Lee of Florida ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nRecognizing the 175th anniversary of the founding of Alpha Delta Pi sorority.\nThat the House of Representatives\u2014\n**(1)**\ncongratulates Alpha Delta Pi sorority on the occasion of its 175th anniversary;\n**(2)**\nacknowledges the contributions of Alpha Delta Pi members to education, science and technology, the arts, athletics, government, the military, business, and community service; and\n**(3)**\nrecognizes the members of Alpha Delta Pi sorority for their lifelong commitment to personal growth, friendship, and community enrichment.",
      "versionDate": "2026-05-13",
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
        "actionDate": "2026-05-14",
        "text": "Referred to the Committee on the Judiciary. (text: CR S2308-2309)"
      },
      "number": "731",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution recognizing the 175th anniversary of the founding of Alpha Delta Pi Sorority.",
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
        "name": "Education",
        "updateDate": "2026-05-27T14:01:17Z"
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
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1281ih.xml"
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
      "title": "Recognizing the 175th anniversary of the founding of Alpha Delta Pi sorority.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T08:18:30Z"
    },
    {
      "title": "Recognizing the 175th anniversary of the founding of Alpha Delta Pi sorority.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T08:07:59Z"
    }
  ]
}
```
