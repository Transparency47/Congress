# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6384?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6384
- Title: Defense Health Agency Prevention Services Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 6384
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-01-06T19:39:43Z
- Update date including text: 2026-01-06T19:39:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6384",
    "number": "6384",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001123",
        "district": "31",
        "firstName": "Gilbert",
        "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
        "lastName": "Cisneros",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Defense Health Agency Prevention Services Enhancement Act",
    "type": "HR",
    "updateDate": "2026-01-06T19:39:43Z",
    "updateDateIncludingText": "2026-01-06T19:39:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6384ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6384\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Cisneros introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of Defense to brief the Armed Services Committee of the House of Representatives on the feasibility of consolidating covered prevention services into a single facility for each military installation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Defense Health Agency Prevention Services Enhancement Act .\n#### 2. Briefing on consolidating covered prevention services\n##### (a) Briefing required\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense, in consultation with each Secretary of a military department, shall provide to the Armed Services Committee of the House of Representatives a briefing on the feasibility of consolidating covered prevention services into a single facility for each military installation (as defined in section 2801 of title 10, United States Code) located in the United States.\n##### (b) Content\nThe briefing required by subsection (a) shall include the following:\n**(1)**\nAn assessment of the feasibility and advisability of consolidating covered prevention services into a single facility for each military installation.\n**(2)**\nA cost estimate for such consolidation.\n**(3)**\nAn evaluation of the efforts of each Secretary of a military department to consolidate covered prevention services into a single facility for each military installation under the jurisdiction of such Secretary and successes and lessons learned from such efforts.\n##### (c) Covered prevention services defined\nIn this section, the term covered prevention services means services offered by the Secretary of Defense or a Secretary of a military department to a member of the Armed Forces or a dependent of such member relating to\u2014\n**(1)**\npreventing sexual assault, suicide, harassment, domestic violence; and\n**(2)**\nother related community-based prevention services.",
      "versionDate": "2025-12-03",
      "versionType": "Introduced in House"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T19:39:43Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6384ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Defense to brief the Armed Services Committee of the House of Representatives on the feasibility of consolidating covered prevention services into a single facility for each military installation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T12:39:50Z"
    },
    {
      "title": "Defense Health Agency Prevention Services Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defense Health Agency Prevention Services Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T12:23:18Z"
    }
  ]
}
```
