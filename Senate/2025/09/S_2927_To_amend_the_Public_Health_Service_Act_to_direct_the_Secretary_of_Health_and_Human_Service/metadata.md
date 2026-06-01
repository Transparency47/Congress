# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2927?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2927
- Title: Mobile Cancer Screening Act
- Congress: 119
- Bill type: S
- Bill number: 2927
- Origin chamber: Senate
- Introduced date: 2025-09-29
- Update date: 2026-03-24T20:05:01Z
- Update date including text: 2026-03-24T20:05:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-29: Introduced in Senate
- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-09-29: Introduced in Senate

## Actions

- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-29",
    "latestAction": {
      "actionDate": "2025-09-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2927",
    "number": "2927",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Mobile Cancer Screening Act",
    "type": "S",
    "updateDate": "2026-03-24T20:05:01Z",
    "updateDateIncludingText": "2026-03-24T20:05:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-29",
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
          "date": "2025-09-29T21:28:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2927is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2927\nIN THE SENATE OF THE UNITED STATES\nSeptember 29, 2025 Mr. Marshall (for himself and Mr. Reed ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to direct the Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, to award grants, contracts, or cooperative agreements for supporting new mobile cancer screening units to expand patient access to essential screening services in rural and underserved communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mobile Cancer Screening Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nEach year, 2,000,000 people in the United States are diagnosed with cancer.\n**(2)**\nLung cancer remains the leading cause of cancer deaths in the United States, with 127,070 deaths in 2023 alone. Despite its prevalence, only 4.5 percent of eligible individuals were screened for lung cancer in 2022.\n**(3)**\nMobile cancer screening units have proven effective in increasing access to essential screenings, including for breast cancer and more recently lung cancer.\n**(4)**\nNationally, only 26.6 percent of lung cancer cases are diagnosed at an early stage when the 5-year survival rate is 63 percent.\n#### 3. Mobile cancer screening grants\nPart D of title III of the Public Health Service Act ( 42 U.S.C. 254b et seq. ) is amended by adding at the end the following:\nXIII Mobile cancer screening units 340J. Grants, contracts, and cooperative agreements (a) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration, shall award grants, contracts, or cooperative agreements to eligible entities for the purpose of supporting new mobile cancer screening units to expand patient access to essential screening services in rural and underserved areas. (b) Eligible entities Entities eligible for an award under subsection (a) include\u2014 (1) a nonprofit hospital; (2) a Federally-qualified health center; (3) an academic health center; (4) a health system; and (5) a consortium or other collaboration of 2 or more entities listed in any of paragraphs (1) through (4). (c) Use of funds For the purpose described in subsection (a), funds awarded under this section may be used for\u2014 (1) purchasing a commercial vehicle to operate a mobile cancer screening unit; (2) acquiring imaging technology; (3) purchasing digital tools needed to operate a mobile cancer screening unit; and (4) covering other costs determined by the Secretary to be essential startup or operational costs. (d) Funding limit The amount of an award under subsection (a) may not exceed $2,000,000. (e) Prioritization In making awards under subsection (a), the Secretary shall prioritize\u2014 (1) applicants with the highest potential impact on patient mortality and screening gaps for high-risk individuals; (2) applicants serving underserved populations, including\u2014 (A) rural areas; and (B) areas served by the Indian Health Service; and (3) applicants able to provide comprehensive follow-up care for abnormal findings within 90 minutes of the unit by ground transportation. (f) Matching funds As a condition on receipt of an award under this section, an eligible entity shall agree that, with respect to costs to be incurred by the entity in carrying out activities for which the award is made, the entity will contribute from non-Federal sources, in cash or in kind, an amount equal to not less than 1 dollar for every 3 dollars provided through the award. (g) Report to Congress (1) Submission Not later than 4 years after the date of enactment of this section, the Secretary shall submit a report to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate. (2) Contents The report required by paragraph (1) shall include\u2014 (A) the total number of patients screened using mobile cancer screening units funded through awards under this section, with data on such total number of patients de-identified and disaggregated by race, ethnicity, age, sex, geographic region, disability status, and other relevant factors; (B) the impact of awards under subsection (a) on increasing screening rates, early cancer detection, and improved patient outcomes; (C) recommendations for improving the program under this section; and (D) such other information and recommendations as the Secretary determines to be relevant. (h) Authorization of appropriations To carry out this section, there is authorized to be appropriated $15,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2025-09-29",
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
        "actionDate": "2025-07-15",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4417",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Mobile Cancer Screening Act",
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
        "name": "Health",
        "updateDate": "2025-12-16T18:46:37Z"
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
      "date": "2025-09-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2927is.xml"
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
      "title": "Mobile Cancer Screening Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mobile Cancer Screening Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to direct the Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, to award grants, contracts, or cooperative agreements for supporting new mobile cancer screening units to expand patient access to essential screening services in rural and underserved communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:16Z"
    }
  ]
}
```
