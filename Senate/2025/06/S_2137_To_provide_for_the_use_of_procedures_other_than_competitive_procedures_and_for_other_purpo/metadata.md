# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2137?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2137
- Title: Expedited Delivery Act
- Congress: 119
- Bill type: S
- Bill number: 2137
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2025-07-17T15:44:05Z
- Update date including text: 2025-07-17T15:44:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2137",
    "number": "2137",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "Expedited Delivery Act",
    "type": "S",
    "updateDate": "2025-07-17T15:44:05Z",
    "updateDateIncludingText": "2025-07-17T15:44:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
          "date": "2025-06-18T19:29:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2137is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2137\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Sheehy introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide for the use of procedures other than competitive procedures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expedited Delivery Act .\n#### 2. Use of procedures other than competitive procedures\nSection 3204 of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (2) through (7) as paragraphs (3) through (8), respectively; or\n**(B)**\nby inserting after paragraph (1), the following:\n(2) market research indicates that the property or service needed by the agency provides differentiated capabilities, accelerated delivery schedules, or continuous improvements; .\n**(2)**\nby striking subsections (b), (c), (d), and (g);\n**(3)**\nby redesignating subsections (e) and (f) as subsections (b) and (c), respectively;\n**(4)**\nin subsection (b), as redesignated by paragraph (3)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by striking and certifies the accuracy and completeness of the justification and inserting in a manner that provides an accurate and complete justification ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby striking $10,000,000 each place it appears and inserting $100,000,000 ;\n**(II)**\nin clause (i), by striking $500,000 and inserting $10,000,000 ; and\n**(III)**\nin clause (iii), by striking $75,000,000 and inserting $500,000,000 ;\n**(B)**\nin paragraph (3), by striking by subsection (a)(2) and inserting by paragraphs (3) or (4)(A) of subsection (a) ; and\n**(C)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (C), by striking subsection (a)(7) and inserting subsection (a)(8) ; and\n**(ii)**\nin subparagraph (E), by striking subsection (a)(4) and inserting subsection (a)(5) ; and\n**(5)**\nin paragraph (1) of subsection (c), as redesignated by paragraph (3)\u2014\n**(A)**\nin subparagraph (A), by striking subsection (e)(1) and inserting subsection (b)(1) ; and\n**(B)**\nin subparagraph (B), by striking subsection (a)(2) and inserting subsection (a)(3) ;",
      "versionDate": "2025-06-18",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-17T15:44:05Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2137is.xml"
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
      "title": "Expedited Delivery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expedited Delivery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the use of procedures other than competitive procedures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:19:07Z"
    }
  ]
}
```
