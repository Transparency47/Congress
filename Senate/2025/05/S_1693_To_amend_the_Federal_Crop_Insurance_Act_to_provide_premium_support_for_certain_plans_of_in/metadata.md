# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1693?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1693
- Title: FARMER Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1693
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-12-05T21:57:00Z
- Update date including text: 2025-12-05T21:57:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1693",
    "number": "1693",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "FARMER Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:57:00Z",
    "updateDateIncludingText": "2025-12-05T21:57:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T17:53:35Z",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "AR"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "KY"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "IA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MS"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "KS"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WV"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "IA"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NE"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "KS"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1693is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1693\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Hoeven (for himself, Mr. Boozman , Mr. McConnell , Ms. Ernst , Mrs. Hyde-Smith , Mr. Marshall , Mr. Justice , Mr. Grassley , Mrs. Fischer , and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Crop Insurance Act to provide premium support for certain plans of insurance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Agriculture Risk Management Enhancement and Resilience Act of 2025 or the FARMER Act of 2025 .\n#### 2. Premium support for certain plans of insurance\nSection 508(e) of the Federal Crop Insurance Act of 1938 ( 7 U.S.C. 1508(e) ) is amended\u2014\n**(1)**\nby redesignating paragraph (8) as paragraph (9);\n**(2)**\nin paragraph (9) (as so redesignated) by striking and (7) and inserting (7), and (8) ; and\n**(3)**\nby inserting after paragraph (7) the following:\n(8) Premium support for certain plans of insurance Notwithstanding subparagraphs (F) and (G) of paragraph (2), in the case of an individual farm-based revenue protection or yield protection plan of insurance, when a producer elects such a plan of insurance based upon enterprise units or whole farm units, the Corporation shall pay a part of the premium as provided under those subparagraphs except that the applicable factor shall be\u2014 (A) 77 percent in the case of the coverage level described in paragraph (2)(F); and (B) 68 percent in the case of the coverage level described in paragraph (2)(G). .\n#### 3. Coverage level and premium subsidy under supplemental coverage option\n##### (a) Coverage level\nSection 508(c)(4)(C) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(c)(4)(C) ) is amended\u2014\n**(1)**\nin clause (ii), by striking 14 and inserting 10 ; and\n**(2)**\nin clause (iii)(I), by striking 86 and inserting 90 .\n##### (b) Premium subsidy\nSection 508(e)(2)(H)(i) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(e)(2)(H)(i) ) is amended by striking 65 and inserting 80 .\n#### 4. Study\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended by adding at the end the following:\n(20) Study on supplemental coverage option (A) In general The Corporation shall carry out a study, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out a study, to determine the feasibility of modifying the supplemental coverage option described in section 508(c)(4)(C) to provide coverage for counties larger than 1,400 square miles\u2014 (i) at a level smaller than county-wide; and (ii) at a level greater than individual coverage. (B) Report Not later than 1 year after the date of enactment of this paragraph, the Corporation shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that describes\u2014 (i) the results of the study carried out under subparagraph (A); and (ii) any recommendations with respect to those results. .",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-08",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "3283",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FARMER Act",
      "type": "HR"
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
        "updateDate": "2025-06-05T14:12:10Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1693is.xml"
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
      "title": "FARMER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FARMER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Agriculture Risk Management Enhancement and Resilience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Crop Insurance Act to provide premium support for certain plans of insurance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-23T02:48:18Z"
    }
  ]
}
```
