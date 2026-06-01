# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/970?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/970
- Title: Helping More Families Save Act
- Congress: 119
- Bill type: S
- Bill number: 970
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2025-12-18T12:03:18Z
- Update date including text: 2025-12-18T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1666-1667)
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1666-1667)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/970",
    "number": "970",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Helping More Families Save Act",
    "type": "S",
    "updateDate": "2025-12-18T12:03:18Z",
    "updateDateIncludingText": "2025-12-18T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1666-1667)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T22:30:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "AL"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "VA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "ID"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "DE"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s970is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 970\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Reed (for himself and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish a pilot program to improve the family self-sufficiency program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping More Families Save Act .\n#### 2. Family self-sufficiency escrow expansion pilot program\nSection 23 of the United States Housing Act of 1937 ( 42 U.S.C. 1437u ) is amended by adding at the end the following:\n(p) Escrow expansion pilot program (1) Definitions In this subsection: (A) Covered family The term covered family means a family that receives assistance under section 8 or 9 of this Act and is enrolled in the pilot program. (B) Eligible entity The term eligible entity means an entity described in subsection (c)(2). (C) Pilot program The term pilot program means the pilot program established under paragraph (2). (D) Welfare assistance The term welfare assistance has the meaning given the term in section 984.103 of title 24, Code of Federal Regulations, or any successor regulation. (2) Establishment The Secretary shall establish a pilot program under which the Secretary shall select not more than 25 eligible entities to establish and manage escrow accounts for not more than 5,000 covered families, in accordance with this subsection. (3) Escrow accounts (A) In general An eligible entity selected to participate in the pilot program\u2014 (i) shall establish an interest-bearing escrow account and place into the account an amount equal to any increase in the amount of rent paid by each covered family in accordance with the provisions of section 3, 8(o), or 8(y), as applicable, that is attributable to increases in earned income by the covered families during the participation of each covered family in the pilot program; and (ii) notwithstanding any other provision of law, may use funds it controls under section 8 or 9 for purposes of making the escrow deposit for covered families assisted under, or residing in units assisted under, section 8 or 9 of this title, respectively, provided such funds are offset by the increase in the amount of rent paid by the covered family. (B) Income limitation An eligible entity may not escrow any amounts for any covered family whose adjusted income exceeds 80 percent of the area median income. (C) Withdrawals A covered family shall be able to withdraw funds, including interest earned, from an escrow account established by an eligible entity under the pilot program\u2014 (i) after the covered family ceases to receive welfare assistance; and (ii) (I) not earlier than the date that is 5 years after the date on which the eligible entity establishes the escrow account under this subsection; (II) not later than the date that is 7 years after the date on which the eligible entity establishes the escrow account under this subsection, if the covered family chooses to continue to participate in the pilot program after the date that is 5 years after the date on which the eligible entity establishes the escrow account; (III) on the date the covered family ceases to receive housing assistance under section 8 or 9, if such date is earlier than 5 years after the date on which the eligible entity establishes the escrow account; (IV) earlier than 5 years after the date on which the eligible entity establishes the escrow account, if the covered family is using the funds to advance a self-sufficiency goal as approved by the eligible entity; or (V) under other circumstances in which the Secretary determines an exemption for good cause is warranted. (D) Interim recertification For purposes of the pilot program, a covered family may recertify the income of the covered family multiple times per year, as determined by the Secretary, and not fewer than once per year. (E) Contract or plan A covered family is not required to complete a standard contract of participation or an individual training and services plan in order to participate in the pilot program. (4) Effect of increases in family income Any increase in the earned income of a covered family during the enrollment of the family in the pilot program may not be considered as income or a resource for purposes of eligibility of the family for other benefits, or amount of benefits payable to the family, under any program administered by the Secretary. (5) Application (A) In general An eligible entity seeking to participate in the pilot program shall submit to the Secretary an application\u2014 (i) at such time, in such manner, and containing such information as the Secretary may require by notice; and (ii) that includes the number of proposed covered families to be served by the eligible entity under this subsection. (B) Geographic and entity variety The Secretary shall ensure that eligible entities selected to participate in the pilot program\u2014 (i) are located across various States and in both urban and rural areas; and (ii) vary by size and type, including both public housing agencies and private owners of projects receiving project-based rental assistance under section 8. (6) Notification and opt-out An eligible entity participating in the pilot program shall\u2014 (A) notify covered families of their enrollment in the pilot program; (B) provide covered families with a detailed description of the pilot program, including how the pilot program will impact their rent and finances; (C) inform covered families that the families cannot simultaneously participate in the pilot program and the Family Self-Sufficiency program under this section; and (D) provide covered families with the ability to elect not to participate in the pilot program\u2014 (i) not less than 2 weeks before the date on which the escrow account is established under paragraph (3); and (ii) at any point during the duration of the pilot program. (7) Maximum rents During the term of participation by a covered family in the pilot program, the amount of rent paid by the covered family shall be calculated under the rental provisions of section 3 or 8(o), as applicable. (8) Pilot program timeline (A) Awards Not later than 18 months after the date of enactment of this subsection, the Secretary shall select the eligible entities to participate in the pilot program. (B) Establishment and term of accounts An eligible entity selected to participate in the pilot program shall\u2014 (i) not later than 6 months after selection, establish escrow accounts under paragraph (3) for covered families; and (ii) maintain those escrow accounts for not less than 5 years, or until the date the family ceases to receive assistance under section 8 or 9, and, at the discretion of the covered family, not more than 7 years after the date on which the escrow account is established. (9) Nonparticipation and housing assistance (A) In general Assistance under section 8 or 9 for a family that elects not to participate in the pilot program shall not be delayed or denied by reason of such election. (B) No termination Housing assistance may not be terminated as a consequence of participating, or not participating, in the pilot program under this subsection for any period of time. (10) Study Not later than 8 years after the date the Secretary selects eligible entities to participate in the pilot program under this subsection, the Secretary shall conduct a study and submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report on outcomes for covered families under the pilot program, which shall evaluate the effectiveness of the pilot program in assisting families to achieve economic independence and self-sufficiency, and the impact coaching and supportive services, or the lack thereof, had on individual incomes. (11) Waivers To allow selected eligible entities to effectively administer the pilot program and make the required escrow account deposits under this subsection, the Secretary may waive requirements under this section. (12) Termination The pilot program under this subsection shall terminate on the date that is 10 years after the date of enactment of this subsection. (13) Authorization of appropriations (A) In general There is authorized to be appropriated to the Secretary for fiscal year 2026 $5,000,000\u2014 (i) for technical assistance related to implementation of the pilot program; and (ii) to carry out an evaluation of the pilot program under paragraph (10). (B) Availability Any amounts appropriated under this subsection shall remain available until expended. .",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-07-14",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "4385",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Helping More Families Save Act",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-04-03T11:32:05Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s970is.xml"
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
      "title": "Helping More Families Save Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Helping More Families Save Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T03:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a pilot program to improve the family self-sufficiency program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T03:03:26Z"
    }
  ]
}
```
