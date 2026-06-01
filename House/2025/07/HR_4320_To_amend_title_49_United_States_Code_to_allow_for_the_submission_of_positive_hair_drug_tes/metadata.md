# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4320?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4320
- Title: Drug and Alcohol Clearinghouse Public Safety Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4320
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-04-29T08:07:08Z
- Update date including text: 2026-04-29T08:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-11 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-11 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4320",
    "number": "4320",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001087",
        "district": "1",
        "firstName": "Eric",
        "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
        "lastName": "Crawford",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Drug and Alcohol Clearinghouse Public Safety Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-29T08:07:08Z",
    "updateDateIncludingText": "2026-04-29T08:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-11",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:07:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-11T16:59:29Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
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
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4320ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4320\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Crawford introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to allow for the submission of positive hair drug test results to the Drug and Alcohol Clearinghouse of the Federal Motor Carrier Safety Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drug and Alcohol Clearinghouse Public Safety Improvement Act of 2025 .\n#### 2. Submission of hair drug test results to Drug and Alcohol Clearinghouse\n##### (a) In general\nSection 31306a of title 49, United States Code, is amended by adding the following new subsection:\n(n) Submission of hair drug test results to Drug and Alcohol Clearinghouse (1) Hair drug test The Secretary shall require a motor carrier, as such term is defined in section 13102, using vehicles weighing not less than 10,000 pounds to promptly submit to the Drug and Alcohol Clearinghouse any record of a positive hair drug test result from a preemployment drug test or a random drug test that is administered through a covered device. (2) Laboratory requirements Any hair drug test result submitted under paragraph (1) shall be from a laboratory that\u2014 (A) is accredited by the College of American Pathologists for forensic hair drug testing; and (B) incorporates, if available, Department of Health and Human Services scientific and technical guidelines for hair testing. (3) Covered device In this subsection, the term covered device means a device that is cleared under section 510(k) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360(k) ). .\n##### (b) Regulations\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation shall issue such regulations as are necessary to carry out the amendment in this section, including updating section 382.107 of title 49, Code of Federal Regulations, to include hair drug test results described in such amendment in the definition of actual knowledge.",
      "versionDate": "2025-07-10",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-04T13:53:06Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4320ih.xml"
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
      "title": "Drug and Alcohol Clearinghouse Public Safety Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Drug and Alcohol Clearinghouse Public Safety Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to allow for the submission of positive hair drug test results to the Drug and Alcohol Clearinghouse of the Federal Motor Carrier Safety Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T02:03:46Z"
    }
  ]
}
```
