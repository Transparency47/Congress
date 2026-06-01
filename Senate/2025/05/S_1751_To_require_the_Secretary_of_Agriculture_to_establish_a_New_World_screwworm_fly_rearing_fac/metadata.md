# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1751?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1751
- Title: STOP Screwworms Act
- Congress: 119
- Bill type: S
- Bill number: 1751
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2025-12-05T22:54:00Z
- Update date including text: 2025-12-05T22:54:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1751",
    "number": "1751",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "STOP Screwworms Act",
    "type": "S",
    "updateDate": "2025-12-05T22:54:00Z",
    "updateDateIncludingText": "2025-12-05T22:54:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T15:52:28Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NM"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "TX"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NM"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MS"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1751is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1751\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Cornyn (for himself, Mr. Luj\u00e1n , Mr. Cruz , Mr. Heinrich , and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo require the Secretary of Agriculture to establish a New World screwworm fly rearing facility, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Tactics to Obstruct the Population of Screwworms Act or the STOP Screwworms Act .\n#### 2. New World screwworm fly rearing facility\nThe Animal Health Protection Act ( 7 U.S.C. 8301 et seq. ) is amended by inserting after section 10409A ( 7 U.S.C. 8308a ) the following:\n10409B. New World screwworm fly rearing facility (a) In general Not later than 180 days after the date of enactment of this section, the Secretary shall begin construction on 1 or more modular New World screwworm fly rearing facilities in eligible areas described in subsection (b). Such a facility shall, in addition to providing for the rearing of sterile New World screwworm flies, provide for the dispersal of such flies to areas at risk of New World screwworm fly infestation. (b) Eligible area described An eligible area described in this subsection is an area of a State that the Secretary determines to be\u2014 (1) at risk of New World screwworm fly infestation due to the migratory pattern of confirmed detections of New World screwworm flies; and (2) suitable for dispersal of sterile New World screwworm flies reared at a New World screwworm fly rearing facility established under this section to additional areas at risk of New World screwworm fly infestation. (c) Report Not later than 1 year after the date of enactment of this section, and annually thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate, and make publicly available on the website of the Department of Agriculture, a report that includes\u2014 (1) an analysis of the current threat posed to agriculture in the United States by New World screwworm flies; and (2) a description of\u2014 (A) the efforts being taken by the Secretary to combat New World screwworm fly migration, including construction and operation of the facilities described in subsection (a); and (B) the effectiveness of such efforts. (d) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $300,000,000, to remain available until expended. .",
      "versionDate": "2025-05-14",
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
        "actionDate": "2025-05-14",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "3392",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STOP Screwworms Act",
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
        "updateDate": "2025-06-05T14:23:35Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1751is.xml"
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
      "title": "STOP Screwworms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STOP Screwworms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Tactics to Obstruct the Population of Screwworms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture to establish a New World screwworm fly rearing facility, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:26Z"
    }
  ]
}
```
