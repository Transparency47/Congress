# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3866?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3866
- Title: Maternal and Infant Syphilis Prevention Act
- Congress: 119
- Bill type: HR
- Bill number: 3866
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2025-12-13T09:06:58Z
- Update date including text: 2025-12-13T09:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-10: Introduced in House

## Actions

- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3866",
    "number": "3866",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001133",
        "district": "6",
        "firstName": "Juan",
        "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
        "lastName": "Ciscomani",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Maternal and Infant Syphilis Prevention Act",
    "type": "HR",
    "updateDate": "2025-12-13T09:06:58Z",
    "updateDateIncludingText": "2025-12-13T09:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T14:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-10T14:03:00Z",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NM"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "NJ"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3866ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3866\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Mr. Ciscomani (for himself and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Health and Human Services to issue guidance on best practices for screening and treatment of congenital syphilis under Medicaid and the Children\u2019s Health Insurance Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maternal and Infant Syphilis Prevention Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 2023, there were 209,253 cases of syphilis in the United States, the highest number since 1950. This represents an 80 percent increase since 2018 and continuing a decades-long upward trend.\n**(2)**\nUntreated, syphilis can seriously damage the heart and brain and can cause blindness, deafness, and paralysis.\n**(3)**\nThe increased rise in syphilis cases is causing the rise in congenital syphilis with more than 3,882, a 3 percent increase from 2022, resulting in 252 stillbirths and 27 infant deaths. The cases are more than 10 times the number diagnosed in 2012.\n**(4)**\nWhen transmitted during pregnancy, congenital syphilis can cause miscarriage, lifelong medical issues, and infant death. Congenital syphilis can present health issues for babies at birth, including neonatal death, meningitis, anemia, and problems with the spleen and liver. If not treated, congenital syphilis can cause bone and joint problems, vision and hearing problems, issues with the nervous system, and developmental delays.\n**(5)**\nHigh incidence rates of congenital syphilis are often due to lack of timely testing or inadequate treatment during pregnancy. Timely syphilis testing and treatment during pregnancy might be able to prevent almost 90 percent of congenital syphilis cases.\n**(6)**\nRequirements for syphilis screening among pregnant women varies by State. The majority of States require syphilis screening in the first visit, significantly less States require syphilis screenings during the third trimester or at delivery.\n**(7)**\nScreening during the third trimester and at delivery can lead to earlier detection of congenital syphilis and prevent adverse health outcomes for mothers and newborn infants.\n**(8)**\nIncreased awareness and education are critical in reducing syphilis among pregnant women to prevent congenital syphilis.\n#### 3. Guidance and technical assistance under State Medicaid programs and State CHIPs\n##### (a) In general\nNot later than 12 months after the date of enactment of this section, the Secretary shall issue guidance to State agencies responsible for administering State Medicaid programs, State CHIPs, or both such programs, the Indian Health Service, Indian Tribes, tribal organizations, and Urban Indian organizations, on best practices with respect to actions that State Medicaid programs, State CHIPs, Indian health programs, and urban Indian health programs operated by an urban Indian organization pursuant to a grant or contract with the Indian Health Service pursuant to title V of the Indian Health Care Improvement Act ( 25 U.S.C. 1601 et seq. ) may take, including by using waivers under section 1115 of the Social Security Act ( 42 U.S.C. 1315 ) and authorities under title XIX of such Act ( 42 U.S.C. 1396 et seq. ) and title XXI of such Act ( 42 U.S.C. 1397aa et seq. ), for the following purposes:\n**(1)**\nImproving access to expand syphilis screening for pregnant women and babies.\n**(2)**\nBest practices for educating medical professionals and pregnant women with respect to syphilis.\n**(3)**\nStrategies for integrating telehealth services and training for providers and patients on the use of telehealth, including working with interpreters to furnish health services and providing resources with respect to congenital syphilis in multiple languages.\n**(4)**\nBest practices for increasing testing for syphilis in the third trimester and at delivery.\n**(5)**\nImproving treatment for syphilis and congenital syphilis.\n##### (b) Definitions\nIn this section:\n**(1) Indian Tribe, tribal organization, Urban Indian, Urban Indian organization, Indian health program**\nThe terms Indian tribe , tribal organization , Urban Indian , Urban Indian organization , and Indian health program have the meanings given those terms in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 ).\n**(2) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(3) State**\nThe term State has the meaning given such term in section 1101(a)(1) of the Social Security Act ( 42 U.S.C. 1301(a)(1) ) for purposes of titles XIX and XXI of such Act.\n**(4) State chip**\nThe term State CHIP means a State child health plan for child health assistance under title XXI of the Social Security Act ( 42 U.S.C. 1397aa et seq. ), and includes any waiver of such a plan.\n**(5) State medicaid program**\nThe term State Medicaid program means a State plan for medical assistance under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), and includes any waiver of such a plan.\n##### (c) Report to Congress\nNot later than 2 years after the date of the enactment of this Act, the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives, the Committee on Health, Education, Labor and Pensions of the Senate, and the Committee on Finance of the Senate, and shall make publicly available, a report analyzing the implementation of the best practices described in subsection (a).",
      "versionDate": "2025-06-10",
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
        "actionDate": "2025-06-10",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2004",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Maternal and Infant Syphilis Prevention Act",
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
        "updateDate": "2025-07-02T13:32:36Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3866ih.xml"
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
      "title": "Maternal and Infant Syphilis Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:59Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maternal and Infant Syphilis Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T08:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Health and Human Services to issue guidance on best practices for screening and treatment of congenital syphilis under Medicaid and the Children's Health Insurance Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T08:03:34Z"
    }
  ]
}
```
