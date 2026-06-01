# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1209?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1209
- Title: American Prairie Conservation Act
- Congress: 119
- Bill type: S
- Bill number: 1209
- Origin chamber: Senate
- Introduced date: 2025-03-31
- Update date: 2025-05-06T20:22:35Z
- Update date including text: 2025-05-06T20:22:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in Senate
- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1926)
- Latest action: 2025-03-31: Introduced in Senate

## Actions

- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1926)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1209",
    "number": "1209",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "American Prairie Conservation Act",
    "type": "S",
    "updateDate": "2025-05-06T20:22:35Z",
    "updateDateIncludingText": "2025-05-06T20:22:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1926)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T21:34:58Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1209is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1209\nIN THE SENATE OF THE UNITED STATES\nMarch 31, 2025 Mr. Thune (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Crop Insurance Act and the Federal Agriculture Improvement and Reform Act of 1996 to make the native sod provisions applicable to the United States and to modify those provisions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Prairie Conservation Act .\n#### 2. Crop production on native sod\n##### (a) Federal crop insurance\nSection 508(o) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(o) ) is amended by striking paragraph (3) and inserting the following:\n(3) Native sod conversion certification (A) Certification As a condition on the receipt of benefits under this subtitle, a producer that has tilled native sod acreage for the production of an insurable crop as described in paragraph (2)(A) shall certify that acreage to the Secretary using\u2014 (i) an acreage report form of the Farm Service Agency (FSA\u2013578 or any successor form); and (ii) 1 or more maps. (B) Corrections Beginning on the date on which a producer submits a certification under subparagraph (A), as soon as practicable after the producer discovers a change in tilled native sod acreage described in that subparagraph, the producer shall submit to the Secretary any appropriate corrections to a form or map described in clause (i) or (ii) of that subparagraph. (C) Annual reports Not later than January 1, 2026, and each January 1 thereafter through January 1, 2030, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that describes the tilled native sod acreage that has been certified under subparagraph (A) in each county and State as of the date of submission of the report. .\n##### (b) Noninsured crop disaster assistance\nSection 196(a)(4) of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333(a)(4) ) is amended by striking subparagraph (C) and inserting the following:\n(C) Native sod conversion certification (i) Certification As a condition on the receipt of benefits under this section, a producer that has tilled native sod acreage for the production of an insurable crop as described in subparagraph (B)(i) shall certify that acreage to the Secretary using\u2014 (I) an acreage report form of the Farm Service Agency (FSA\u2013578 or any successor form); and (II) 1 or more maps. (ii) Corrections Beginning on the date on which a producer submits a certification under clause (i), as soon as practicable after the producer discovers a change in tilled native sod acreage described in that clause, the producer shall submit to the Secretary any appropriate corrections to a form or map described in subclause (I) or (II) of that clause. (iii) Annual reports Not later than January 1, 2026, and each January 1 thereafter through January 1, 2030, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that describes the tilled native sod acreage that has been certified under clause (i) in each county and State as of the date of submission of the report. .",
      "versionDate": "2025-03-31",
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
        "updateDate": "2025-05-06T20:22:35Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1209is.xml"
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
      "title": "American Prairie Conservation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Prairie Conservation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Crop Insurance Act and the Federal Agriculture Improvement and Reform Act of 1996 to make the native sod provisions applicable to the United States and to modify those provisions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:21Z"
    }
  ]
}
```
