# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2117?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2117
- Title: Crop Insurance for Future Farmers Act
- Congress: 119
- Bill type: HR
- Bill number: 2117
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-08-09T08:05:38Z
- Update date including text: 2025-08-09T08:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2117",
    "number": "2117",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Crop Insurance for Future Farmers Act",
    "type": "HR",
    "updateDate": "2025-08-09T08:05:38Z",
    "updateDateIncludingText": "2025-08-09T08:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T13:13:20Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MN"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "MN"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "IA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "IL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "NE"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "IA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NC"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "MI"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "IL"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "MD"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2117ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2117\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Feenstra (for himself and Ms. Craig ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Crop Insurance Act to promote crop insurance support for beginning farmers and ranchers and veteran farmers and ranchers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Crop Insurance for Future Farmers Act .\n#### 2. Crop insurance support for beginning farmers and ranchers and veteran farmers and ranchers\n##### (a) Definition of beginning farmer or rancher\nSection 502(b)(3) of the Federal Crop Insurance Act ( 7 U.S.C. 1502(b)(3) ) is amended by striking 5 crop years and inserting 10 crop years .\n##### (b) Definition of veteran farmers and ranchers\nSection 502(b)(14)(B) of the Federal Crop Insurance Act ( 7 U.S.C. 1502(b)(14)(B) ) is amended\u2014\n**(1)**\nin clause (ii), by striking 5 years and inserting 10 crop years ; and\n**(2)**\nin clause (iii), by striking 5-year and inserting 10-year .\n##### (c) Increase in assistance\nSection 508(e)(8) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(e)(8) ) is amended\u2014\n**(1)**\nby striking Notwithstanding and inserting the following:\n(A) In general Notwithstanding ;\n**(2)**\nby striking is 10 percentage points greater than and inserting is the number of percentage points specified in subparagraph (B) greater than ; and\n**(3)**\nby adding at the end the following:\n(B) Percentage points adjustments For purposes of subparagraph (A), the percentage points specified in this subparagraph are as follows: (i) For each of the first and second reinsurance years that a beginning farmer or rancher or veteran farmer or rancher participates as a beginning farmer or rancher or veteran farmer or rancher in the applicable policy or plan of insurance, 15 percentage points, respectively. (ii) For the third reinsurance year that a beginning farmer or rancher or veteran farmer or rancher participates as a beginning farmer or rancher or veteran farmer or rancher in the applicable policy or plan of insurance, 13 percentage points, respectively. (iii) For the fourth reinsurance year that a beginning farmer or rancher or veteran farmer or rancher participates as a beginning farmer or rancher or veteran farmer or rancher in the applicable policy or plan of insurance, 11 percentage points, respectively. (iv) For each of the fifth through tenth reinsurance years that a beginning farmer or rancher or veteran farmer or rancher participates as a beginning farmer or rancher or veteran farmer or rancher in the applicable policy or plan of insurance, 10 percentage points, respectively. .\n##### (d) Conforming amendment\nSection 522(c)(7) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c)(7) ) is amended by striking subparagraph (F).",
      "versionDate": "2025-03-14",
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
        "actionDate": "2025-03-14",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1073",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Crop Insurance for Future Farmers Act",
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
        "updateDate": "2025-05-06T17:00:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2117",
          "measure-number": "2117",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-08-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2117v00",
            "update-date": "2025-08-07"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Crop Insurance for Future Farmers Act</strong></p><p>This bill amends the federal crop insurance program (FCIP) to increase the premium assistance rate for beginning and veteran farmers or ranchers. (FCIP offers subsidized crop insurance policies that producers can purchase to cover a wide variety of crops and livestock.)</p><p>Specifically, the bill amends the amount of percentage points that are added to the premium assistance rate for\u00a0beginning farmers or ranchers and veteran farmers or ranchers for an applicable insurance policy or plan (currently 10 percentage points) to provide</p><ul><li>15 percentage points in each of the 1st and 2nd reinsurance years,</li><li>13 percentage points in the 3rd year,</li><li>11 percentage points in the 4th year, and</li><li>10 percentage points in each of the 5th through the 10th reinsurance years.</li></ul><p>Under the bill, farmers and ranchers, and veteran farmers and ranchers, are eligible to qualify for the program for 10 years, an increase from 5 years under current law. Specifically, to be considered a beginning farmer or rancher, a person must not have actively operated and managed a farm or ranch for more than 10 crop years. To be considered a veteran farmer or rancher, a veteran must have (1) not operated a farm or ranch for more than 10 crop years, or (2) first obtained veteran status in the past 10 years.</p>"
        },
        "title": "Crop Insurance for Future Farmers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2117.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Crop Insurance for Future Farmers Act</strong></p><p>This bill amends the federal crop insurance program (FCIP) to increase the premium assistance rate for beginning and veteran farmers or ranchers. (FCIP offers subsidized crop insurance policies that producers can purchase to cover a wide variety of crops and livestock.)</p><p>Specifically, the bill amends the amount of percentage points that are added to the premium assistance rate for\u00a0beginning farmers or ranchers and veteran farmers or ranchers for an applicable insurance policy or plan (currently 10 percentage points) to provide</p><ul><li>15 percentage points in each of the 1st and 2nd reinsurance years,</li><li>13 percentage points in the 3rd year,</li><li>11 percentage points in the 4th year, and</li><li>10 percentage points in each of the 5th through the 10th reinsurance years.</li></ul><p>Under the bill, farmers and ranchers, and veteran farmers and ranchers, are eligible to qualify for the program for 10 years, an increase from 5 years under current law. Specifically, to be considered a beginning farmer or rancher, a person must not have actively operated and managed a farm or ranch for more than 10 crop years. To be considered a veteran farmer or rancher, a veteran must have (1) not operated a farm or ranch for more than 10 crop years, or (2) first obtained veteran status in the past 10 years.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119hr2117"
    },
    "title": "Crop Insurance for Future Farmers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Crop Insurance for Future Farmers Act</strong></p><p>This bill amends the federal crop insurance program (FCIP) to increase the premium assistance rate for beginning and veteran farmers or ranchers. (FCIP offers subsidized crop insurance policies that producers can purchase to cover a wide variety of crops and livestock.)</p><p>Specifically, the bill amends the amount of percentage points that are added to the premium assistance rate for\u00a0beginning farmers or ranchers and veteran farmers or ranchers for an applicable insurance policy or plan (currently 10 percentage points) to provide</p><ul><li>15 percentage points in each of the 1st and 2nd reinsurance years,</li><li>13 percentage points in the 3rd year,</li><li>11 percentage points in the 4th year, and</li><li>10 percentage points in each of the 5th through the 10th reinsurance years.</li></ul><p>Under the bill, farmers and ranchers, and veteran farmers and ranchers, are eligible to qualify for the program for 10 years, an increase from 5 years under current law. Specifically, to be considered a beginning farmer or rancher, a person must not have actively operated and managed a farm or ranch for more than 10 crop years. To be considered a veteran farmer or rancher, a veteran must have (1) not operated a farm or ranch for more than 10 crop years, or (2) first obtained veteran status in the past 10 years.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119hr2117"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2117ih.xml"
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
      "title": "Crop Insurance for Future Farmers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T14:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Crop Insurance for Future Farmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T14:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Crop Insurance Act to promote crop insurance support for beginning farmers and ranchers and veteran farmers and ranchers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T14:18:40Z"
    }
  ]
}
```
