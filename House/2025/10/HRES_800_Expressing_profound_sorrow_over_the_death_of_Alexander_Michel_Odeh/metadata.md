# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/800?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/800
- Title: Expressing profound sorrow over the death of Alexander Michel Odeh.
- Congress: 119
- Bill type: HRES
- Bill number: 800
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2025-11-19T21:55:52Z
- Update date including text: 2025-11-19T21:55:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-10-10 - IntroReferral: Submitted in House
- 2025-10-10 - IntroReferral: Submitted in House
- Latest action: 2025-10-10: Submitted in House

## Actions

- 2025-10-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-10-10 - IntroReferral: Submitted in House
- 2025-10-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/800",
    "number": "800",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001110",
        "district": "46",
        "firstName": "J.",
        "fullName": "Rep. Correa, J. Luis [D-CA-46]",
        "lastName": "Correa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing profound sorrow over the death of Alexander Michel Odeh.",
    "type": "HRES",
    "updateDate": "2025-11-19T21:55:52Z",
    "updateDateIncludingText": "2025-11-19T21:55:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
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
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:31:15Z",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres800ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 800\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mr. Correa (for himself and Ms. Tlaib ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing profound sorrow over the death of Alexander Michel Odeh.\nThat\u2014\n**(1)**\nthe House of Representatives acknowledges with profound sorrow the death of Alexander Michel Odeh, a victim of domestic terrorism;\n**(2)**\nthe House of Representatives tenders its deep sympathy to the members of the family of the late Mr. Odeh and the American-Arab Anti-Discrimination Committee in their bereavement;\n**(3)**\nthe Clerk of the House of Representatives will communicate this resolution to the Senate and transmit a copy thereof to the family of the deceased; and\n**(4)**\nwhen the House of Representatives adjourns today, it adjourns as a further mark of respect to the memory of Mr. Odeh.",
      "versionDate": "2025-10-10",
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
        "updateDate": "2025-11-19T21:55:52Z"
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
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres800ih.xml"
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
      "title": "Expressing profound sorrow over the death of Alexander Michel Odeh.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T08:18:16Z"
    },
    {
      "title": "Expressing profound sorrow over the death of Alexander Michel Odeh.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-11T08:05:31Z"
    }
  ]
}
```
