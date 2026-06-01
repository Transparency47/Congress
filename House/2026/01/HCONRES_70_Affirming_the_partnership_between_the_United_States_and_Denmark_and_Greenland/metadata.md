# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/70?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/70
- Title: Affirming the partnership between the United States and Denmark and Greenland.
- Congress: 119
- Bill type: HCONRES
- Bill number: 70
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-02-05T09:06:21Z
- Update date including text: 2026-02-05T09:06:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-01-15 - IntroReferral: Submitted in House
- Latest action: 2026-01-15: Submitted in House

## Actions

- 2026-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-01-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/70",
    "number": "70",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Affirming the partnership between the United States and Denmark and Greenland.",
    "type": "HCONRES",
    "updateDate": "2026-02-05T09:06:21Z",
    "updateDateIncludingText": "2026-02-05T09:06:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "NE"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres70ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 70\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Khanna (for himself and Mr. Bacon ) submitted the following concurrent resolution; which was referred to the Committee on Foreign Affairs\nCONCURRENT RESOLUTION\nAffirming the partnership between the United States and Denmark and Greenland.\nThat it is the sense of Congress that\u2014\n**(1)**\nthe United States Government affirms its respect for the sovereignty of the Kingdom of Denmark, including Greenland, consistent with longstanding treaty commitments, including the North Atlantic Treaty;\n**(2)**\nany change in the status of Greenland, or any use of United States military force involving Greenland, must comply with treaty obligations and is subject to authorization by Congress;\n**(3)**\nthe United States should continue to strengthen diplomatic, economic, and security cooperation with Denmark and Greenland through partnership, consent, and alliance-based engagement; and\n**(4)**\nthe Arctic remains the most secure when the United States leads through cooperation with allies rather than coercion.",
      "versionDate": "2026-01-15",
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
        "text": "Referred to the Committee on Foreign Relations. (text: CR S261)"
      },
      "number": "26",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A concurrent resolution affirming the partnership between the United States and Denmark and Greenland.",
      "type": "SCONRES"
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
        "name": "International Affairs",
        "updateDate": "2026-01-16T19:01:41Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres70ih.xml"
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
      "title": "Affirming the partnership between the United States and Denmark and Greenland.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T09:18:41Z"
    },
    {
      "title": "Affirming the partnership between the United States and Denmark and Greenland.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T09:06:27Z"
    }
  ]
}
```
