# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/949?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/949
- Title: Expressing support for the designation of the first Saturday in May as "National Lowrider Day".
- Congress: 119
- Bill type: HRES
- Bill number: 949
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-04-29T08:07:24Z
- Update date including text: 2026-04-29T08:07:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-12 - IntroReferral: Submitted in House
- 2025-12-12 - IntroReferral: Submitted in House
- Latest action: 2025-12-12: Submitted in House

## Actions

- 2025-12-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-12 - IntroReferral: Submitted in House
- 2025-12-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/949",
    "number": "949",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Expressing support for the designation of the first Saturday in May as \"National Lowrider Day\".",
    "type": "HRES",
    "updateDate": "2026-04-29T08:07:24Z",
    "updateDateIncludingText": "2026-04-29T08:07:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "CA"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "NV"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "NM"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "WA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres949ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 949\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Ms. Leger Fernandez (for herself, Mrs. Torres of California , Ms. Friedman , Mr. Correa , Ms. Rivas , Mr. Horsford , and Ms. Stansbury ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of the first Saturday in May as National Lowrider Day .\nThat the House of Representatives\u2014\n**(1)**\nrecognizes and celebrates lowrider culture as an integral part of the historical and cultural fabric of the United States;\n**(2)**\nhonors the contributions of lowrider builders, artists, families, and clubs who have preserved and promoted the lowriding tradition for generations;\n**(3)**\nrecognizes the importance of lowrider culture as a method of community building;\n**(4)**\nacknowledges the challenges faced by the lowrider community, including discrimination and criminalization; and\n**(5)**\ncalls upon local, State, and Federal entities to support public events and educational programs that honor lowrider culture and heritage.",
      "versionDate": "2025-12-12",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-12-15T16:43:43Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres949ih.xml"
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
      "title": "Expressing support for the designation of the first Saturday in May as \"National Lowrider Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T10:03:26Z"
    },
    {
      "title": "Expressing support for the designation of the first Saturday in May as \"National Lowrider Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T09:06:55Z"
    }
  ]
}
```
