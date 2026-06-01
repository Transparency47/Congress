# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4417?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4417
- Title: Mobile Cancer Screening Act
- Congress: 119
- Bill type: HR
- Bill number: 4417
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-05-21T08:08:42Z
- Update date including text: 2026-05-21T08:08:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4417",
    "number": "4417",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Mobile Cancer Screening Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:42Z",
    "updateDateIncludingText": "2026-05-21T08:08:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:00:40Z",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "CO"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4417ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4417\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Ruiz (for himself, Mr. Evans of Colorado , and Ms. Wasserman Schultz ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to direct the Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, to award grants, contracts, or cooperative agreements for supporting new mobile cancer screening units to expand patient access to essential screening services in rural and underserved communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mobile Cancer Screening Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nEach year, 2,000,000 people in the United States are diagnosed with cancer.\n**(2)**\nLung cancer remains the leading cause of cancer deaths in the United States, with 127,070 deaths in 2023 alone. Despite its prevalence, only 4.5 percent of eligible individuals were screened for lung cancer in 2022.\n**(3)**\nMobile cancer screening units have proven effective in increasing access to essential screenings, including for breast cancer and more recently lung cancer.\n**(4)**\nNationally, only 26.6 percent of lung cancer cases are diagnosed at an early stage when the 5-year survival rate is 63 percent.\n#### 3. Mobile cancer screening grants\nPart D of title III of the Public Health Service Act ( 42 U.S.C. 254b et seq. ) is amended by adding at the end the following:\nXIII Mobile cancer screening units 340J. Grants, contracts, and cooperative agreements (a) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration, shall award grants, contracts, or cooperative agreements to eligible entities for the purpose of supporting new mobile cancer screening units to expand patient access to essential screening services in rural and underserved areas. (b) Eligible entities Entities eligible for an award under subsection (a) include\u2014 (1) a nonprofit hospital; (2) a Federally qualified health center; (3) an academic health center; (4) a health system; and (5) a consortium or other collaboration of two or more entities listed in any of paragraphs (1) through (4). (c) Use of funds For the purpose described in subsection (a), funds awarded under this section may be used for\u2014 (1) purchasing a commercial vehicle to operate a mobile cancer screening unit; (2) acquiring imaging technology; (3) purchasing digital tools needed to operate a mobile cancer screening unit; and (4) covering other costs determined by the Secretary to be essential startup or operational costs. (d) Funding limit The amount of an award under subsection (a) may not exceed $2,000,000. (e) Prioritization In making awards under subsection (a), the Secretary shall prioritize\u2014 (1) applicants with the highest potential impact on patient mortality and screening gaps for high-risk individuals; (2) applicants serving underserved populations, including\u2014 (A) rural areas; and (B) areas served by the Indian Health Service; and (3) applicants able to provide comprehensive follow-up care for abnormal findings within 90 minutes of the unit by ground transportation. (f) Matching funds As a condition on receipt of an award under this section, an eligible entity shall agree that, with respect to costs to be incurred by the entity in carrying out activities for which the award is made, the entity will contribute from non-Federal sources, in cash or in kind, an amount equal to not less than one dollar for every three dollars provided through the award. (g) Report to Congress (1) Submission Not later than 4 years after the date of enactment of this section, the Secretary shall submit a report to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate. (2) Contents The report required by paragraph (1) shall include\u2014 (A) the total number of patients screened using mobile cancer screening units funded through awards under this section, with data on such total number of patients de-identified and disaggregated by race, ethnicity, age, sex, geographic region, disability status, and other relevant factors; (B) the impact of awards under subsection (a) on increasing screening rates, early cancer detection, and improved patient outcomes; (C) recommendations for improving the program under this section; and (D) such other information and recommendations as the Secretary determines to be relevant. (h) Authorization of appropriations To carry out this section, there is authorized to be appropriated $15,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2025-07-15",
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
        "actionDate": "2025-09-29",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2927",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Mobile Cancer Screening Act",
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
        "name": "Health",
        "updateDate": "2025-09-09T15:19:52Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4417ih.xml"
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
      "title": "Mobile Cancer Screening Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T11:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mobile Cancer Screening Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T11:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to direct the Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, to award grants, contracts, or cooperative agreements for supporting new mobile cancer screening units to expand patient access to essential screening services in rural and underserved communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T11:48:21Z"
    }
  ]
}
```
