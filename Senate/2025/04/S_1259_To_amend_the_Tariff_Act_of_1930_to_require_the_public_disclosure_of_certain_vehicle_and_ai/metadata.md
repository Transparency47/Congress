# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1259?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1259
- Title: Manifest Modernization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1259
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2025-12-05T22:54:32Z
- Update date including text: 2025-12-05T22:54:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1259",
    "number": "1259",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Manifest Modernization Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:54:32Z",
    "updateDateIncludingText": "2025-12-05T22:54:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-04-02T18:22:31Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "RI"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1259is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1259\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Cassidy (for himself, Mr. Whitehouse , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Tariff Act of 1930 to require the public disclosure of certain vehicle and aircraft manifest information.\n#### 1. Short title\nThis Act may be cited as the Manifest Modernization Act of 2025 .\n#### 2. Public disclosure of vehicle and aircraft manifest information\n##### (a) In general\nSection 431 of the Tariff Act of 1930 ( 19 U.S.C. 1431 ) is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) In general Each of the following shall have a manifest that complies with the requirements prescribed under subsection (d): (1) Every vessel required to make entry under section 434 or obtain clearance under section 60105 of title 46, United States Code. (2) Every vehicle arriving in the United States as described under section 433. (3) Every aircraft arriving in the United States as described under section 433. ; and\n**(2)**\nin subsection (c)(1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking subparagraph (2) and all that follows through public disclosure and inserting paragraph (2), when included in a vessel, vehicle, or aircraft manifest, the following information shall be available for public disclosure ;\n**(B)**\nin subparagraph (B), by inserting and each subheading of the Harmonized Tariff Schedule of the United States under which the cargo is classified before the period at the end;\n**(C)**\nin subparagraph (D), by striking vessel, aircraft, or carrier and inserting vessel, vehicle, or aircraft ; and\n**(D)**\nin subparagraph (G), by striking country of origin of the shipment and inserting country of origin of the cargo and the last country through which the cargo was transported by the vessel, vehicle, or aircraft .\n##### (b) Definition of aircraft\nSection 401 of the Tariff Act of 1930 ( 19 U.S.C. 1401 ) is amended by adding at the end the following:\n(u) Aircraft The term aircraft means a civil, military, or public contrivance invented, used, or designed to navigate, fly, or travel in the air. .\n##### (c) Applicability\nThe amendments made by subsections (a) and (b) shall apply with respect to each vessel, vehicle, and aircraft arriving in the United States on or after the date that is 30 days after the date of the enactment of this Act.",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-03",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2653",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Manifest Modernization Act of 2025",
      "type": "HR"
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-14T16:23:12Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1259is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Manifest Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Manifest Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Tariff Act of 1930 to require the public disclosure of certain vehicle and aircraft manifest information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:17Z"
    }
  ]
}
```
