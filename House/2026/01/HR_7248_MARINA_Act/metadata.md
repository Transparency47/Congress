# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7248?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7248
- Title: MARINA Act
- Congress: 119
- Bill type: HR
- Bill number: 7248
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-02-11T14:49:42Z
- Update date including text: 2026-02-11T14:49:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7248",
    "number": "7248",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001108",
        "district": "1",
        "firstName": "James",
        "fullName": "Rep. Comer, James [R-KY-1]",
        "lastName": "Comer",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "MARINA Act",
    "type": "HR",
    "updateDate": "2026-02-11T14:49:42Z",
    "updateDateIncludingText": "2026-02-11T14:49:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:33:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "R000395",
      "district": "5",
      "firstName": "Harold",
      "fullName": "Rep. Rogers, Harold [R-KY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "KY"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "KY"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "TN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7248ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7248\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Comer (for himself, Mr. Rogers of Kentucky , Mr. Guthrie , Mr. Rose , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Corps of Engineers to take certain actions with respect to rental amounts and administrative fees charged to certain marinas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maintaining Access to Recreational Industry and Necessary Adjustments Act or the MARINA Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMarina concessionaires, individually and collectively, allow the Corps of Engineers to fulfill their responsibility to enhance public usage and enjoyment of Corps of Engineers facilities.\n**(2)**\nLeases for commercial concession purposes provide a direct benefit to the public and the Federal Government.\n**(3)**\nThe Corps of Engineers lacks a coordinated schedule or assessment for charging administrative fees to concessionaires across all Corps of Engineers districts.\n#### 3. Rental amounts, fees, and lease periods for covered marinas\n##### (a) Limitation on rental amounts\nIn determining the amount of rent charged to the operator of a covered marina for a covered lease, the Secretary shall, for purposes of applying the Revised Graduated Rental System\u2014\n**(1)**\nexclude from the total gross receipts calculation the combined covered receipts; and\n**(2)**\nestablish a percentage rate applicable to such combined covered receipts of not more than 1 percent.\n##### (b) Fee schedules for administrative fees\n**(1) In general**\nThe Secretary shall establish, for covered leases, a standardized fee schedule for administrative fees assessed to operators of covered marinas, applicable to all Corps of Engineers districts, that specifies under what circumstances and at what time such a fee is to be assessed.\n**(2) Limitations**\n**(A) Amounts**\nThe Secretary may assess, for a covered lease\u2014\n**(i)**\nan administrative fee of not more than $50,000 to the operator of a covered marina only for\u2014\n**(I)**\nactivities involving land disturbances that require a major review effort, coordination and concurrence with State agencies, other Federal agencies, or Tribal governments, and review and approval at the headquarters level of the Corps of Engineers; and\n**(II)**\nactivities relating to lease area expansions of 100 acres or more;\n**(ii)**\nan administrative fee of not more than $5,000 to the operator of a covered marina only for activities (not involving land disturbances) that require a moderate review effort, which may involve coordination and concurrence with State agencies, other Federal agencies, or Tribal governments; and\n**(iii)**\nan administrative fee of not more than $1,000 to the operator of a covered marina for any other activities.\n**(B) Prohibition**\nThe Secretary may not assess, for a covered lease, an administrative fee to the operator of a covered marina for a standard lease renewal, an extension of lease terms, or activities relating to lease transfers or sales to an entity other than a covered marina.\n**(3) Publication**\nThe Secretary shall post the fee schedule established under paragraph (1) on a public website of the Corps of Engineers.\n##### (c) Lease periods\nSection 4 of the Flood Control Act of 1944 ( 16 U.S.C. 460d ) is amended by inserting (which shall be not less than 50 years for an initial lease or for the first renewal after the date of enactment of the MARINA Act of a lease in effect on such date, and not less than 25 years for any subsequent lease renewal) after at water resource development projects for such periods .\n##### (d) Wage provision\nExcept as required by section 6703 of title 41, United States Code, the Secretary may not require, as a condition of a covered lease, the operator of a covered marina to compensate the employees of the operator at a rate higher than the Federal minimum wage established under section 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ).\n##### (e) Rulemaking\nThe Secretary shall issue a final rule to carry out this section and the amendment made by this section, which final rule shall take effect not later than 1 year after the date of enactment of this Act.\n##### (f) Effect on existing leases\nNothing in this section authorizes the Secretary to modify a lease in effect on the date of enactment of this Act, except as necessary to implement the requirements of this section and the amendment made by this section.\n##### (g) Definitions\nIn this section:\n**(1) Combined covered receipts**\nThe term combined covered receipts means the combined receipts, from business operations conducted at a covered marina, of the operator of the covered marina and all entities operating pursuant to a contract with such operator, from prepared food, beverages, fuel, boats, and expensive, boat-related items, such as boat motors and boat lifts.\n**(2) Covered lease**\nThe term covered lease means a lease for commercial concession purposes under section 4 of the Flood Control Act of 1944 ( 16 U.S.C. 460d ).\n**(3) Covered marina**\nThe term covered marina means a marina operating pursuant to a covered lease.\n**(4) Revised Graduated Rental System**\nThe term Revised Graduated Rental System means the Revised Graduated Rental System established in Engineer Regulation 405\u20131\u201312, or any successor rental system used by the Secretary for purposes of calculating rental amounts for covered leases.\n**(5) Secretary**\nThe term Secretary means the Secretary of the Army, acting through the Chief of Engineers.",
      "versionDate": "2026-01-27",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-02-11T14:49:42Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7248ih.xml"
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
      "title": "MARINA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T08:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MARINA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T08:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maintaining Access to Recreational Industry and Necessary Adjustments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T08:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Corps of Engineers to take certain actions with respect to rental amounts and administrative fees charged to certain marinas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T08:48:45Z"
    }
  ]
}
```
