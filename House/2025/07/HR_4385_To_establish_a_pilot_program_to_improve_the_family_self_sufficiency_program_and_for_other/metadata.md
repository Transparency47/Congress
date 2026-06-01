# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4385?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4385
- Title: Helping More Families Save Act
- Congress: 119
- Bill type: HR
- Bill number: 4385
- Origin chamber: House
- Introduced date: 2025-07-14
- Update date: 2026-03-19T08:07:21Z
- Update date including text: 2026-03-19T08:07:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-14: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-07-14: Introduced in House

## Actions

- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4385",
    "number": "4385",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Helping More Families Save Act",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:21Z",
    "updateDateIncludingText": "2026-03-19T08:07:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-14",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T16:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "SC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "IA"
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
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "LA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "OH"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "GA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4385ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4385\nIN THE HOUSE OF REPRESENTATIVES\nJuly 14, 2025 Mr. Torres of New York (for himself and Mr. Timmons ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo establish a pilot program to improve the family self-sufficiency program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping More Families Save Act .\n#### 2. Family self-sufficiency escrow expansion pilot program\nSection 23 of the United States Housing Act of 1937 ( 42 U.S.C. 1437u ) is amended by adding at the end the following:\n(p) Escrow expansion pilot program (1) Definitions In this subsection: (A) Covered family The term covered family means a family that receives assistance under section 8 or 9 of this Act and is enrolled in the pilot program. (B) Eligible entity The term eligible entity means an entity described in subsection (c)(2). (C) Pilot program The term pilot program means the pilot program established under paragraph (2). (D) Welfare assistance The term welfare assistance has the meaning given the term in section 984.103 of title 24, Code of Federal Regulations, or any successor regulation. (2) Establishment The Secretary shall establish a pilot program under which the Secretary shall select not more than 25 eligible entities to establish and manage escrow accounts for not more than 5,000 covered families, in accordance with this subsection. (3) Escrow accounts (A) In general An eligible entity selected to participate in the pilot program\u2014 (i) shall establish an interest-bearing escrow account and place into the account an amount equal to any increase in the amount of rent paid by each covered family in accordance with the provisions of section 3, 8(o), or 8(y), as applicable, that is attributable to increases in earned income by the covered families during the participation of each covered family in the pilot program; and (ii) notwithstanding any other provision of law, may use funds it controls under section 8 or 9 for purposes of making the escrow deposit for covered families assisted under, or residing in units assisted under, section 8 or 9 of this title, respectively, provided such funds are offset by the increase in the amount of rent paid by the covered family. (B) Income limitation An eligible entity may not escrow any amounts for any covered family whose adjusted income exceeds 80 percent of the area median income. (C) Withdrawals A covered family shall be able to withdraw funds, including interest earned, from an escrow account established by an eligible entity under the pilot program\u2014 (i) after the covered family ceases to receive welfare assistance; and (ii) (I) not earlier than the date that is 5 years after the date on which the eligible entity establishes the escrow account under this subsection; (II) not later than the date that is 7 years after the date on which the eligible entity establishes the escrow account under this subsection, if the covered family chooses to continue to participate in the pilot program after the date that is 5 years after the date on which the eligible entity establishes the escrow account; (III) on the date the covered family ceases to receive housing assistance under section 8 or 9, if such date is earlier than 5 years after the date on which the eligible entity establishes the escrow account; (IV) earlier than 5 years after the date on which the eligible entity establishes the escrow account, if the covered family is using the funds to advance a self-sufficiency goal as approved by the eligible entity; or (V) under other circumstances in which the Secretary determines an exemption for good cause is warranted. (D) Interim recertification For purposes of the pilot program, a covered family may recertify the income of the covered family multiple times per year, as determined by the Secretary, and not fewer than once per year. (E) Contract or plan A covered family is not required to complete a standard contract of participation or an individual training and services plan in order to participate in the pilot program. (4) Effect of increases in family income Any increase in the earned income of a covered family during the enrollment of the family in the pilot program may not be considered as income or a resource for purposes of eligibility of the family for other benefits, or amount of benefits payable to the family, under any program administered by the Secretary. (5) Application (A) In general An eligible entity seeking to participate in the pilot program shall submit to the Secretary an application\u2014 (i) at such time, in such manner, and containing such information as the Secretary may require by notice; and (ii) that includes the number of proposed covered families to be served by the eligible entity under this subsection. (B) Geographic and entity variety The Secretary shall ensure that eligible entities selected to participate in the pilot program\u2014 (i) are located across various States and in both urban and rural areas; and (ii) vary by size and type, including both public housing agencies and private owners of projects receiving project-based rental assistance under section 8. (6) Notification and opt-out An eligible entity participating in the pilot program shall\u2014 (A) notify covered families of their enrollment in the pilot program; (B) provide covered families with a detailed description of the pilot program, including how the pilot program will impact their rent and finances; (C) inform covered families that the families cannot simultaneously participate in the pilot program and the Family Self-Sufficiency program under this section; and (D) provide covered families with the ability to elect not to participate in the pilot program\u2014 (i) not less than 2 weeks before the date on which the escrow account is established under paragraph (3); and (ii) at any point during the duration of the pilot program. (7) Maximum rents During the term of participation by a covered family in the pilot program, the amount of rent paid by the covered family shall be calculated under the rental provisions of section 3 or 8(o), as applicable. (8) Pilot program timeline (A) Awards Not later than 18 months after the date of enactment of this subsection, the Secretary shall select the eligible entities to participate in the pilot program. (B) Establishment and term of accounts An eligible entity selected to participate in the pilot program shall\u2014 (i) not later than 6 months after selection, establish escrow accounts under paragraph (3) for covered families; and (ii) maintain those escrow accounts for not less than 5 years, or until the date the family ceases to receive assistance under section 8 or 9, and, at the discretion of the covered family, not more than 7 years after the date on which the escrow account is established. (9) Nonparticipation and housing assistance (A) In general Assistance under section 8 or 9 for a family that elects not to participate in the pilot program shall not be delayed or denied by reason of such election. (B) No termination Housing assistance may not be terminated as a consequence of participating, or not participating, in the pilot program under this subsection for any period of time. (10) Study Not later than 8 years after the date the Secretary selects eligible entities to participate in the pilot program under this subsection, the Secretary shall conduct a study and submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report on outcomes for covered families under the pilot program, which shall evaluate the effectiveness of the pilot program in assisting families to achieve economic independence and self-sufficiency, and the impact coaching and supportive services, or the lack thereof, had on individual incomes. (11) Waivers To allow selected eligible entities to effectively administer the pilot program and make the required escrow account deposits under this subsection, the Secretary may waive requirements under this section. (12) Termination The pilot program under this subsection shall terminate on the date that is 10 years after the date of enactment of this subsection. (13) Authorization of appropriations (A) In general There is authorized to be appropriated to the Secretary for fiscal year 2026 $5,000,000\u2014 (i) for technical assistance related to implementation of the pilot program; and (ii) to carry out an evaluation of the pilot program under paragraph (10). (B) Availability Any amounts appropriated under this subsection shall remain available until expended. .",
      "versionDate": "2025-07-14",
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
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1666-1667)"
      },
      "number": "970",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Helping More Families Save Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-01",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 143."
      },
      "number": "2651",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ROAD to Housing Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-11T16:45:08Z"
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
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4385ih.xml"
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
      "title": "Helping More Families Save Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T11:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping More Families Save Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T11:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a pilot program to improve the family self-sufficiency program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T11:33:23Z"
    }
  ]
}
```
