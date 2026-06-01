# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7145
- Title: To amend title XIX of the Social Security Act to establish a definition of essential health system in statute and for other related purposes.
- Congress: 119
- Bill type: HR
- Bill number: 7145
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-05-13T08:06:04Z
- Update date including text: 2026-05-13T08:06:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7145",
    "number": "7145",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000482",
        "district": "3",
        "firstName": "Lori",
        "fullName": "Rep. Trahan, Lori [D-MA-3]",
        "lastName": "Trahan",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "To amend title XIX of the Social Security Act to establish a definition of essential health system in statute and for other related purposes.",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:04Z",
    "updateDateIncludingText": "2026-05-13T08:06:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "LA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CO"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NY"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "MO"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "UT"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MO"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "AL"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7145ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7145\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mrs. Trahan (for herself, Mr. Valadao , Mr. Ciscomani , Mr. Carter of Louisiana , Mr. Veasey , and Mr. Soto ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to establish a definition of essential health system in statute and for other related purposes.\n#### 1. Establishing a definition of essential health system in statute\n##### (a)\n**(1) In general**\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended by adding at the end the following new subsection:\n(ll) Essential health system The term essential health system means a hospital\u2014 (1) (A) that is a subsection (d) hospital (as defined in section 1886(d)(1)(B)); (B) that is a non-Federal governmental or private nonprofit hospital; and (C) that met one of the following three criteria in at least two of the three most recent fiscal years, demonstrating the hospital provides a high-volume of care to Medicaid and other low-income patients: (i) Medicaid and low-income medicare criteria (I) The hospital had a Medicare disproportionate patient percentage of at least 35 percent (as defined in section 1886(d)(5)(F)(vi)). (ii) Uncompensated care criteria (I) The hospital had a Medicare disproportionate share hospital uncompensated care payment factor of 0.0005 or more (as defined in section 1886(r)(2)(C)). (iii) State-adjusted low-income care criteria (I) The hospital had a value for the criteria described in clause (i) or clause (ii) that is in the top 16th percentile for subsection (d) hospitals (as defined in section 1886(d)(1)(B)) in the state in which it is located. In determining whether a hospital meets at least one of the criteria specified in subparagraph (C), the Secretary shall utilize data published with the final rules revising the Medicare inpatient prospective payment systems for the three most recent fiscal years. (2) Period of designation The designation of an essential health system under paragraph (1) shall be effective for a period of 5 years, provided the hospital continues to meet the criteria in subparagraphs (A) and (B) in each year, and shall be subject to redesignation thereafter under paragraph (1) for five year periods thereafter. .\n##### (b) Essential health system designation and index\nSection 1900(b) of the Social Security Act ( 42 U.S.C. 1396(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (7) through (14) as paragraphs (8) through (15) respectively; and\n**(2)**\nby inserting after paragraph (6) the following:\n(7) Essential health system index (A) Not later than six months after the date of enactment and by August 1st in each year thereafter, MACPAC shall\u2014 (i) Prepare and submit to Congress a list of essential health systems that meet the criteria specified in section1905(ll), including hospitals newly meeting the criteria and those that were so designated in one of the previous four fiscal years; and (ii) Establish and publish essential health system index values for each hospital that is a subsection (d) hospital (as defined in section 1886(d)(1)(B)) in accordance with subparagraph (B). (B) In this subparagraph, the term essential health system index value is a computation of each hospital\u2019s percentile ranking for the most recent fiscal year for which data is available on the measures described in section1905(ll)(1)(C)(i) and (ii) compared to other subsection (d) hospitals in the: (i) same core-based statistical area (if applicable), (ii) same state, and (iii) nationally. (C) MACPAC shall report these values individually and shall also report a composite index value calculated as the average of the individual index values specified in subparagraph (B). .\n##### (c) MACPAC agenda\nSection 1900(b)(2)(A) of the Social Security Act ( 42 U.S.C. 1396(b)(2)(A) ) is amended\u2014\n**(1)**\nin clause (ii), by striking and at the end;\n**(2)**\nin clause (iii), by striking the period at the end and inserting ; and at the end; and\n**(3)**\nby adding at the end the following new clause:\n(iv) payment policies that use the criteria described in subparagraph (b)(7) to provide targeted support for essential health systems and ensure access to the essential community services that they provide. .",
      "versionDate": "2026-01-16",
      "versionType": "Introduced in House"
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
        "name": "Health",
        "updateDate": "2026-02-18T18:13:30Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7145ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to establish a definition of essential health system in statute and for other related purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T04:48:21Z"
    },
    {
      "title": "To amend title XIX of the Social Security Act to establish a definition of essential health system in statute and for other related purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T09:05:51Z"
    }
  ]
}
```
