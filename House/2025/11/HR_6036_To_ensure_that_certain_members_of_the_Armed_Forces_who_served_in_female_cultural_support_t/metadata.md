# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6036?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6036
- Title: To ensure that certain members of the Armed Forces who served in female cultural support teams receive proper credit for such service.
- Congress: 119
- Bill type: HR
- Bill number: 6036
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2025-12-20T09:07:03Z
- Update date including text: 2025-12-20T09:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-12 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-12 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6036",
    "number": "6036",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To ensure that certain members of the Armed Forces who served in female cultural support teams receive proper credit for such service.",
    "type": "HR",
    "updateDate": "2025-12-20T09:07:03Z",
    "updateDateIncludingText": "2025-12-20T09:07:03Z"
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
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-20T18:33:16Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-12T17:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "IA"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CO"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "PA"
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
      "sponsorshipDate": "2025-12-03",
      "state": "VA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-19",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6036ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6036\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Issa (for himself, Mrs. Miller-Meeks , Mr. Crow , and Ms. Houlahan ) introduced the following bill; which was referred to the Committee on Veterans' Affairs , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo ensure that certain members of the Armed Forces who served in female cultural support teams receive proper credit for such service.\n#### 1. Credit for certain members of the Armed Forces who served in female cultural support teams\n##### (a) Military service: records; calculation of retired pay\nNot later than one year after the date of the enactment of this Act, the Secretary concerned shall ensure that the performance of covered service is included in\u2014\n**(1)**\nthe military service record of each individual who performed covered service; and\n**(2)**\nthe computation of retired pay for each individual who performed covered service.\n##### (b) Claims for veterans benefits arising from covered service\n**(1) Determination of service connection**\nUpon the filing of a claim by an individual for service-connected disability or death incurred or aggravated in the course of covered service, the Secretary of Veterans Affairs shall determine whether such disability or death was service-connected.\n**(2) Treatment of covered service**\nIn the consideration of a claim under this subsection, the Secretary shall treat covered service as engagement in combat with the enemy in the course of active military, naval, air, or space service.\n**(3) Effective date of award**\nExcept as provided by subparagraph (B), the effective date of an award under this subsection shall be determined in accordance with section 5110 of title 38, United States Code.\n**(4) Processing of claims**\nThe Secretary of Veterans Affairs, in consultation with the Secretary of Defense, shall improve training and guidance for employees who may process a claim under this subsection.\n**(5) Outreach**\nThe Secretary shall conduct outreach to inform individuals who performed covered service (and survivors of such individuals) that they may submit supplemental claims for service-connected disability or death incurred or aggravated in the course of covered service. Such outreach shall include the following:\n**(A)**\nThe Secretary shall publish on the internet website of the Department a notice that such individuals may elect to file a supplemental claim.\n**(B)**\nThe Secretary shall notify, in writing or by electronic means, veterans service organizations of the ability of such individuals to file a supplemental claim.\n##### (c) Study and report on certain members of the Armed Forces\n**(1) Study**\nThe Secretary of Defense, in collaboration with the Secretary of Veterans Affairs, shall conduct a study to identify the size and number of groups of individuals who\u2014\n**(A)**\nperformed service as a member of the Armed Forces that the Secretary of Defense and Secretary of Veterans Affairs determine is substantially similar to covered service; and\n**(B)**\nhave a military service record that does not include such service as a member of the Armed Forces.\n**(2) Report**\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense and the Secretary of Veterans Affairs shall submit to Congress a report that includes the findings of the study under paragraph (1).\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term covered service means service\u2014\n**(A)**\nas a member of the Armed Forces;\n**(B)**\nin a female cultural support team;\n**(C)**\nwith the personnel development skill identifier of R2J or 5DK; and\n**(D)**\nduring the period beginning on January 1, 2010, and ending on August 31, 2021.\n**(2)**\nThe terms active military, naval, air, or space service and service-connected have the meanings given such terms in section 101 of title 38, United States Code.\n**(3)**\nThe term Secretary concerned has the meaning given such term in section 101 of title 10, United States Code.\n#### 2. Report on certain claims for service-connected disability\n##### (a) Report required\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report regarding covered claims. Such report shall include the numbers of covered claims, disaggregated by gender of the claimant and whether the military service record of the claimant includes a combat identifier, that, respectively\u2014\n**(1)**\nwere submitted;\n**(2)**\nwere granted;\n**(3)**\nwere denied;\n**(4)**\nwere unresolved; or\n**(5)**\nwere appealed.\n##### (b) Definitions\nIn this section:\n**(1)**\nThe term covered claim means a claim\u2014\n**(A)**\nfor service-connected disability;\n**(B)**\non the basis of post-traumatic stress disorder or traumatic brain injury; and\n**(C)**\nsubmitted to the Secretary of Veterans Affairs on or after January 1, 1990.\n**(2)**\nThe term service-connected has the meaning given such term in section 101 of title 38, United States Code.\n#### 3. Modification of certain housing loan fees\nThe loan fee table in section 3729(b)(2) of title 38, United States Code, is amended by striking November 15, 2031 each place it appears and inserting December 3, 2031 .",
      "versionDate": "2025-11-12",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-18T16:26:21Z"
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
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6036ih.xml"
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
      "title": "To ensure that certain members of the Armed Forces who served in female cultural support teams receive proper credit for such service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-18T09:18:19Z"
    },
    {
      "title": "To ensure that certain members of the Armed Forces who served in female cultural support teams receive proper credit for such service.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T09:05:49Z"
    }
  ]
}
```
