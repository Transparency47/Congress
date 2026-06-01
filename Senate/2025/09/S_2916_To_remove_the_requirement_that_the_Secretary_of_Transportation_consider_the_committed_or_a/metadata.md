# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2916?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2916
- Title: Long-Distance Corridor Relief Act
- Congress: 119
- Bill type: S
- Bill number: 2916
- Origin chamber: Senate
- Introduced date: 2025-09-19
- Update date: 2025-12-16T17:40:16Z
- Update date including text: 2025-12-16T17:40:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in Senate
- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-09-19: Introduced in Senate

## Actions

- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2916",
    "number": "2916",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Long-Distance Corridor Relief Act",
    "type": "S",
    "updateDate": "2025-12-16T17:40:16Z",
    "updateDateIncludingText": "2025-12-16T17:40:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T16:45:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2916is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2916\nIN THE SENATE OF THE UNITED STATES\nSeptember 19 (legislative day, September 16), 2025 Mr. Sheehy introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo remove the requirement that the Secretary of Transportation consider the committed or anticipated non-Federal funding for long distance intercity passenger rail routes under the Corridor Identification and Development Program.\n#### 1. Short title\nThis Act may be cited as the Long-Distance Corridor Relief Act .\n#### 2. Modification of consideration requirement of non-Federal funding for corridor selection\nSection 25101(c) of title 49, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraphs (1) through (14) as subparagraphs (A) through (N), respectively, and indenting such subparagraphs, as so redesignated, 2 ems to the right;\n**(2)**\nin the matter preceding subparagraph (A), as so redesignated, by striking In selecting and inserting the following:\n(1) In general In selecting .\n**(3)**\nin subparagraph (F), as so redesignated, by striking committed or and by inserting except as provided in paragraph (2), committed or ; and\n**(4)**\nby adding at the end the following:\n(2) Exception for long-distance route corridor For the purposes of this subsection, the Secretary shall not consider committed or anticipated non-Federal funding for operating or capital costs for any intercity passenger rail corridor on a long-distance route. .",
      "versionDate": "2025-09-19",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-16T17:40:15Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2916is.xml"
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
      "title": "Long-Distance Corridor Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-09T04:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Long-Distance Corridor Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-09T04:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to remove the requirement that the Secretary of Transportation consider the committed or anticipated non-Federal funding for long distance intercity passenger rail routes under the Corridor Identification and Development Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-09T04:48:17Z"
    }
  ]
}
```
