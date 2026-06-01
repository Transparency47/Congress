# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5109?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5109
- Title: To require the Administrator of the Transportation Security Administration of the United States to develop guidelines to improve returning citizens' access to the Transportation Worker Identification Credential program, to assist individuals in custody of Federal, State, and local prisons in pre-applying or preparing applications for Transportation Worker Identification Credential cards, and to assist individuals requesting an appeal or waiver of preliminary determination of ineligibility, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5109
- Origin chamber: House
- Introduced date: 2025-09-03
- Update date: 2026-05-16T08:06:58Z
- Update date including text: 2026-05-16T08:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-09-04 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2025-09-03: Introduced in House

## Actions

- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-09-04 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5109",
    "number": "5109",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001125",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Carter, Troy A. [D-LA-2]",
        "lastName": "Carter",
        "party": "D",
        "state": "LA"
      }
    ],
    "title": "To require the Administrator of the Transportation Security Administration of the United States to develop guidelines to improve returning citizens' access to the Transportation Worker Identification Credential program, to assist individuals in custody of Federal, State, and local prisons in pre-applying or preparing applications for Transportation Worker Identification Credential cards, and to assist individuals requesting an appeal or waiver of preliminary determination of ineligibility, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-16T08:06:58Z",
    "updateDateIncludingText": "2026-05-16T08:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-04T04:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "LA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MS"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "MS"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "TX"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5109ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5109\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 3, 2025 Mr. Carter of Louisiana (for himself and Mr. Higgins of Louisiana ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo require the Administrator of the Transportation Security Administration of the United States to develop guidelines to improve returning citizens\u2019 access to the Transportation Worker Identification Credential program, to assist individuals in custody of Federal, State, and local prisons in pre-applying or preparing applications for Transportation Worker Identification Credential cards, and to assist individuals requesting an appeal or waiver of preliminary determination of ineligibility, and for other purposes.\n#### 1. Findings\nCongress finds the following:\n**(1)**\nThe Maritime Transportation Security Act of 2002 (in this Act referred to as MTSA ) was introduced following the terrorist attacks on September 11, 2001, and became Public Law 107\u2013295 in 2002.\n**(2)**\nThe MTSA provided that Transportation Worker Identification Credential cards (in this Act referred to as TWIC cards ) were to be issued to workers who require access to secure areas of the Nation\u2019s maritime facilities and vessels.\n**(3)**\nThe Transportation Security Administration (in this Act referred to as TSA ) and the United States Coast Guard jointly administer the TWIC card program.\n**(4)**\nCongress passed statutes for the TWIC program that authorize the Department of Homeland Security and the Transportation Security Administration to review an applicant\u2019s request for an appeals or waiver if the Transportation Security Administration determines that the individual may pose a security risk.\n**(5)**\nAt year end 2021, the United States prison population was 1,204,300, a 25 percent decrease since 2011.\n**(6)**\nThe Louisiana Department of Public Safety and Corrections releases over 13,000 individuals back into the community each year and supervises over 44,000 individuals.\n**(7)**\nSecuring a TWIC card as soon as possible after release may provide for more opportunities for employment.\n**(8)**\nAccording to the Ports Association of Louisiana, 525,000 jobs in Louisiana are tied to the State\u2019s ports, and there are over 260,000 jobs in Louisiana related to the oil and gas industry, many of which require a valid TWIC card.\n**(9)**\nAccording to the American Association of Port Authorities, between 2014 and 2018, the total number of jobs supported by cargo moving through the America\u2019s deep-draft ports increased by more than one-third, from 23,100,000 jobs to 30,800,000.\n**(10)**\nThe total economic value that United States coastal ports provide in terms of revenue to businesses, personal income and economic output by exporters and importers rose 17 percent from $4,600,000,000 to $5,400,000,000, representing nearly 26 percent of the nation\u2019s economy.\n**(11)**\nAccording to a Homeland Security Operational Analysis Center (HSOAC) 2019 Comprehensive Security Assessment of the TWIC Program, MTSA affects approximately 13,825 vessels, 3,270 facilities, and 56 Outer Continental Shelf facilities.\n**(12)**\nAccording to TSA\u2019s Transportation Worker Identification Credential Appeal Timelines Fiscal Year 2019 Report to Congress , 2,300,000 people nationwide hold the credential, which is valid for 5 years.\n**(13)**\nEmployment is critical to the success of those on supervision and studies show that unemployment is a major predictor of recidivism.\n**(14)**\nIt is critical to national security to protect and secure the Nation\u2019s maritime facilities and vessels through the TWIC card process.\n**(15)**\nIt is also critical that opportunities are available to those who have demonstrated rehabilitation and are seeking a second chance.\n**(16)**\nBrennan Center for Justice 2015 report found that between 70,000,000 to 100,000,000 U.S. residents, a median of 27 percent, have criminal records.\n**(17)**\nHSOAC\u2019s 2019 Comprehensive Security Assessment estimates that between 99.99997 percent and 99.997 percent of the United States population are not terrorists and asserts that Few people with risk factors engage in terrorism, meaning that the great majority of people with disqualifying criminal histories present no terrorism risk. .\n**(18)**\nAccording to TSA, individuals in the custody of Federal, State, and local prisons are not eligible to apply for a TWIC card until after they have been released from custody.\n**(19)**\nTSA may issue TWIC cards under the current regulations to individuals with certain felony convictions through the waiver process.\n**(20)**\nThe appeal and waiver process may take up to 90 days, depending on the applicant\u2019s response and supporting documentation, the complexity of the applicant\u2019s case, and response time for TSA to review conviction details, circumstances, proof of rehabilitation, and whether the person is in the process of rehabilitation before issuing a waiver.\n**(21)**\nBased on a sample verified by TSA, approximately 98 percent of total applicants are issued a TWIC card, including initial and redress cases, and approximately 62 percent of applicants do not respond to redress.\n**(22)**\nApplying for a TWIC card and beginning the appeal and waiver process prior to a person\u2019s release from Federal, State, and local prisons may increase chances of employment shortly after release.\n#### 2. Discussion on development of guidelines and procedures\n##### (a) In general\nThe Administrator of the Transportation Security Administration shall develop guidelines to improve returning citizens\u2019 access to the TWIC program.\n##### (b) Guidelines\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Transportation Security Administration shall develop guidelines to assist individuals in custody of Federal, State, and local prisons in pre-applying or preparing applications for TWIC cards and guidelines to assist individuals requesting an appeal or waiver of preliminary determination of ineligibility for TWIC cards.\n##### (c) Briefing\nNot later than 1 year after the date of enactment of this Act, the Transportation Security Administration of the United States shall brief Congress on improvements to addressing access to the TWIC program.\n##### (d) Transmission\nThe clerk of the House of Representatives shall transit a copy of this Act to the Committee on Homeland Security and Governmental Affairs of the Senate, the Committee on Homeland Security of the House of Representatives, the Committee on Health, Education, Labor, and Pensions of the Senate, the Committee on Education and Workforce of the House of Representatives, the Secretary of Homeland Security, the Administrator of the Transportation Security Administration, and the presiding officers of the Senate and House of Representatives of the United States.",
      "versionDate": "2025-09-03",
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
        "updateDate": "2025-09-22T14:06:57Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5109ih.xml"
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
      "title": "To require the Administrator of the Transportation Security Administration of the United States to develop guidelines to improve returning citizens' access to the Transportation Worker Identification Credential program, to assist individuals in custody of Federal, State, and local prisons in pre-applying or preparing applications for Transportation Worker Identification Credential cards, and to assist individuals requesting an appeal or waiver of preliminary determination of ineligibility, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:20Z"
    },
    {
      "title": "To require the Administrator of the Transportation Security Administration of the United States to develop guidelines to improve returning citizens' access to the Transportation Worker Identification Credential program, to assist individuals in custody of Federal, State, and local prisons in pre-applying or preparing applications for Transportation Worker Identification Credential cards, and to assist individuals requesting an appeal or waiver of preliminary determination of ineligibility, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-04T08:06:21Z"
    }
  ]
}
```
