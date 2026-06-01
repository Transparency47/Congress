# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2769?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2769
- Title: Safeguarding Personal Information Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2769
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2025-09-23T15:18:10Z
- Update date including text: 2025-09-23T15:18:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2769",
    "number": "2769",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Safeguarding Personal Information Act of 2025",
    "type": "S",
    "updateDate": "2025-09-23T15:18:10Z",
    "updateDateIncludingText": "2025-09-23T15:18:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T15:05:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2769is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2769\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Paul introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo repeal title II of the REAL ID Act of 2005 in order to safeguard civil liberties and individual privacy.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Personal Information Act of 2025 .\n#### 2. Repeal of certain requirements for documents accepted for Federal identification purposes\nTitle II of the REAL ID Act of 2005 ( 49 U.S.C. 30301 note; division B of Public Law 109\u201313 ) is repealed.\n#### 3. Conforming amendments\n##### (a) Benefits for Afghanistan nationals\nSection 2502(b)(3) of the Afghanistan Supplemental Appropriations Act, 2022 ( 8 U.S.C. 1101 note) is amended by striking under section 202 of the REAL ID Act of 2005 (division B of Public Law 109\u201313 ; 49 U.S.C. 30301 note), notwithstanding subsection (c)(2)(B) of such Act .\n##### (b) Grants to States\nSection 475(5)(I) of the Social Security Act( 42 U.S.C. 675(5)(I) ) is amended by striking in accordance with the requirements of section 202 of the REAL ID Act of 2005 .",
      "versionDate": "2025-09-11",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-23T15:18:10Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2769is.xml"
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
      "title": "Safeguarding Personal Information Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-23T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safeguarding Personal Information Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-23T04:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal title II of the REAL ID Act of 2005 in order to safeguard civil liberties and individual privacy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-23T04:18:19Z"
    }
  ]
}
```
