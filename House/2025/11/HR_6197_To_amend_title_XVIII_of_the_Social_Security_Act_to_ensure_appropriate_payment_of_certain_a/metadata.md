# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6197?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6197
- Title: Health Tech Investment Act
- Congress: 119
- Bill type: HR
- Bill number: 6197
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-12T08:05:45Z
- Update date including text: 2026-05-12T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6197",
    "number": "6197",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000302",
        "district": "13",
        "firstName": "John",
        "fullName": "Rep. Joyce, John [R-PA-13]",
        "lastName": "Joyce",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Health Tech Investment Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:45Z",
    "updateDateIncludingText": "2026-05-12T08:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:12:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:11:50Z",
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
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TX"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
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
      "sponsorshipDate": "2026-01-27",
      "state": "VA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6197ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6197\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Joyce of Pennsylvania (for himself, Mr. Peters , Ms. Van Duyne , Mr. Schneider , Mr. Obernolte , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to ensure appropriate payment of certain algorithm-based healthcare services under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Health Tech Investment Act .\n#### 2. Ensuring appropriate payment of certain algorithm-based healthcare services under the Medicare Program\n##### (a) In general\nSection 1833(t) of the Social Security Act ( 42 U.S.C. 1395l(t) ) is amended\u2014\n**(1)**\nin paragraph (2)(E), by inserting and new technology ambulatory payment classification of algorithm-based healthcare services under paragraph (16)(H) after (16)(G) ; and\n**(2)**\nin paragraph (16), by adding at the end the following new subparagraph:\n(H) Special rule for certain algorithm-based healthcare services (i) In general In the case of a covered OPD service furnished on or after January 1, 2026, that is an algorithm-based healthcare service (as defined in clause (ii)) that is assigned to a new technology ambulatory payment classification (as described in the final rule entitled Medicare Program; Changes to the Hospital Outpatient Prospective Payment System for Calendar Year 2002 published by the Department of Health and Human Services on November 30, 2001 (66 Fed. Reg. 59897)) on or after the date of the enactment of this subparagraph or for which, as of such date, is currently and has been assigned to a new technology ambulatory payment classification for a period of less than 5 years, the Secretary\u2014 (I) shall ensure that such service is assigned to a new technology ambulatory payment classification based on the cost of such service as submitted by the manufacturer of such service in a form and manner specified by the Secretary, including costs for the technology based on invoice prices, subscription-based prices, clinical staff, overhead, and other costs associated with providing the service; (II) shall adjust the new technology ambulatory payment classification pursuant to subclause (I) as necessary; and (III) may not remove such service from the new technology ambulatory payment classification as determined under subclauses (I) and (II) until the Secretary determines that adequate claims data exists to reassign such service to another ambulatory payment classification (which in no case may be before such service has received payment under the assigned new technology ambulatory payment classification for at least 5 years). (ii) Adjustment The Secretary shall adjust the application process and criteria for the new technology ambulatory payment classification to ensure that, in addition to currently eligible algorithm-based healthcare services, algorithm-based healthcare services that otherwise meet the eligibility requirements for such classification and are distinct from but performed concurrently with, adjunctive to, or provided in any other modality or form as part of an underlying service and require additional resources, meet\u2014 (I) the eligibility requirement that they are distinct new procedures with a beginning, middle, and end; or (II) any subsequent similar new technology ambulatory payment classification eligibility requirement. (iii) Definition of algorithm-based healthcare service For purposes of this subparagraph, the term algorithm-based healthcare service means a service delivered through a device cleared or approved by the Food and Drug Administration that uses artificial intelligence, machine learning, or other similarly designed software to yield clinical outputs or generate clinical conclusions for use by a physician or practitioner in the screening, detection, diagnosis, or treatment of an individual\u2019s condition or disease, or any such other similar service as the Secretary determines appropriate in consultation with appropriate organizations. .\n##### (b) Codifying OPPS payment for software as a service\nEffective for services provided on or after January 1, 2023, the Secretary of Health and Human Services shall apply the hospital outpatient prospective payment system payment for software as a service policy described in the final rule entitled, Medicare Program: Hospital Outpatient Prospective Payment and Ambulatory Surgical Center Payment Systems and Quality Reporting Programs; Organ Acquisition; Rural Emergency Hospitals: Payment Policies, Conditions of Participation, Provider Enrollment, Physician Self-Referral; New Service Category for Hospital Outpatient Department Prior Authorization Process; Overall Hospital Quality Star Rating; COVID\u201319 published by the Department of Health and Human Services on November 23, 2022 (87 Fed. Reg. 71748).",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1399",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Health Tech Investment Act",
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
        "updateDate": "2025-12-01T19:47:32Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6197ih.xml"
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
      "title": "Health Tech Investment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-27T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health Tech Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T02:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to ensure appropriate payment of certain algorithm-based healthcare services under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-27T02:18:28Z"
    }
  ]
}
```
