# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5243?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5243
- Title: To amend title XVIII of the Social Security Act to increase data transparency for supplemental benefits under Medicare Advantage.
- Congress: 119
- Bill type: HR
- Bill number: 5243
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2025-09-24T14:07:06Z
- Update date including text: 2025-09-24T14:07:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5243",
    "number": "5243",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001227",
        "district": "4",
        "firstName": "Jennifer",
        "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
        "lastName": "McClellan",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "To amend title XVIII of the Social Security Act to increase data transparency for supplemental benefits under Medicare Advantage.",
    "type": "HR",
    "updateDate": "2025-09-24T14:07:06Z",
    "updateDateIncludingText": "2025-09-24T14:07:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:00:25Z",
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
          "date": "2025-09-10T14:00:20Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5243ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5243\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Ms. McClellan introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to increase data transparency for supplemental benefits under Medicare Advantage.\n#### 1. Increasing data transparency for supplemental benefits under Medicare Advantage\n##### (a) In general\nSection 1857(e) of the Social Security Act ( 42 U.S.C. 1395w\u201327(e) ) is amended by adding at the end the following new paragraph:\n(6) Reporting of enrollee-level data on supplemental benefits (A) In general Beginning with plan years beginning on or after January 1, 2029, a contract under this section with an MA organization shall require the organization to submit to the Secretary, for each MA plan offered by the organization, enrollee-level data on supplemental benefits (by item or service, or category of item or service, as determined appropriate by the Secretary, and national provider identifier), including eligibility for such benefits, the types of benefit categories offered, data on utilization of and payments for such benefits (including the total amount spent by the plan for each enrollee who utilized such benefits and the total out-of-pocket cost per utilization for each enrollee). (B) Data access (i) In general On the first Monday in October of each year (beginning with 2030), the Secretary shall make data submitted under subparagraph (A) available to individuals and entities for the purpose of conducting\u2014 (I) evaluations and other analysis to support the program under this title; and (II) other health care related research. (ii) Public use data file Not later than October 1 of each year (beginning with 2030), the Secretary shall make a public use data file containing the data submitted under subparagraph (A) available on the internet website of the Centers for Medicare & Medicaid Services. (iii) Confidentiality In making data available under this subparagraph, the Secretary shall have in place procedures to safeguard the privacy of any individually identifiable enrollee information. .\n##### (b) Rule of construction\nNothing in the amendments made by this section shall affect the collection of information as proposed pursuant to the notice entitled Agency Information Collection Activities: Proposed Collection; Comment Request , published in the Federal Register on March 14, 2023 (88 Fed. Reg. 15726).",
      "versionDate": "2025-09-10",
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
        "updateDate": "2025-09-24T14:07:06Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5243ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to increase data transparency for supplemental benefits under Medicare Advantage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T11:18:18Z"
    },
    {
      "title": "To amend title XVIII of the Social Security Act to increase data transparency for supplemental benefits under Medicare Advantage.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T08:06:08Z"
    }
  ]
}
```
