# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1024?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1024
- Title: Expressing support for the designation of January 2026 as "National Human Trafficking Prevention Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1024
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-02-03T15:48:36Z
- Update date including text: 2026-02-03T15:48:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-30 - IntroReferral: Submitted in House
- 2026-01-30 - IntroReferral: Submitted in House
- Latest action: 2026-01-30: Submitted in House

## Actions

- 2026-01-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-30 - IntroReferral: Submitted in House
- 2026-01-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1024",
    "number": "1024",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001239",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. McGuire, John J. [R-VA-5]",
        "lastName": "McGuire",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Expressing support for the designation of January 2026 as \"National Human Trafficking Prevention Month\".",
    "type": "HRES",
    "updateDate": "2026-02-03T15:48:36Z",
    "updateDateIncludingText": "2026-02-03T15:48:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
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
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:33:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1024ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1024\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. McGuire submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nExpressing support for the designation of January 2026 as National Human Trafficking Prevention Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Human Trafficking Prevention Month and affirms the Nation\u2019s commitment to ending all forms of human trafficking;\n**(2)**\nencourages State, local, and Tribal Governments, faith-based institutions, community organizations, and private sector partners to engage in prevention efforts, victim support, and public education tailored to local needs;\n**(3)**\nurges strong law enforcement action, including secure borders, effective immigration enforcement, and prosecution of traffickers to the fullest extent of the law;\n**(4)**\nrecognizes the indispensable role of survivors, families, faith leaders, and community advocates in shaping effective, compassionate, and accountable responses to trafficking; and\n**(5)**\nencourages all Americans to remain vigilant, learn the indicators of trafficking, and report suspicious activity promptly.",
      "versionDate": "2026-01-30",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-03T15:48:36Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1024ih.xml"
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
      "title": "Expressing support for the designation of January 2026 as \"National Human Trafficking Prevention Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-02T22:03:26Z"
    },
    {
      "title": "Expressing support for the designation of January 2026 as \"National Human Trafficking Prevention Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-31T09:05:37Z"
    }
  ]
}
```
