# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6906?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6906
- Title: Protecting Patients from Rehab Fraud Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6906
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-22T16:09:30Z
- Update date including text: 2026-01-22T16:09:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6906",
    "number": "6906",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Protecting Patients from Rehab Fraud Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-22T16:09:30Z",
    "updateDateIncludingText": "2026-01-22T16:09:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:08:25Z",
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
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "OR"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6906ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6906\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Vindman (for himself, Mr. Bentz , and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Attorney General and the Comptroller General of the United States to submit to Congress reports on the drug addiction treatment and recovery industry.\n#### 1. Short title\nThis Act may be cited as the Protecting Patients from Rehab Fraud Act of 2025 .\n#### 2. Reports on the drug addiction treatment and recovery industry\n##### (a) DOJ report\nNot later than 1 year after the date of the enactment of this Act, the Attorney General shall submit to Congress a report on the drug addiction treatment and recovery industry. Such report shall include the following:\n**(1)**\nThe prevalence of entities using illegal tactics to entice individuals to enter a rehabilitation facility.\n**(2)**\nThe prevalence of insurance fraud in plans offered through an Exchange established under the Patient Protection and Affordable Care Act relating to individuals housed in such facilities.\n**(3)**\nThe practice of brokers encouraging patients to commit insurance fraud to enroll in high-cost out-of-network insurance plans.\n**(4)**\nThe prevalence of drug use and trafficking within these facilities.\n**(5)**\nThe practice of patient dumping, also known as curbing, by which patients are removed from a facility and abandoned once their insurer no longer pays the facility.\n**(6)**\nThe prevalence of patients being dumped in places other than the original location they came from to attend such a facility.\n**(7)**\nAny research on the prevalence of homelessness and relapse among individuals who are dumped.\n**(8)**\nRecommendations for Congress to crack down on illegal practices and false dealing in the rehabilitation industry and protect prospective patients seeking rehabilitation.\n##### (b) GAO report\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on the drug addiction treatment and recovery industry. Such report shall include the following:\n**(1)**\nThe actions currently being undertaken by the Secretary of Health and Human Services and other Federal actors to curb the type of insurance fraud described in subsection (a)(2).\n**(2)**\nThe actions currently being undertaken by States to curb this type of insurance fraud.\n**(3)**\nThe extent and effectiveness of Federal expenditures for rehabilitation facilities to date.\n**(4)**\nRecommendations for Congress to crack down on illegal practices and false dealing in the rehabilitation industry and protect prospective patients seeking rehabilitation.",
      "versionDate": "2025-12-18",
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
        "updateDate": "2026-01-22T16:09:29Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6906ih.xml"
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
      "title": "Protecting Patients from Rehab Fraud Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Patients from Rehab Fraud Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Attorney General and the Comptroller General of the United States to submit to Congress reports on the drug addiction treatment and recovery industry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:18Z"
    }
  ]
}
```
