# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/645?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/645
- Title: Original Resolution Honoring John Brown
- Congress: 119
- Bill type: HRES
- Bill number: 645
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2025-09-18T19:40:44Z
- Update date including text: 2025-09-18T19:40:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-08-08 - IntroReferral: Submitted in House
- 2025-08-08 - IntroReferral: Submitted in House
- Latest action: 2025-08-08: Submitted in House

## Actions

- 2025-08-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-08-08 - IntroReferral: Submitted in House
- 2025-08-08 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/645",
    "number": "645",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Original Resolution Honoring John Brown",
    "type": "HRES",
    "updateDate": "2025-09-18T19:40:44Z",
    "updateDateIncludingText": "2025-09-18T19:40:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:31:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres645ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 645\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Green of Texas submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring John Brown\u2019s relentless endeavors in his pursuit of liberty for all human beings, his unyielding opposition to the institution of slavery, and his significant role in the abolition of this monstrous crime against humanity.\n#### 1. Short title\nThis resolution may be cited as the Original Resolution Honoring John Brown .\n#### 2. Honoring John Brown\nThat the House of Representatives\u2014\n**(1)**\nacknowledges and honors John Brown\u2019s relentless endeavors in his pursuit of liberty for all human beings, his unyielding opposition to the institution of slavery, and his significant role in the abolition of this monstrous crime against humanity; and\n**(2)**\nencourages every American to reflect on our Nation\u2019s diverse and complex history as we strive for a more perfect Union, one that is truly inclusive and upholds the majestic, inalienable rights of life, liberty, and the pursuit of happiness for all.",
      "versionDate": "2025-08-08",
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
        "updateDate": "2025-09-18T19:40:44Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres645ih.xml"
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
      "title": "Original Resolution Honoring John Brown",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Original Resolution Honoring John Brown",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honoring John Brown's relentless endeavors in his pursuit of liberty for all human beings, his unyielding opposition to the institution of slavery, and his significant role in the abolition of this monstrous crime against humanity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T08:19:10Z"
    }
  ]
}
```
