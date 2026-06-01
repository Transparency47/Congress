# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3283?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3283
- Title: FARMER Act
- Congress: 119
- Bill type: HR
- Bill number: 3283
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2025-12-05T21:57:55Z
- Update date including text: 2025-12-05T21:57:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Agriculture.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3283",
    "number": "3283",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "FARMER Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:57:55Z",
    "updateDateIncludingText": "2025-12-05T21:57:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MN"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NE"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WI"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NE"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WA"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "TX"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-05-09",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3283ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3283\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mr. Finstad (for himself, Mrs. Fischbach , Mr. Smith of Nebraska , Mr. Van Orden , Mr. Bacon , Mr. Newhouse , and Mr. Jackson of Texas ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Crop Insurance Act to provide premium support for certain plans of crop insurance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Agriculture Risk Management Enhancement and Resilience Act or the FARMER Act .\n#### 2. Premium support for certain plans of crop insurance\nSection 508(e) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(e) ) is amended\u2014\n**(1)**\nby redesignating paragraph (8) as paragraph (9);\n**(2)**\nin paragraph (9) (as so redesignated) by striking and (7) and inserting (7), and (8) ; and\n**(3)**\nby inserting after paragraph (7) the following:\n(8) Premium support for certain plans of insurance Notwithstanding subparagraphs (F) and (G) of paragraph (2), in the case of an individual farm-based revenue protection or yield protection plan of insurance, when a producer elects such a plan of insurance based upon enterprise units or whole farm units, the Corporation shall pay a part of the premium as provided under those subparagraphs except that the applicable factor shall be\u2014 (A) 77 percent in the case of the coverage level described in paragraph (2)(F); and (B) 68 percent in the case of the coverage level described in paragraph (2)(G). .\n#### 3. Coverage level and premium subsidy under supplemental coverage option\n##### (a) Coverage level\nSection 508(c)(4)(C) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(c)(4)(C) ) is amended\u2014\n**(1)**\nin clause (ii), by striking 14 and inserting 10 ; and\n**(2)**\nin clause (iii)(I), by striking 86 and inserting 90 .\n##### (b) Premium subsidy\nSection 508(e)(2)(H)(i) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(e)(2)(H)(i) ) is amended by striking 65 and inserting 80 .\n#### 4. Study\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended by adding at the end the following:\n(20) Study on supplemental coverage option (A) In general The Corporation shall carry out a study, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out a study, to determine the feasibility of modifying the supplemental coverage option described in section 508(c)(4)(C) to provide coverage for counties larger than 1,400 square miles\u2014 (i) at a level smaller than county-wide; and (ii) at a level greater than individual coverage. (B) Report Not later than 1 year after the date of enactment of this paragraph, the Corporation shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that describes\u2014 (i) the results of the study carried out under subparagraph (A); and (ii) any recommendations with respect to those results. .",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1693",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FARMER Act of 2025",
      "type": "S"
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
        "updateDate": "2025-06-05T14:11:18Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3283ih.xml"
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
      "title": "FARMER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-18T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FARMER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Agriculture Risk Management Enhancement and Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Crop Insurance Act to provide premium support for certain plans of crop insurance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:33:30Z"
    }
  ]
}
```
