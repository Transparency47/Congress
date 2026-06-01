# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4078?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4078
- Title: Stop Unlawful Detention and End Mistreatment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4078
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2026-05-16T08:07:58Z
- Update date including text: 2026-05-16T08:07:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-06-23: Introduced in House

## Actions

- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4078",
    "number": "4078",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "F000476",
        "district": "10",
        "firstName": "Maxwell",
        "fullName": "Rep. Frost, Maxwell [D-FL-10]",
        "lastName": "Frost",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Stop Unlawful Detention and End Mistreatment Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:58Z",
    "updateDateIncludingText": "2026-05-16T08:07:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-24T20:26:47Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-23T16:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "FL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "AZ"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4078ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4078\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mr. Frost (for himself, Ms. Wasserman Schultz , and Mr. Espaillat ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Homeland Security to establish a publicly available online immigration detention database, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Unlawful Detention and End Mistreatment Act of 2025 .\n#### 2. Immigration detention database\n##### (a) In general\nThe Secretary of Homeland Security shall establish a publicly available, online database that includes the following:\n**(1)**\nWith respect to any individual in the custody of U.S. Immigration and Customs Enforcement, the following information:\n**(A)**\nThe legal authority under which the individual is being detained.\n**(B)**\nThe duration for which the individual has been detained.\n**(C)**\nThe location where the individual is being detained, except in the case of a minor, an individual whose location may not be disclosed pursuant to a protection order, or an individual who is a participant in a witness protection program.\n**(D)**\nWhether the individual has been transferred to a different location after being so detained, and the number of such transfers.\n**(E)**\nWhether the individual is subject to an order of removal.\n**(2)**\nWith respect to the population of individuals in the custody of U.S. Immigration and Customs Enforcement, the following information:\n**(A)**\nDemographic information about the population of individuals detained, including nationality, age, status under the immigration laws.\n**(B)**\nAny disciplinary actions taken against such an individual, including any use of force or transfer of such an individual to another location.\n**(C)**\nAny deportations of such individuals.\n**(3)**\nWith respect to each non-traditional location described in subsection (d) at which an individual in the custody of U.S. Immigration and Customs Enforcement is detained, the following information:\n**(A)**\nThe type and specific location for the nontraditional detention location.\n**(B)**\nA justification for utilization.\n**(C)**\nThe number of detention beds that will be utilized.\n**(D)**\nDetails of efforts to ensure compliance with all reporting, access, and due process requirements.\n**(E)**\nA copy of detention standard of care that will be applied, including facilitation of access to medical services.\n**(F)**\nA timeline, estimated costs, budget, and utilized funds.\n**(G)**\nA copy of any agreements for use of the nontraditional location, including a record of any funding or proposed payments.\n**(4)**\nAny open or unresolved recommendations of the Office of the Immigration Detention Ombudsman, the Office for Civil Rights and Civil Liberties of the Department of Homeland Security, the Office of the Inspector General of the Department of Homeland Security, or the Government Accountability Office, along with the projected timeline of U.S. Immigration and Customs Enforcement for implementing such recommendation, or the rationale determining not to adopt the recommendation.\n##### (b) Updates\nThe database established under subsection (a) shall be updated on a daily basis. Information for previous days shall be archived and made available on an annual basis.\n##### (c) No personally identifiable information\nThe database established under subsection (a) shall not include any personally identifiable information of any individual in the custody of U.S. Immigration and Customs Enforcement.\n##### (d) Non-Traditional locations described\nA non-traditional location described in this subsection is any of the following:\n**(1)**\nAny building, grounds, or property under the jurisdiction, custody, or control of the Department of Defense.\n**(2)**\nAny building, grounds, or property located on Indian lands (as such term is defined in section 502.12 of title 25, Code of Federal Regulations).\n**(3)**\nAny lands outside the external boundary of the continental United States.\n#### 3. Continued operation of the Office of the Immigration Detention Ombudsman and the Office for Civil Rights and Civil Liberties of the Department of Homeland Security\nSubject to the availability of appropriations, the Secretary of Homeland Security may not discontinue or reduce the operation of either the Office of the Immigration Detention Ombudsman or the Office for Civil Rights and Civil Liberties of the Department of Homeland Security.",
      "versionDate": "2025-06-23",
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
        "name": "Immigration",
        "updateDate": "2025-07-17T10:36:52Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4078ih.xml"
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
      "title": "Stop Unlawful Detention and End Mistreatment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Unlawful Detention and End Mistreatment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T13:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Homeland Security to establish a publicly available online immigration detention database, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T13:48:20Z"
    }
  ]
}
```
