# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2230?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2230
- Title: Independent Programmers Tax Incentive Act
- Congress: 119
- Bill type: HR
- Bill number: 2230
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-05-09T13:55:15Z
- Update date including text: 2025-05-09T13:55:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2230",
    "number": "2230",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Independent Programmers Tax Incentive Act",
    "type": "HR",
    "updateDate": "2025-05-09T13:55:15Z",
    "updateDateIncludingText": "2025-05-09T13:55:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:06:20Z",
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
          "date": "2025-03-18T16:06:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "WA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "WV"
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
      "sponsorshipDate": "2025-03-24",
      "state": "FL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2230ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2230\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Steube (for himself, Mr. Bilirakis , Mr. Panetta , Ms. Clarke of New York , Ms. Van Duyne , Ms. DelBene , Ms. Castor of Florida , Mr. Soto , Ms. Kelly of Illinois , Mr. Thanedar , Mr. Espaillat , Mr. Veasey , Mrs. Harshbarger , Mr. Carter of Georgia , Mr. Gimenez , and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide tax credits for carriage of independent programmers by certain multichannel video programming distributors.\n#### 1. Short title\nThis Act may be cited as the Independent Programmers Tax Incentive Act .\n#### 2. Carriage of Independent Programmers Tax Credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Carriage of Independent Programmers Credit (a) Allowance of credit For purposes of section 38, in the case of any eligible distributor, the carriage of independent programmers credit determined under this section for the taxable year is, with respect to each agreement for qualifying carriage entered into by such eligible distributor, the lesser of\u2014 (1) the net license fees paid or incurred by such eligible distributor during such taxable year under such agreement for qualifying carriage, or (2) the product of $0.10 multiplied by the average number of monthly subscribers (for calendar months during such taxable year) to which carriage is provided under such agreement. (b) Maximum credit The credit determined under this section with respect to any eligible distributor for any taxable year shall not exceed the product of $0.30 multiplied by the average number of monthly subscribers (for calendar months during such taxable year). (c) Definitions and special rules For purposes of this section\u2014 (1) Eligible distributor The term eligible distributor means any person which is either\u2014 (A) engaged in the trade or business of being a multichannel video programming distributor, or (B) a virtual multichannel video programming distributor. (2) Multichannel video programming distributor The term multichannel video programming distributor means an entity engaged in the business of making available for purchase, by subscribers or customers, multiple channels of video programming. Such entities include, but are not limited to, a cable operator, a BRS/EBS provider, a direct broadcast satellite service, a television receive-only satellite program distributor, and a satellite master antenna television system operator, as well as buying groups or agents of all such entities. (3) Virtual multichannel video programming distributor The term virtual multichannel video programming distributor means any person engaged in the trade or business of making available directly to the end user, by means of the Internet or other IP-based transmission path, multiple streams of linear video programming. (4) Video programming The term video programming means programming provided by, or generally considered comparable to programming provided by, a television broadcast station, but not including consumer-generated media. (5) Agreement for qualifying carriage The term agreement for qualifying carriage means a written agreement between an eligible distributor and a qualified independent programmer that provides for new or expanded carriage of one or more linear video programming streams of a qualified independent programmer to at least 40 percent of the eligible distributor\u2019s subscriber base in aggregate for such linear video programming streams and which requires the eligible distributor to pay a license fee to the qualified independent programmer. (6) Qualified independent programmer (A) In general The term qualified independent programmer means a United States-based person engaged in the production, creation, or wholesale distribution of linear video programming if\u2014 (i) such person is not a publicly traded company, multichannel video programming distributor, virtual multichannel video programming distributor, network, or television station company, and (ii) no publicly traded company, multichannel video programming distributor, virtual multichannel video programming distributor, network, or television station company has a cognizable interest in such person. (B) Network The term network means an entity that offers programming on a regular basis for 15 or more hours per week to at least 25 affiliates in 10 or more States. (C) Television station company The term television station company means any person if, after taking into account the audience reach of all television stations under common control with such person, such person has a national audience reach in excess of 3 percent. Terms used in this subparagraph which are also used in section 202(c) of the Telecommunications Act of 1996 (or in the regulations issued pursuant to such section) shall have the same meaning as when used in such section (or such regulations). (D) Cognizable interest The term cognizable interest means partnership and direct ownership interests and any voting stock interest amounting to 5 percent or more of the outstanding voting stock of an entity. (7) License fees Except as otherwise provided by the Secretary, in the case of an agreement for qualifying carriage which is net effective rate positive for the qualified independent programmer, the appropriate amount shall be treated as a license fee paid by the eligible distributor to the qualified independent programmer. (d) Denial of double benefit No deduction shall be allowed under this chapter for any amount to the extent that such amount is allowed as a credit under this section. .\n##### (b) Credit made part of general business credit\nSubsection (b) of section 38 of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the carriage of independent programmers credit determined under section 45BB. .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Carriage of Independent Programmers Credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to expenses paid or incurred after the date of the enactment of this Act, in taxable years ending after such date.\n#### 3. Biennial report by FCC to Congress\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and not less frequently than every 2 years thereafter, the Federal Communications Commission shall submit to Congress a report that\u2014\n**(1)**\nstates the number of qualified independent programmers that have a linear video programming stream that is distributed to subscribers of one or more eligible distributors and the average length of time for which such a linear video programming stream has been so distributed by the same eligible distributor;\n**(2)**\nstates the number of qualified independent programmers that have a linear video programming stream that is distributed to subscribers of one or more multichannel video programming distributors and the average length of time for which such a linear video programming stream has been so distributed by the same multichannel video programming distributor;\n**(3)**\nstates the number of qualified independent programmers that have a linear video programming stream that is distributed to subscribers of one or more virtual multichannel video programming distributors and the average length of time for which such a linear video programming stream has been so distributed by the same virtual multichannel video programming distributor; and\n**(4)**\ncontains recommendations for how to increase the number of qualified independent programmers described in paragraph (1).\n##### (b) Disclosure of tax return information\nSection 6103(l) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(23) Disclosure of return information to Federal Communications Commission for biennial reports to Congress (A) In general The Secretary shall, upon written request from the Federal Communications Commission, disclose to officers and employees of such Commission such return information of taxpayers claiming the credit allowable under section 45BB as such Commission determines necessary to prepare the reports required under section 2 of the Independent Programmers Tax Incentive Act . (B) Restriction on disclosure Return information disclosed under subparagraph (A) may be used by officers and employees of the Federal Communications Commission for the purposes of, and to the extent necessary in, preparing the reports required under section 2 of the Independent Programmers Tax Incentive Act . Such reports shall not include return information which is identifiable as being with respect to a particular taxpayer. .",
      "versionDate": "2025-03-18",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T13:55:15Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2230ih.xml"
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
      "title": "Independent Programmers Tax Incentive Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T12:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Independent Programmers Tax Incentive Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T12:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide tax credits for carriage of independent programmers by certain multichannel video programming distributors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T12:03:23Z"
    }
  ]
}
```
