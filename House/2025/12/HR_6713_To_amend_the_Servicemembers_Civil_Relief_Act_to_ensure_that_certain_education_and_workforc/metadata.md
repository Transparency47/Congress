# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6713?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6713
- Title: Protect Veteran Students, Job Seekers, and Entrepreneurs Housing Act
- Congress: 119
- Bill type: HR
- Bill number: 6713
- Origin chamber: House
- Introduced date: 2025-12-15
- Update date: 2026-01-22T09:06:12Z
- Update date including text: 2026-01-22T09:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-15 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-12-15: Introduced in House

## Actions

- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-15 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6713",
    "number": "6713",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Protect Veteran Students, Job Seekers, and Entrepreneurs Housing Act",
    "type": "HR",
    "updateDate": "2026-01-22T09:06:12Z",
    "updateDateIncludingText": "2026-01-22T09:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
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
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T17:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-15T18:13:17Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6713ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6713\nIN THE HOUSE OF REPRESENTATIVES\nDecember 15, 2025 Mr. Espaillat introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend the Servicemembers Civil Relief Act to ensure that certain education and workforce development benefits administered by the Secretary of Veterans Affairs are treated as income by landlords evaluating the ability of a servicemember, veteran, or a spouse or child of a servicemember or veteran, to pay rent, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Veteran Students, Job Seekers, and Entrepreneurs Housing Act .\n#### 2. Treatment of certain Department of Veterans Affairs benefits in determining income for purposes of entering into residential leases\n##### (a) In general\nTitle III of the Servicemembers Civil Relief Act ( 50 U.S.C. 3951 et seq. ) is amended by adding at the end the following new section (and conforming the table of contents at the beginning of such Act accordingly):\n309. Treatment of certain Department of Veterans Affairs benefits in determining income for purposes of entering into residential leases (a) Protection In determining whether a covered individual has an income sufficient to enter into a lease of premises for a residential purpose, the landlord (or other person with paramount title) of the premises shall treat any educational assistance received by the covered individual under any of chapter 30, 31, 32, 33, 34, 35, or 36 of title 38, United States Code, or chapter 1606 or 1607 of title 10, United States Code, as income. (b) Lease period When entering into a lease of premises for a residential purpose with a covered individual pursuant to subsection (a), the landlord (or other person with paramount title) shall guarantee that the period of the lease does not exceed the number of months of entitlement the individual has for the educational assistance described in such subsection. (c) Penalties (1) A landlord (or other person with paramount title) who knowingly takes an action contrary to this section, or attempts to do so, may not participate in a covered Federally assisted rental housing program. (2) A person who knowingly takes an action contrary to this section, or attempts to do so, shall be fined as provided in title 18, United States Code, or imprisoned for not more than one year, or both. (d) Definitions In this section: (1) The term covered individual means a servicemember, veteran, or a spouse or child of a servicemember or veteran, who is entitled to educational assistance under chapter 30, 31, 32, 33, 34, 35, or 36 of title 38, United States Code, or chapter 1606 or 1607 of title 10, United States Code. (2) The term covered Federally assisted rental housing means a residential dwelling unit that is made available for rental and for which assistance is provided, or that is part of a housing project for which assistance is provided, under any program administered by the Secretary of Housing and Urban Development, the Secretary of Veterans Affairs (other than stipends made in connection with educational assistance), the Secretary of Agriculture, or the Secretary of the Treasury, including\u2014 (A) the public housing program under the United States Housing Act of 1937 ( 42 U.S.C. 1437 et seq. ); (B) the program for rental assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ); (C) the HOME Investment Partnerships program under title II of the Cranton-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12721 et seq. ); (D) title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 et seq. ); (E) housing assistance for homeless veterans under section 2041 of title 38, United States Code; (F) the Housing Trust Fund program under section 1338 of the Housing and Community Development Act of 1992 ( 12 U.S.C. 4568 ); (G) the program for supportive housing for the elderly under section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q ); (H) the program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 ); (I) the AIDS Housing Opportunities program under subtitle D of title VIII of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12901 et seq. ); (J) the program for Native American housing under the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4101 et seq. ); (K) the program for housing assistance for Native Hawaiians under title VIII of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4221 et seq. ); (L) the programs for assistance for rural rental housing under title V of the Housing Act of 1949 ( 42 U.S.C. 1471 et seq. ); and (M) the low-income housing tax credit program under section 42 of the Internal Revenue Code. .\n##### (b) Extended grace period To maintain benefits\nChapter 36 of title 38, United States Code, is amended by adding at the end the following new section (and conforming the table of sections at the beginning of such chapter accordingly):\n3699C. Grace period for individuals to maintain benefits (a) Requirement If the Secretary determines that a covered individual is not eligible for educational assistance described in subsection (b)(1) by reason of the covered individual failing to fulfill a single program requirement, the Secretary may not terminate the individual from using such assistance until\u2014 (1) the Secretary notifies the individual of such failure; and (2) a period of 60 days has elapsed following such notification. (b) Definitions In this section: (1) The term covered individual means an individual who is entitled to educational assistance under chapter 30, 31, 32, 33, 34, 35, or 36 of this title or chapter 1606 or 1607 of title 10. (2) The term program requirement means a requirement to participate in educational assistance described in paragraph (1) relating to any of the following: (A) Missing a recertification appointment. (B) Withdrawing from a class. (C) With respect to a dependent, the death of the veteran. (D) Loss of employment. (E) Any other requirement the Secretary determines appropriate. .",
      "versionDate": "2025-12-15",
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
        "updateDate": "2026-01-06T17:01:07Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6713ih.xml"
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
      "title": "Protect Veteran Students, Job Seekers, and Entrepreneurs Housing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T08:42:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Veteran Students, Job Seekers, and Entrepreneurs Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T08:42:11Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Servicemembers Civil Relief Act to ensure that certain education and workforce development benefits administered by the Secretary of Veterans Affairs are treated as income by landlords evaluating the ability of a servicemember, veteran, or a spouse or child of a servicemember or veteran, to pay rent, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T08:33:52Z"
    }
  ]
}
```
