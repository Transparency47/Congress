# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2653?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2653
- Title: Manifest Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2653
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-05-21T08:08:05Z
- Update date including text: 2026-05-21T08:08:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2653",
    "number": "2653",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001183",
        "district": "1",
        "firstName": "David",
        "fullName": "Rep. Schweikert, David [R-AZ-1]",
        "lastName": "Schweikert",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Manifest Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:05Z",
    "updateDateIncludingText": "2026-05-21T08:08:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:01:25Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "TX"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "MI"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "TX"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "WV"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2653ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2653\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Schweikert (for himself, Mr. Doggett , Mr. Moolenaar , and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Tariff Act of 1930 to require the public disclosure of certain vehicle and aircraft manifest information.\n#### 1. Short title\nThis Act may be cited as the Manifest Modernization Act of 2025 .\n#### 2. Public disclosure of vehicle and aircraft manifest information\n##### (a) In general\nSection 431 of the Tariff Act of 1930 ( 19 U.S.C. 1431 ) is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) In general Each of the following shall have a manifest that complies with the requirements prescribed under subsection (d): (1) Every vessel required to make entry under section 434 or obtain clearance under section 60105 of title 46, United States Code. (2) Every vehicle arriving in the United States as described under section 433. (3) Every aircraft arriving in the United States as described under section 433. ; and\n**(2)**\nin subsection (c)(1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking subparagraph (2) and all that follows through public disclosure and inserting paragraph (2), when included in a vessel, vehicle, or aircraft manifest, the following information shall be available for public disclosure ;\n**(B)**\nin subparagraph (B), by inserting and each subheading of the Harmonized Tariff Schedule of the United States under which the cargo is classified before the period at the end;\n**(C)**\nin subparagraph (D), by striking vessel, aircraft, or carrier and inserting vessel, vehicle, or aircraft ; and\n**(D)**\nin subparagraph (G), by striking country of origin of the shipment and inserting country of origin of the cargo and the last country through which the cargo was transported by the vessel, vehicle, or aircraft .\n##### (b) Definition of aircraft\nSection 401 of the Tariff Act of 1930 ( 19 U.S.C. 1401 ) is amended by adding at the end the following:\n(u) Aircraft The term aircraft means a civil, military, or public contrivance invented, used, or designed to navigate, fly, or travel in the air. .\n##### (c) Applicability\nThe amendments made by subsections (a) and (b) shall apply with respect to each vessel, vehicle, and aircraft arriving in the United States on or after the date that is 30 days after the date of the enactment of this Act.",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-04-02",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1259",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Manifest Modernization Act of 2025",
      "type": "S"
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
        "updateDate": "2025-05-14T16:24:36Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2653ih.xml"
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
      "title": "Manifest Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Manifest Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Tariff Act of 1930 to require the public disclosure of certain vehicle and aircraft manifest information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:21Z"
    }
  ]
}
```
