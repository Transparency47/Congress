# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/26?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/26
- Title: A concurrent resolution affirming the partnership between the United States and Denmark and Greenland.
- Congress: 119
- Bill type: SCONRES
- Bill number: 26
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-01-21T08:03:42Z
- Update date including text: 2026-01-21T08:03:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S261)
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S261)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/26",
    "number": "26",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "A concurrent resolution affirming the partnership between the United States and Denmark and Greenland.",
    "type": "SCONRES",
    "updateDate": "2026-01-21T08:03:42Z",
    "updateDateIncludingText": "2026-01-21T08:03:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S261)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T15:58:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sconres/BILLS-119sconres26is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. CON. RES. 26\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. Gallego (for himself and Ms. Murkowski ) submitted the following concurrent resolution; which was referred to the Committee on Foreign Relations\nCONCURRENT RESOLUTION\nAffirming the partnership between the United States and Denmark and Greenland.\nThat it is the sense of Congress that\u2014\n**(1)**\nthe United States Government affirms its respect for the sovereignty of the Kingdom of Denmark, including Greenland, consistent with longstanding treaty commitments, including the North Atlantic Treaty;\n**(2)**\nany change in the status of Greenland, or any use of United States military force involving Greenland, must comply with treaty obligations and is subject to authorization by Congress;\n**(3)**\nthe United States should continue to strengthen diplomatic, economic, and security cooperation with Denmark and Greenland through partnership, consent, and alliance-based engagement; and\n**(4)**\nthe Arctic remains the most secure when the United States leads through cooperation with allies rather than coercion.",
      "versionDate": "2026-01-15",
      "versionType": "IS"
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
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "70",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Affirming the partnership between the United States and Denmark and Greenland.",
      "type": "HCONRES"
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
        "updateDate": "2026-01-20T15:46:23Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sconres/BILLS-119sconres26is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A concurrent resolution affirming the partnership between the United States and Denmark and Greenland.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T08:03:42Z"
    },
    {
      "title": "A concurrent resolution affirming the partnership between the United States and Denmark and Greenland.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T11:56:15Z"
    }
  ]
}
```
