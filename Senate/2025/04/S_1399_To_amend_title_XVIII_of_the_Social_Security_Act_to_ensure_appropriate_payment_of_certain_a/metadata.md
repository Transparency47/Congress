# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1399?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1399
- Title: Health Tech Investment Act
- Congress: 119
- Bill type: S
- Bill number: 1399
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2025-12-05T22:56:26Z
- Update date including text: 2025-12-05T22:56:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1399",
    "number": "1399",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Health Tech Investment Act",
    "type": "S",
    "updateDate": "2025-12-05T22:56:26Z",
    "updateDateIncludingText": "2025-12-05T22:56:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T21:10:31Z",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NM"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "TN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "DE"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1399is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1399\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Rounds (for himself, Mr. Heinrich , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to ensure appropriate payment of certain algorithm-based healthcare services under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Health Tech Investment Act .\n#### 2. Ensuring appropriate payment of certain algorithm-based healthcare services under the Medicare Program\n##### (a) In general\nSection 1833(t) of the Social Security Act ( 42 U.S.C. 1395l(t) ) is amended\u2014\n**(1)**\nin paragraph (2)(E), by inserting and new technology ambulatory payment classification of algorithm-based healthcare services under paragraph (16)(H) after (16)(G) ; and\n**(2)**\nin paragraph (16), by adding at the end the following new subparagraph:\n(H) Special rule for certain algorithm-based healthcare services (i) In general In the case of a covered OPD service furnished on or after January 1, 2026, that is an algorithm-based healthcare service (as defined in clause (ii)) that is assigned to a new technology ambulatory payment classification (as described in the final rule entitled Medicare Program; Changes to the Hospital Outpatient Prospective Payment System for Calendar Year 2002 published by the Department of Health and Human Services on November 30, 2001 (66 Fed. Reg. 59897)) on or after the date of the enactment of this subparagraph or for which, as of such date, is currently and has been assigned to a new technology ambulatory payment classification for a period of less than 5 years, the Secretary\u2014 (I) shall ensure that such service is assigned to a new technology ambulatory payment classification based on the cost of such service as submitted by the manufacturer of such service in a form and manner specified by the Secretary, including costs for the technology based on invoice prices, subscription-based prices, clinical staff, overhead, and other costs associated with providing the service; (II) shall adjust the new technology ambulatory payment classification pursuant to subclause (I) as necessary; and (III) may not remove such service from the new technology ambulatory payment classification as determined under subclauses (I) and (II) until the Secretary determines that adequate claims data exists to reassign such service to another ambulatory payment classification (which in no case may be before such service has received payment under the assigned new technology ambulatory payment classification for at least 5 years). (ii) Adjustment The Secretary shall adjust the application process and criteria for the new technology ambulatory payment classification to ensure that, in addition to currently eligible algorithm-based healthcare services, algorithm-based healthcare services that otherwise meet the eligibility requirements for such classification and are distinct from but performed concurrently with, adjunctive to, or provided in any other modality or form as part of an underlying service and require additional resources, meet\u2014 (I) the eligibility requirement that they are distinct new procedures with a beginning, middle, and end; or (II) any subsequent similar new technology ambulatory payment classification eligibility requirement. (iii) Definition of algorithm-based healthcare service For purposes of this subparagraph, the term algorithm-based healthcare service means a service delivered through a device cleared or approved by the Food and Drug Administration that uses artificial intelligence, machine learning, or other similarly designed software to yield clinical outputs or generate clinical conclusions for use by a physician or practitioner in the screening, detection, diagnosis, or treatment of an individual\u2019s condition or disease, or any such other similar service as the Secretary determines appropriate in consultation with appropriate organizations. .\n##### (b) Codifying OPPS payment for software as a service\nEffective for services provided on or after January 1, 2023, the Secretary of Health and Human Services shall apply the hospital outpatient prospective payment system payment for software as a service policy described in the final rule entitled, Medicare Program: Hospital Outpatient Prospective Payment and Ambulatory Surgical Center Payment Systems and Quality Reporting Programs; Organ Acquisition; Rural Emergency Hospitals: Payment Policies, Conditions of Participation, Provider Enrollment, Physician Self-Referral; New Service Category for Hospital Outpatient Department Prior Authorization Process; Overall Hospital Quality Star Rating; COVID\u201319 published by the Department of Health and Human Services on November 23, 2022 (87 Fed. Reg. 71748).",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6197",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Health Tech Investment Act",
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
        "updateDate": "2025-05-19T14:52:32Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1399is.xml"
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
      "title": "Health Tech Investment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Health Tech Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to ensure appropriate payment of certain algorithm-based healthcare services under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:29Z"
    }
  ]
}
```
