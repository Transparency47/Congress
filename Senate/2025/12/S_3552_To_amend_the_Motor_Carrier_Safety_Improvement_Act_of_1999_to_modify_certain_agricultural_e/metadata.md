# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3552?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3552
- Title: HAULS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3552
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-20T15:38:43Z
- Update date including text: 2026-01-20T15:38:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3552",
    "number": "3552",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "HAULS Act of 2025",
    "type": "S",
    "updateDate": "2026-01-20T15:38:43Z",
    "updateDateIncludingText": "2026-01-20T15:38:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T23:33:41Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3552is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3552\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mrs. Fischer introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Motor Carrier Safety Improvement Act of 1999 to modify certain agricultural exemptions for hours of service requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Haulers of Agriculture and Livestock Safety Act of 2025 or the HAULS Act of 2025 .\n#### 2. Transportation of agricultural commodities and farm supplies\nSection 229 of the Motor Carrier Safety Improvement Act of 1999 ( 49 U.S.C. 31136 note; Public Law 106\u2013159 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking during planting and harvest periods, as determined by each State, ; and\n**(B)**\nby striking subparagraph (A) and inserting the following:\n(A) drivers transporting agricultural commodities within a 150 air-mile radius from\u2014 (i) the source of the agricultural commodities; or (ii) the destination of the agricultural commodities; ; and\n**(2)**\nin subsection (e)(8), by striking during the planting and harvesting seasons within each State, as determined by the State, and livestock feed at any time of the year and inserting and livestock feed .\n#### 3. Definition of agricultural commodity\n##### (a) In general\nSection 229(e) of the Motor Carrier Safety Improvement Act of 1999 ( 49 U.S.C. 31136 note; Public Law 106\u2013159 ) is amended by striking paragraph (7) and inserting the following:\n(7) Agricultural commodity The term agricultural commodity has the meaning given the term in section 395.2 of title 49, Code of Federal Regulations (or a successor regulation). .\n##### (b) Rulemaking\nNot later than 180 days after the date of enactment of this Act, the Secretary of Transportation shall revise the definition of the term agricultural commodity in section 395.2 of title 49, Code of Federal Regulations, to include\u2014\n**(1)**\nany nonprocessed product planted or harvested for food, feed, fuel, or fiber;\n**(2)**\n**(A)**\nany nonhuman living animal, including\u2014\n**(i)**\nfish;\n**(ii)**\ninsects; and\n**(iii)**\nlivestock (as defined in section 602 of the Emergency Livestock Feed Assistance Act of 1988 ( 7 U.S.C. 1471 )); and\n**(B)**\nthe nonprocessed products of any nonhuman living animal, including\u2014\n**(i)**\nmilk;\n**(ii)**\neggs; and\n**(iii)**\nhoney;\n**(3)**\nnonprocessed forestry, aquacultural, horticultural, and floricultural commodities;\n**(4)**\nfresh or minimally processed fruits and vegetables, including fruits and vegetables that are rinsed, cooled, cut, ripened, or otherwise minimally processed, as determined by the Secretary; and\n**(5)**\nanimal feed, including the ingredients of animal feed.",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-20T15:38:43Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3552is.xml"
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
      "title": "HAULS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T06:23:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HAULS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T06:23:42Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Haulers of Agriculture and Livestock Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T06:23:42Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Motor Carrier Safety Improvement Act of 1999 to modify certain agricultural exemptions for hours of service requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T06:18:53Z"
    }
  ]
}
```
