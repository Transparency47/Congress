# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1972
- Title: Bioweapon Prevention Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1972
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2025-07-18T13:07:07Z
- Update date including text: 2025-07-18T13:07:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1972",
    "number": "1972",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Bioweapon Prevention Act of 2025",
    "type": "S",
    "updateDate": "2025-07-18T13:07:07Z",
    "updateDateIncludingText": "2025-07-18T13:07:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T17:44:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1972is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1972\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo prohibit Federal funding for research centers and laboratories in which nationals of countries of concern conduct agricultural research.\n#### 1. Short title\nThis Act may be cited as the Bioweapon Prevention Act of 2025 .\n#### 2. Prohibition on funding for research centers and laboratories in which nationals of countries of concern conduct agricultural research\n##### (a) In general\nNo Federal funding shall be available to any research center or laboratory in which a national of a country of concern conducts agricultural research.\n##### (b) Definition of country of concern\nIn this section, the term country of concern means\u2014\n**(1)**\nthe Republic of Cuba;\n**(2)**\nthe Islamic Republic of Iran;\n**(3)**\nthe Russian Federation;\n**(4)**\nthe People's Republic of China, including the Special Administrative Region of Hong Kong and the Special Administrative Region of Macau;\n**(5)**\nthe Bolivarian Republic of Venezuela; and\n**(6)**\nthe Democratic People's Republic of Korea.",
      "versionDate": "2025-06-05",
      "versionType": "Introduced in Senate"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-18T13:07:07Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1972is.xml"
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
      "title": "Bioweapon Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Bioweapon Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit Federal funding for research centers and laboratories in which nationals of countries of concern conduct agricultural research.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T05:33:20Z"
    }
  ]
}
```
