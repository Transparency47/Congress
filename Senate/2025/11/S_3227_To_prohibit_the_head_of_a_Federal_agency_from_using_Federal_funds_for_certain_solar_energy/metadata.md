# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3227?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3227
- Title: Protecting American Farmland Act
- Congress: 119
- Bill type: S
- Bill number: 3227
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-17T15:18:05Z
- Update date including text: 2025-12-17T15:18:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3227",
    "number": "3227",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Protecting American Farmland Act",
    "type": "S",
    "updateDate": "2025-12-17T15:18:05Z",
    "updateDateIncludingText": "2025-12-17T15:18:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T16:40:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3227is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3227\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mrs. Blackburn (for herself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo prohibit the head of a Federal agency from using Federal funds for certain solar energy projects that would result in the conversion of farmland, to exclude from certain tax credits relating to clean energy facilities placed in service on prime farmland, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting American Farmland Act .\n#### 2. Prohibition on agency funding for covered solar energy projects\n##### (a) In general\nThe head of a Federal agency may not use Federal funds, including by providing funds, a loan, or a loan guarantee to any person, to carry out a covered solar energy project that would result in the conversion of prime farmland.\n##### (b) Definitions\nIn this section:\n**(1) Conversion**\nThe term conversion means, with respect to prime farmland, any activity that results in the farmland failing to meet the requirements of a State (as such term is defined in section 343 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991 )) for agricultural production, activity, or use.\n**(2) Covered solar energy project**\nThe term covered solar energy project means a project for the installation, operation, and maintenance of a ground-mounted facility for the generation of electricity from solar energy, primarily for the purpose of sale of such electricity.\n**(3) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code.\n**(4) Prime farmland**\nThe term prime farmland means farmland described in section 1540(c)(1)(A) of the Farmland Protection Policy Act ( 7 U.S.C. 4201(c)(1)(A) ).\n#### 3. Exclusion of property placed in service on prime farmland from residential clean energy credit\n##### (a) In general\nSection 25D(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(9) Exclusion of solar property located on prime farmland (A) In general Qualified solar electric property expenditures which are properly allocable to property placed in service on prime farmland shall not be taken into account for purposes of this section. (B) Prime farmland defined For purposes of this paragraph, the term prime farmland means farmland described in section 1540(c)(1)(A) of the Farmland Protection Policy Act ( 7 U.S.C. 4201(c)(1)(A) ). .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after the date of the enactment of this section.\n#### 4. Exclusion of facilities located on prime farmland from renewable electricity production credit\n##### (a) In general\nSection 45(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(14) Exclusion of solar energy facilities located on prime farmland The term qualified facility shall not include any facility using solar energy to produce electricity which is located on prime farmland (as defined in section 25D(e)(9)(B)). .\n##### (b) Effective date\nThe amendment made by this section shall apply to facilities placed in service after the date of the enactment of this section.\n#### 5. Exclusion of facilities located on prime farmland from clean electricity production credit\n##### (a) In general\nSection 45Y(g) of the Internal Revenue Code of 1986, as amended by section 70512 of Public Law 119\u201321 , is amended by adding at the end the following new paragraph:\n(14) Exclusion of solar facilities located on prime farmland The term qualified facility shall not include any facility using solar energy to produce electricity which is located on prime farmland (as defined in section 25D(e)(9)(B)). .\n##### (b) Effective date\nThe amendment made by this section shall apply to facilities placed in service after the date of the enactment of this section.\n#### 6. Exclusion of property placed in service on prime farmland from energy credit\n##### (a) In general\nSection 48(a)(3) of the Internal Revenue Code of 1986 is amended by inserting or any property located on prime farmland (as defined in section 25D(e)(9)(B)) after any prior taxable year .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after the date of the enactment of this section.\n#### 7. Exclusion of property placed in service on prime farmland from clean electricity investment credit\n##### (a) In general\nSection 48E(d) of the Internal Revenue Code of 1986, as amended by section 70513 of Public Law 119\u201321 , is amended by adding at the end the following new paragraph:\n(7) Exclusion of solar facilities located on prime farmland Expenditures which are properly allocable to any facility using solar energy to produce electricity which is placed in service on prime farmland (as defined in section 25D(e)(9)(B)) shall not be taken into account for purposes of this section. .\n##### (b) Effective date\nThe amendment made by this section shall apply to qualified investments with respect to facilities placed in service after the date of the enactment of this section.",
      "versionDate": "2025-11-20",
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
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3313",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting American Farmland Act",
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
        "name": "Taxation",
        "updateDate": "2025-12-02T20:05:25Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3227is.xml"
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
      "title": "Protecting American Farmland Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-26T05:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting American Farmland Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T05:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the head of a Federal agency from using Federal funds for certain solar energy projects that would result in the conversion of farmland, to exclude from certain tax credits relating to clean energy facilities placed in service on prime farmland, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-26T05:33:23Z"
    }
  ]
}
```
