# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3313?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3313
- Title: Protecting American Farmland Act
- Congress: 119
- Bill type: HR
- Bill number: 3313
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2025-12-17T15:18:06Z
- Update date including text: 2025-12-17T15:18:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3313",
    "number": "3313",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David J. [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Protecting American Farmland Act",
    "type": "HR",
    "updateDate": "2025-12-17T15:18:06Z",
    "updateDateIncludingText": "2025-12-17T15:18:06Z"
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
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-05-08T13:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-08T13:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "OH"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WY"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3313ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3313\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mr. Taylor (for himself, Mr. Davidson , and Ms. Hageman ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the head of a Federal agency from using Federal funds for certain solar energy projects that would result in the conversion of farmland, to exclude from certain tax credits relating to clean energy facilities placed in service on prime farmland, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting American Farmland Act .\n#### 2. Prohibition on agency funding for covered solar energy projects\n##### (a) In general\nThe head of a Federal agency may not use Federal funds, including by providing funds, a loan, or a loan guarantee to any person, to carry out a covered solar energy project that would result in the conversion of prime farmland.\n##### (b) Definitions\nIn this section:\n**(1) Conversion**\nThe term conversion means, with respect to prime farmland, any activity that results in the farmland failing to meet the requirements of a State (as such term is defined in section 343 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991 )) for agricultural production, activity, or use.\n**(2) Covered solar energy project**\nThe term covered solar energy project means a project for the installation, operation, and maintenance of a ground-mounted facility for the generation of electricity from solar energy, primarily for the purpose of sale of such electricity.\n**(3) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code.\n**(4) Prime farmland**\nThe term prime farmland means farmland described in section 1540(c)(1)(A) of the Farmland Protection Policy Act ( 7 U.S.C. 4201(c)(1)(A) ).\n#### 3. Exclusion of property placed in service on prime farmland from residential clean energy credit\n##### (a) In general\nSection 25D(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(9) Exclusion of solar property located on prime farmland (A) In general Qualified solar electric property expenditure which are properly allocable to property placed in service on prime farmland shall not be taken into account for purposes of this section. (B) Prime farmland defined For purposes of this paragraph, the term prime farmland means farmland described in section 1540(c)(1)(A) of the Farmland Protection Policy Act. .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after the date of the enactment of this section.\n#### 4. Exclusion of facilities located on prime farmland from renewable electricity production credit\n##### (a) In general\nSection 45(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(14) Exclusion of solar energy facilities located on prime farmland The term qualified facility shall not include any solar energy facility located on prime farmland (as defined in section 25D(e)(9)(B)). .\n##### (b) Effective date\nThe amendment made by this section shall apply to facilities placed in service after the date of the enactment of this section.\n#### 5. Exclusion of facilities located on prime farmland from clean electricity production credit\n##### (a) In general\nSection 45Y(g) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(13) Exclusion of solar facilities located on prime farmland The term qualified facility shall not include any solar energy facility located on prime farmland (as defined in section 25D(e)(9)(B)). .\n##### (b) Effective date\nThe amendment made by this section shall apply to facilities placed in service after the date of the enactment of this section.\n#### 6. Exclusion of property placed in service on prime farmland from energy credit\n##### (a) In general\nSection 48(a)(3) of the Internal Revenue Code of 1986 is amended by inserting or any property located on prime farmland (as defined in section 25D(e)(9)(B)) after any prior taxable year .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after the date of the enactment of this section.\n#### 7. Exclusion of property placed in service on prime farmland from clean electricity investment credit\n##### (a) In general\nSection 48E(d) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(6) Exclusion of solar facilities located on prime farmland Expenditures which are properly allocable to solar energy property placed in service on prime farmland (as defined in section 25D(e)(9)(B)) shall not be taken into account for purposes of this section. .\n##### (b) Effective date\nThe amendment made by this section shall apply to qualified investments with respect to facilities placed in service after the date of the enactment of this section.",
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
        "actionDate": "2025-11-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3227",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting American Farmland Act",
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
        "name": "Taxation",
        "updateDate": "2025-09-29T16:31:16Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3313ih.xml"
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
      "title": "Protecting American Farmland Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-18T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting American Farmland Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the head of a Federal agency from using Federal funds for certain solar energy projects that would result in the conversion of farmland, to exclude from certain tax credits relating to clean energy facilities placed in service on prime farmland, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:33:25Z"
    }
  ]
}
```
