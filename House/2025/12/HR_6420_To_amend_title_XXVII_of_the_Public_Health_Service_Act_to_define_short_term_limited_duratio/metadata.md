# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6420?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6420
- Title: ACCESS Act
- Congress: 119
- Bill type: HR
- Bill number: 6420
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-01-06T15:24:46Z
- Update date including text: 2026-01-06T15:24:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6420",
    "number": "6420",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001222",
        "district": "7",
        "firstName": "Max",
        "fullName": "Rep. Miller, Max L. [R-OH-7]",
        "lastName": "Miller",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "ACCESS Act",
    "type": "HR",
    "updateDate": "2026-01-06T15:24:46Z",
    "updateDateIncludingText": "2026-01-06T15:24:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:03:40Z",
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
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "GA"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6420ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6420\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Miller of Ohio (for himself and Mr. Allen ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXVII of the Public Health Service Act to define short-term limited duration insurance.\n#### 1. Short title\nThis Act may be cited as the Affordable Care Economic Stability and Small Business Act or the ACCESS Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAmericans, including small businesses in the Nation, could benefit from access to efficient, quality, and more affordable health care coverage options.\n**(2)**\nHealth insurance coverage designed to fill temporary gaps in coverage when an individual is transitioning from one plan or coverage to another, such as transitions in employment, is valuable.\n**(3)**\nSmall businesses are particularly challenged by escalating health care costs threatening their viability and ability to continue supporting their employees and contributing to their local economies.\n**(4)**\nWith continuously rising health care costs, short-term limited duration affordable health plans may provide a critical means for small business owners to provide portable coverage for United States workers.\n**(5)**\nAccess to flexible health care choices for American consumers and the small business community is paramount, including insurance plans that provide affordable and flexible coverage, building a path toward stronger health care coverage in the Nation.\n#### 3. Short-term limited duration insurance\n##### (a) Definition\nSection 2791(b) of the Public Health Service Act ( 42 U.S.C. 300gg\u201391(b) ) is amended by adding at the end the following new paragraph:\n(6) Short-term limited duration insurance The term short-term limited duration insurance means health insurance coverage provided under a contract with a health insurance issuer that\u2014 (A) has an expiration date specified in the contract that is less than 12 months after the original effective date of the contract; and (B) has a duration of not more than 3 years (taking into account renewals or extensions) after the original effective date of the contract. .\n##### (b) Guaranteed renewability\nSection 2703 of the Public Health Service Act ( 42 U.S.C. 300gg\u20132 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting or offers short-term limited duration insurance after group market ; and\n**(2)**\nby adding at the end the following:\n(f) Application to short-Term limited duration insurance (1) In general In applying this section in the case of short-term limited duration insurance\u2014 (A) a reference to health insurance coverage with respect to such coverage offered in the individual market shall be deemed to include short-term limited duration insurance; and (B) a reference to health insurance issuer with respect to health insurance coverage offered in the individual market shall be deemed to include an issuer of short-term limited duration insurance. (2) Special rule for short-term limited duration insurance In the case of short-term limited duration insurance, at the time of application for enrollment in such insurance coverage, an individual may decline renewability of such coverage in accordance with this section, and the contract between such individual and the health insurance issuer shall specify whether the individual opted for renewability or no renewability. .\n##### (c) Applicability\nThe amendments made by this section shall apply with respect to contracts for short-term limited duration insurance that take effect on or after the date of the enactment of this section.",
      "versionDate": "2025-12-04",
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
        "updateDate": "2026-01-06T15:24:46Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6420ih.xml"
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
      "title": "ACCESS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-24T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACCESS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable Care Economic Stability and Small Business Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXVII of the Public Health Service Act to define short-term limited duration insurance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T04:03:19Z"
    }
  ]
}
```
