# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7098?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7098
- Title: Homeland Threat Response Act
- Congress: 119
- Bill type: HR
- Bill number: 7098
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-02-05T16:31:39Z
- Update date including text: 2026-02-05T16:31:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7098",
    "number": "7098",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000594",
        "district": "23",
        "firstName": "Tony",
        "fullName": "Rep. Gonzales, Tony [R-TX-23]",
        "lastName": "Gonzales",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Homeland Threat Response Act",
    "type": "HR",
    "updateDate": "2026-02-05T16:31:39Z",
    "updateDateIncludingText": "2026-02-05T16:31:39Z"
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
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7098ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7098\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Tony Gonzales of Texas introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Homeland Security Act of 2002 to authorize the deployment and assistance of CBP relating to investigations of certain violent acts, shootings, and mass killings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Homeland Threat Response Act .\n#### 2. Deployment and assistance of CBP relating to investigations of certain violent acts, shootings, and mass killings\nParagraph (1) of section 875(d) of the Homeland Security Act of 2002 ( 6 U.S.C. 455(d) ) is amended\u2014\n**(1)**\nby striking or United States Immigration and Customs Enforcement and inserting , U.S. Immigration and Customs Enforcement, or U.S. Customs and Border Protection ; and\n**(2)**\ninserting response, threat mitigation, resolution, and before investigation .",
      "versionDate": "2026-01-15",
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
        "name": "Immigration",
        "updateDate": "2026-02-05T16:31:39Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7098ih.xml"
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
      "title": "To amend the Homeland Security Act of 2002 to authorize the deployment and assistance of CBP relating to investigations of certain violent acts, shootings, and mass killings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:43Z"
    },
    {
      "title": "Homeland Threat Response Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Homeland Threat Response Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```
